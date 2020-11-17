package com.kelompoksatu.sispakdurian.ui.history.views

import android.app.Dialog
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.view.Window
import androidx.fragment.app.Fragment
import androidx.lifecycle.Observer
import com.kelompoksatu.sispakdurian.R
import com.kelompoksatu.sispakdurian.databinding.FragmentHistoryBinding
import com.kelompoksatu.sispakdurian.ui.diagnosis.viewmodel.AskViewModel
import com.kelompoksatu.sispakdurian.ui.history.adapter.DiagnosisHistoryAdapter
import kotlinx.android.synthetic.main.dialog_clear_history.*
import org.koin.androidx.viewmodel.ext.android.viewModel

class HistoryFragment : Fragment() {
    private lateinit var binding: FragmentHistoryBinding
    private val viewModel by viewModel<AskViewModel>()
    private lateinit var diagnosisHistoryAdapter: DiagnosisHistoryAdapter

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        binding = FragmentHistoryBinding.inflate(inflater, container, false)
        binding.lifecycleOwner = this
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        initView()
        setupRecyclerView()
        observe()
    }

    private fun initView() {
        with(binding) {
            tvBack.setOnClickListener {
                requireActivity().onBackPressed()
            }
            mbClearHistory.setOnClickListener {
                showDialogDelete()
            }
        }
    }

    private fun observe() {
        viewModel.getDiagnosisHistory()?.observe(viewLifecycleOwner, Observer {
            if (it.isEmpty()){
                binding.llNoHistory.visibility = View.VISIBLE
            }
            diagnosisHistoryAdapter.submitList(it)
        })
    }

    private fun setupRecyclerView() {
        diagnosisHistoryAdapter = DiagnosisHistoryAdapter()
        binding.rvHistoryDiagnosis.adapter = diagnosisHistoryAdapter
    }

    private fun showDialogDelete() {
        val dialog = Dialog(binding.root.context)
        dialog.window?.setBackgroundDrawableResource(android.R.color.transparent)
        dialog.requestWindowFeature(Window.FEATURE_NO_TITLE)
        dialog.setCancelable(false)
        dialog.setContentView(R.layout.dialog_clear_history)

        dialog.btnDeleteItem.setOnClickListener {
            viewModel.deleteDiagnosisHistory()
            diagnosisHistoryAdapter.notifyDataSetChanged()
            dialog.dismiss()
        }
        dialog.btnCancel.setOnClickListener {
            dialog.dismiss()
        }
        dialog.show()
    }
}