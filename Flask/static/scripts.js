// Ваши скрипты JavaScript могут быть добавлены здесь
// Например, для взаимодействия с пользовательским интерфейсом

// Пример: скрытие сообщений об ошибке после нажатия на input
document.querySelectorAll('input').forEach(function(input) {
    input.addEventListener('input', function() {
        hideErrorMessages();
    });
});

function hideErrorMessages() {
    var errorMessages = document.querySelectorAll('.alert');
    errorMessages.forEach(function(message) {
        message.style.display = 'none';
    });
}
