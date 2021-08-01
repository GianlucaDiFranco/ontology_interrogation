FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /app/first
COPY requirements.txt /app/first/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/first/

CMD python manage.py runserver 0.0.0.0:8001