package com.kelompoksatu.sispakdurian.data.repository

import android.content.Context
import com.google.gson.Gson
import com.kelompoksatu.sispakdurian.data.model.Diagnosis
class AppRepository(context: Context) : Repository {

    private val db = DbDiagnoseRepository(context)

    override fun diagnosisHistory() = db.getAllDiagnosis()

    override suspend fun insertDiagnosis(symptomps: Diagnosis) {
        db.insertDiagnosis(symptomps)
    }

    override suspend fun deleteDiagnosisHistory() {
        db.deleteAllDiagnosis()
    }

}
