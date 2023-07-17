$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";
 $conn = mysqli_connect($servername, $username, $password, $dbname);
 // Регистрация нового пользователя
if(isset($_POST['register'])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $password = $_POST['password'];
     // Проверка, существует ли пользователь с таким же email
    $sql = "SELECT * FROM users WHERE email='$email'";
    $result = mysqli_query($conn, $sql);
     if(mysqli_num_rows($result) > 0) {
        echo "Пользователь с таким email уже существует";
    } else {
        // Добавление нового пользователя в базу данных
        $sql = "INSERT INTO users (name, email, password) VALUES ('$name', '$email', '$password')";
        if(mysqli_query($conn, $sql)) {
            echo "Регистрация прошла успешно";
        } else {
            echo "Ошибка при регистрации: " . mysqli_error($conn);
        }
    }
}
 // Авторизация пользователя
if(isset($_POST['login'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];
     // Проверка, существует ли пользователь с таким же email и паролем
    $sql = "SELECT * FROM users WHERE email='$email' AND password='$password'";
    $result = mysqli_query($conn, $sql);
     if(mysqli_num_rows($result) > 0) {
        echo "Авторизация прошла успешно";
    } else {
        echo "Неверный email или пароль";
    }
}
 mysqli_close($conn);
?>