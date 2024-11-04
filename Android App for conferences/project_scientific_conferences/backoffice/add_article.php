<?php
session_start();
include 'functions.php';
include 'config.php';
redirectIfNotLoggedIn();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $title = $_POST['title'];
    $authors = $_POST['authors'];
    $abstract = $_POST['abstract'];
    
    // File upload handling
    if (isset($_FILES['pdf_file']) && $_FILES['pdf_file']['error'] === UPLOAD_ERR_OK) {
        // Directory where files will be stored
        $uploadDir = 'C:/xampp3/htdocs/project_scientific_conferences/files/';
        $fileTmpPath = $_FILES['pdf_file']['tmp_name'];
        $fileName = basename($_FILES['pdf_file']['name']);
        $destPath = $uploadDir . $fileName;
        
        // Move the uploaded file to the destination directory
        if (move_uploaded_file($fileTmpPath, $destPath)) {
            // File uploaded successfully
            $pdf_link = $fileName; // Store only the file name in the database
            
            // Insert article details into the database
            $stmt = $conn->prepare("INSERT INTO articles (title, authors, abstract, pdf_link) VALUES (?, ?, ?, ?)");
            $stmt->bind_param("ssss", $title, $authors, $abstract, $pdf_link);

            if ($stmt->execute()) {
                echo "Article added successfully.";
            } else {
                echo "Error adding article: " . $conn->error;
            }

            $stmt->close();
        } else {
            echo "Error moving uploaded file.";
        }
    } else {
        echo "Error uploading file: " . $_FILES['pdf_file']['error'];
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add Article</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <?php
    include_once 'header.php'; // This already includes functions.php and starts session
    redirectIfNotLoggedIn();
    ?>
    <h2>Add Article</h2>
    <form action="add_article.php" method="post" enctype="multipart/form-data">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <label for="authors">Authors:</label>
        <input type="text" id="authors" name="authors" required>
        <label for="abstract">Abstract:</label>
        <textarea id="abstract" name="abstract" required></textarea>
        <label for="pdf_file">PDF File:</label>
        <input type="file" id="pdf_file" name="pdf_file" accept=".pdf" required>
        <button type="submit">Add Article</button>
    </form>
</body>
</html>