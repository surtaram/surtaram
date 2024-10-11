pipeline {
    agent any  // Executes on any available agent

    stages {
        stage('Build') {
            steps {
                // Commands to build your application
                echo 'Building...'
                sh 'mvn clean install'  // Example for Maven-based projects
            }
        }
        stage('Test') {
            steps {
                // Commands to test your application
                echo 'Testing...'
                sh 'mvn test'  // Example for running tests
            }
        }
        stage('Deploy') {
            steps {
                // Commands to deploy your application
                echo 'Deploying...'
                sh 'mvn deploy'  // Example for deploying
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
