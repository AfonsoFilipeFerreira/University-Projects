<?php
include 'session.php';
include 'connect.php';

$profilePictureDir = 'profile_pics/';
$defaultProfilePicture = 'user-pic.jpg';
$profilePicture = '';

// Check if the form is submitted and the username is provided
if (isset($_POST['user'])) {
    $user = $_POST['user'];

    if (!empty($user)) {
        // Retrieve the user's profile picture
        $profilePicture = $profilePictureDir . $defaultProfilePicture; // Default profile picture path

        // Check if the user has a profile picture 
        $files = scandir($profilePictureDir);

        // Look for a file with the username in the file name
        foreach ($files as $file) {
            if (strpos($file, $user) !== false) {
                $profilePicture = $profilePictureDir . $file;
                break;
            }
        }

        // Retrieve the user's publications
        $sql = "SELECT * FROM publication WHERE username = '$user' AND aproved = 1 ORDER BY id DESC";
        $result = mysqli_query($link, $sql);
    }
}
/// Function to check if a user has permission to delete a comment
function canDeleteComment($commentUsername)
{
    global $username;
    // Allow deletion if the logged-in user is the comment owner or an admin
    return $commentUsername === $username || $username === "Admin";
}

// Check if the comment deletion form is submitted
if (isset($_POST['delete_comment'])) {
    $commentId = $_POST['comment_id'];

    // Retrieve the comment's owner username
    $commentOwnerSql = "SELECT username FROM comments WHERE id = $commentId";
    $commentOwnerResult = mysqli_query($link, $commentOwnerSql);
    $commentOwnerRow = mysqli_fetch_assoc($commentOwnerResult);
    $commentOwner = $commentOwnerRow['username'];

    // Check if the logged-in user has permission to delete the comment
    if (canDeleteComment($commentOwner)) {
        // Perform the deletion query
        $deleteCommentSql = "DELETE FROM comments WHERE id = $commentId";
        $deleteCommentResult = mysqli_query($link, $deleteCommentSql);

        if ($deleteCommentResult) {
            // Comment deleted successfully
            header("Location: search.php?username=$username");
            exit();
        } else {
            // Comment deletion failed
            die("Comment deletion failed: " . mysqli_error($link));
        }
    } else {
        // User does not have permission to delete the comment
        die("You do not have permission to delete this comment.");
    }
}
?>

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="search.css">
    <title>Journey Jornals</title>
</head>

<header>
    <div class="header">
        <div class="logo-container">
            <a href="homeloged.php?username=<?php echo $username; ?>"><img src="logo.png" class="logo"></a>
        </div>
        <div class="navs">
            <a href="search.php?username=<?php echo $username; ?>">
                <div class="navigator">Search</div>
            </a>
            <a href="explore.php?username=<?php echo $username; ?>">
                <div class="navigator">Explore</div>
            </a>
            <a href="ProfilePage.php?username=<?php echo $username; ?>">
                <div class="navigator">Profile</div>
            </a>
            <a href="create.php?username=<?php echo $username; ?>">
                <div class="navigator">Create</div>
            </a>
        </div>
        <div class="user-dropdown">
            <span class="hp">
                <?php echo $username; ?>
            </span>
            <span class="arrow">▼</span>
            <div class="dropdown-content">
                <a href="#" onclick="logout()">Logout</a>
                <?php if ($username === "Admin"): ?>
                    <a href="review.php?username=<?php echo $username; ?>">Content Review</a>
                <?php endif; ?>
            </div>
        </div>


    </div>
</header>

<body>

    <main class="main-content">
        <div class="search">
            <form action="" method="POST">
                <input type="text" name="user" placeholder="Enter username">
                <input type="submit" value="Search" class="search-button">
            </form>
        </div>


        <?php if (isset($user) && isset($result) && mysqli_num_rows($result) > 0): ?>
            <div class="profile-section">
                <h2>
                    <?php echo $user; ?>
                </h2>
                <img src="<?php echo $profilePicture; ?>" class="profile-picture">
            </div>

            <div class="publications">
                <h1>Publications</h1>
                <?php while ($row = mysqli_fetch_assoc($result)): ?>
                    <?php
                    // Check if the user has already liked the publication
                    $publicationId = $row['id'];
                    $likeSql = "SELECT * FROM likes WHERE username = '$username' AND publication_id = $publicationId AND `like` = 1";
                    $likeResult = mysqli_query($link, $likeSql);

                    if ($likeResult) {
                        $userLiked = mysqli_num_rows($likeResult) > 0;
                    } else {
                        die("Error: " . mysqli_error($link)); // Display error message if query fails
                    }
                    
                    //number of likes
                    $publicationId = $row['id'];
                    $countLikesSql = "SELECT COUNT(*) AS likeCount FROM likes WHERE publication_id = $publicationId AND `like` = 1";
                    $countLikesResult = mysqli_query($link, $countLikesSql);

                    if ($countLikesResult) {
                        $countLikesRow = mysqli_fetch_assoc($countLikesResult);
                        $likeCount = $countLikesRow['likeCount'];
                    } else {
                        die("Error: " . mysqli_error($link)); // Display error message if query fails
                    }
                    ?>
                    <div class="publication">
                        <div class="publication-header">
                            <h3>
                                <?php echo $row['title']; ?>
                            </h3>
                            <h6>
                                <?php echo $row['username']; ?>
                            </h6>
                        </div>
                        <div class="publication-content">
                            <?php
                            $imagePath = 'publication_images/' . $row['image_name'];
                            if (file_exists($imagePath)) {
                                echo '<img src="' . $imagePath . '" alt="Publication Image" class="publication-image"> ';
                            }
                            ?>
                            <div class="publication-map">
                                <?php echo $row['location']; ?>
                            </div>
                            <div class="pub-interactions">
                                <?php if ($userLiked): ?>
                                    <form action="unlikesearch.php?username=<?php echo $username; ?>" method="POST">
                                        <input type="hidden" name="username" value="<?php echo $username; ?>">
                                        <input type="hidden" name="publication_id" value="<?php echo $row['id']; ?>">
                                        <button type="submit" name="unlike" class="like"
                                            data-publication-id="<?php echo $row['id']; ?>">
                                            <img src="liked_button-removebg-preview.png" alt="Like" class="like">
                                        </button>
                                    </form>
                                <?php else: ?>
                                    <form action="likesearch.php?username=<?php echo $username; ?>" method="POST">
                                        <input type="hidden" name="username" value="<?php echo $username; ?>">
                                        <input type="hidden" name="publication_id" value="<?php echo $row['id']; ?>">
                                        <button type="submit" name="like" class="like"
                                            data-publication-id="<?php echo $row['id']; ?>">
                                            <img src="like_button-removebg-preview.png" alt="Like" class="like">
                                        </button>
                                    </form>
                                <?php endif; ?>
                                <div class="Nlikes">
                                    <?php echo $likeCount . " " . "Likes" ?>
                                </div>
                                <a class="toggle-button" href="#">Show Map</a>
                            </div>
                            <p class="publication-description">
                                <?php echo $row['description']; ?>
                            </p>
                            <!-- Comment form -->
                            <div class="comments-session">
                                <div>
                                    <form action="add_comment_search.php?username=<?php echo $username; ?>" method="POST"
                                        class="comment-form">
                                        <input type="hidden" name="publication_id" value="<?php echo $row['id']; ?>">
                                        <textarea name="comment" placeholder="Write your comment here"></textarea>
                                        <input type="submit" value="Submit Comment">
                                    </form>
                                </div>

                                <!-- Display comments -->
                                <div class="comments">
                                    <h2>Comments</h2>
                                    <?php
                                    $publicationId = $row['id'];
                                    $commentSql = "SELECT * FROM comments WHERE publication_id = $publicationId";
                                    $commentResult = mysqli_query($link, $commentSql);
                                    while ($commentRow = mysqli_fetch_assoc($commentResult)) {
                                        echo '<div class="comment">';
                                        echo '<strong>' . $commentRow['username'] . '</strong>: ' . $commentRow['comment'];

                                        // Add delete button if the user has permission
                                        if (canDeleteComment($commentRow['username'])) {
                                            echo '<form method="POST" class="delete-comment-form" style="display: inline-block;">';
                                            echo '<input type="hidden" name="comment_id" value="' . $commentRow['id'] . '">';
                                            echo '<button type="submit" name="delete_comment" class="delete-button">Delete</button>';
                                            echo '</form>';
                                        }

                                        echo '</div>';
                                    }
                                    ?>
                                </div>
                            </div>
                            <!-- Delete publication button -->
                            <?php if ($username === $row['username']): ?>
                                <form action="delete_pub_search.php" method="POST" class="delete-publication-form">
                                    <input type="hidden" name="username" value="<?php echo $username; ?>">
                                    <input type="hidden" name="publication_id" value="<?php echo $row['id']; ?>">
                                    <button type="submit" name="delete_publication" class="delete-button">Delete
                                        Publication</button>
                                </form>
                            <?php endif; ?>
                        </div>
                    </div>
                <?php endwhile; ?>
            </div>
        <?php else: ?>
            <p style="margin-top: 100px;">No publications found.</p>
        <?php endif; ?>
    </main>

</body>
<footer>
    <p class="footer">&copy; Journey Jornals 2023. All rights reserved.</p>
</footer>
<script src="search.js"></script>
<script>
    //logout button
    function logout() {
        // Unset the session variable for the username
        <?php unset($_SESSION["username"]); ?>

        // Redirect to the logout page or any other desired location
        window.location.href = "homepage.php";
    }
</script>