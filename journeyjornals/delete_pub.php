<?php
include 'session.php';
include 'connect.php';

if (isset($_POST['username']) && isset($_POST['publication_id'])) {
    $username = $_POST['username'];
    $publicationId = $_POST['publication_id'];

    // Retrieve the publication details
    $publicationSql = "SELECT * FROM publication WHERE id = $publicationId";
    $publicationResult = mysqli_query($link, $publicationSql);
    $publicationRow = mysqli_fetch_assoc($publicationResult);

    // Check if the logged-in user has permission to delete the publication
    if ($username === $publicationRow['username']) {
        // Delete the likes associated with the publication
        $deleteLikesSql = "DELETE FROM likes WHERE publication_id = $publicationId";
        $deleteLikesResult = mysqli_query($link, $deleteLikesSql);

        // Delete the comments associated with the publication
        $deleteCommentsSql = "DELETE FROM comments WHERE publication_id = $publicationId";
        $deleteCommentsResult = mysqli_query($link, $deleteCommentsSql);

        // Delete the publication from the publication table
        $deletePublicationSql = "DELETE FROM publication WHERE id = $publicationId";
        $deletePublicationResult = mysqli_query($link, $deletePublicationSql);

        // Delete the corresponding image file
        $imagePath = 'publication_images/' . $publicationRow['image_name'];
        if (file_exists($imagePath)) {
            unlink($imagePath);
        }

        if ($deleteLikesResult && $deleteCommentsResult && $deletePublicationResult) {
            // Deletion successful
            header("Location: homeloged.php?username=$username");
            exit();
        } else {
            // Deletion failed
            die("Publication deletion failed: " . mysqli_error($link));
        }
    } else {
        // User does not have permission to delete the publication
        die("You do not have permission to delete this publication.");
    }
}

// Redirect back to the homeloged.php page after the operation
header("Location: homeloged.php?username=$username");
exit();
?>