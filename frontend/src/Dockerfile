FROM python:3
EXPOSE 8501
WORKDIR /app
COPY requirements.txt /app/
COPY app.py /app/
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "streamlit","run","app.py" ]