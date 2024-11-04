package com.example.project

import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import android.os.AsyncTask
import android.os.Bundle
import android.util.Log
import android.widget.AdapterView
import android.widget.ImageButton
import android.widget.ListView
import android.widget.SearchView
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import org.json.JSONArray
import java.net.HttpURLConnection
import java.net.URL
import java.text.SimpleDateFormat
import java.util.*

class ArticlesListActivity : AppCompatActivity() {
    private lateinit var sharedPreferences: SharedPreferences
    private lateinit var headerText: TextView
    private lateinit var dateText: TextView
    private lateinit var articlesList: ListView
    private lateinit var articleListAdapter: ArticleListAdapter
    private lateinit var searchView: SearchView
    private var originalArticles = mutableListOf<Article>()
    private var filteredArticles = mutableListOf<Article>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_articles_list)

        sharedPreferences = getSharedPreferences("user_prefs", Context.MODE_PRIVATE)
        val username = sharedPreferences.getString("username", "User") ?: "User"

        // Initialize views
        headerText = findViewById(R.id.header_text)
        headerText.text = username

        dateText = findViewById(R.id.date_text)
        dateText.text = getCurrentDate()

        articlesList = findViewById(R.id.articles_list)

        // Initialize search view
        searchView = findViewById(R.id.search_view)
        searchView.setOnQueryTextListener(object : SearchView.OnQueryTextListener {
            override fun onQueryTextSubmit(query: String?): Boolean {
                return false
            }

            override fun onQueryTextChange(newText: String?): Boolean {
                filteredArticles = if (newText.isNullOrEmpty()) {
                    originalArticles
                } else {
                    originalArticles.filter {
                        it.title.contains(newText, ignoreCase = true) ||
                                it.authors.contains(newText, ignoreCase = true)
                    }.toMutableList()
                }
                articleListAdapter.updateArticles(filteredArticles)
                return true
            }
        })

        val homeButton = findViewById<ImageButton>(R.id.homeButton)
        val logoutButton = findViewById<ImageButton>(R.id.logoutButton)
        val messagesButton = findViewById<ImageButton>(R.id.messageButton)

        messagesButton.setOnClickListener {
            val intent = Intent(this, UserRequestsActivity::class.java)
            startActivity(intent)
        }

        homeButton.setOnClickListener {
            val intent = Intent(this, HomeActivity::class.java)
            startActivity(intent)
        }
        logoutButton.setOnClickListener {
            val intent = Intent(this, MainActivity::class.java)
            startActivity(intent)
        }
        articlesList.onItemClickListener = AdapterView.OnItemClickListener { _, _, position, _ ->
            val intent = Intent(this, ArticleDetailActivity::class.java)
            intent.putExtra("ARTICLE_ID", filteredArticles[position].id)
            startActivity(intent)
        }
        // Fetch articles from the server
        FetchArticlesTask().execute("http://10.0.2.2/project_scientific_conferences/app/get_articles.php")
    }

    private fun getCurrentDate(): String {
        val dateFormat = SimpleDateFormat("MMMM dd, yyyy", Locale.getDefault())
        return dateFormat.format(Date())
    }

    private inner class FetchArticlesTask : AsyncTask<String, Void, List<Article>>() {
        override fun doInBackground(vararg urls: String?): List<Article> {
            val url = URL(urls[0])
            val connection = url.openConnection() as HttpURLConnection
            connection.requestMethod = "GET"
            connection.connect()

            val inputStream = connection.inputStream
            val jsonResponse = inputStream.bufferedReader().use { it.readText() }

            val jsonArray = JSONArray(jsonResponse)
            val articlesList = mutableListOf<Article>()
            for (i in 0 until jsonArray.length()) {
                val jsonObject = jsonArray.getJSONObject(i)
                val article = Article(
                    jsonObject.getInt("id"),
                    jsonObject.getString("title"),
                    jsonObject.getString("authors")
                )
                articlesList.add(article)
            }
            Log.d("FetchArticlesTask", "Fetched ${articlesList.size} articles")
            return articlesList
        }

        override fun onPostExecute(result: List<Article>?) {
            if (result != null) {
                originalArticles.clear()
                originalArticles.addAll(result.toMutableList())
                filteredArticles.clear()
                filteredArticles.addAll(result)
                Log.d("ArticlesListActivity", "Articles fetched and updated: ${originalArticles.size}")

                articleListAdapter = ArticleListAdapter(this@ArticlesListActivity, filteredArticles)
                articlesList.adapter = articleListAdapter
            } else {
                Log.e("ArticlesListActivity", "Failed to fetch articles")
            }
        }
    }
}
