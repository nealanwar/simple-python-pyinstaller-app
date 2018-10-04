pipeline {
    agent none

    parameters {
      string(name: 'MESSAGE', defaultValue: 'a message string')
      string(name: 'DAI_IMAGE')
      string(name: 'SETTINGS')
      string(name: 'TRAIN')
      string(name: 'TEST')
      string(name: 'REGISTRY_USERNAME')
      string(name: 'REGISTRY_PASSWORD')
      string(name: 'H2OAI_RUNTIME_DOCKER_TAG')
    }

    stages {
        stage('Set up Driverless AI image') {
            agent {
              docker {
                image 'python:2-alpine'
              }
            }
            steps {
                sh """
                wget $DAI_IMAGE -O dai
                tar -xzf dai
                docker run dai
                """
            }
        }
        stage('Collection') {
            agent {
              docker {
                image 'python:2-alpine'
              }
            }
            steps {
                sh """
                python collection.sh
                """
            }
        }
    }
}
