package com.kelompoksatu.sispakdurian.data.model


import android.os.Parcelable
import androidx.room.Entity
import androidx.room.PrimaryKey
import com.google.gson.annotations.SerializedName
import kotlinx.android.parcel.Parcelize

@Parcelize
@Entity(tableName = "diagnosis")
data class Diagnosis(
    @PrimaryKey
    @SerializedName("id_prediction")
    var idPrediction: String,
    @SerializedName("timestamps")
    var timestamps: String,
    @SerializedName("cf")
    var cf: Double,
    @SerializedName("classification_result")
    var classificationResult: String,
    @SerializedName("posterior")
    var posterior: Double,
    @SerializedName("input_symptomps")
    var inputSymptomps: List<String>,
    @SerializedName("type")
    var type: String
) : Parcelable