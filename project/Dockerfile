FROM python:3.9-slim

WORKDIR /app

COPY project/requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY project/ .

CMD ["gunicorn", "project.wsgi:application", "--bind", "0:8000" ]
