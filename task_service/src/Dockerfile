FROM python:3

EXPOSE 5000

WORKDIR /app
COPY requirements.txt /app/
COPY task_service/task_service.py /app/
RUN pip install --no-cache-dir -r requirements.txt
