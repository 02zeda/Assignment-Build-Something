FROM python:3

EXPOSE 5001

WORKDIR /app
COPY requirements.txt /app/
COPY user_service/ /app/
RUN pip install --no-cache-dir -r requirements.txt
