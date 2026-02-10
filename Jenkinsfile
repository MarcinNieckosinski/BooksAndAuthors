pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    dockerImage = docker.build("books-and-authors-tests")
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'pytest'
                    }
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'report.html', fingerprint: true
                }
                unsuccessful {
                    echo "Tests failed!"
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline finished successfully."
        }
        failure {
            echo "Pipeline failed."
        }
    }
}
