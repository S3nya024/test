# Дашборд для анализа данных о восхождении и закате солнца

## Описание проекта

Этот дашборд разработан для визуализации и анализа данных о восхождении и закате солнца. Он позволяет загружать данные из CSV-файлов, содержащих информацию о времени восхождения и заката солнца по дням. Данные могут быть фильтрованы по месяцам, а также отображаются в виде линейных графиков и таблиц.

## Функциональность

- **Загрузка данных**: Поддерживается загрузка данных через интерфейс дашборда с помощью функционала `dcc.Upload`.
- **Фильтрация данных**: Возможность выбора временного периода (месяцы) для анализа данных.
- **Визуализация данных**:
  - Линейные графики показывают динамику восхождения и заката солнца в выбранном временном периоде.
  - Таблица отображает детальную информацию о каждом наблюдении.
- **Обработка ошибок**: При возникновении ошибок при загрузке или обработке данных пользователю предоставляется соответствующее сообщение.

## Как использовать

1. Запустите сервер, используя команду `python <имя_файла>.py` в терминале.
2. Откройте браузер и перейдите по адресу, указанному в консоли после запуска сервера (обычно это `http://127.0.0.1:8050/`).
3. Используйте раздел `dcc.Upload` для загрузки CSV-файла с данными.
4. Выберите временной период для анализа данных через выпадающий список.
5. Анализируйте полученные данные на линейных графиках и в таблице.

## Требования

Для работы с этим дашбордом необходимы:

- Python 3.x
- Библиотеки: Dash, Pandas, Plotly, io, base64

Этот документ составлен для описания и использования дашборда. Для дополнительной информации обращайтесь к автору.
