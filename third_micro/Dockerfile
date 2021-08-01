FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /app/third
COPY requirements.txt /app/third/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/third/

CMD python manage.py runserver 0.0.0.0:8003