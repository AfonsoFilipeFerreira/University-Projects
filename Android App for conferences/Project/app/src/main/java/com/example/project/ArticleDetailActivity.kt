package com.example.project

import android.content.ActivityNotFoundException
import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import android.graphics.Color
import android.graphics.Typeface
import android.net.Uri
import android.os.AsyncTask
import android.os.Bundle
import android.text.SpannableString
import android.text.SpannableStringBuilder
import android.text.style.StyleSpan
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.ImageButton
import android.widget.LinearLayout
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.text.HtmlCompat
import com.android.volley.Request
import com.android.volley.RequestQueue
import com.android.volley.Response
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import org.json.JSONArray
import org.json.JSONException
import org.json.JSONObject
import java.io.BufferedReader
import java.io.InputStreamReader
import java.net.HttpURLConnection
import java.net.URL
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

class ArticleDetailActivity : AppCompatActivity() {
    // Declare views and variables
    private lateinit var sharedPreferences: SharedPreferences
    private lateinit var headerText: TextView
    private lateinit var dateText: TextView
    private lateinit var titleText: TextView
    private lateinit var authorsText: TextView
    private lateinit var abstractText: TextView
    private lateinit var pdfButton: Button
    private lateinit var requestQueue: RequestQueue

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_article_detail)

        requestQueue = Volley.newRequestQueue(applicationContext)

        // Initialize SharedPreferences and views
        sharedPreferences = getSharedPreferences("user_prefs", Context.MODE_PRIVATE)
        val username = sharedPreferences.getString("username", "User") ?: "User"
        Log.d("ArticleDetailActivity", "Username: $username")

        // Set username in header view
        headerText = findViewById(R.id.header_text)
        headerText.text = username

        // Set current date
        dateText = findViewById(R.id.date_text)
        dateText.text = getCurrentDate()

        // Initialize other views
        titleText = findViewById(R.id.page)
        authorsText = findViewById(R.id.article_authors)
        abstractText = findViewById(R.id.article_abstract)
        pdfButton = findViewById(R.id.pdf_button)

        // Set listeners for navigation buttons
        val homeButton = findViewById<ImageButton>(R.id.homeButton)
        val logoutButton = findViewById<ImageButton>(R.id.logoutButton)
        val pdfButton = findViewById<Button>(R.id.pdf_button)
        val postCommentButton = findViewById<Button>(R.id.post_comment_button)
        val messagesButton = findViewById<ImageButton>(R.id.messageButton)

        messagesButton.setOnClickListener {
            val intent = Intent(this, UserRequestsActivity::class.java)
            startActivity(intent)
        }

        // Handle PDF button click
        pdfButton.setOnClickListener {
            // Open the PDF link if available
            val articleDetail = pdfButton.tag as? ArticleDetail
            articleDetail?.let {
                val pdfLink = it.pdfLink
                if (!pdfLink.isNullOrBlank()) { // Check if pdfLink is not null or blank
                    openPdfInBrowser(pdfLink)
                } else {
                    Toast.makeText(this, "PDF link not found", Toast.LENGTH_SHORT).show()
                }
            } ?: run {
                Toast.makeText(this, "PDF link not found", Toast.LENGTH_SHORT).show()
            }
        }

        // Set listener for post comment button
        postCommentButton.setOnClickListener {
            val commentInput = findViewById<EditText>(R.id.comment_input).text.toString().trim()
            if (commentInput.isNotEmpty()) {
                val articleId = intent.getIntExtra("ARTICLE_ID", -1)
                if (articleId != -1) {
                    // Call PostCommentTask asynchronously
                    PostCommentTask().execute(articleId.toString(), commentInput, username)
                } else {
                    Toast.makeText(this@ArticleDetailActivity, "Article ID not found", Toast.LENGTH_SHORT).show()
                    Log.e("PostCommentButton", "Article ID not found in intent extras")
                }
            } else {
                Toast.makeText(this@ArticleDetailActivity, "Please enter a comment", Toast.LENGTH_SHORT).show()
            }
        }


        // Navigate to home screen
        homeButton.setOnClickListener {
            val intent = Intent(this, HomeActivity::class.java)
            startActivity(intent)
        }

        // Logout user and navigate to login screen
        logoutButton.setOnClickListener {
            val intent = Intent(this, MainActivity::class.java)
            startActivity(intent)
        }

        // Fetch article details based on article ID passed via intent extras
        val articleId = intent.getIntExtra("ARTICLE_ID", -1)
        if (articleId != -1) {
            Log.d("ArticleDetailActivity", "Fetching article details for ID: $articleId")
            FetchArticleDetailTask().execute("http://10.0.2.2/project_scientific_conferences/app/get_article_detail.php?id=$articleId")
        } else {
            Toast.makeText(this, "Article ID not found", Toast.LENGTH_SHORT).show()
            Log.e("ArticleDetailActivity", "Article ID not found in intent extras")
            finish() // Close the activity if no article ID is provided
        }
    }

    // AsyncTask to fetch article details from the server
    private inner class FetchArticleDetailTask : AsyncTask<String, Void, ArticleDetail?>() {
        override fun doInBackground(vararg urls: String?): ArticleDetail? {
            return try {
                val url = URL(urls[0])
                val connection = url.openConnection() as HttpURLConnection
                connection.requestMethod = "GET"
                connection.connect()

                val inputStream = connection.inputStream
                val reader = BufferedReader(InputStreamReader(inputStream))
                val response = StringBuilder()
                var line: String?

                while (reader.readLine().also { line = it } != null) {
                    response.append(line)
                }

                reader.close()
                parseJsonResponse(response.toString())
            } catch (e: Exception) {
                Log.e("FetchArticleDetailTask", "Error fetching article details", e)
                null
            }
        }

        // Parse JSON response and return ArticleDetail object
        private fun parseJsonResponse(jsonResponse: String): ArticleDetail? {
            return try {
                val jsonObject = JSONObject(jsonResponse)
                ArticleDetail(
                    jsonObject.getInt("id"),
                    jsonObject.getString("title"),
                    jsonObject.getString("authors"),
                    jsonObject.getString("abstract"),
                    jsonObject.getString("pdf_link")
                )
            } catch (e: JSONException) {
                Log.e("FetchArticleDetailTask", "Error parsing JSON response", e)
                null
            }
        }

        // Update UI with fetched article details
        override fun onPostExecute(result: ArticleDetail?) {
            if (result != null) {
                Log.d("FetchArticleDetailTask", "Article details fetched: $result")
                titleText.text = result.title
                authorsText.text = result.authors
                abstractText.text = HtmlCompat.fromHtml("<html><body style='text-align:justify;'>${result.abstract}</body></html>", HtmlCompat.FROM_HTML_MODE_LEGACY)
                // Store ArticleDetail object in pdfButton's tag for later use
                pdfButton.tag = result

                // Fetch approved comments for the article
                fetchApprovedComments()
            } else {
                Toast.makeText(this@ArticleDetailActivity, "Error loading article details", Toast.LENGTH_SHORT).show()
                Log.e("FetchArticleDetailTask", "Article detail result is null")
            }
        }
    }
    // Remove references to user_id in PostCommentTask

    private inner class PostCommentTask : AsyncTask<String, Void, Boolean>() {
        override fun doInBackground(vararg params: String?): Boolean {
            val username = sharedPreferences.getString("username", "User") ?: "User"
            Log.d("PostCommentTask", "Username: $username")
            if (username.isEmpty()) return false // Handle if username is not available
            val articleId = params[0]?.toIntOrNull() ?: return false
            val message = params[1] ?: return false

            val url = "http://10.0.2.2/project_scientific_conferences/app/post_comment.php"

            val stringRequest = object : StringRequest(
                Request.Method.POST, url,
                Response.Listener { response ->
                    try {
                        val jsonResponse = JSONObject(response)
                        val status = jsonResponse.getString("status")
                        if (status == "success") {
                            Toast.makeText(this@ArticleDetailActivity, "Comment submitted for approval", Toast.LENGTH_SHORT).show()
                            // Clear comment input field if needed
                            findViewById<EditText>(R.id.comment_input).setText("")
                            // Refresh comments section if needed
                            fetchApprovedComments()
                        } else {
                            Toast.makeText(this@ArticleDetailActivity, "Failed to submit comment", Toast.LENGTH_SHORT).show()
                        }
                    } catch (e: JSONException) {
                        Toast.makeText(this@ArticleDetailActivity, "Error parsing response", Toast.LENGTH_SHORT).show()
                        Log.e("PostCommentTask", "Error parsing response", e)
                    }
                },
                Response.ErrorListener { error ->
                    Log.e("PostCommentTask", "Error posting comment", error)
                    Toast.makeText(this@ArticleDetailActivity, "Failed to submit comment", Toast.LENGTH_SHORT).show()
                }
            ) {
                override fun getParams(): Map<String, String> {
                    val params = HashMap<String, String>()
                    params["username"] = username
                    params["article_id"] = articleId.toString()
                    params["message"] = message
                    return params
                }
            }

            // Add the request to the RequestQueue
            requestQueue.add(stringRequest)

            return true // Assuming success as the request is queued asynchronously
        }

        override fun onPostExecute(result: Boolean) {
            super.onPostExecute(result)

            runOnUiThread {
                if (result) {
                    Toast.makeText(this@ArticleDetailActivity, "Comment submitted for approval", Toast.LENGTH_SHORT).show()
                    // Clear comment input field if needed
                    findViewById<EditText>(R.id.comment_input).setText("")
                    // Refresh comments section if needed
                    fetchApprovedComments()
                } else {
                    Toast.makeText(this@ArticleDetailActivity, "Failed to submit comment", Toast.LENGTH_SHORT).show()
                }
            }
        }
    }



    // Function to fetch approved comments from server
    private fun fetchApprovedComments() {
        // Execute AsyncTask or use Retrofit/Volley to fetch approved comments
        val articleId = intent.getIntExtra("ARTICLE_ID", -1)
        if (articleId != -1) {
            FetchCommentsTask().execute(articleId.toString())
        } else {
            Toast.makeText(this, "Article ID not found", Toast.LENGTH_SHORT).show()
        }
    }

    // AsyncTask to fetch comments from server
    private inner class FetchCommentsTask : AsyncTask<String, Void, List<Comment>>() {
        override fun doInBackground(vararg params: String?): List<Comment> {
            val articleId = params[0]?.toIntOrNull() ?: return emptyList()

            return try {
                val url = URL("http://10.0.2.2/project_scientific_conferences/app/get_comments.php?article_id=$articleId")
                val connection = url.openConnection() as HttpURLConnection
                connection.requestMethod = "GET"
                connection.connect()

                val inputStream = connection.inputStream
                val reader = BufferedReader(InputStreamReader(inputStream))
                val response = StringBuilder()
                var line: String?

                while (reader.readLine().also { line = it } != null) {
                    response.append(line)
                }

                reader.close()
                parseCommentsJson(response.toString())
            } catch (e: Exception) {
                Log.e("FetchCommentsTask", "Error fetching comments", e)
                emptyList()
            }
        }

        private fun parseCommentsJson(jsonResponse: String): List<Comment> {
            val comments = mutableListOf<Comment>()
            try {
                val jsonArray = JSONArray(jsonResponse)
                for (i in 0 until jsonArray.length()) {
                    val jsonObject = jsonArray.getJSONObject(i)
                    comments.add(
                        Comment(
                            jsonObject.getInt("id"),
                            jsonObject.getString("username"),
                            jsonObject.getInt("article_id"),
                            jsonObject.getString("message"),
                            jsonObject.getInt("approved"),
                            jsonObject.getString("created_at")
                        )
                    )
                }
            } catch (e: JSONException) {
                Log.e("FetchCommentsTask", "Error parsing JSON response", e)
            }
            return comments
        }

        override fun onPostExecute(result: List<Comment>) {
            val commentsSection = findViewById<LinearLayout>(R.id.comments_section)
            commentsSection.removeAllViews()

            if (result.isEmpty()) {
                val noCommentsText = TextView(this@ArticleDetailActivity)
                noCommentsText.text = "No comments yet."
                noCommentsText.setTextColor(Color.BLACK)
                noCommentsText.textSize = 16f
                commentsSection.addView(noCommentsText)
            } else {
                for (comment in result) {
                    val commentText = TextView(this@ArticleDetailActivity)
                    // Use SpannableStringBuilder to format the text
                    val formattedText = SpannableStringBuilder()
                    val usernameSpan = SpannableString("${comment.username}:\n")
                    usernameSpan.setSpan(StyleSpan(Typeface.BOLD), 0, usernameSpan.length, 0)
                    formattedText.append(usernameSpan)
                    formattedText.append(comment.message)

                    commentText.text = formattedText
                    commentText.setTextColor(Color.BLACK)
                    commentText.textSize = 16f

                    // Add margin to the TextView
                    val layoutParams = LinearLayout.LayoutParams(
                        LinearLayout.LayoutParams.MATCH_PARENT,
                        LinearLayout.LayoutParams.WRAP_CONTENT
                    )
                    layoutParams.setMargins(0, 0, 0, 25) // Add 16dp bottom margin for spacing between comments
                    commentText.layoutParams = layoutParams

                    commentsSection.addView(commentText)
                }
            }
        }
    }

    // Function to get the current date in the desired format
    private fun getCurrentDate(): String {
        val dateFormat = SimpleDateFormat("MMMM dd, yyyy", Locale.getDefault())
        return dateFormat.format(Date())
    }

    // Function to open PDF link in a browser
    private fun openPdfInBrowser(pdfFileName: String) {
        val baseUrl = "http://10.0.2.2/project_scientific_conferences/files/"
        val pdfLink = "$baseUrl${Uri.encode(pdfFileName)}"
        val intent = Intent(Intent.ACTION_VIEW)
        val uri = Uri.parse(pdfLink)

        // Directly open the HTTP/HTTPS link
        intent.data = uri

        try {
            startActivity(intent)
        } catch (e: ActivityNotFoundException) {
            Toast.makeText(this, "No application available to view PDF", Toast.LENGTH_SHORT).show()
            e.printStackTrace()
        }
    }
}

