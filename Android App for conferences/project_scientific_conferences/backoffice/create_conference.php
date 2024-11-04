<?php
session_start();
include 'functions.php';
include 'config.php';
redirectIfNotLoggedIn();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = $_POST['name'];
    $start_date = $_POST['start_date'];
    $end_date = $_POST['end_date'];
    $address = $_POST['address']; // Added location details

    // For simplicity, assume latitude and longitude are initially set to 0.0
    $latitude = 0.0;
    $longitude = 0.0;

    // You should ideally fetch latitude and longitude based on the address
    // using a geocoding service like Google Maps API and update your database accordingly.

    $stmt = $conn->prepare("INSERT INTO conferences (name, start_date, end_date, address) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("ssss", $name, $start_date, $end_date, $address);

    if ($stmt->execute()) {
        echo "Conference created successfully.";
    } else {
        echo "Error creating conference: " . $conn->error;
    }

    $stmt->close();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Create Conference</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<?php
include_once 'header.php';
redirectIfNotLoggedIn();
?>

<h2>Create Conference</h2>
<form action="create_conference.php" method="post">
    <label for="name">Conference Name:</label>
    <input type="text" id="name" name="name" required>
    <label for="start_date">Start Date:</label>
    <input type="date" id="start_date" name="start_date" required>
    <label for="end_date">End Date:</label>
    <input type="date" id="end_date" name="end_date" required>
    <label for="address">Location Address:</label>
    <input type="text" id="address" name="address" required>
    <button type="submit">Create Conference</button>
</form>
</body>
</html>