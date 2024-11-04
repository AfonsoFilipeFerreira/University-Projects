<?php
session_start();
include 'functions.php';
include 'config.php';
redirectIfNotLoggedIn();

// Fetch conferences for the dropdown
$conferences = [];
$result = $conn->query("SELECT id, name, address FROM conferences");
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $conferences[] = $row;
    }
}

// Fetch articles for the dropdown
$articles = [];
$result = $conn->query("SELECT id, title FROM articles");
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $articles[] = $row;
    }
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $conference_id = $_POST['conference_id'];
    $title = $_POST['title'];
    $start_time = $_POST['start_time'];
    $end_time = $_POST['end_time'];
    $room = $_POST['room'];
    $day = $_POST['day'];
    $article_ids = $_POST['article_ids']; // Changed to an array of article IDs

    $stmt = $conn->prepare("INSERT INTO sessions (conference_id, title, start_time, end_time, room, day) VALUES (?, ?, ?, ?, ?, ?)");
    $stmt->bind_param("issssi", $conference_id, $title, $start_time, $end_time, $room, $day);

    if ($stmt->execute()) {
        $session_id = $stmt->insert_id;

        // Insert articles related to the session
        foreach ($article_ids as $article_id) {
            $stmt_article = $conn->prepare("INSERT INTO session_articles (session_id, article_id) VALUES (?, ?)");
            $stmt_article->bind_param("ii", $session_id, $article_id);
            $stmt_article->execute();
            $stmt_article->close();
        }
        echo "Session scheduled successfully.";
    } else {
        echo "Error scheduling session: " . $conn->error;
    }

    $stmt->close();
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Schedule Session</title>
    <link rel="stylesheet" href="styles.css">
    <script>
        function addArticleDropdown() {
            // Get the container where we'll append new dropdowns
            var container = document.getElementById('articles-container');
            
            // Create a new select element
            var newSelect = document.createElement('select');
            newSelect.name = 'article_ids[]';
            newSelect.required = true;  // Making it required

            // Add options to the new select element
            var articles = <?php echo json_encode($articles); ?>;
            articles.forEach(function(article) {
                var option = document.createElement('option');
                option.value = article.id;
                option.text = article.title;
                newSelect.appendChild(option);
            });

            // Create a label for the new select element
            var newLabel = document.createElement('label');
            newLabel.innerHTML = 'Select Article:';

            // Append the label and select element to the container
            container.appendChild(newLabel);
            container.appendChild(newSelect);
            container.appendChild(document.createElement('br')); // Add a line break for better spacing
        }
    </script>
</head>
<body>
<?php
include_once 'header.php';
redirectIfNotLoggedIn();
?>

<h2>Schedule Session</h2>
<form action="schedule_session.php" method="post">
    <label for="conference_id">Select Conference:</label>
    <select id="conference_id" name="conference_id" required>
        <?php foreach ($conferences as $conference): ?>
            <option value="<?php echo $conference['id']; ?>"><?php echo $conference['name']; ?></option>
        <?php endforeach; ?>
    </select>

    <div id="articles-container">
        <label for="article_ids">Select Article:</label>
        <select id="article_ids" name="article_ids[]" required>
            <?php foreach ($articles as $article): ?>
                <option value="<?php echo $article['id']; ?>"><?php echo $article['title']; ?></option>
            <?php endforeach; ?>
        </select>
        <br>
    </div>
    <button type="button" onclick="addArticleDropdown()">Add Another Article</button>

    <label for="title">Session Title:</label>
    <input type="text" id="title" name="title" required>
    
    <label for="start_time">Start Time:</label>
    <input type="datetime-local" id="start_time" name="start_time" required>
    
    <label for="end_time">End Time:</label>
    <input type="datetime-local" id="end_time" name="end_time" required>
    
    <label for="room">Room:</label>
    <input type="text" id="room" name="room" required>
    
    <label for="day">Day of Conference:</label>
    <input type="number" id="day" name="day" required>
    
    <button type="submit">Schedule Session</button>
</form>
</body>
</html>
