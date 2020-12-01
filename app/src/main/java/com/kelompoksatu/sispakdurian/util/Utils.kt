package com.kelompoksatu.sispakdurian.util

import com.kelompoksatu.sispakdurian.ui.diagnosisresult.data.*

object Utils {

    fun printList(listString: List<String>): String {
        var output = ""
        var index = 0
        for (data in listString) {
            if (index != 0) {
                output = "$output $data"
            }
            index++
        }
        return output
    }

    fun convertPercentageToInformation(num: Double): String {
        if (num > 90){
            return "Pasti"
        } else if (num > 80){
            return "Hampir Pasti"
        } else if (num > 60){
            return "Kemungkinan Besar"
        } else if (num > 40){
            return "Mungkin"
        } else {
            return "Tidak"
        }
    }

    fun getGejalaDanCaraPenanganan(label : String):String{
        var penanganan = Penanganan("","")
        when (label.toLowerCase()){
            "kutu loncat"-> penanganan = kutuLoncat
            "lebah mini"-> penanganan = lebahMini
            "penggerek buah"-> penanganan = penggerekBuah
            "embug"-> penanganan = embug
            "ulat penggerek bunga"-> penanganan = ulatPenggerekBunga
            "ulat daun"-> penanganan = ulatDaun
            "rayap"-> penanganan = rayap
            "kutu putih"-> penanganan = kutuPutih
            "penggerek batang"-> penanganan = penggerekBatang
            "jamur daun"-> penanganan = jamurDaun
            "busuk akar"-> penanganan = busukAkar
            "kanker batang" -> penanganan = kankerBatang
            "jamus upas" -> penanganan = jamurUpas
            "busuk buah" -> penanganan = busukBuah
            "kanker bercak" -> penanganan = kankerBercak
        }
        return "Gejala :\n" +
                penanganan.gejala + "\n\n" +
                "Cara Penanganan :\n" +
                penanganan.cara
    }

}