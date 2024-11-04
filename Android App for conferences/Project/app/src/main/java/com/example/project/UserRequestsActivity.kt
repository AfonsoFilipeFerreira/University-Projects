package com.example.project

import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import android.os.Bundle
import android.util.Log
import android.widget.ImageButton
import android.widget.ListView
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.android.volley.Request
import com.android.volley.RequestQueue
import com.android.volley.toolbox.JsonArrayRequest
import com.android.volley.toolbox.Volley
import org.json.JSONException
import org.json.JSONObject
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

class UserRequestsActivity : AppCompatActivity() {

    private lateinit var sharedPreferences: SharedPreferences
    private lateinit var requestQueue: RequestQueue
    private lateinit var requestListView: ListView
    private lateinit var requestListAdapter: RequestListAdapter
    private lateinit var requestList: MutableList<RequestItem>
    private lateinit var headerText: TextView
    private lateinit var dateText: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_user_requests)

        sharedPreferences = getSharedPreferences("user_prefs", Context.MODE_PRIVATE)
        val userId = sharedPreferences.getInt("user_id", -1)
        val username = sharedPreferences.getString("username", "User") ?: "User"
        Log.d("ArticleDetailActivity", "Username: $username")

        // Set username in header view
        headerText = findViewById(R.id.header_text)
        headerText.text = username

        // Set current date
        dateText = findViewById(R.id.date_text)
        dateText.text = getCurrentDate()

        requestQueue = Volley.newRequestQueue(this)
        requestListView = findViewById(R.id.request_list_view)
        requestList = mutableListOf()
        requestListAdapter = RequestListAdapter(this, requestList)
        requestListView.adapter = requestListAdapter
        val homeButton = findViewById<ImageButton>(R.id.homeButton)
        val logoutButton = findViewById<ImageButton>(R.id.logoutButton)

        fetchUserRequests(userId)

        homeButton.setOnClickListener {
            val intent = Intent(this, HomeActivity::class.java)
            startActivity(intent)
        }
        logoutButton.setOnClickListener {
            val intent = Intent(this, MainActivity::class.java)
            startActivity(intent)
        }
    }

    // Function to get the current date in the desired format
    private fun getCurrentDate(): String {
        val dateFormat = SimpleDateFormat("MMMM dd, yyyy", Locale.getDefault())
        return dateFormat.format(Date())
    }

    private fun fetchUserRequests(userId: Int) {
        val url = "http://10.0.2.2/project_scientific_conferences/app/get_user_requests.php?user_id=$userId"

        val jsonArrayRequest = JsonArrayRequest(
            Request.Method.GET, url, null,
            { response ->
                try {
                    for (i in 0 until response.length()) {
                        val jsonObject: JSONObject = response.getJSONObject(i)
                        val id = jsonObject.getInt("id")
                        val message = jsonObject.getString("message")
                        val answered = jsonObject.getInt("answered")
                        var replyMessage = ""

                        // Check if there's a reply
                        if (answered == 1 && !jsonObject.isNull("reply_message")) {
                            replyMessage = jsonObject.getString("reply_message")
                        }

                        val requestItem = RequestItem(id, message, answered, replyMessage)
                        requestList.add(requestItem)
                    }
                    requestListAdapter.notifyDataSetChanged()
                } catch (e: JSONException) {
                    Toast.makeText(this, "Error parsing JSON response", Toast.LENGTH_SHORT).show()
                }
            },
            { error ->
                Toast.makeText(this, "Error fetching user requests: ${error.message}", Toast.LENGTH_SHORT).show()
            })

        requestQueue.add(jsonArrayRequest)
    }
}
