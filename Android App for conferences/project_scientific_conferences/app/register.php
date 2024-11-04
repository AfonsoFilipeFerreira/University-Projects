<?php
include 'config.php'; // Include database connection

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['user'];
    $password = $_POST['pass'];
    $email = $_POST['email'];
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // Insert the new user
    $stmt = $conn->prepare("INSERT INTO users (username, password, email) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $username, $hashed_password, $email);
    
    if ($stmt->execute()) {
        echo $stmt->insert_id; // Return the user id of the newly created user
    } else {
        echo "Error registering user";
    }
    
    $stmt->close();
}
$conn->close();
?>