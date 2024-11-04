<?php
include 'connect.php';

session_start(); // Start the session

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    // Retrieve user from the table
    $sql = "SELECT * FROM registuser WHERE username = '$username'";
    $result = mysqli_query($link, $sql);

    if (mysqli_num_rows($result) == 1) {
        $row = mysqli_fetch_assoc($result);
        $storedPassword = $row['password'];

        if ($password == $storedPassword) {
            $_SESSION["username"] = $username; // Store the username in the session
            header("Location: homeloged.php?username=" . urlencode($username)); // Redirect to the homeloged.php page
            exit;
        }
    }

    echo "<script>alert('Wrong username or password.'); window.location.href = 'homepage.php';</script>";
} else {
    header("Location: homepage.php"); // Redirect to the homepage.php page
}
?>