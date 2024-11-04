package com.example.project

import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.ImageButton
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.android.volley.Request
import com.android.volley.RequestQueue
import com.android.volley.Response
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import org.json.JSONException
import org.json.JSONObject
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

class RequestInfoActivity : AppCompatActivity() {
    private lateinit var sharedPreferences: SharedPreferences
    private lateinit var headerText: TextView
    private lateinit var requestQueue: RequestQueue
    private lateinit var dateText: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_request_information)

        sharedPreferences = getSharedPreferences("user_prefs", Context.MODE_PRIVATE)
        val username = sharedPreferences.getString("username", "User") ?: "User"
        val userId = sharedPreferences.getInt("user_id", -1)

        // Initialize views
        headerText = findViewById(R.id.header_text)
        headerText.text = username

        dateText = findViewById(R.id.date_text)
        dateText.text = getCurrentDate()

        val messageField: EditText = findViewById(R.id.message_input)
        val submitButton: Button = findViewById(R.id.submit_request_button)
        val homeButton = findViewById<ImageButton>(R.id.homeButton)
        val logoutButton = findViewById<ImageButton>(R.id.logoutButton)
        val messagesButton = findViewById<ImageButton>(R.id.messageButton)

        messagesButton.setOnClickListener {
            val intent = Intent(this, UserRequestsActivity::class.java)
            startActivity(intent)
        }

        requestQueue = Volley.newRequestQueue(this)

        submitButton.setOnClickListener {
            val message = messageField.text.toString().trim()
            if (message.isNotEmpty() && userId != -1) {
                submitRequest(userId, username, message)
            } else {
                if (message.isEmpty()) {
                    Toast.makeText(this, "Please enter a message", Toast.LENGTH_SHORT).show()
                }
                if (userId == -1) {
                    Toast.makeText(this, "User ID is invalid", Toast.LENGTH_SHORT).show()
                }
            }
        }

        homeButton.setOnClickListener {
            val intent = Intent(this, HomeActivity::class.java)
            startActivity(intent)
        }

        logoutButton.setOnClickListener {
            val intent = Intent(this, MainActivity::class.java)
            startActivity(intent)
        }
    }

    private fun getCurrentDate(): String {
        val dateFormat = SimpleDateFormat("MMMM dd, yyyy", Locale.getDefault())
        return dateFormat.format(Date())
    }

    private fun submitRequest(userId: Int, username: String, message: String) {
        val url = "http://10.0.2.2/project_scientific_conferences/app/post_information_request.php"

        val request = object : StringRequest(
            Request.Method.POST, url,
            Response.Listener { response ->
                try {
                    val jsonResponse = JSONObject(response)
                    val status = jsonResponse.getString("status")
                    if (status == "success") {
                        Toast.makeText(this, "Request submitted successfully", Toast.LENGTH_SHORT).show()
                        findViewById<EditText>(R.id.message_input).text.clear()
                    } else {
                        Toast.makeText(this, "Failed to submit request", Toast.LENGTH_SHORT).show()
                    }
                } catch (e: JSONException) {
                    Toast.makeText(this, "Error parsing response", Toast.LENGTH_SHORT).show()
                }
            },
            Response.ErrorListener { error ->
                Toast.makeText(this, "Failed to submit request: ${error.message}", Toast.LENGTH_SHORT).show()
            }
        ) {
            override fun getParams(): Map<String, String> {
                val params = HashMap<String, String>()
                params["user_id"] = userId.toString()
                params["username"] = username
                params["message"] = message
                return params
            }
        }

        requestQueue.add(request)
    }
}
