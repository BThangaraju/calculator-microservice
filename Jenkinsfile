pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -f docker/Dockerfile -t calculator-microservice:latest .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run calculator-microservice pytest tests/'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([url: 'https://index.docker.io/v1/', credentialsId: 'dockerhub-credentials']) {
                    sh 'docker push calculator-microservice:latest'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f kubernetes/deployment.yml'
                sh 'kubectl apply -f kubernetes/service.yml'
            }
        }

        stage('Ansible Post-Configuration') {
            steps {
                sh 'ansible-playbook -i ansible/inventory ansible/playbook.yml'
            }
        }
    }
}
