# Project Organizer

Учебный Django-проект для демонстрации упорядочивания данных: добавление записей, просмотр данных из SQLite, поиск, фильтрация и сортировка через GET-параметры.

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata demo_records  # необязательно: миграции уже создают одну запись как на скриншоте
python manage.py createsuperuser
python manage.py runserver
```

Главная страница: <http://127.0.0.1:8000/>
Страница `structureproject`: <http://127.0.0.1:8000/structureproject/>
Админ-панель: <http://127.0.0.1:8000/admin/>

Если нужно открыть макет без запуска Django, используйте файл `structureproject.html` или `structureproject/index.html`. Эти HTML-страницы выглядят как демонстрационный экран из задания.

## Тестовые данные через админку

После создания суперпользователя можно добавить записи модели «Записи» вручную:

- Сервер — Инфраструктура — в работе — Высокий.
- Отчёт по практике — Документы — готово — Средний.
- Заявка клиента — CRM — ожидает — Критический.

Также можно загрузить готовый набор командой `python manage.py loaddata demo_records`.
