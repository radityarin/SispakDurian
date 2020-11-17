package com.kelompoksatu.sispakdurian.ui.onboarding

import android.content.Intent
import android.graphics.Color
import android.os.Bundle
import androidx.core.content.ContextCompat
import androidx.fragment.app.Fragment
import com.github.appintro.AppIntro2
import com.github.appintro.AppIntroFragment
import com.kelompoksatu.sispakdurian.R
import com.kelompoksatu.sispakdurian.ui.main.MainActivity

class OnBoardingScreen : AppIntro2() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Make sure you don't call setContentView!

        // Call addSlide passing your Fragments.
        // You can use AppIntroFragment to use a pre-built fragment
        addSlide(
            AppIntroFragment.newInstance(
                imageDrawable = R.drawable.ic_step_1,
                description = "Membantu diagnosis hama dan\n" +
                        "penyakit yang terjadi pada tanaman\n" +
                        "durian anda",
                backgroundColor = Color.WHITE,
                descriptionColor = Color.BLACK
            )
        )
        addSlide(
            AppIntroFragment.newInstance(
                imageDrawable = R.drawable.ic_step_2,
                description = "Membantu memberikan cara penanganan\n" +
                        "hama dan penyakit tanaman durian\n" +
                        "anda",
                backgroundColor = Color.WHITE,
                descriptionColor = Color.BLACK
            )
        )
        addSlide(
            AppIntroFragment.newInstance(
                imageDrawable = R.drawable.ic_step_3,
                description = "Memberikan nilai keyakinan seorang\n" +
                        "pakar untuk diagnosis hama penyakit\n" +
                        "tanaman durian anda",
                backgroundColor = Color.WHITE,
                descriptionColor = Color.BLACK
            )
        )
        isIndicatorEnabled = true

        setIndicatorColor(
            selectedIndicatorColor = ContextCompat.getColor(this,R.color.primary),
            unselectedIndicatorColor = ContextCompat.getColor(this,R.color.primary_fade)
        )
    }

    override fun onSkipPressed(currentFragment: Fragment?) {
        super.onSkipPressed(currentFragment)

        Intent(this, MainActivity::class.java).also {
            startActivity(it)
            finish()
        }
    }

    override fun onDonePressed(currentFragment: Fragment?) {
        super.onDonePressed(currentFragment)

        Intent(this, MainActivity::class.java).also {
            startActivity(it)
            finish()
        }
    }
}