package com.kelompoksatu.sispakdurian.ui.diagnosis.viewmodel

import android.content.Context
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
//import com.chaquo.python.Python
//import com.chaquo.python.android.AndroidPlatform
import com.kelompoksatu.sispakdurian.data.model.Diagnosis
import com.kelompoksatu.sispakdurian.data.repository.AppRepository
import com.kelompoksatu.sispakdurian.util.Constant
import kotlinx.coroutines.launch

class AskViewModel constructor(
    private val repository: AppRepository
) : ViewModel() {

    var output: MutableLiveData<String> = MutableLiveData()

    fun diagnosa(type: String, usedSymtomps: List<String>, certaintyFactor: List<Double>, context: Context) {
        var usedSymtompsString = ""
        for (us in usedSymtomps) {
            usedSymtompsString = "$usedSymtompsString $us"
        }
        var certaintyFactorString = ""
        for (cf in certaintyFactor) {
            certaintyFactorString = "$certaintyFactorString $cf"
        }
        viewModelScope.launch {
            if (!Python.isStarted()) {
                Python.start(AndroidPlatform(context))
            }
            val py = Python.getInstance()
            val pyf = py.getModule("durian_diagnose")
            when (type) {
                Constant.HAMA -> {
                    val obj = pyf.callAttr("diagnose", Constant.HAMA, usedSymtompsString, certaintyFactorString)
                    output.postValue(obj.toString())
                }
                Constant.PENYAKIT -> {
                    val obj =
                        pyf.callAttr("diagnose", Constant.PENYAKIT, usedSymtompsString, certaintyFactorString)
                    output.postValue(obj.toString())
                }
            }
        }
    }

    fun insertDiagnosis(symptomps: Diagnosis) = viewModelScope.launch {
        repository.insertDiagnosis(symptomps)
    }

    fun getDiagnosisHistory() = repository.diagnosisHistory()

    fun deleteDiagnosisHistory() = viewModelScope.launch {
        repository.deleteDiagnosisHistory()
    }


}