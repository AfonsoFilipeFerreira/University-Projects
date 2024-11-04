<?php
include 'connect.php';
include 'session.php';

// Retrieve unpublished publications
$sql = "SELECT * FROM publication WHERE aproved = 0";
$result = mysqli_query($link, $sql);
if (!$result) {
    die("Query failed: " . mysqli_error($link));
}

// Handle approve button click
if (isset($_POST['approve'])) {
    $publicationId = $_POST['publication_id'];

    // Update the 'approved' column to 1
    $updateSql = "UPDATE publication SET aproved = 1 WHERE id = $publicationId";
    mysqli_query($link, $updateSql);

    // Redirect to the same page to update the publication list
    header("Location: review.php?username=$username");
    exit();
}

// Handle disapprove button click
if (isset($_POST['disapprove'])) {
    $publicationId = $_POST['publication_id'];

    // Retrieve the image name from the database
    $getImageSql = "SELECT image_name FROM publication WHERE id = $publicationId";
    $imageResult = mysqli_query($link, $getImageSql);
    if ($imageResult && mysqli_num_rows($imageResult) > 0) {
        $row = mysqli_fetch_assoc($imageResult);
        $imageName = $row['image_name'];

        // Delete the row from the 'publication' table
        $deleteSql = "DELETE FROM publication WHERE id = $publicationId";
        mysqli_query($link, $deleteSql);

        // Delete the corresponding image file
        $imagePath = 'publication_images/' . $imageName;
        if (file_exists($imagePath)) {
            unlink($imagePath);
        }

        // Redirect to the same page to update the publication list
        header("Location: review.php?username=$username");
        exit();
    }
}
?>

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="review.css">
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
<main class="main-content">
    <h1>Review</h1>
    <div class="publications">
        <?php while ($row = mysqli_fetch_assoc($result)): ?>
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
                    <p class="publication-description">
                        <?php echo $row['description']; ?>
                    </p>
                </div>
                <!-- Approve button -->
                <form method="post" action="">
                    <input type="hidden" name="publication_id" value="<?php echo $row['id']; ?>">
                    <input type="submit" name="approve" value="Approve" class="custom-button">
                </form>

                <!-- Disapprove button -->
                <form method="post" action="">
                    <input type="hidden" name="publication_id" value="<?php echo $row['id']; ?>">
                    <input type="submit" name="disapprove" value="Disapprove" class="custom-button">
                </form>
            </div>
        <?php endwhile; ?>
    </div>
</main>
<footer>
    <p class="footer">&copy; Journey Jornals 2023. All rights reserved.</p>
</footer>
<script>
    //logout button
    function logout() {
        // Unset the session variable for the username
        <?php unset($_SESSION["username"]); ?>

        // Redirect to the logout page or any other desired location
        window.location.href = "homepage.php";
    }
</script>