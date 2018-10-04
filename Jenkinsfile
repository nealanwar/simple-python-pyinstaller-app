pipeline {
    agent none

    environment {
          MESSAGE = 'print me'
    }

    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'echo $MESSAGE'
                sh 'echo $MESSAGE > out.txt'
            }
            post {
              success {
                archiveArtifacts 'out.txt'
              }
            }
        }
    }
}
