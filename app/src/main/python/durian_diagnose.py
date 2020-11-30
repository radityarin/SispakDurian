from datetime import datetime
import uuid
import json

class SistemPakarDurian(object):
      '''
            Sistem Pakar Durian dengan Naive Bayes dan Certainty Factor

            Parameter:
                  1. jenis (string) = "Penyakit" atau "Hama
                  2. input_gejala (list(string)) = ex: ['G1', 'G8', 'G9']

      '''
      def __init__(self):            
            self.jenis = None

      def fit(self,jenis):
            self.jenis = jenis
            '''
                  Parameter:
                        1. jenis (string) = "Penyakit" atau "Hama
            '''
      def predict(self,input_gejala,input_cf,jenis):
            '''
                  Parameter:
                        1. input_gejala (list(string)) = ex: ['G1', 'G8', 'G9']
                  Return value:
                        1. Hasil Klasifikasi
                        2. Nilai Posterior
                        3. Certainty Factor
            '''
            likelihood_dict = json.loads(self.get_likelihood_string_json(jenis))
            prior_dict = json.loads(self.get_prior_string_json(jenis))
            index = 0
            perkalian_likelihood = {}
            for gejala in likelihood_dict.keys():
                  value = likelihood_dict.get(gejala)
                  if(gejala in ['G1', 'G2', 'G7', 'G13']):
                        if(index == 0):
                              perkalian_likelihood = value
                        else:
                              dict2 = value
                              perkalian_likelihood = {key: dict2[key] * perkalian_likelihood[key] for key in dict2.keys()}
                        index += 1
            posterior = {key: prior_dict[key] * perkalian_likelihood[key] for key in perkalian_likelihood.keys()}
            keymax = max(posterior, key=posterior.get)
            keymin = min(posterior, key=posterior.get)
            certaintyfactor_max, certaintyfactor_min = self.__get_certainty_factor(keymax, keymin, input_cf, jenis)
            return keymax, max(posterior.values()), keymin, min(posterior.values()), certaintyfactor_max, certaintyfactor_min

      def get_likelihood_string_json(self, jenis):
            if (jenis == "Penyakit"):
                  likelihood_penyakit = '''
                  {
                        "G1": {
                        "Jamur Daun": 0.4,
                        "Busuk Akar": 0.0625,
                        "Kanker Batang": 0.05555555555555555,
                        "Jamur Upas": 0.0625,
                        "Busuk Buah": 0.07142857142857142,
                        "Kanker Bercak": 0.05
                        },
                        "G2": {
                        "Jamur Daun": 0.45,
                        "Busuk Akar": 0.0625,
                        "Kanker Batang": 0.3333333333333333,
                        "Jamur Upas": 0.0625,
                        "Busuk Buah": 0.07142857142857142,
                        "Kanker Bercak": 0.05
                        },
                        "G3": {
                        "Jamur Daun": 0.05,
                        "Busuk Akar": 0.5,
                        "Kanker Batang": 0.05555555555555555,
                        "Jamur Upas": 0.0625,
                        "Busuk Buah": 0.07142857142857142,
                        "Kanker Bercak": 0.05
                        },
                        "G4": {
                        "Jamur Daun": 0.05,
                        "Busuk Akar": 0.3125,
                        "Kanker Batang": 0.05555555555555555,
                        "Jamur Upas": 0.0625,
                        "Busuk Buah": 0.07142857142857142,
                        "Kanker Bercak": 0.05
                        },
                        "G5": {
                        "Jamur Daun": 0.05,
                        "Busuk Akar": 0.0625,
                        "Kanker Batang": 0.5555555555555556,
                        "Jamur Upas": 0.0625,
                        "Busuk Buah": 0.07142857142857142,
                        "Kanker Bercak": 0.05
                        },
                        "G6": {
                        "Jamur Daun": 0.05,
                        "Busuk Akar": 0.0625,
                        "Kanker Batang": 0.05555555555555555,
                        "Jamur Upas": 0.5,
                        "Busuk Buah": 0.07142857142857142,
                        "Kanker Bercak": 0.05
                        },
                        "G7": {
                        "Jamur Daun": 0.05,
                        "Busuk Akar": 0.0625,
                        "Kanker Batang": 0.05555555555555555,
                        "Jamur Upas": 0.0625,
                        "Busuk Buah": 0.42857142857142855,
                        "Kanker Bercak": 0.05
                        },
                        "G8": {
                        "Jamur Daun": 0.05,
                        "Busuk Akar": 0.0625,
                        "Kanker Batang": 0.05555555555555555,
                        "Jamur Upas": 0.0625,
                        "Busuk Buah": 0.07142857142857142,
                        "Kanker Bercak": 0.35
                        },
                        "G9": {
                        "Jamur Daun": 0.05,
                        "Busuk Akar": 0.0625,
                        "Kanker Batang": 0.05555555555555555,
                        "Jamur Upas": 0.0625,
                        "Busuk Buah": 0.07142857142857142,
                        "Kanker Bercak": 0.5
                        }
                  }
                  '''
                  return likelihood_penyakit
            else:
                  likelihood_hama = '''
                  {
                        "G1": {
                        "Kutu Loncat": 0.39285714285714285,
                        "Lebah Mini": 0.045454545454545456,
                        "Penggerek Buah": 0.047619047619047616,
                        "Ulat Penggerek Bunga": 0.045454545454545456,
                        "Embug": 0.043478260869565216,
                        "Ulat Daun": 0.05263157894736842,
                        "Rayap": 0.05263157894736842,
                        "Kutu Putih": 0.045454545454545456,
                        "Penggerek Batang": 0.05555555555555555
                        },
                        "G2": {
                        "Kutu Loncat": 0.17857142857142858,
                        "Lebah Mini": 0.045454545454545456,
                        "Penggerek Buah": 0.047619047619047616,
                        "Ulat Penggerek Bunga": 0.045454545454545456,
                        "Embug": 0.043478260869565216,
                        "Ulat Daun": 0.05263157894736842,
                        "Rayap": 0.05263157894736842,
                        "Kutu Putih": 0.18181818181818182,
                        "Penggerek Batang": 0.05555555555555555
                        },
                        "G3": {
                        "Kutu Loncat": 0.2857142857142857,
                        "Lebah Mini": 0.045454545454545456,
                        "Penggerek Buah": 0.047619047619047616,
                        "Ulat Penggerek Bunga": 0.045454545454545456,
                        "Embug": 0.043478260869565216,
                        "Ulat Daun": 0.05263157894736842,
                        "Rayap": 0.05263157894736842,
                        "Kutu Putih": 0.045454545454545456,
                        "Penggerek Batang": 0.05555555555555555
                        },
                        "G4": {
                        "Kutu Loncat": 0.03571428571428571,
                        "Lebah Mini": 0.3181818181818182,
                        "Penggerek Buah": 0.047619047619047616,
                        "Ulat Penggerek Bunga": 0.045454545454545456,
                        "Embug": 0.043478260869565216,
                        "Ulat Daun": 0.05263157894736842,
                        "Rayap": 0.05263157894736842,
                        "Kutu Putih": 0.045454545454545456,
                        "Penggerek Batang": 0.05555555555555555
                        },
                        "G5": {
                        "Kutu Loncat": 0.03571428571428571,
                        "Lebah Mini": 0.045454545454545456,
                        "Penggerek Buah": 0.047619047619047616,
                        "Ulat Penggerek Bunga": 0.045454545454545456,
                        "Embug": 0.2608695652173913,
                        "Ulat Daun": 0.05263157894736842,
                        "Rayap": 0.05263157894736842,
                        "Kutu Putih": 0.045454545454545456,
                        "Penggerek Batang": 0.05555555555555555
                        },
                        "G6": {
                        "Kutu Loncat": 0.03571428571428571,
                        "Lebah Mini": 0.045454545454545456,
                        "Penggerek Buah": 0.047619047619047616,
                        "Ulat Penggerek Bunga": 0.045454545454545456,
                        "Embug": 0.34782608695652173,
                        "Ulat Daun": 0.05263157894736842,
                        "Rayap": 0.05263157894736842,
                        "Kutu Putih": 0.045454545454545456,
                        "Penggerek Batang": 0.05555555555555555
                        },
                        "G7": {
                        "Kutu Loncat": 0.03571428571428571,
                        "Lebah Mini": 0.045454545454545456,
                        "Penggerek Buah": 0.047619047619047616,
                        "Ulat Penggerek Bunga": 0.045454545454545456,
                        "Embug": 0.17391304347826086,
                        "Ulat Daun": 0.05263157894736842,
                        "Rayap": 0.05263157894736842,
                        "Kutu Putih": 0.045454545454545456,
                        "Penggerek Batang": 0.05555555555555555
                        },
                        "G8": {
                        "Kutu Loncat": 0.03571428571428571,
                        "Lebah Mini": 0.045454545454545456,
                        "Penggerek Buah": 0.047619047619047616,
                        "Ulat Penggerek Bunga": 0.045454545454545456,
                        "Embug": 0.043478260869565216,
                        "Ulat Daun": 0.05263157894736842,
                        "Rayap": 0.05263157894736842,
                        "Kutu Putih": 0.3181818181818182,
                        "Penggerek Batang": 0.05555555555555555
                        },
                        "G9": {
                        "Kutu Loncat": 0.03571428571428571,
                        "Lebah Mini": 0.045454545454545456,
                        "Penggerek Buah": 0.047619047619047616,
                        "Ulat Penggerek Bunga": 0.045454545454545456,
                        "Embug": 0.043478260869565216,
                        "Ulat Daun": 0.05263157894736842,
                        "Rayap": 0.05263157894736842,
                        "Kutu Putih": 0.045454545454545456,
                        "Penggerek Batang": 0.16666666666666666
                        },
                        "G10": {
                        "Kutu Loncat": 0.03571428571428571,
                        "Lebah Mini": 0.045454545454545456,
                        "Penggerek Buah": 0.047619047619047616,
                        "Ulat Penggerek Bunga": 0.18181818181818182,
                        "Embug": 0.043478260869565216,
                        "Ulat Daun": 0.05263157894736842,
                        "Rayap": 0.05263157894736842,
                        "Kutu Putih": 0.045454545454545456,
                        "Penggerek Batang": 0.05555555555555555
                        },
                        "G11": {
                        "Kutu Loncat": 0.03571428571428571,
                        "Lebah Mini": 0.045454545454545456,
                        "Penggerek Buah": 0.047619047619047616,
                        "Ulat Penggerek Bunga": 0.2727272727272727,
                        "Embug": 0.043478260869565216,
                        "Ulat Daun": 0.05263157894736842,
                        "Rayap": 0.05263157894736842,
                        "Kutu Putih": 0.045454545454545456,
                        "Penggerek Batang": 0.05555555555555555
                        },
                        "G12": {
                        "Kutu Loncat": 0.03571428571428571,
                        "Lebah Mini": 0.045454545454545456,
                        "Penggerek Buah": 0.047619047619047616,
                        "Ulat Penggerek Bunga": 0.13636363636363635,
                        "Embug": 0.043478260869565216,
                        "Ulat Daun": 0.05263157894736842,
                        "Rayap": 0.05263157894736842,
                        "Kutu Putih": 0.045454545454545456,
                        "Penggerek Batang": 0.05555555555555555
                        },
                        "G13": {
                        "Kutu Loncat": 0.14285714285714285,
                        "Lebah Mini": 0.045454545454545456,
                        "Penggerek Buah": 0.047619047619047616,
                        "Ulat Penggerek Bunga": 0.045454545454545456,
                        "Embug": 0.043478260869565216,
                        "Ulat Daun": 0.21052631578947367,
                        "Rayap": 0.05263157894736842,
                        "Kutu Putih": 0.045454545454545456,
                        "Penggerek Batang": 0.05555555555555555
                        },
                        "G14": {
                        "Kutu Loncat": 0.03571428571428571,
                        "Lebah Mini": 0.045454545454545456,
                        "Penggerek Buah": 0.047619047619047616,
                        "Ulat Penggerek Bunga": 0.045454545454545456,
                        "Embug": 0.043478260869565216,
                        "Ulat Daun": 0.05263157894736842,
                        "Rayap": 0.21052631578947367,
                        "Kutu Putih": 0.045454545454545456,
                        "Penggerek Batang": 0.05555555555555555
                        },
                        "G15": {
                        "Kutu Loncat": 0.03571428571428571,
                        "Lebah Mini": 0.045454545454545456,
                        "Penggerek Buah": 0.2857142857142857,
                        "Ulat Penggerek Bunga": 0.045454545454545456,
                        "Embug": 0.043478260869565216,
                        "Ulat Daun": 0.05263157894736842,
                        "Rayap": 0.05263157894736842,
                        "Kutu Putih": 0.045454545454545456,
                        "Penggerek Batang": 0.05555555555555555
                        },
                        "G16": {
                        "Kutu Loncat": 0.03571428571428571,
                        "Lebah Mini": 0.045454545454545456,
                        "Penggerek Buah": 0.19047619047619047,
                        "Ulat Penggerek Bunga": 0.045454545454545456,
                        "Embug": 0.043478260869565216,
                        "Ulat Daun": 0.05263157894736842,
                        "Rayap": 0.05263157894736842,
                        "Kutu Putih": 0.045454545454545456,
                        "Penggerek Batang": 0.05555555555555555
                        }
                  }
                  '''
                  return likelihood_hama

      def get_prior_string_json(self, jenis):
            if (jenis == "Penyakit"):
                  prior_penyakit = '''
                        {
                        "Jamur Daun": 0.22,
                        "Busuk Akar": 0.14,
                        "Kanker Batang": 0.18,
                        "Jamur Upas": 0.14,
                        "Busuk Buah": 0.1,
                        "Kanker Bercak": 0.22
                        }
                  '''
                  return prior_penyakit
            else:
                  prior_hama = '''
                        {
                        "Kutu Loncat": 0.24,
                        "Lebah Mini": 0.12,
                        "Penggerek Buah": 0.1,
                        "Ulat Penggerek Bunga": 0.12,
                        "Embug": 0.14,
                        "Ulat Daun": 0.06,
                        "Rayap": 0.06,
                        "Kutu Putih": 0.12,
                        "Penggerek Batang": 0.04
                        }
                  '''
                  return prior_hama

      def get_cf_string_json(self, jenis):
            if jenis == "Hama":
                  cf = '''
                              {
                              "Kode": {
                              "0": "G1",
                              "1": "G2",
                              "2": "G3",
                              "3": "G4",
                              "4": "G5",
                              "5": "G6",
                              "6": "G7",
                              "7": "G8",
                              "8": "G9",
                              "9": "G10",
                              "10": "G11",
                              "11": "G12",
                              "12": "G13",
                              "13": "G14",
                              "14": "G15",
                              "15": "G16"
                              },
                              "Gejala": {
                              "0": "Bintik-bintik berwarna kecokelatan pada daun",
                              "1": "Daun keriting",
                              "2": "Berukuran kerdil",
                              "3": "Adanya luka gerekan pada daun dan ranting muda",
                              "4": "Pertumbuhan pohon durian sangat lama",
                              "5": "Daun secara perlahan layu dan mengering diikuti oleh ranting dan batang",
                              "6": "Daun yang kering tidak jatuh semua melainkan masih melekat pada tangkainya",
                              "7": "Bunga atau buah mengalami kerontokan",
                              "8": "Adanya kotoran dibawah batang",
                              "9": "Rusaknya kuncup bunga sehingga putik bunga berguguran",
                              "10": "Rusaknya benang sari dan tajuk bunga",
                              "11": "Kuncup dan putik patah karena luka digerek",
                              "12": "Daun berlubang",
                              "13": "Adanya alur dari tanah yang menempel di bagian batang",
                              "14": "Kulit dan duri buah menjadi hitam seperti busuk",
                              "15": "Buah jatuh sebelum tua"
                              },
                              "Kutu Loncat": {
                              "0": 0.4,
                              "1": 0.8,
                              "2": 0.8,
                              "3": 0.0,
                              "4": 0.0,
                              "5": 0.0,
                              "6": 0.0,
                              "7": 0.0,
                              "8": 0.0,
                              "9": 0.0,
                              "10": 0.0,
                              "11": 0.0,
                              "12": 0.4,
                              "13": 0.0,
                              "14": 0.0,
                              "15": 0.0
                              },
                              "Lebah Mini": {
                              "0": 0.0,
                              "1": 0.0,
                              "2": 0.0,
                              "3": 0.8,
                              "4": 0.0,
                              "5": 0.0,
                              "6": 0.0,
                              "7": 0.0,
                              "8": 0.0,
                              "9": 0.0,
                              "10": 0.0,
                              "11": 0.0,
                              "12": 0.0,
                              "13": 0.0,
                              "14": 0.0,
                              "15": 0.0
                              },
                              "Penggerek Buah": {
                              "0": 0.0,
                              "1": 0.0,
                              "2": 0.0,
                              "3": 0.0,
                              "4": 0.0,
                              "5": 0.0,
                              "6": 0.0,
                              "7": 0.0,
                              "8": 0.0,
                              "9": 0.0,
                              "10": 0.0,
                              "11": 0.0,
                              "12": 0.0,
                              "13": 0.0,
                              "14": 0.8,
                              "15": 0.8
                              },
                              "Ulat Penggerek Bunga": {
                              "0": 0.0,
                              "1": 0.0,
                              "2": 0.0,
                              "3": 0.0,
                              "4": 0.0,
                              "5": 0.0,
                              "6": 0.0,
                              "7": 0.0,
                              "8": 0.0,
                              "9": 0.8,
                              "10": 0.8,
                              "11": 0.8,
                              "12": 0.0,
                              "13": 0.0,
                              "14": 0.0,
                              "15": 0.0
                              },
                              "Embug": {
                              "0": 0.0,
                              "1": 0.0,
                              "2": 0.0,
                              "3": 0.0,
                              "4": 0.8,
                              "5": 0.8,
                              "6": 0.8,
                              "7": 0.4,
                              "8": 0.0,
                              "9": 0.0,
                              "10": 0.0,
                              "11": 0.0,
                              "12": 0.0,
                              "13": 0.0,
                              "14": 0.0,
                              "15": 0.0
                              },
                              "Ulat Daun": {
                              "0": 0.0,
                              "1": 0.0,
                              "2": 0.0,
                              "3": 0.0,
                              "4": 0.0,
                              "5": 0.0,
                              "6": 0.0,
                              "7": 0.0,
                              "8": 0.0,
                              "9": 0.0,
                              "10": 0.0,
                              "11": 0.0,
                              "12": 0.8,
                              "13": 0.0,
                              "14": 0.0,
                              "15": 0.0
                              },
                              "Rayap": {
                              "0": 0.0,
                              "1": 0.0,
                              "2": 0.0,
                              "3": 0.0,
                              "4": 0.0,
                              "5": 0.0,
                              "6": 0.0,
                              "7": 0.0,
                              "8": 0.0,
                              "9": 0.0,
                              "10": 0.0,
                              "11": 0.0,
                              "12": 0.0,
                              "13": 0.8,
                              "14": 0.0,
                              "15": 0.0
                              },
                              "Kutu Putih": {
                              "0": 0.0,
                              "1": 0.8,
                              "2": 0.0,
                              "3": 0.0,
                              "4": 0.0,
                              "5": 0.0,
                              "6": 0.0,
                              "7": 0.8,
                              "8": 0.0,
                              "9": 0.0,
                              "10": 0.0,
                              "11": 0.0,
                              "12": 0.0,
                              "13": 0.0,
                              "14": 0.0,
                              "15": 0.0
                              },
                              "Penggerek Batang": {
                              "0": 0.0,
                              "1": 0.0,
                              "2": 0.0,
                              "3": 0.0,
                              "4": 0.0,
                              "5": 0.0,
                              "6": 0.0,
                              "7": 0.0,
                              "8": 0.8,
                              "9": 0.0,
                              "10": 0.0,
                              "11": 0.0,
                              "12": 0.0,
                              "13": 0.0,
                              "14": 0.0,
                              "15": 0.0
                              }
                              }
                  '''
                  return cf
            else:
                  cf = '''
                              {
                              "Kode": {
                              "0": "G1",
                              "1": "G2",
                              "2": "G3",
                              "3": "G4",
                              "4": "G5",
                              "5": "G6",
                              "6": "G7",
                              "7": "G8",
                              "8": "G9"
                              },
                              "Gejala": {
                              "0": "Daun menguning",
                              "1": "Daun berguguran",
                              "2": "Bercak yang berawal dari ujung akar lateral",
                              "3": "Jaringan akar berwarna cokelat",
                              "4": "Bekas luka pada batang seperti blendok berwarna coklat kemerahan",
                              "5": "Terdapat kerak berwarna merah jambu",
                              "6": "Bercak – bercak berwarna cokelat kehitaman dan basah pada kulit buah",
                              "7": "Tanaman terlihat layu",
                              "8": "Tumbuh spora berwarna putih disekitar bawah daun"
                              },
                              "Jamur Daun": {
                              "0": 0.4,
                              "1": 0.4,
                              "2": 0.0,
                              "3": 0.0,
                              "4": 0.0,
                              "5": 0.0,
                              "6": 0.0,
                              "7": 0.0,
                              "8": 0.0
                              },
                              "Busuk Akar": {
                              "0": 0.0,
                              "1": 0.0,
                              "2": 0.8,
                              "3": 0.8,
                              "4": 0.0,
                              "5": 0.0,
                              "6": 0.0,
                              "7": 0.0,
                              "8": 0.0
                              },
                              "Kanker Batang": {
                              "0": 0.0,
                              "1": 0.4,
                              "2": 0.0,
                              "3": 0.0,
                              "4": 0.8,
                              "5": 0.0,
                              "6": 0.0,
                              "7": 0.0,
                              "8": 0.0
                              },
                              "Jamur Upas": {
                              "0": 0.0,
                              "1": 0.0,
                              "2": 0.0,
                              "3": 0.0,
                              "4": 0.0,
                              "5": 0.8,
                              "6": 0.0,
                              "7": 0.0,
                              "8": 0.0
                              },
                              "Busuk Buah": {
                              "0": 0.0,
                              "1": 0.0,
                              "2": 0.0,
                              "3": 0.0,
                              "4": 0.0,
                              "5": 0.0,
                              "6": 0.8,
                              "7": 0.0,
                              "8": 0.0
                              },
                              "Kanker Bercak": {
                              "0": 0.0,
                              "1": 0.0,
                              "2": 0.0,
                              "3": 0.0,
                              "4": 0.0,
                              "5": 0.0,
                              "6": 0.0,
                              "7": 0.6,
                              "8": 0.6
                              }
                              }

                  '''
                  return cf

      def __get_certainty_factor(self,klasifikasi_max,klasifikasi_min,input_cf,jenis):
            data_cf_pakar_dict = json.loads(self.get_cf_string_json(jenis))
            cf_klasifikasi_max= data_cf_pakar_dict[klasifikasi_max]
            cf_klasifikasi_min= data_cf_pakar_dict[klasifikasi_min]
            cf_pakar_max = []
            cf_pakar_min = []
            cf_gejala_max = []
            cf_gejala_min = []
            for index in cf_klasifikasi_max:
                  cf_pakar_max.append(cf_klasifikasi_max.get(index))
                  cf_pakar_min.append(cf_klasifikasi_min.get(index))

            for cf in range(len(cf_pakar_max)):
                  # print(cf_pakar_max)
                  # print(input_cf)
                  # print(cf)
                  cf_gejala_max.append(cf_pakar_max[cf]*input_cf[cf])
                  cf_gejala_min.append(cf_pakar_min[cf]*input_cf[cf])

            CF_max=[]
            CF_min=[]
            for index in range(len(cf_gejala_max) - 1):
                  if index == 0:
                        CF_max.append(cf_gejala_max[0] + cf_gejala_max[1] * (1 - cf_gejala_max[0]))
                        CF_min.append(cf_gejala_min[0] + cf_gejala_min[1] * (1 - cf_gejala_min[0]))
                  else:
                        CF_max.append(CF_max[index-1] + cf_gejala_max[index+1] * (1 - CF_max[index-1]))
                        CF_min.append(CF_min[index-1] + cf_gejala_min[index+1] * (1 - CF_min[index-1]))
            persentase_max = max(CF_max) * 100
            persentase_min = max(CF_min) * 100
            return persentase_max, persentase_min

      def parse(self,worksheet):
            first_row = []
            for col in range(worksheet.ncols):
                  first_row.append( worksheet.cell_value(0,col) )
            data =[]
            for row in range(1, worksheet.nrows):
                  elm = {}
                  for col in range(worksheet.ncols):
                        elm[first_row[col]]=worksheet.cell_value(row,col)
                  data.append(elm)
            return data

def diagnose(jenis,input_gejala,temp):
      input_gejala = input_gejala.split(" ")
      temp = temp.split()
      input_cf_user = []
      index = 0
      for i in range(len(temp)):
            input_cf_user.append(float(temp[i]))

      spk = SistemPakarDurian()
      spk.fit(jenis)
      hasil_klasifikasi_max, posterior_max, hasil_klasifikasi_min, posterior_min, certaintyfactor_max, certaintyfactor_min = spk.predict(input_gejala, input_cf_user, jenis)
      result_dict = {}
      dateTimeObj = datetime.now()
      timestampStr = dateTimeObj.strftime("%d/%b/%Y")
      cf_max = float("%.3f" % certaintyfactor_max)
      cf_min = float("%.3f" % certaintyfactor_min)
      result_dict["success"] = True
      result_dict["message"] = "Diagnose Complete"
      result_dict["data"] = {"type":jenis,"input_symptomps":input_gejala,"timestamps":timestampStr,"classification_result_max":hasil_klasifikasi_max,"classification_result_min":hasil_klasifikasi_min,"posterior_max":posterior_max,"posterior_min":posterior_min,"cf_max":cf_max,"cf_min":cf_min,"id_prediction":uuid.uuid4()}
      return result_dict

print(diagnose("Penyakit","G2, G5, G7, G9","0.0 0.6 0.0 0.0 0.8 0.0 0.8 0.0 0.8 0.0 0.0 0.0 0.0 0.0 0.0 0.0"))
