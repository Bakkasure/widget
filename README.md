# Проект "Виджет банковских операций клиента"

## Описание:

Проект "Виджет банковских операций клиента" - это новая фича в личном кабинете клиента,
которая показывает несколько последних успешных банковских операций клиента. 
Данный проект готовит данные для отображения в новом виджете.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/Bakkasure/widget.git
```
2. Установите зависимости:
```
poetry install requests
```

## Описание модулей
### Модуль masks
1. Функция get_mask_card_number
- принимает номер карты и отдает на выход маску номера карты
- пример маски номера 7000 79** **** 6361

2. Функция get_mask_account 
- принимает номер счета и отдает на выход маску номера счета
- пример маски номера **4305

### Модуль widget 
1. Функция mask_account_card 
- принимает имя и номер карты или счета отдает на выход имя и маску номера карты или счета
- привер ввода: Visa Platinum 7000 7922 8960 6361
- Счет 73654108430135874305
- Visa Classic 6831982476737658
- Маску номера получает в модуле masks

### Модуль processing
1. Функция filter_by_state
- принимает список словарей и возвращает отсортированный по ключу "state"
2. Функция sort_by_date
- Принимает список словарей и возвращает отсортированный по ключу "date"
- сортировка True - по убыванию, False - по возрастанию

### Модуль generators
1. Функция filter_by_currency 
- выдает транзакции, где валюта операции соответствует заданной.
2. Функция transaction_descriptions 
- принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
3. Функция card_number_generator 
- может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.

### Модуль decorators
Функция log
- Декоратор который автоматически регистрирует детали выполнения функций, такие как время вызова, имя функции, передаваемые аргументы, результат выполнения и информация об ошибках.
По умолчанию, логи выводятся в консоль. Для сохранения информации в файл, необходимо указать название файла и расширение в аргументе filename, который принимает декоратор. 

Пример:
```
filename="log.txt"
```

## Тестирование

Проект покрыт юнит-тестами Pytest на 100%.
Для их запуска введите команду:
```
pytest 'путь к директории, которую тестируем'
```
## Документация:

Для получения дополнительной информации обратитесь к [документации](README.md).
