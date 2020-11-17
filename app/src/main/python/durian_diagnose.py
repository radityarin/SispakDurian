import pandas as pd
from datetime import datetime
import uuid
from os.path import dirname, abspath, join
import xlrd
import os

class SistemPakarDurian(object):
      '''
            Sistem Pakar Durian dengan Naive Bayes dan Certainty Factor

            Parameter:
                  1. jenis (string) = "Penyakit" atau "Hama
                  2. input_gejala (list(string)) = ex: ['G1', 'G8', 'G9']

      '''
      def __init__(self):            
            loc=join(dirname(abspath(__file__)))
            loc = os.path.join(loc, 'data.xlsx')
            wb=xlrd.open_workbook(loc)
            data_cf_hama=self.parse(wb.sheet_by_index(8))
            data_cf_penyakit=self.parse(wb.sheet_by_index(9))
            data_latih_hama=self.parse(wb.sheet_by_index(10))
            data_latih_penyakit=self.parse(wb.sheet_by_index(11))
            self.data_dict_hama = pd.DataFrame(data_latih_hama)
            self.data_dict_penyakit = pd.DataFrame(data_latih_penyakit)
            self.data_cf_penyakit_pakar = pd.DataFrame(data_cf_penyakit)
            self.data_cf_hama_pakar = pd.DataFrame(data_cf_hama)

      def fit(self,jenis):
            self.jenis = jenis
            '''
                  Parameter:
                        1. jenis (string) = "Penyakit" atau "Hama
            '''
            data_dict = None
            if(self.jenis == 'Hama'):
                  data_dict = self.data_dict_hama
            else:
                  data_dict = self.data_dict_penyakit     
            self.jumlah_gejala = data_dict.groupby(['Jenis_'+jenis], sort=False).sum()
            self.jumlah_jenis_gejala = data_dict.columns.size - 1
            self.jumlah_hama = data_dict.groupby(['Jenis_'+jenis], sort=False).G1.count()
            self.jumlah_data = data_dict.index.size
            self.prior = pd.Series([a/self.jumlah_data for a in self.jumlah_hama], index=self.jumlah_hama.index)
            self.likelihood = pd.DataFrame([(self.jumlah_gejala.iloc[n]+1)/(self.jumlah_hama[n]+self.jumlah_jenis_gejala) for n in range(self.jumlah_hama.size)])

      def predict(self,input_gejala,input_cf):
            '''
                  Parameter:
                        1. input_gejala (list(string)) = ex: ['G1', 'G8', 'G9']
                  Return value:
                        1. Hasil Klasifikasi
                        2. Nilai Posterior
                        3. Certainty Factor
            '''
            perkalian_likelihood = (self.likelihood.reindex(columns=input_gejala).prod(axis=1))
            posterior = (perkalian_likelihood * self.prior).to_dict()
            keymax = max(posterior, key=posterior.get)
            certaintyfactor = self.__get_certainty_factor(keymax, input_cf)
            return keymax, max(posterior.values()), certaintyfactor

      def __get_certainty_factor(self,klasifikasi,input_cf):
            data_cf = None
            if(self.jenis == 'Hama'):
                  data_cf = self.data_cf_hama_pakar
            else:
                  data_cf = self.data_cf_penyakit_pakar 
            CFPakar = data_cf[klasifikasi]
            CFgejala = pd.DataFrame({'Hasil':[CFPakar[z]*input_cf[z] for z in data_cf.index]}, index=data_cf['Gejala'])
            CF=[]
            for index in range(CFgejala.size-1):
                  if index == 0:
                        CF.append(CFgejala.Hasil[0] + CFgejala.Hasil[1] * (1 - CFgejala.Hasil[0]))
                  else:
                        CF.append(CF[index-1] + CFgejala.Hasil[index+1] * (1 - CF[index-1]))
            persentase = max(CF) * 100
            return persentase

      def parse(self,worksheet):
            first_row = [] # The row where we stock the name of the column
            for col in range(worksheet.ncols):
                  first_row.append( worksheet.cell_value(0,col) )
            # tronsform the workbook to a list of dictionnary
            data =[]
            for row in range(1, worksheet.nrows):
                  elm = {}
                  for col in range(worksheet.ncols):
                        elm[first_row[col]]=worksheet.cell_value(row,col)
                  data.append(elm)
            return data


def diagnose(jenis,input_gejala,temp):
      input_gejala = input_gejala.split(" ")
      input_cf_user = []
      index = 0
      for icu in temp.split(" "):
            if(index != 0 ):
                  input_cf_user.append(float(icu))
            index+=1
      spk = SistemPakarDurian()
      spk.fit(jenis)
      hasil_klasifikasi, posterior, cf = spk.predict(input_gejala,input_cf_user)
      result_dict = {}
      dateTimeObj = datetime.now()
      timestampStr = dateTimeObj.strftime("%d/%b/%Y")
      cf = float("%.3f" % cf)
      result_dict["success"] = True
      result_dict["message"] = "Diagnose Complete"
      result_dict["data"] = {"type":jenis,"input_symptomps":input_gejala,"timestamps":timestampStr,"classification_result":hasil_klasifikasi,"posterior":posterior,"cf":cf,"id_prediction":uuid.uuid4()}
      return result_dict 

print(diagnose("Penyakit","G1 G2 G7 G13","0.2 0.4 0 0 0 0 1 0 0 0 0 0 0.6 0 0 0"))