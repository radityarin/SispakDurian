package com.kelompoksatu.sispakdurian.ui.diagnosis.views

import android.content.ContentValues.TAG
import android.os.Bundle
import android.os.Handler
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import androidx.navigation.fragment.findNavController
import androidx.navigation.fragment.navArgs
import com.google.gson.Gson
import com.kelompoksatu.sispakdurian.R
import com.kelompoksatu.sispakdurian.data.model.Diagnosis
import com.kelompoksatu.sispakdurian.data.response.PredictionResponse
import com.kelompoksatu.sispakdurian.databinding.FragmentDiagnosisBinding
import com.kelompoksatu.sispakdurian.ui.diagnosis.adapter.SymptompsAdapter
import com.kelompoksatu.sispakdurian.ui.diagnosis.model.Symptomp
import com.kelompoksatu.sispakdurian.ui.diagnosis.viewmodel.AskViewModel
import com.kelompoksatu.sispakdurian.util.Constant.HAMA
import com.kelompoksatu.sispakdurian.util.Constant.PENYAKIT
import com.kelompoksatu.sispakdurian.util.CustomProgressDialog
import org.koin.androidx.viewmodel.ext.android.viewModel

class DiagnosisFragment : Fragment() {

    private val viewModel by viewModel<AskViewModel>()
    private lateinit var binding: FragmentDiagnosisBinding
    private lateinit var symptompsAdapter: SymptompsAdapter
    private val args: DiagnosisFragmentArgs by navArgs()
    private lateinit var progressDialog: CustomProgressDialog
    private lateinit var handler: Handler

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        binding = FragmentDiagnosisBinding.inflate(inflater, container, false)
        binding.lifecycleOwner = this
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        initView()
        observeLiveData()
        setupRecyclerView()
        handler = Handler()
    }

    private fun setupRecyclerView() {
        symptompsAdapter = SymptompsAdapter()
        binding.rvSymptomp.adapter = symptompsAdapter
        showDummyData()
    }

    private fun showDummyData() {
        var listGejala = mutableListOf<Symptomp>()
        when (args.type) {
            HAMA -> {
                listGejala.add(Symptomp("Bintik-bintik berwarna kecokelatan pada daun", "0"))
                listGejala.add(Symptomp("Daun keriting", "0"))
                listGejala.add(Symptomp("Berukuran kerdil", "0"))
                listGejala.add(Symptomp("Adanya luka gerekan pada daun dan ranting muda", "0"))
                listGejala.add(Symptomp("Pertumbuhan pohon durian sangat lama", "0"))
                listGejala.add(
                    Symptomp(
                        "Daun secara perlahan layu dan mengering diikuti oleh ranting dan batang",
                        "0"
                    )
                )
                listGejala.add(
                    Symptomp(
                        "Daun yang kering tidak jatuh semua melainkan masih melekat pada tangkainya",
                        "0"
                    )
                )
                listGejala.add(Symptomp("Bunga atau buah mengalami kerontokan", "0"))
                listGejala.add(Symptomp("Adanya kotoran dibawah batang", "0"))
                listGejala.add(
                    Symptomp(
                        "Rusaknya kuncup bunga sehingga putik bunga berguguran",
                        "0"
                    )
                )
                listGejala.add(Symptomp("Rusaknya benang sari dan tajuk bunga", "0"))
                listGejala.add(Symptomp("Kuncup dan putik patah karena luka digerek", "0"))
                listGejala.add(Symptomp("Daun berlubang", "0"))
                listGejala.add(
                    Symptomp(
                        "Adanya alur dari tanah yang menempel di bagian batang",
                        "0"
                    )
                )
                listGejala.add(Symptomp("Kulit dan duri buah menjadi hitam seperti busuk", "0"))
                listGejala.add(Symptomp("Buah jatuh sebelum tua", "0"))
            }
            PENYAKIT -> {
                listGejala.add(Symptomp("Daun menguning", "0"))
                listGejala.add(Symptomp("Daun berguguran", "0"))
                listGejala.add(Symptomp("Bercak yang berawal dari ujung akar lateral", "0"))
                listGejala.add(Symptomp("Jaringan akar berwarna cokelat", "0"))
                listGejala.add(
                    Symptomp(
                        "Bekas luka pada batang seperti blendok berwarna coklat kemerahan",
                        "0"
                    )
                )
                listGejala.add(Symptomp("Terdapat kerak berwarna merah jambu", "0"))
                listGejala.add(
                    Symptomp(
                        "Bercak – bercak berwarna cokelat kehitaman dan basah pada kulit buah",
                        "0"
                    )
                )
                listGejala.add(Symptomp("Tanaman terlihat layu", "0"))
                listGejala.add(Symptomp("Tumbuh spora berwarna putih disekitar bawah daun", "0"))
            }
        }
        symptompsAdapter.submitList(listGejala)
        symptompsAdapter.resetCurrentData()
    }

    private fun initView() {
        progressDialog = CustomProgressDialog(
            requireContext(),
            getString(R.string.processing)
        )
        when (args.type) {
            HAMA -> {
                binding.tvTitle.text = "Pilih Gejala " + HAMA
            }
            PENYAKIT -> {
                binding.tvTitle.text = "Pilih Gejala " + PENYAKIT
            }
        }
        with(binding) {
            mbDiagnosis.setOnClickListener {
                progressDialog.show()
                diagnose()
            }
            tvBack.setOnClickListener {
                requireActivity().onBackPressed()
            }
            mbReset.setOnClickListener {
                showDummyData()
            }
        }
    }

    private fun observeLiveData() {
        viewModel.output.observe(viewLifecycleOwner, Observer {
            val diagnosis: PredictionResponse = Gson().fromJson(it, PredictionResponse::class.java)
            onDataLoaded(diagnosis.diagnosis)
        })
    }

    private fun onDataLoaded(diagnosis: Diagnosis) {
        progressDialog.dismiss()
        viewModel.insertDiagnosis(diagnosis)
        val action =
            DiagnosisFragmentDirections.actionDiagnosisFragmentToDiagnosisResultFragment(diagnosis)
        findNavController().navigate(action)
    }

    private fun diagnose() {
        val usedSymtomps = symptompsAdapter.getUsedSymptomps()
        val certaintyFactor = symptompsAdapter.getCertaintyFactor()
        Log.d(TAG, "diagnose: " + usedSymtomps)
        Log.d(TAG, "diagnose: " + certaintyFactor)
        handler.postDelayed({
            when (args.type) {
                HAMA -> {
                    viewModel.diagnosa(HAMA, usedSymtomps, certaintyFactor, requireContext())
                }
                PENYAKIT -> {
                    viewModel.diagnosa(PENYAKIT, usedSymtomps, certaintyFactor, requireContext())
                }
            }
        }, 500)

    }
}