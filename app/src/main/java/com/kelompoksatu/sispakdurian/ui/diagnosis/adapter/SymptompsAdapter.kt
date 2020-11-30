package com.kelompoksatu.sispakdurian.ui.diagnosis.adapter

import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.kelompoksatu.sispakdurian.R
import com.kelompoksatu.sispakdurian.ui.diagnosis.model.Symptomp
import kotlinx.android.synthetic.main.item_symptomps.view.*

class SymptompsAdapter : RecyclerView.Adapter<SymtompViewHolder>() {

    private val items = mutableListOf<Symptomp>()
    private val symptompsCode = listOf(
        "G1",
        "G2",
        "G3",
        "G4",
        "G5",
        "G6",
        "G7",
        "G8",
        "G9",
        "G10",
        "G11",
        "G12",
        "G13",
        "G14",
        "G15",
        "G16"
    )
    private var certaintyFactor = mutableListOf(
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
    )
    private val usedSymptomps = mutableListOf<String>()

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): SymtompViewHolder {
        return SymtompViewHolder.from(parent)
    }

    override fun onBindViewHolder(holder: SymtompViewHolder, position: Int) {
        val model = items[position]
        holder.bind(model)
        holder.itemView.setOnClickListener {
            when (holder.itemView.rgOptionGroup.visibility == View.GONE) {
                true -> {
                    holder.itemView.rgOptionGroup.visibility = View.VISIBLE
                }
                false -> {
                    holder.itemView.rgOptionGroup.visibility = View.GONE
                }
            }
            if (holder.itemView.rgOptionGroup.checkedRadioButtonId > 0) {
                holder.itemView.tvName.setCompoundDrawablesWithIntrinsicBounds(
                    0,
                    0,
                    R.drawable.ic_baseline_check_24,
                    0
                )
            }
        }
        holder.itemView.rgOptionGroup.setOnCheckedChangeListener { _, checkedId ->
            when (checkedId) {
                R.id.rg0 -> {
                    certaintyFactor[position] = 0.0
                }
                R.id.rg1 -> {
                    certaintyFactor[position] = 0.4
                    usedSymptomps.add(symptompsCode[position])
                }
                R.id.rg2 -> {
                    certaintyFactor[position] = 0.6
                    usedSymptomps.add(symptompsCode[position])
                }
                R.id.rg3 -> {
                    certaintyFactor[position] = 0.8
                    usedSymptomps.add(symptompsCode[position])
                }
                R.id.rg4 -> {
                    certaintyFactor[position] = 0.9
                    usedSymptomps.add(symptompsCode[position])
                }
            }
        }
    }

    override fun getItemCount() = items.size

    fun submitList(data: List<Symptomp>) {
        items.clear()
        items.addAll(data)
        notifyDataSetChanged()
    }

    fun resetCurrentData() {
        certaintyFactor = mutableListOf(
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0
        )
        usedSymptomps.clear()
        notifyDataSetChanged()
    }

    fun getCertaintyFactor(): List<Double> {
        return certaintyFactor
    }

    fun getUsedSymptomps(): List<String> {
        return usedSymptomps.distinct()
    }

}