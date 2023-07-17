<?php
// Подключаемся к файлу базы данных
$db = new PDO('sqlite:users.db');

// Получаем данные из формы входа
$username = $_POST['username'];
$password = $_POST['password'];

// Получаем данные пользователя из базы данных
$stmt = $db->prepare("SELECT * FROM users WHERE username = ?");
$stmt->execute([$username]);
$user = $stmt->fetch();

// Проверяем правильность введенного пароля
if ($user && password_verify($password, $user['password'])) {
  // Сессия пользователя
  session_start();
  $_SESSION['user_id'] = $user['id'];
  
  // Перенаправляем пользователя на страницу профиля
  header('Location: profile.php');
  exit();
} else {
  // Если данные введены неправильно, перенаправляем на страницу входа с ошибкой
  header('Location: login.php?error=1');
  exit();
}
?>