<?php
include 'config.php'; // Include database connection

// Check if POST data exists
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['user_id']) && isset($_POST['username']) && isset($_POST['message'])) {
    
    // Prepare data for insertion
    $user_id = intval($_POST['user_id']);
    $username = $conn->real_escape_string($_POST['username']);
    $message = $conn->real_escape_string($_POST['message']); // Sanitize message input

    // Insert information request into database using prepared statement
    $stmt = $conn->prepare("INSERT INTO information_requests (user_id, username, message, answered) VALUES (?, ?, ?, 0)");
    $stmt->bind_param("iss", $user_id, $username, $message); // 'i' for integer, 's' for string

    if ($stmt->execute()) {
        // Request inserted successfully
        echo json_encode(array("status" => "success", "message" => "Request submitted successfully"));
    } else {
        // Error inserting request
        echo json_encode(array("status" => "error", "message" => "Error: " . $stmt->error));
    }
    
    $stmt->close();
} else {
    // Invalid request
    echo json_encode(array("status" => "error", "message" => "Invalid request"));
}

$conn->close();
?>
