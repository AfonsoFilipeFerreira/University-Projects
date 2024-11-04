<?php
include 'connect.php';

// Retrieve last three approved publications
$sql = "SELECT * FROM publication WHERE aproved = 1 ORDER BY id DESC LIMIT 3";
$result = mysqli_query($link, $sql);
if (!$result) {
    die("Query failed: " . mysqli_error($link));
}
?>

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Homepage.css">
    <title>Journey Jornals</title>
</head>
<dialog id="myDialog">
    <div id="Login" class="box">
        <h1>Login</h1>
        <form action="dologin.php" method="post">
            <label for="user">Username:</label>
            <input type="user" id="username" name="username"><br>
            <label for="password">Password:</label>
            <div>
                <input type="password" id="password" name="password">
                <img src="eye hide.png">
                <img src="eye show.png" style="display: none;">
            </div><br>
            <input type="submit" value="Login" id="log" class="button">
        </form>
        <a href="#" id="registLink">Don't have an account yet? Click here to regist.</a>
    </div>
    <div id="Registe" style="display: none;" class="box">
        <div id="registdiv">
            <h1>Registe an account</h1>
            <form action="doregister.php" method="post">    
                <label for="email">Email:</label>
                <input type="email" id="email" name="email"><br>

                <label for="user">Username:</label>
                <input type="user" id="user" name="user"><br>

                <label for="password">Password:</label>
                <div>
                    <input type="password" name="pass" id="pass">
                    <img src="eye hide.png">
                    <img src="eye show.png" style="display: none;">
                </div><br>
                <label for="passwordconfimation">Comfirm your password:</label>
                <div>
                    <input type="password" name="passc" id="passc">
                    <img src="eye hide.png">
                    <img src="eye show.png" style="display: none;">
                </div>
                <divalert id="alert" style="display: none;">The passwords do not match!</divalert><br>
                <input type="button" value="Sign up" id="signup" class="button">
            </form>
        </div>
    </div>
</dialog>
<header>
    <div class="header">
        <div class="logo-container">
            <img src="logo.png" class="logo">
        </div>
        <div class="navs">
            <div class="navigator" id="myButton">Search</div>
            <div class="navigator" id="myButton">Explore</div>
            <div class="navigator" id="myButton">Profile</div>
            <div class="navigator" id="myButton">Create</div>
            <div class="navigator" id="myButton" style="margin-left: 400px;">Login/Regist</div>
        </div>
    </div>
</header>

<body>
    <main class="main-content">
        <section>
            <h1>About Our Site</h1>
            <p> Our site intents for the user to share memories and experiences made during their travels. Share with
                the
                other users pictures of places you have been to, what did you do there, and if you would like to come
                back
                and recommend it to other users. You can share the coordinates of the mentioned place and other info you
                like. Here Below you can see the latest posts made by other users. Log in or register an account to see
                more.</p>
        </section>
        <section class="latest-posts">
            <h1>Latest Posts</h1>
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
                        <div class="pub-interactions">
                            <img src="like_button-removebg-preview.png" class="like"> <img
                                src="liked_button-removebg-preview.png" class="like" style="display: none;"><a
                                class="toggle-button" href="#">Show Map</a>
                        </div>
                        <p class="publication-description">
                            <?php echo $row['description']; ?>
                        </p>
                    </div>
                </div>
            <?php endwhile; ?>
        </section>
    </main>

</body>
<footer>
    <p class="footer">&copy; Journey Jornals 2023. All rights reserved.</p>
</footer>
<script src="homepage.js"></script>

</html>