pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/BThangaraju/calculator-microservice.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t iiitb/calculator-microservice:latest -f docker/Dockerfile .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run -e PYTHONPATH=/app calculator-microservice pytest /tests'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([url: 'https://index.docker.io/v1/', credentialsId: 'DockerHubCred']) {
                    sh 'docker push iiitb/calculator-microservice:latest'
                }
            }
        }

        stage('Pull from Docker Hub') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: './ansible/playbook_pull.yml',
                        inventory: 'inventory'
                     )
                }
            }
        }  
    
        stage('Deploy to Kubernetes') {
            steps {
                withKubeConfig([credentialsId: 'KubernetesCred', serverUrl: 'https://192.168.49.2:8443']) {
                    sh 'kubectl apply -f kubernetes/deployment.yml --validate=false'
                    sh 'kubectl apply -f kubernetes/service.yml --validate=false'
                }
            }
        }
           
        stage('Ansible Post-Configuration') {
            steps {
                sh 'ansible-playbook -i ansible/inventory ansible/playbook.yml'
            }
        }
    }
}
