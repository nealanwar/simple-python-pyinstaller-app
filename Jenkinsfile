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
              docker {
                image 'jpetazzo/dind'
              }
            }
            steps {
                sh """
                mkdir /etc/docker
                touch /etc/docker/daemon.json
                echo "
                {
                  "insecure-registries" : ["docker.h2o.ai:8080"]
                }" > /etc/docker/daemon.json
                sudo systemctl restart docker
                docker login -u $REGISTRY_USERNAME -p $REGISTRY_PASSWORD https://docker.h2o.ai
                docker run https://docker.h2o.ai/$DAI_IMAGE:$H2OAI_RUNTIME_DOCKER_TAG
                python collection.sh
                """
            }
        }
    }
}
