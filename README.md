# Экспорт Яндекс Календаря в Google Calendar
Чтобы обойти ограничение импорта приватных событий в Google, можно воспользоваться этой неофициальной функцией. При импорте событий через эту функцию, они будут передаваться в Google как публичные. Инструкция по настройке:

1. Создать функцию в [Yandex Cloud Function](https://yandex.cloud/ru/services/functions)
2. Скопировать в неё файл `yandex_to_google.py`
3. Сделать функцию публичной и скопировать ссылку для вызова вида `https://functions.yandexcloud.net/0123456789abcdef`
4. Скопировать ссылку для экспорта Яндекс Календаря вида `https://calendar.yandex.ru/export/ics.xml?private_token=fedcba9876543210&tz_id=Europe/Moscow`
5. Объединить ссылки, чтобы получить ссылку вида `https://functions.yandexcloud.net/0123456789abcdef?private_token=fedcba9876543210&tz_id=Europe/Moscow`
6. Добавить календарь в Google по получившейся ссылке

> [!IMPORTANT]
> Это неофициальная функция, используйте её на свой страх и риск.
