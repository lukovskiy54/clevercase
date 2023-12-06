// Получаем значение из localStorage или устанавливаем по умолчанию в false
var isNotificationEnabled = JSON.parse(localStorage.getItem('notificationEnabled')) || false;

// Функция для обновления состояния и стиля
function updateNotificationDisplay() {
    if (isNotificationEnabled) {
        document.getElementById('notification-list').style.display = 'block';
    } else {
        document.getElementById('notification-list').style.display = 'none';
    }
}

// Вызываем функцию для установки начального стиля при загрузке страницы
updateNotificationDisplay();

// Обработчик события при клике на кнопку
document.getElementById('not-btn').addEventListener('click', function () {
    isNotificationEnabled = !isNotificationEnabled; // Инвертируем значение
    localStorage.setItem('notificationEnabled', JSON.stringify(isNotificationEnabled)); // Сохраняем в localStorage
    updateNotificationDisplay(); // Обновляем стиль
    console.log(isNotificationEnabled);
});
