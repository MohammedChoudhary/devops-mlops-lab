import mlflow
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_failure_email(error_message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)

        message = f"Subject: Pipeline Failed\n\nError: {error_message}"
        server.sendmail(EMAIL_USER, EMAIL_USER, message)

        server.quit()
        print("Failure email sent")

    except Exception as e:
        print("Email failed:", e)

try:
    print("Pipeline started")

    with mlflow.start_run():
        accuracy = 0.90
        mlflow.log_metric("accuracy", accuracy)

    print("Pipeline finished successfully")

except Exception as e:
    send_failure_email(str(e))
    print("Pipeline error:", e)
