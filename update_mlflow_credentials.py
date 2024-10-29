import os
from mlflow.server import get_app_client


# Export the env variable for the MLflow tracking server credentials
os.environ["MLFLOW_TRACKING_USERNAME"] = "admin"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "password"

## Create a new admin user and update the password of the default admin user
# Connect to the MLflow tracking server
auth_client = get_app_client("basic-auth", tracking_uri="<TRACKING_URI>")

# Create a new admin user
auth_client.create_user(username="<YOUR_CHOSEN_USERNAME>", password="<YOUR_CHOSEN_PASSWORD>")
auth_client.update_user_admin(username="YOUR_CHOSEN_USERNAME", is_admin=True)

# Update the password of the default admin user
auth_client.update_user_password(username="admin", password="<NEW_PASSWORD>")
