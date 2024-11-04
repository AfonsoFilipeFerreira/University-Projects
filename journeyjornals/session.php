<?php
include 'connect.php';
// Start the session
session_start();

if (isset($_GET['username'])) {
     // Store the username from the GET parameter in the session
    $_SESSION['username'] = $_GET['username'];
}

// Access session variables
$username = $_SESSION["username"];