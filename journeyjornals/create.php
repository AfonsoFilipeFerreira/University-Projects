<?php
include 'session.php';
?>


<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="create.css">
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
        <form class="inputs" action="save_pub.php?username=<?php echo $username; ?>" method="POST" enctype="multipart/form-data">
            <div>
                <label for="title">Publication Title:</label>
                <input type="text" name="title" maxlength="255">
            </div>
            <div>
                <label for="image">Upload an image:</label>
                <input type="file" name="image">
            </div>
            <div>
                <label for="location">To upload the location follow this setps: <br>
                    1.Go to <a href="https://www.google.com/maps" target="_blank">google maps</a> and search the location or the path you wish to
                    share; <br>
                    2.On the overview click on share, this will open a box;<br>
                    3.Click on Embed a map; <br>
                    4.Click on the button COPY HTML; <br>
                    5.Paste what you just copied here. </label>
                <textarea name="location" id="frame" cols="30" rows="10"></textarea>
            </div>
            <div>
                <label for="description">Write a brief description of the place you visit, the path you've made and/or share a story you
                    experienced during your journey:</label>
                <textarea name="description" id="descripetion" cols="30" rows="10" maxlength="5000"></textarea>
            </div>
            <div><input type="submit" value="Post" id="pub"></div>

        </form>
    </main>

</body>
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