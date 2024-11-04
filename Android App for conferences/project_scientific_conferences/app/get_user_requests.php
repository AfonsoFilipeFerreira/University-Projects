<?php
include 'config.php';

// Check if user ID is provided in the URL
if (!isset($_GET['user_id'])) {
    echo json_encode(array('error' => 'User ID not provided'));
    exit;
}

// Sanitize and validate user ID (assuming integer input)
$user_id = intval($_GET['user_id']);
if ($user_id <= 0) {
    echo json_encode(array('error' => 'Invalid user ID'));
    exit;
}

// Fetch user requests and associated replies
$sql = "SELECT ir.id, ir.user_id, ir.username, ir.message, ir.answered, r.message AS reply_message 
        FROM information_requests ir 
        LEFT JOIN replies r ON ir.id = r.request_id 
        WHERE ir.user_id = ?";

$stmt = $conn->prepare($sql);
if (!$stmt) {
    echo json_encode(array('error' => 'Prepare statement failed: ' . $conn->error));
    exit;
}

$stmt->bind_param("i", $user_id);
if (!$stmt->execute()) {
    echo json_encode(array('error' => 'Execute query failed: ' . $stmt->error));
    exit;
}

$result = $stmt->get_result();

$user_requests = array();

while ($row = $result->fetch_assoc()) {
    $user_requests[] = array(
        'id' => $row['id'],
        'user_id' => $row['user_id'],
        'username' => $row['username'],
        'message' => $row['message'],
        'answered' => $row['answered'],
        'reply_message' => $row['reply_message']
    );
}

$stmt->close();

// Convert the result array to JSON format
echo json_encode($user_requests);
?>
