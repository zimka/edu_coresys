Установка
---------

1. Установить пакет:

  ::

    pip install edu_coresys

2. Добавить приложение в INSTALLED_APPS

  ::

    INSTALLED_APPS += ('edu_coresys',)

3. Запустить миграции

  ::

    python manage.py migrate edu_coresys --settings=YOUR_SETTINGS

4. Задать в settings.py: DIRECTION_UUIDS, PLE_BASE_URL, PLE_APP_TOKEN, PLE_GUID_UUIDS(для скачивания тестов), LRS_BASE_URL, LRS_AUTH_TOKEN, LRS_ARCHETYPES_GUID, DP_BASE_URL, DP_APP_TOKEN
