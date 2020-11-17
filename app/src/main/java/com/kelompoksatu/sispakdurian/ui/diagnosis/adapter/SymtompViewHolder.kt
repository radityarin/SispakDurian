package com.kelompoksatu.sispakdurian.ui.diagnosis.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.kelompoksatu.sispakdurian.databinding.ItemSymptompsBinding
import com.kelompoksatu.sispakdurian.ui.diagnosis.model.Symptomp

class SymtompViewHolder(val binding: ItemSymptompsBinding) : RecyclerView.ViewHolder(binding.root) {

    fun bind(model: Symptomp) {
        binding.symptomp = model
    }

    companion object {
        fun from(parent: ViewGroup): SymtompViewHolder {
            val inflater = LayoutInflater.from(parent.context)
            val binding: ItemSymptompsBinding = ItemSymptompsBinding.inflate(inflater, parent, false)
            return SymtompViewHolder(binding)
        }
    }
}