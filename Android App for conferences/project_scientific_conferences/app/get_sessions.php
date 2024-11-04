<?php
include 'config.php';

// Get parameters
$conference_id = isset($_GET['conference_id']) ? intval($_GET['conference_id']) : 0;
$date = isset($_GET['date']) ? $_GET['date'] : '';

// Log the parameters to verify
file_put_contents('log.txt', "conference_id: $conference_id, date: $date\n", FILE_APPEND);

if ($conference_id == 0 || $date == '') {
    echo json_encode([]);
    exit;
}

// Prepare and execute the SQL query to fetch sessions and their articles
$query = "
    SELECT s.id AS session_id, s.title AS session_title, s.start_time, s.end_time, s.room, a.id AS article_id, a.title AS article_title, a.authors
    FROM sessions s
    LEFT JOIN session_articles sa ON s.id = sa.session_id
    LEFT JOIN articles a ON sa.article_id = a.id
    WHERE s.conference_id = ? AND DATE(s.start_time) = ?
    ORDER BY s.start_time
";

$stmt = $conn->prepare($query);
if ($stmt === false) {
    die('Prepare failed: ' . htmlspecialchars($conn->error));
}

$stmt->bind_param('is', $conference_id, $date);
if (!$stmt->execute()) {
    die('Execute failed: ' . htmlspecialchars($stmt->error));
}

$result = $stmt->get_result();
if ($result === false) {
    die('Get result failed: ' . htmlspecialchars($stmt->error));
}

$sessions = [];
$session_map = [];

while ($row = $result->fetch_assoc()) {
    $session_id = $row['session_id'];

    if (!isset($session_map[$session_id])) {
        $session_map[$session_id] = [
            'id' => $session_id,
            'title' => $row['session_title'],
            'start_time' => $row['start_time'],
            'end_time' => $row['end_time'],
            'room' => $row['room'],
            'articles' => []
        ];
    }

    if (!empty($row['article_id'])) {
        $session_map[$session_id]['articles'][] = [
            'id' => $row['article_id'],
            'title' => $row['article_title'],
            'authors' => $row['authors']
        ];
    }
}

$sessions = array_values($session_map);

echo json_encode($sessions);

// Log the final result to see what's being output
file_put_contents('log.txt', print_r($sessions, true), FILE_APPEND);

// Close the database connection
$conn->close();
?>