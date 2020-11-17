package com.kelompoksatu.sispakdurian.di

import com.kelompoksatu.sispakdurian.ui.diagnosis.viewmodel.AskViewModel
import org.koin.androidx.viewmodel.dsl.viewModel
import org.koin.dsl.module

val viewModelModule = module {
    viewModel {
        AskViewModel(
            get()
        )
    }
}