FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install typing_extensions --upgrade
RUN pip install mlflow dvc python-dotenv

CMD ["python", "app.py"]
