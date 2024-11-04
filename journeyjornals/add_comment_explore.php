<?php
include 'session.php';
include 'connect.php';

$publicationId = $_POST['publication_id'];
$comment = $_POST['comment'];
$username = $_SESSION['username'];

// Insert the comment into the comments table
$insertSql = "INSERT INTO comments (publication_id, username, comment) VALUES ('$publicationId', '$username', '$comment')";
$insertResult = mysqli_query($link, $insertSql);

if (!$insertResult) {
    die("Query failed: " . mysqli_error($link));
}

// Redirect back to the explore page after adding the comment
header("Location: explore.php?username=" .$username );
exit();