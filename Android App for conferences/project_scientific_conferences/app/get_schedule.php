<?php
include 'config.php'; // Include database connection

// Query to retrieve conferences
$conferencesQuery = "SELECT id, name, start_date, end_date, address FROM conferences";
$conferencesResult = $conn->query($conferencesQuery);

$conferences = array();
if ($conferencesResult->num_rows > 0) {
    while ($row = $conferencesResult->fetch_assoc()) {
        $conferences[] = $row;
    }
}

// Close connection
$conn->close();

// Prepare response as JSON
$response = array(
    'conferences' => $conferences
);

header('Content-Type: application/json');
echo json_encode($response);
?>