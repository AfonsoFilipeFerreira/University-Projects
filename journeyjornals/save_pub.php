<?php
include 'connect.php';
include 'session.php';

// Check if all fields have inputs
if (!empty($_POST['title']) && !empty($_POST['location']) && !empty($_POST['description']) && !empty($_FILES['image']['tmp_name'])) {
    $imageTmp = $_FILES['image']['tmp_name'];
    $imageName = $_FILES['image']['name'];

    // Define the target directory where the image will be stored
    $targetDirectory = 'publication_images/';

    // Move the uploaded image to the target directory without changing its name
    $targetPath = $targetDirectory . $imageName;
    move_uploaded_file($imageTmp, $targetPath);

    // Retrieve the form data
    $username = $_SESSION['username']; 
    $title = $_POST['title'];
    $location = $_POST['location'];
    $description = mysqli_real_escape_string($link, $_POST['description']);

    // Insert the data into the 'publication' table
    $sql = "INSERT INTO publication (username, title, location, description, image_name)
            VALUES ('$username', '$title', '$location', '$description', '$imageName')";

    if (mysqli_query($link, $sql)) {
        // Data inserted successfully
        echo '<script>alert("Your publication was sent for review."); window.location.href = "create.php?username=' . $username . '"; </script>';
        exit;
    } else {
        // Error occurred
        echo "Error: " . mysqli_error($link);
    }
} else {
    echo '<script>alert("Please fill in all required fields."); window.location.href = "create.php?username=' . $username . '";</script>';
    exit;
}