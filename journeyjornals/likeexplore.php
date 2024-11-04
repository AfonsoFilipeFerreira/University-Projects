<?php
include 'session.php';
include 'connect.php';

if (isset($_POST['like'])) {
    $username = $_POST['username'];
    $publicationId = $_POST['publication_id'];

    // Check if the user has already liked the publication
    $likeSql = "SELECT * FROM likes WHERE username = '$username' AND publication_id = $publicationId";
    $likeResult = mysqli_query($link, $likeSql);

    if ($likeResult) {
        if (mysqli_num_rows($likeResult) > 0) {
            // User has already liked the publication, do nothing
        } else {
            // User has not liked the publication, insert a new row with like value 1
            $insertSql = "INSERT INTO likes (username, publication_id, `like`) VALUES ('$username', $publicationId, 1)";
            $insertResult = mysqli_query($link, $insertSql);

            if (!$insertResult) {
                die("Error: " . mysqli_error($link)); // Display error message if query fails
            }
        }
    } else {
        die("Error: " . mysqli_error($link)); // Display error message if query fails
    }
}

// Redirect back to the homeloged.php page after the operation
header("Location: explore.php?username=$username");
exit();
?>