<?php
// Подключаемся к файлу базы данных
$db = new PDO('sqlite:users.db');

// Получаем данные из формы регистрации
$username = $_POST['username'];
$email = $_POST['email'];
$password = password_hash($_POST['password'], PASSWORD_DEFAULT);

// Добавляем данные пользователя в базу данных
$stmt = $db->prepare("INSERT INTO users (username, email, password) VALUES (?, ?, ?)");
$stmt->execute([$username, $email, $password]);

// Перенаправляем пользователя на страницу входа
header('Location: login.php');
exit();
?>