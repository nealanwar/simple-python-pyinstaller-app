pipeline {
  // agent "any" starts the pipeline on my local machine,
  // with a local copy of the DAI image
  agent any
  parameters {
      string(name: 'MESSAGE', defaultValue: 'a message string')
      string(name: 'DAI_DOWNLOAD')
      string(name: 'DAI_IMAGE')
      string(name: 'VERSION')
      string(name: 'SETTINGS')
      string(name: 'TRAIN')
      string(name: 'TEST')
      string(name: 'REGISTRY_USERNAME')
      string(name: 'REGISTRY_PASSWORD')
      string(name: 'H2OAI_RUNTIME_DOCKER_TAG')
    }

    stages {
        stage('Set up Driverless AI image') {
            // for the sake of testing on a CPU all the steps to prepare
            // a GPU host to use (install nvidia-docker, tweak options, etc.)
            // are not included, they should be in the final Jenkinsfile

            // docker load < /home/${DAI_DOWNLOAD}
            steps {
                sh """
                ls home > out.txt
                python3 a
                cd /home/dai_rel_1.3.1
                docker images
                docker run \
                  --pid=host \
                  --init \
                  --rm \
                  --shm-size=256m \
                  -u `id -u`:`id -g` \
                  -p 12345:12345 \
                  -v `pwd`/data:/data \
                  -v `pwd`/log:/log \
                  -v `pwd`/license:/license \
                  -v `pwd`/tmp:/tmp \
                  h2oai/${DAI_IMAGE}:${VERSION} &
                """
            }
            post {
                success {
                    archiveArtifacts 'out.txt'
                }
            }
        }
        stage('Collection') {
            // begin data collection on the Driverless AI image
            steps {
                sh """
                python3 collection.py ${SETTINGS} ${TRAIN} ${TEST}
                """
            }
        }
    }
}
