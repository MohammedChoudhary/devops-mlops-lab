# DevOps + MLOps Lab Project

This project demonstrates a simple ML pipeline with automation.

## Features
- GitHub CI/CD pipeline
- Dataset tracking using DVC
- Experiment logging with MLflow
- Email alert on failure
- Docker container setup

## Run locally

pip install mlflow dvc python-dotenv
python app.py

## Run with Docker

docker build -t devops-lab .
docker run devops-lab

## Tools Used

Python, GitHub Actions, DVC, MLflow, Docker
