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
    @SerializedName("cf_max")
    var cfMax: Double,
    @SerializedName("cf_min")
    var cfMin: Double,
    @SerializedName("classification_result_max")
    var classificationResultMax: String,
    @SerializedName("classification_result_min")
    var classificationResultMin: String,
    @SerializedName("input_symptomps")
    var inputSymptomps: List<String>,
    @SerializedName("posterior_max")
    var posteriorMax: Double,
    @SerializedName("posterior_min")
    var posteriorMin: Double,
    @SerializedName("timestamps")
    var timestamps: String,
    @SerializedName("type")
    var type: String
) : Parcelable