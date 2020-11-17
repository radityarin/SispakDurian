package com.kelompoksatu.sispakdurian.ui.splash

import android.content.Intent
import android.os.Bundle
import android.view.View
import androidx.appcompat.app.AppCompatActivity
import com.kelompoksatu.sispakdurian.R
import com.kelompoksatu.sispakdurian.ui.onboarding.OnBoardingScreen

class SplashActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)
    }
    fun toOnBoardingScreen(v: View?) {
        Intent(this@SplashActivity, OnBoardingScreen::class.java).also {
            startActivity(it)
            finish()
        }
    }

}