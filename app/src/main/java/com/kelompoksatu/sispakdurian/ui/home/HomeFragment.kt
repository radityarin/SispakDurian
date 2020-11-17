package com.kelompoksatu.sispakdurian.ui.home

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.navigation.findNavController
import androidx.navigation.fragment.findNavController
import com.kelompoksatu.sispakdurian.databinding.FragmentHomeBinding
import com.kelompoksatu.sispakdurian.util.Constant.HAMA
import com.kelompoksatu.sispakdurian.util.Constant.PENYAKIT

class HomeFragment : Fragment() {
    private lateinit var binding: FragmentHomeBinding

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        binding = FragmentHomeBinding.inflate(inflater, container, false)
        binding.lifecycleOwner = this
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        with(binding){
            mcvDiagnosisHama.setOnClickListener {
                val action = HomeFragmentDirections.actionHomeFragmentToDiagnosisFragment(HAMA)
                findNavController().navigate(action)
            }
            mcvDiagnosisPenyakit.setOnClickListener {
                val action = HomeFragmentDirections.actionHomeFragmentToDiagnosisFragment(PENYAKIT)
                findNavController().navigate(action)
            }
            mcvRiwayatDiagnosis.setOnClickListener {
                val action = HomeFragmentDirections.actionHomeFragmentToHistoryFragment()
                findNavController().navigate(action)
            }
            mcvInformasiHamaDurian.setOnClickListener {
                val action = HomeFragmentDirections.actionHomeFragmentToInformationFragment(HAMA)
                findNavController().navigate(action)
            }
            mcvInformasiPenyakitDurian.setOnClickListener {
                val action = HomeFragmentDirections.actionHomeFragmentToInformationFragment(PENYAKIT)
                findNavController().navigate(action)
            }
        }
    }

}