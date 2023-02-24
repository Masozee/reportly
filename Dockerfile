FROM python:3.9.6-alpine AS builder

WORKDIR /propertly

COPY requirements.txt /propertly

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /propertly

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
