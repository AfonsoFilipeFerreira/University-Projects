<?php
include 'config.php';

if (isset($_GET['article_id'])) {
    $article_id = intval($_GET['article_id']);

    $stmt = $conn->prepare("SELECT * FROM comments WHERE article_id = ? AND approved = 1");
    $stmt->bind_param("i", $article_id);

    $stmt->execute();
    $result = $stmt->get_result();

    $comments = [];
    while ($row = $result->fetch_assoc()) {
        $comments[] = $row;
    }

    echo json_encode($comments);

    $stmt->close();
    $conn->close();
} else {
    echo json_encode(["error" => "No article ID provided"]);
}
?>
