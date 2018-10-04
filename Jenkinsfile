pipeline {
    agent none

    parameters {
      string(name: 'MESSAGE', defaultValue: 'a message string')
      string(name: 'DAI_IMAGE')
      string(name: 'SETTINGS')
      string(name: 'TRAIN')
      string(name: 'TEST')
    }

    stages {
        stage('Build') {
            agent {
                docker {
                    image DAI_IMAGE
                }
            }
            steps {
                sh 'python collection.sh'
            }
        }
    }
}
