<?php
include 'config.php';

// Fetch conferences from the database
$sql = "SELECT id, name, start_date, end_date, address FROM conferences";
$result = $conn->query($sql);

$conferences = array();

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $conference = array(
            'id' => $row['id'],
            'name' => $row['name'],
            'start_date' => $row['start_date'],
            'end_date' => $row['end_date'],
            'address' => $row['address']
        );
        array_push($conferences, $conference);
    }
}

// Return conferences data as JSON
header('Content-Type: application/json');
echo json_encode($conferences);

$conn->close();
?>