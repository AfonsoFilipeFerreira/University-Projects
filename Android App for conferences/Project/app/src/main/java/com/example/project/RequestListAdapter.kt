package com.example.project

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import android.widget.TextView

class RequestListAdapter(private val context: Context, private val requestList: List<RequestItem>) : BaseAdapter() {

    override fun getCount(): Int {
        return requestList.size
    }

    override fun getItem(position: Int): Any {
        return requestList[position]
    }

    override fun getItemId(position: Int): Long {
        return position.toLong()
    }

    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        var view = convertView
        val holder: ViewHolder

        if (view == null) {
            view = LayoutInflater.from(context).inflate(R.layout.request_item, parent, false)
            holder = ViewHolder()
            holder.messageTextView = view.findViewById(R.id.message_text_view)
            holder.answeredTextView = view.findViewById(R.id.answered_text_view)
            holder.replyTextView = view.findViewById(R.id.reply_text_view)
            view.tag = holder
        } else {
            holder = view.tag as ViewHolder
        }

        val requestItem = requestList[position]
        holder.messageTextView.text = requestItem.message
        holder.answeredTextView.text = if (requestItem.answered == 1) "Answered" else "Not Answered"
        holder.replyTextView.text = requestItem.replyMessage

        return view!!
    }

    private class ViewHolder {
        lateinit var messageTextView: TextView
        lateinit var answeredTextView: TextView
        lateinit var replyTextView: TextView
    }
}
