package com.example.project

import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import android.graphics.Typeface
import android.os.Bundle
import android.text.TextUtils
import android.util.Log
import android.view.View
import android.view.ViewGroup
import android.widget.*
import androidx.appcompat.app.AppCompatActivity
import androidx.core.text.HtmlCompat
import com.android.volley.Request
import com.android.volley.toolbox.JsonArrayRequest
import com.android.volley.toolbox.Volley
import org.json.JSONObject
import java.text.SimpleDateFormat
import java.util.*

class ScheduleActivity : AppCompatActivity() {

    private lateinit var calendarView: CalendarView
    private lateinit var eventsTextView: TextView
    private lateinit var conferenceSpinner: Spinner
    private val conferences = mutableListOf<Conference>()
    private lateinit var sharedPreferences: SharedPreferences
    private lateinit var headerText: TextView
    private lateinit var dateText: TextView
    private lateinit var articlesListView: ListView // Declare ListView for articles
    private lateinit var conferenceNameTextView: TextView
    private lateinit var conferenceDetailsTextView: TextView
    private lateinit var sessionTitle: TextView
    private lateinit var sessionRoom: TextView
    private lateinit var sessionTime: TextView
    private lateinit var viewLocationButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_schedule)

        // Initialize views
        headerText = findViewById(R.id.header_text)
        dateText = findViewById(R.id.date_text)
        calendarView = findViewById(R.id.calendarView)
        conferenceSpinner = findViewById(R.id.conferenceSpinner)
        articlesListView = findViewById(R.id.articlesListView) // Initialize ListView
        viewLocationButton = findViewById(R.id.view_location_button)

        // Initialize other views in RelativeLayout (session details)
        conferenceNameTextView = findViewById(R.id.conferenceNameTextView)
        conferenceDetailsTextView = findViewById(R.id.conferenceDetailsTextView)
        sessionTitle = findViewById(R.id.sessionTitle)
        val params = sessionTitle.layoutParams as ViewGroup.MarginLayoutParams
        params.topMargin = resources.getDimensionPixelSize(R.dimen.session_title_margin_top)
        sessionTitle.layoutParams = params
        sessionRoom = findViewById(R.id.sessionRoom)
        sessionTime = findViewById(R.id.sessionTime)

        // Initialize SharedPreferences
        sharedPreferences = getSharedPreferences("user_prefs", Context.MODE_PRIVATE)
        val username = sharedPreferences.getString("username", "User") ?: "User"
        headerText.text = username

        dateText.text = getCurrentDate()

        // Fetch conferences data from server
        fetchConferencesData()

        // Set up Spinner listener
        conferenceSpinner.onItemSelectedListener = object : AdapterView.OnItemSelectedListener {
            override fun onItemSelected(parent: AdapterView<*>, view: View?, position: Int, id: Long) {
                if (position > 0) {
                    val selectedDateStr = conferenceDates[position - 1]
                    // Update calendarView to show the selected date
                    updateCalendar(selectedDateStr)
                    // Fetch and show conferences for the selected date
                    showConferencesForDate(selectedDateStr)
                } else {
                    // Reset calendarView and session details when "Select a conference" is selected
                    resetCalendar()
                    resetSessionDetails()
                }
            }

            override fun onNothingSelected(parent: AdapterView<*>) {
                // Implement what should happen when nothing is selected in the spinner
                // For example, you might want to reset views or display a message
                resetCalendar()
                resetSessionDetails()
            }
        }

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
        // Assuming you're using a ListView to display the articles
        articlesListView.setOnItemClickListener { parent, view, position, id ->
            val selectedArticle = parent.getItemAtPosition(position) as Article // Your Article class
            val intent = Intent(this, ArticleDetailActivity::class.java)
            intent.putExtra("ARTICLE_ID", selectedArticle.id) // Pass the article ID
            startActivity(intent)
        }
        viewLocationButton.setOnClickListener {
            val selectedPosition = conferenceSpinner.selectedItemPosition
            if (selectedPosition > 0) {
                val selectedConference = conferences[selectedPosition - 1] // -1 to account for the "Select a conference" item
                val address = selectedConference.address
                Log.d("SelectedConference", "Conference: ${selectedConference.name}, Address: $address")
                if (address.isNotEmpty()) {
                    val intent = Intent(this, MapActivity::class.java)
                    intent.putExtra("ADDRESS", address)
                    startActivity(intent)
                } else {
                    Toast.makeText(this, "Conference address not available", Toast.LENGTH_SHORT).show()
                }
            } else {
                Toast.makeText(this, "Conference not found", Toast.LENGTH_SHORT).show()
            }
        }

        // Initialize the CalendarView
        initCalendar()
    }

    private fun updateCalendar(selectedDate: String) {
        val sdf = SimpleDateFormat("yyyy-MM-dd", Locale.getDefault())
        val date = sdf.parse(selectedDate) ?: return
        val calendar = Calendar.getInstance()
        calendar.time = date
        calendarView.date = calendar.timeInMillis
    }

    private fun resetCalendar() {
        // Reset the calendar to the current date
        calendarView.date = System.currentTimeMillis()
    }

    private fun getCurrentDate(): String {
        val dateFormat = SimpleDateFormat("MMMM dd, yyyy", Locale.getDefault())
        return dateFormat.format(Date())
    }

    private fun initCalendar() {
        calendarView.setOnDateChangeListener { _, year, month, dayOfMonth ->
            val selectedDate = Calendar.getInstance().apply {
                set(year, month, dayOfMonth)
            }.time

            val sdf = SimpleDateFormat("yyyy-MM-dd", Locale.getDefault())
            val formattedDate = sdf.format(selectedDate)

            // Update the selected date text
            dateText.text = sdf.format(selectedDate)

            // Reset session details
            resetSessionDetails()

            // Find the position in spinner for the selected date
            val spinnerPosition = findSpinnerPositionForDate(formattedDate)
            conferenceSpinner.setSelection(spinnerPosition)
        }
    }

    private fun resetSessionDetails() {
        // Clear session details
        conferenceNameTextView.text = ""
        conferenceDetailsTextView.text = ""
        sessionTitle.text = ""
        sessionRoom.text = ""
        sessionTime.text = ""
        articlesListView.adapter = null
        articlesListView.visibility = View.GONE
    }

    private fun fetchConferencesData() {
        val url = "http://10.0.2.2/project_scientific_conferences/app/get_conferences.php"

        val jsonArrayRequest = JsonArrayRequest(
            Request.Method.GET, url, null,
            { response ->
                try {
                    for (i in 0 until response.length()) {
                        val conferenceJson: JSONObject = response.getJSONObject(i)
                        val id = conferenceJson.getInt("id")
                        val name = conferenceJson.getString("name")
                        val startDate = conferenceJson.getString("start_date")
                        val endDate = conferenceJson.getString("end_date")
                        val address = conferenceJson.getString("address")

                        val conference = Conference(id, name, startDate, endDate, address)
                        conferences.add(conference)
                    }

                    // Sort conferences by start date
                    conferences.sortBy { it.startDate }

                    // Set up Spinner adapter
                    setupSpinner()

                } catch (e: Exception) {
                    e.printStackTrace()
                }
            },
            { error ->
                Log.e("Volley Error", error.toString())
                Toast.makeText(applicationContext, "Error fetching data", Toast.LENGTH_SHORT).show()
            })

        // Add the request to the RequestQueue
        Volley.newRequestQueue(this).add(jsonArrayRequest)
    }

    private val conferenceDates = mutableListOf<String>() // To store actual dates for each day

    private fun setupSpinner() {
        val displayNames = mutableListOf("Select a conference")

        for (conference in conferences) {
            val startDate = SimpleDateFormat("yyyy-MM-dd", Locale.getDefault()).parse(conference.startDate)
            val endDate = SimpleDateFormat("yyyy-MM-dd", Locale.getDefault()).parse(conference.endDate)
            if (startDate != null && endDate != null) {
                val startCalendar = Calendar.getInstance()
                startCalendar.time = startDate
                val endCalendar = Calendar.getInstance()
                endCalendar.time = endDate
                var dayCount = 1
                while (!startCalendar.time.after(endCalendar.time)) {
                    val dateStr = SimpleDateFormat("yyyy-MM-dd", Locale.getDefault()).format(startCalendar.time)
                    displayNames.add("${conference.name} - Day $dayCount")
                    conferenceDates.add(dateStr) // Store the date in the list
                    startCalendar.add(Calendar.DATE, 1)
                    dayCount++
                }
            }
        }

        val adapter = object : ArrayAdapter<String>(this, R.layout.spinner_dropdown_item, displayNames) {
            override fun getView(position: Int, convertView: View?, parent: ViewGroup): View {
                val view = super.getView(position, convertView, parent) as TextView
                view.maxLines = 2 // Set the number of lines to show
                view.ellipsize = TextUtils.TruncateAt.END
                return view
            }

            override fun getDropDownView(position: Int, convertView: View?, parent: ViewGroup): View {
                val view = super.getDropDownView(position, convertView, parent) as TextView
                view.maxLines = 5 // Adjust the number of lines as needed
                view.ellipsize = null // Disable ellipsize to show full text
                return view
            }
        }

        conferenceSpinner.adapter = adapter
        conferenceSpinner.dropDownWidth = ViewGroup.LayoutParams.MATCH_PARENT
        viewLocationButton.visibility = View.GONE
    }


    private fun showConferencesForDate(selectedDate: String) {
        val selectedCalendar = Calendar.getInstance().apply {
            time = SimpleDateFormat("yyyy-MM-dd", Locale.getDefault()).parse(selectedDate) ?: return
        }

        val conferencesForDate = conferences.filter { conference ->
            val sdf = SimpleDateFormat("yyyy-MM-dd", Locale.getDefault())
            val startDate = sdf.parse(conference.startDate) ?: return@filter false
            val endDate = sdf.parse(conference.endDate) ?: return@filter false

            selectedCalendar.timeInMillis >= startDate.time && selectedCalendar.timeInMillis <= endDate.time
        }

        if (conferencesForDate.isNotEmpty()) {
            val conference = conferencesForDate[0]
            fetchSessionsData(conference.id, selectedDate)
        } else {
            // No conferences found for selected date
            resetSessionDetails()
            eventsTextView.text = "No events"
        }
    }

    private fun fetchSessionsData(conferenceId: Int, selectedDate: String) {
        val url = "http://10.0.2.2/project_scientific_conferences/app/get_sessions.php?conference_id=$conferenceId&date=$selectedDate"

        val jsonArrayRequest = JsonArrayRequest(
            Request.Method.GET, url, null,
            { response ->
                try {
                    val sessions = mutableListOf<Session>()

                    for (i in 0 until response.length()) {
                        val sessionJson = response.getJSONObject(i)
                        val sessionId = sessionJson.getInt("id")
                        val title = sessionJson.getString("title")
                        val startTime = sessionJson.getString("start_time")
                        val endTime = sessionJson.getString("end_time")
                        val room = sessionJson.getString("room")

                        val articlesJsonArray = sessionJson.getJSONArray("articles")
                        val articles = mutableListOf<Article>()
                        for (j in 0 until articlesJsonArray.length()) {
                            val articleJson = articlesJsonArray.getJSONObject(j)
                            val articleId = articleJson.getInt("id")
                            val articleTitle = articleJson.getString("title")
                            val authors = articleJson.getString("authors")

                            articles.add(Article(articleId, articleTitle, authors))
                        }

                        sessions.add(Session(sessionId, conferenceId, title, startTime, endTime, room, articles))
                    }

                    // Display sessions after fetching
                    displaySessions(sessions)

                } catch (e: Exception) {
                    e.printStackTrace()
                }
            },
            { error ->
                Log.e("Volley Error", error.toString())
                Toast.makeText(applicationContext, "Error fetching sessions", Toast.LENGTH_SHORT).show()
            })

        // Add the request to the RequestQueue
        Volley.newRequestQueue(this).add(jsonArrayRequest)
    }

    private fun displaySessions(sessions: List<Session>) {
        if (sessions.isNotEmpty()) {
            // Clear previous session details
            resetSessionDetails()
            viewLocationButton.visibility = View.VISIBLE
            // Initialize variables to track current conference ID
            var currentConferenceId = -1

            // StringBuilder to build the session details text
            val sessionDetailsBuilder = StringBuilder()

            for (session in sessions) {
                // Check if conference ID has changed
                if (session.conferenceId != currentConferenceId) {
                    // Update conference details for the new conference
                    conferenceNameTextView.text = getConferenceName(session.conferenceId)
                    conferenceDetailsTextView.text = getConferenceAddress(session.conferenceId)

                    // Reset session details for each new conference
                    sessionDetailsBuilder.clear()
                    currentConferenceId = session.conferenceId
                }

                // Append session details to StringBuilder with HTML formatting
                sessionDetailsBuilder.append("<b>Session:</b> ${session.title}<br>")
                sessionDetailsBuilder.append("<b>Room:</b> ${session.room}<br>")
                sessionDetailsBuilder.append("<b>Time:</b> ${formatTime(session.startTime)} - ${formatTime(session.endTime)}<br><br>")

                // Append articles if any
                if (session.articles.isNotEmpty()) {
                    sessionDetailsBuilder.append("<b>Articles:</b><br>")
                    for (article in session.articles) {
                        sessionDetailsBuilder.append("- ${article.title} by ${article.authors}<br><br><br>") // Add multiple <br> for extra spacing
                    }
                    sessionDetailsBuilder.append("<br>")
                }
            }

            // Set session title text and apply bold typeface
            sessionTitle.apply {
                text = "Sessions Details"
                setTypeface(null, Typeface.BOLD)
            }

            // Display the built session details text in sessionRoom TextView
            sessionRoom.text = HtmlCompat.fromHtml(sessionDetailsBuilder.toString(), HtmlCompat.FROM_HTML_MODE_COMPACT)

            // Display articles if any in ListView
            val articles = sessions.flatMap { it.articles }
            val articleAdapter = ArticleListAdapter(this, articles.toMutableList())
            articlesListView.adapter = articleAdapter
            articlesListView.visibility = View.VISIBLE
        } else {
            // No sessions found
            resetSessionDetails()
            Toast.makeText(applicationContext, "No sessions found for this conference", Toast.LENGTH_SHORT).show()
            viewLocationButton.visibility = View.GONE
        }
    }

    private fun getConferenceName(conferenceId: Int): String {
        return conferences.find { it.id == conferenceId }?.name ?: ""
    }

    private fun getConferenceAddress(conferenceId: Int): String {
        return conferences.find { it.id == conferenceId }?.address ?: ""
    }


    private fun formatTime(dateTime: String): String {
        val sdf = SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.getDefault())
        val date = sdf.parse(dateTime) ?: return ""
        val timeFormat = SimpleDateFormat("HH:mm", Locale.getDefault())
        return timeFormat.format(date)
    }

    data class Conference(val id: Int, val name: String, val startDate: String, val endDate: String, val address: String)
    data class Session(val id: Int, val conferenceId: Int, val title: String, val startTime: String, val endTime: String, val room: String, val articles: List<Article>)

    private fun findSpinnerPositionForDate(selectedDate: String): Int {
        return conferenceDates.indexOf(selectedDate) + 1 // +1 to account for the "Select a conference" item
    }
}

