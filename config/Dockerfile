FROM docker.arvancloud.ir/python:latest

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -U pip && \
    pip install -r requirements.txt

COPY . /code/

EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver"]
