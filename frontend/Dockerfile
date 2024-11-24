FROM python:3
RUN pip install streamlit
EXPOSE 3000
WORKDIR /app
COPY . .
ENTRYPOINT [ "streamlit","run","app.py" ]