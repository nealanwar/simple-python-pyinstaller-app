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
        stage('Build') {
            agent {
            steps {$REGISTRY_USERNAME -p $REGISTRY_PASSWORD docker.h2o.ai
                docker pull docker.h2o.ai/$DAI_IMAGE:$H2OAI_RUNTIME_DOCKER_TAG
                sh """
                docker login -u $REGISTRY_USERNAME -p $REGISTRY_PASSWORD docker.h2o.ai
                docker pull docker.h2o.ai/$DAI_IMAGE:$H2OAI_RUNTIME_DOCKER_TAG
                python collection.sh
                """
            }
        }
    }
}
