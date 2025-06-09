<?php
require "config.php";

$result = $conn->query("SELECT * FROM users"); 
?>

<!DOCTYPE html>
<html>
<head>
    <title>Управление пользователями</title>
</head>
<body>
    <h2>Добавить пользователя</h2>
    <form method="post" action="add.php">
        <input type="text" name="name" placeholder="Имя" required><br>
        <input type="text" name="surname" placeholder="Фамилия" required><br>
        <input type="email" name="email" placeholder="Email" required><br>
        <input type="number" name="age" placeholder="Возраст" required><br>
        <button type="submit">Добавить</button>
    </form>

    <h2>Список пользователей</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Surname</th>
            <th>Email</th>
            <th>Age</th>
            <th>Actions</th>
        </tr>

        <?php while ($row = $result->fetch_assoc()): ?>
            <td><?= $row['id'] ?></td>
            <td><?= $row['name'] ?></td>
            <td><?= $row['surname'] ?></td>
            <td><?= $row['email'] ?></td>
            <td><?= $row['age'] ?></td>

            <td>
                <a href="edit.php?id=<?= $row['id'] ?>">Редактировать</a> |
                <a href="delete.php?id=<?= $row['id'] ?>" onclick="return confirm('Удалить?')">Удалить</a>
            </td>
        <?php endwhile; ?>

    </table>
</body>
</html>
