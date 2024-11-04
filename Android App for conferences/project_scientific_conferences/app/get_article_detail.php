<?php
include 'config.php'; // Include database connection

// Check if ID parameter is provided
if (isset($_GET['id'])) {
    $articleId = $_GET['id'];
    // Query to fetch article details for the given ID
    $sql = "SELECT id, title, authors, abstract, pdf_link FROM articles WHERE id = $articleId";
    $result = $conn->query($sql);

    // Check if there are results
    if ($result->num_rows > 0) {
        // Fetch data and store in array
        $article = $result->fetch_assoc();
        // Output JSON format
        echo json_encode($article);
    } else {
        echo "{}"; // Return empty JSON object if article not found
    }
} else {
    echo "{}"; // Return empty JSON object if no ID provided
}

// Close connection
$conn->close();
?>