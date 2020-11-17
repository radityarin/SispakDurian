package com.kelompoksatu.sispakdurian.data.repository

import androidx.lifecycle.LiveData
import com.kelompoksatu.sispakdurian.data.model.Diagnosis

interface Repository {
    fun diagnosisHistory(): LiveData<List<Diagnosis>>?
    suspend fun insertDiagnosis(symptomps: Diagnosis)
    suspend fun deleteDiagnosisHistory()
}