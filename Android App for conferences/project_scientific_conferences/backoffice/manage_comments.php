<?php
session_start();
include 'functions.php';
include 'config.php';
redirectIfNotLoggedIn(); // Assuming this function checks if the user is logged in as admin

// Handle marking a comment as approved
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['approve_comment'])) {
    $comment_id = intval($_POST['comment_id']);
    $stmt = $conn->prepare("UPDATE comments SET approved = 1 WHERE id = ?");
    $stmt->bind_param("i", $comment_id);

    if ($stmt->execute()) {
        header("Location: aprove_comments.php");
        exit();
    } else {
        echo "Error approving comment: " . $conn->error;
    }

    $stmt->close();
}

// Handle deleting a comment
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['delete_comment'])) {
    $comment_id = intval($_POST['comment_id']);
    $stmt = $conn->prepare("DELETE FROM comments WHERE id = ?");
    $stmt->bind_param("i", $comment_id);

    if ($stmt->execute()) {
        header("Location: aprove_comments.php");
        exit();
    } else {
        echo "Error deleting comment: " . $conn->error;
    }

    $stmt->close();
}
?>
