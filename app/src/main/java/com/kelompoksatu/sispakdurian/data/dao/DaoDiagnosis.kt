package com.kelompoksatu.sispakdurian.data.dao

import androidx.lifecycle.LiveData
import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import com.kelompoksatu.sispakdurian.data.model.Diagnosis

@Dao
interface DaoDiagnosis {
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertDiagnosis(model: Diagnosis)

    @Query("SELECT * FROM diagnosis")
    fun getAllDiagnosis(): LiveData<List<Diagnosis>>

    @Query("DELETE FROM diagnosis")
    suspend fun deleteAllDiagnosis()

}