<?php
include 'config.php'; // Include database connection

// Check if POST data exists
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['username']) && isset($_POST['article_id']) && isset($_POST['message'])) {
    
    // Prepare data for insertion
    $username = $_POST['username'];
    $article_id = intval($_POST['article_id']);
    $message = $conn->real_escape_string($_POST['message']); // Sanitize message input

    // Insert comment into database using prepared statement
    $stmt = $conn->prepare("INSERT INTO comments (username, article_id, message) VALUES (?, ?, ?)");
    $stmt->bind_param("sis", $username, $article_id, $message); // 's' for string, 'i' for integer

    if ($stmt->execute()) {
        // Comment inserted successfully
        echo json_encode(array("status" => "success"));
    } else {
        // Error inserting comment
        echo json_encode(array("status" => "error", "message" => "Error: " . $conn->error));
    }
    
    $stmt->close();
} else {
    // Invalid request
    echo json_encode(array("status" => "error", "message" => "Invalid request"));
}

$conn->close();
?>
