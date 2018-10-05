pipeline {
  // agent "any" starts the pipeline on my local machine,
  // with a local copy of the DAI image
  agent any
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
            steps {
                sh """
                docker run /home/$DAI_IMAGE > out.txt
                """
            }
            post {
                success {
                    archiveArtifacts 'out.txt'
                }
            }
        }
        stage('Collection') {
            steps {
                sh """
                python collection.sh
                """
            }
        }
    }
}
