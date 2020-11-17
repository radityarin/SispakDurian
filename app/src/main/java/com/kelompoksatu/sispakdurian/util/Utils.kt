package com.kelompoksatu.sispakdurian.util

object Utils {

    fun generateRandomInt(digits: Int): String {
        try {
            val str = StringBuilder()
            for (i in 0 until digits) {
                str.append((0..9).random())
            }
            return str.toString()
        } catch (e: Exception) {
            return ""
        }
    }

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

}