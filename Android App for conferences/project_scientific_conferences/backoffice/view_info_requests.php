<?php
session_start();
include 'functions.php';
include 'config.php';
redirectIfNotLoggedIn();

// Handle marking request as answered and submitting replies
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['request_id'])) {
    $request_id = $_POST['request_id'];
    $reply_message = $_POST['reply_message'];
    $user_id = $_POST['user_id'];
    $user_message = $_POST['user_message'];

    // Check if the request is already answered
    $stmt = $conn->prepare("SELECT answered FROM information_requests WHERE id = ?");
    $stmt->bind_param("i", $request_id);
    $stmt->execute();
    $stmt->bind_result($answered);
    $stmt->fetch();
    $stmt->close();

    if ($answered == 0) {
        // Begin transaction for atomicity
        $conn->begin_transaction();

        try {
            // Update information_requests table to mark as answered
            $stmt = $conn->prepare("UPDATE information_requests SET answered = 1 WHERE id = ?");
            $stmt->bind_param("i", $request_id);
            $stmt->execute();
            $stmt->close();

            // Insert reply into replies table
            $stmt = $conn->prepare("INSERT INTO replies (user_id, message, request_id) VALUES (?, ?, ?)");
            $stmt->bind_param("isi", $user_id, $reply_message, $request_id);
            $stmt->execute();
            $stmt->close();

            // Commit transaction
            $conn->commit();

            echo "Reply submitted and information request marked as answered.";
        } catch (Exception $e) {
            // Rollback transaction on error
            $conn->rollback();
            echo "Error: " . $e->getMessage();
        }
    } else {
        echo "This request is already marked as answered.";
    }
}

// Fetch information requests excluding those already answered
$info_requests = $conn->query("SELECT * FROM information_requests WHERE answered = 0");

// Display information requests in a table
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>View Information Requests</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <?php include_once 'header.php'; // Ensure this includes functions.php and starts session ?>
    <h2>View Information Requests</h2>
    <table>
        <tr>
            <th>ID</th>
            <th>User ID</th>
            <th>Username</th>
            <th>Message</th>
            <th>Action</th>
        </tr>
        <?php while ($row = $info_requests->fetch_assoc()): ?>
        <tr>
            <td><?php echo $row['id']; ?></td>
            <td><?php echo $row['user_id']; ?></td>
            <td><?php echo $row['username']; ?></td>
            <td><?php echo $row['message']; ?></td>
            <td>
                <!-- Form to submit reply and mark as answered -->
                <form action="view_info_requests.php" method="post">
                    <input type="hidden" name="request_id" value="<?php echo $row['id']; ?>">
                    <input type="hidden" name="user_id" value="<?php echo $row['user_id']; ?>">
                    <input type="hidden" name="user_message" value="<?php echo $row['message']; ?>">
                    <textarea name="reply_message" placeholder="Enter your reply" rows="3" cols="40" required></textarea>
                    <br>
                    <button type="submit">Submit Reply and Mark as Answered</button>
                </form>
            </td>
        </tr>
        <?php endwhile; ?>
    </table>
</body>
</html>
