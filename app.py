import mlflow

print("Pipeline started")

with mlflow.start_run():
    accuracy = 0.85
    mlflow.log_metric("accuracy", accuracy)

print("Metric logged to MLflow")
print("Pipeline finished successfully")
