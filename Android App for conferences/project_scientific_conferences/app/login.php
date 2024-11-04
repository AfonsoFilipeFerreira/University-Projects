<?php
include 'config.php'; // Include database connection

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['user'];
    $password = $_POST['pass'];

    // Check if the user exists
    $stmt = $conn->prepare("SELECT id, password FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $stmt->bind_result($user_id, $hashed_password);
    $stmt->fetch();
    
    if ($user_id && password_verify($password, $hashed_password)) {
        echo $user_id; // Return the user id if login is successful
    } else {
        echo "Invalid credentials";
    }
    
    $stmt->close();
}
$conn->close();
?>
