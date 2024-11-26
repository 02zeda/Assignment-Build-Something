FROM python:3
RUN pip install streamlit
EXPOSE 8501
WORKDIR /app
COPY . .
ENTRYPOINT [ "streamlit","run","app.py" ]