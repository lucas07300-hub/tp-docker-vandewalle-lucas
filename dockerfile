FROM python:3.11-slim
WORKDIR /app
RUN pip install flask
RUN pip install pymongo
COPY . .
EXPOSE 80
CMD ["python", "app.py"]