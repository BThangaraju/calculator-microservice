**Repository Overview:** The calculator-microservice project is a simple demonstration of a CI/CD pipeline for a calculator microservice built using Python and Flask. The pipeline encompasses various stages, including building, testing, containerization, deployment using Kubernetes, configuration with Ansible, and monitoring with Prometheus.

Key Files and Directories: 

**app/ Directory:** Contains the main application code for the calculator microservice. This includes the Flask application defining the endpoints for various calculator operations.

**docker/ Directory:** Includes Docker-related files, such as the Dockerfile, which is used to containerize the application for deployment.

**kubernetes/ Directory:** Holds Kubernetes configuration files, such as deployment and service manifests, facilitating the deployment of the microservice within a Kubernetes cluster.

**ansible/ Directory:** Contains Ansible playbooks and related configurations used for automating post-deployment tasks and configurations.

**Jenkinsfile:** Defines the CI/CD pipeline stages for Jenkins, outlining the steps for building, testing, containerizing, and deploying the application.

**README.md:** Provides an overview of the project, detailing the tech stack, pipeline stages, and instructions for setting up and running the microservice.
This structure supports a comprehensive CI/CD pipeline, ensuring efficient development, deployment, and management of the calculator microservice.


# calculator-microservice
# Step-by-Step Guide for CI/CD Pipeline Demo  
## Project: Calculator Microservice (Simple Demo) 

**Tech Stack**: Python (Flask)  
**Pipeline Stages**: 
1. Build
2. Test
3. Containerize
4. Push Docker Image
5. Deploy using Kubernetes
6. Configure with Ansible
7. Monitor with Prometheus
