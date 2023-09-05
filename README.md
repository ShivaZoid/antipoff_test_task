# antipoff_test_task
Technical specification for the developer's backend (junior)

## Test task (https://disk.yandex.ru/i/R-6bw71atkO66Q)

### Как запустить проект:
Клонируем репозиторий и переходим в него:
~~~
cd antipoff_test_task
cd project
~~~

Создаем и активируем виртуальное окружение:
~~~
python -m venv venv

source venv/Scripts/activate

python -m pip install --upgrade pip
~~~

Ставим зависимости из requirements.txt:
~~~
pip install -r requirements.txt
~~~

Добавьте файл (.env) , расположенный по пути project/.env
~~~
SECRET_KEY='key'
CSRF_TRUSTED_ORIGINS='http://127.0.0.1, http://localhost'
~~~

Переходим в папку с файлом docker-compose.yaml:
~~~
cd ..
cd infra
~~~

Добавьте файл (.env) , расположенный по пути infra/.env
~~~
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
~~~

Далее выполняем команду:
~~~
sudo docker-compose up -d --build
~~~

Для доступа к контейнеру выполняем следующие команды:
~~~
sudo docker-compose exec web python manage.py migrate --noinput
~~~
~~~
sudo docker-compose exec web python manage.py createsuperuser
~~~
~~~
sudo docker-compose exec web python manage.py collectstatic --no-input
~~~


Остановить:
~~~
sudo docker-compose stop
~~~

Удалить:
~~~
sudo docker-compose down -v
~~~


### Примеры API

Отправка запроса:
~~~
POST http://127.0.0.1/api/query/
{
  "cadastre_number": "90:09:0045012:000",
  "latitude": 80.45,
  "longitude": 10.999
}
~~~

Получение списка запросов:
~~~
GET http://127.0.0.1/api/history/
~~~

Получение результата:
~~~
GET http://127.0.0.1/api/result/{cadastre_number}
~~~

Проверка, что  сервер запустился:
~~~
GET http://127.0.0.1/api/ping

Так как в этом коде только *эмулируется работа сервера, то
необходимо через админку создать 1 экземпляр
и выбрать run (default=False)
~~~


### Документация

~~~
https://documenter.getpostman.com/view/24514266/2s9Y5ePfNY
~~~

Также есть в папке static/ есть openapi:
~~~
schema.yaml
swagger.json
~~~

Для более удобного просмотра можно воспользоваться Swagger'ом
~~~
Скопировать находящийся код из schema.yaml или swagger.json
и вставить в
https://editor.swagger.io/
~~~
