## CloudVirta
CloudVirta is a comprehensive platform for managing virtual machines (VMs) and containers in cloud environments. It provides tools for provisioning, monitoring, and orchestrating resources, leveraging modern cloud technologies.

## Features

- **Web Interface**: Manage VMs and containers via a user-friendly React.js frontend.
- **VM Management**: Interact with OpenStack for VM lifecycle operations.
- **Container Management**: Handle Docker and Kubernetes containers seamlessly.
- **Cloud Provisioning**: Use Terraform and Ansible to automate resource deployment.
- **Security**: Secure API access with JWT-based authentication.
- **Monitoring and Alerting**: Integrated Prometheus for monitoring and CloudWatch for alerts.

## Deployment

## Backend (Flask API)
**Installation**
pip install -r requirements.txt

# Run the Flask Server
python app.py
The Flask server will run at http://localhost:5000.

## Frontend (React.js)
Installation
cd frontend
npm install

# Run the React App
npm start
The React development server will run at http://localhost:3000.

## Cloud Provisioning (Terraform & Ansible)
# Terraform Setup
Ensure Terraform is installed and configured with your cloud provider credentials.
cd infrastructure
terraform init

## Deploy Resources
terraform apply

## Monitoring and Alerts (Prometheus & CloudWatch)
# Prometheus Configuration
Update prometheus.yml as needed and ensure Prometheus is correctly scraping endpoints.

# CloudWatch Alerts
Configure CloudWatch alerts using cloudwatch_alerts.tf to monitor resource thresholds.
