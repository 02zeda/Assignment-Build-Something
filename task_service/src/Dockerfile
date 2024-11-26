FROM python:3
RUN pip install fastapi[standard]
EXPOSE 5000
WORKDIR /app
COPY . .
ENTRYPOINT [ "fastapi", "dev","task_service.py" ]