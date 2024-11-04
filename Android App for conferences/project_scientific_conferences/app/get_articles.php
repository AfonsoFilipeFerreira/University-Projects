<?php
include 'config.php'; // Include database connection

// Query to fetch articles ordered by title alphabetically
$sql = "SELECT id, title, authors, abstract, pdf_link, created_at FROM articles ORDER BY title ASC";
$result = $conn->query($sql);

// Check if there are results
if ($result->num_rows > 0) {
    // Fetch data and store in array
    $articles = array();
    while ($row = $result->fetch_assoc()) {
        $articles[] = $row;
    }
    // Output JSON format
    echo json_encode($articles);
} else {
    echo json_encode([]); // Output empty JSON array if no results
}

// Close connection
$conn->close();
?>