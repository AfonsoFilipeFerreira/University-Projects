<?php
if (session_status() == PHP_SESSION_NONE) {
    session_start();
}
include_once 'functions.php';

if (!isLoggedIn() && basename($_SERVER['PHP_SELF']) != 'index.php' && basename($_SERVER['PHP_SELF']) != 'login.php') {
    header("Location: index.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Admin Panel</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="container">
            <div id="branding">
                <h1>Admin Panel</h1>
            </div>
            <nav>
                <ul>
                    <li><a href="add_article.php">Add Article</a></li>
                    <li><a href="create_conference.php">Create Conference</a></li>
                    <li><a href="schedule_session.php">Schedule Session</a></li>
                    <li><a href="aprove_comments.php">Comments</a></li>
                    <li><a href="view_info_requests.php">View Info Requests</a></li>
                    <li><a href="logout.php">Logout</a></li>
                </ul>
            </nav>
        </div>
    </header>
    <div class="container">