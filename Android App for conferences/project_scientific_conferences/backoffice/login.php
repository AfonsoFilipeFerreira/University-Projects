<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($username === 'Admin' && $password === 'admin') {
        $_SESSION['admin_logged_in'] = true;
        header("Location: dashboard.php");
        exit();
    } else {
        echo "Invalid credentials.";
    }
} else {
    header("Location: index.php");
    exit();
}
?>