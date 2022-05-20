FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /test_messager
COPY . /test_messager/
WORKDIR /test_messager

COPY ./requirements.txt usr/src/requirements/txt

RUN pip install --upgrade pip
RUN pip install -r /usr/src/requirements/txt


ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "127.0.0.1:8000"]