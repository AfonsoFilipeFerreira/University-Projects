<?php
include 'session.php';
include 'connect.php';

if (isset($_POST['unlike'])) {
    $username = $_POST['username'];
    $publicationId = $_POST['publication_id'];

    // Delete the like from the likes table
    $deleteSql = "DELETE FROM likes WHERE username = '$username' AND publication_id = $publicationId";
    $deleteResult = mysqli_query($link, $deleteSql);

    if (!$deleteResult) {
        die("Error: " . mysqli_error($link)); // Display error message if query fails
    }
}

// Redirect back to the homeloged.php page after the operation
header("Location: ProfilePage.php?username=" . $username);
exit();
?>