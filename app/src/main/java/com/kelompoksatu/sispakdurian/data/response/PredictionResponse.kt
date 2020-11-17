package com.kelompoksatu.sispakdurian.data.response

import com.google.gson.annotations.SerializedName
import com.kelompoksatu.sispakdurian.data.model.Diagnosis

data class PredictionResponse(
    @SerializedName("data")
    var diagnosis: Diagnosis,
    @SerializedName("message")
    var message: String,
    @SerializedName("success")
    var success: Boolean
)