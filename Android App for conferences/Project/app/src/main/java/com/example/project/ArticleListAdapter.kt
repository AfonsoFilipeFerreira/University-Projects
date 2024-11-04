package com.example.project

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import android.widget.TextView

class ArticleListAdapter(private val context: Context, private var articles: MutableList<Article>) : BaseAdapter() {

    override fun getCount(): Int {
        return articles.size
    }

    override fun getItem(position: Int): Article {
        return articles[position]
    }

    override fun getItemId(position: Int): Long {
        return position.toLong()
    }

    override fun getView(position: Int, convertView: View?, parent: ViewGroup): View {
        var listItemView = convertView
        if (listItemView == null) {
            listItemView = LayoutInflater.from(context).inflate(R.layout.article_list_item, parent, false)
        }

        val article = getItem(position)

        val titleTextView = listItemView!!.findViewById<TextView>(R.id.titleTextView)
        val authorsTextView = listItemView.findViewById<TextView>(R.id.authorsTextView)

        titleTextView.text = article.title
        authorsTextView.text = article.authors

        return listItemView
    }

    fun updateArticles(newArticles: List<Article>) {
        articles.clear()
        articles.addAll(newArticles)
        notifyDataSetChanged()
    }
}