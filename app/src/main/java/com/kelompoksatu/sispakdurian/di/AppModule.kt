package com.kelompoksatu.sispakdurian.di

import com.kelompoksatu.sispakdurian.R
import org.koin.dsl.module
import uk.co.chrisjenx.calligraphy.CalligraphyConfig

const val DEFAULT_FONT = "assets/onts/GoogleSans-Regular.ttf"

val appModule = module {

    single {
        CalligraphyConfig.Builder()
            .setDefaultFontPath(DEFAULT_FONT)
            .setFontAttrId(R.attr.fontPath)
            .build()
    }

}