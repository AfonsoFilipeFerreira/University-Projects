package com.example.project

import android.location.Geocoder
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.google.android.gms.maps.CameraUpdateFactory
import com.google.android.gms.maps.GoogleMap
import com.google.android.gms.maps.MapView
import com.google.android.gms.maps.MapsInitializer
import com.google.android.gms.maps.OnMapReadyCallback
import com.google.android.gms.maps.model.LatLng
import com.google.android.gms.maps.model.MarkerOptions

class MapActivity : AppCompatActivity(), OnMapReadyCallback {

    private lateinit var mapView: MapView
    private var googleMap: GoogleMap? = null
    private lateinit var address: String

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_map)

        mapView = findViewById(R.id.mapView)
        mapView.onCreate(savedInstanceState)
        mapView.getMapAsync(this)

        // Get address from intent
        address = intent.getStringExtra("ADDRESS") ?: ""

        MapsInitializer.initialize(this)
    }

    override fun onMapReady(map: GoogleMap) {
        googleMap = map
        showLocationOnMap(address)
    }

    private fun showLocationOnMap(address: String) {
        // Use Geocoding API to convert address to LatLng
        val geocoder = Geocoder(this)
        val addresses = geocoder.getFromLocationName(address, 1)
        if (addresses != null && addresses.isNotEmpty()) {
            val location = addresses[0]
            val latLng = LatLng(location.latitude, location.longitude)
            googleMap?.addMarker(MarkerOptions().position(latLng).title("Conference Location"))
            googleMap?.moveCamera(CameraUpdateFactory.newLatLngZoom(latLng, 15f))
        } else {
            Toast.makeText(this, "Location not found", Toast.LENGTH_SHORT).show()
        }
    }

    override fun onResume() {
        super.onResume()
        mapView.onResume()
    }

    override fun onPause() {
        super.onPause()
        mapView.onPause()
    }

    override fun onDestroy() {
        super.onDestroy()
        mapView.onDestroy()
    }

    override fun onLowMemory() {
        super.onLowMemory()
        mapView.onLowMemory()
    }
}
