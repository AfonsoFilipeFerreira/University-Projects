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
        echo "Comment approved successfully.";
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
        echo "Comment deleted successfully.";
    } else {
        echo "Error deleting comment: " . $conn->error;
    }

    $stmt->close();
}

// Fetch all comments that are not approved yet
$comments = $conn->query("SELECT * FROM comments WHERE approved = 0");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Approve Comments</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<?php include_once 'header.php'; // Include header with session management ?>

<h2>Approve Comments</h2>
<table>
    <tr>
        <th>ID</th>
        <th>Username</th>
        <th>Article ID</th>
        <th>Message</th>
        <th>Approved</th>
        <th>Action</th>
    </tr>
    <?php while ($row = $comments->fetch_assoc()): ?>
        <tr>
            <td><?php echo $row['id']; ?></td>
            <td><?php echo $row['username']; ?></td>
            <td><?php echo $row['article_id']; ?></td>
            <td><?php echo $row['message']; ?></td>
            <td><?php echo $row['approved'] ? 'Yes' : 'No'; ?></td>
            <td>
                <form action="manage_comments.php" method="post">
                    <input type="hidden" name="comment_id" value="<?php echo $row['id']; ?>">
                    <?php if (!$row['approved']): ?>
                        <button type="submit" name="approve_comment">Approve</button>
                    <?php endif; ?>
                    <button type="submit" name="delete_comment">Delete</button>
                </form>
            </td>
        </tr>
    <?php endwhile; ?>
</table>

</body>
</html>
