FROM python:3.8
ENV PYTHONUNBUFFERED=1
ENV ONT_INTERROGATION_API_URL="http://host.docker.internal:8001/ont_interrogation/api/"
ENV SQL_MAKER_API_URL="http://host.docker.internal:8003/sql/api/"
WORKDIR /app/second
COPY requirements.txt /app/second/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/second/

CMD python manage.py runserver 0.0.0.0:8002