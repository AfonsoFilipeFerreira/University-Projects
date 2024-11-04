package com.example.project

import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import android.os.Bundle
import android.widget.Button
import android.widget.ImageButton
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import java.text.SimpleDateFormat
import java.util.*



class HomeActivity : AppCompatActivity() {

    private lateinit var sharedPreferences: SharedPreferences
    private lateinit var headerText: TextView
    private lateinit var dateText: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_home)

        sharedPreferences = getSharedPreferences("user_prefs", Context.MODE_PRIVATE)
        val username = sharedPreferences.getString("username", "User") ?: "User"

        // Initialize views
        headerText = findViewById(R.id.header_text)
        headerText.text = "$username"

        dateText = findViewById(R.id.date_text)
        dateText.text = getCurrentDate()

        val articleButton: Button = findViewById(R.id.article_button)
        val scheduleButton: Button = findViewById(R.id.schedule_button)
        val requestInfoButton: Button = findViewById(R.id.request_info_button)
        val homeButton = findViewById<ImageButton>(R.id.homeButton)
        val logoutButton = findViewById<ImageButton>(R.id.logoutButton)
        val messagesButton = findViewById<ImageButton>(R.id.messageButton)

        messagesButton.setOnClickListener {
            val intent = Intent(this, UserRequestsActivity::class.java)
            startActivity(intent)
        }

        articleButton.setOnClickListener {
            val intent = Intent(this, ArticlesListActivity::class.java)
            startActivity(intent)
        }

        scheduleButton.setOnClickListener {
            val intent = Intent(this, ScheduleActivity::class.java)
            startActivity(intent)
        }

        requestInfoButton.setOnClickListener {
            val intent = Intent(this, RequestInfoActivity::class.java)
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
    }
    // Function to get the current date in the desired format
    private fun getCurrentDate(): String {
        val dateFormat = SimpleDateFormat("MMMM dd, yyyy", Locale.getDefault())
        return dateFormat.format(Date())
    }

}
