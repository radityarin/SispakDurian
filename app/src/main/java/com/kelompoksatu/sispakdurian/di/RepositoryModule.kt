package com.kelompoksatu.sispakdurian.di

import com.kelompoksatu.sispakdurian.data.repository.AppRepository
import org.koin.android.ext.koin.androidContext
import org.koin.dsl.module

val repositoryModule = module {
    factory {
        AppRepository(this.androidContext())
    }
}