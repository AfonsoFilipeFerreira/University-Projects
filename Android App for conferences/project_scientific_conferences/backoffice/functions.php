<?php
if (!function_exists('isLoggedIn')) {
    function isLoggedIn() {
        return isset($_SESSION['loggedin']) && $_SESSION['loggedin'] === true;
    }
}

if (!function_exists('login')) {
    function login($username, $password) {
        if ($username == 'Admin' && $password == 'admin') {
            $_SESSION['loggedin'] = true;
            return true;
        }
        return false;
    }
}

if (!function_exists('logout')) {
    function logout() {
        session_destroy();
        header("Location: index.php");
        exit();
    }
}

if (!function_exists('redirectIfNotLoggedIn')) {
    function redirectIfNotLoggedIn() {
        if (!isLoggedIn()) {
            header("Location: index.php");
            exit();
        }
    }
}
?>