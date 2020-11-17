package com.kelompoksatu.sispakdurian.ui.history.adapter

import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.kelompoksatu.sispakdurian.data.model.Diagnosis


class DiagnosisHistoryAdapter : RecyclerView.Adapter<DiagnosisHistoryViewHolder>() {

    private val items = mutableListOf<Diagnosis>()

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): DiagnosisHistoryViewHolder {
        return DiagnosisHistoryViewHolder.from(parent)
    }

    override fun onBindViewHolder(holder: DiagnosisHistoryViewHolder, position: Int) {
        val model = items[position]
        holder.bind(model)
    }

    override fun getItemCount() = items.size

    fun submitList(data: List<Diagnosis>) {
        items.clear()
        items.addAll(data)
        notifyDataSetChanged()
    }


}