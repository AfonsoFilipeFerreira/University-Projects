<?php
include 'connect.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST["email"];
    $username = $_POST["user"];
    $password = $_POST["pass"];

      // Check if user or email already exists
      $checkQuery = "SELECT * FROM registuser WHERE username = '$username' OR email = '$email'";
      $checkResult = mysqli_query($link, $checkQuery);
  
      if (mysqli_num_rows($checkResult) > 0) {
          // User or email already exists
          echo "<script>alert('Username or email already exists.'); window.location.href = 'homepage.php';</script>";
          exit; // Stop further execution of the script
      }
  
      // Insert the data into the table
      $sql = "INSERT INTO registuser (email, username, password) VALUES ('$email', '$username', '$password')";
  
      if (mysqli_query($link, $sql)) {
          echo "<script>alert('Registration successful!'); window.location.href = 'homepage.php';</script>";
          exit; // Stop further execution of the script
      } else {
          echo "Error: " . $sql . "<br>" . mysqli_error($link);
      }
  }