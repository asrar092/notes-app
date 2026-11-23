@Library("shared") _
pipeline{
    agent { label "ashif"}
    
    stages{
        stage("Hello"){
            steps{
                script{
                    hello()
                }
            }
        }
        stage("Code"){
            steps{
                echo "This is a Code Colening"
                git url:"https://github.com/asrar092/notes-app.git", branch: "main"
            }
        }
        stage("build"){
            steps{
                echo "This is Code Building"
                sh "docker build -t note-app ."
            }
        }
        stage("Images Push in Docker Hub"){
            steps{
                echo "This is Push image in DockerHub"
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'dockerHubUser',
                    passwordVariable: 'dockerHubPass')]){
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                sh "docker tag note-app ${env.dockerHubUser}/note-app"
                sh "docker push ${env.dockerHubUser}/note-app"
                echo "It is Done Bro!!"
                }
            }
        }
        stage("Deploy"){
            steps{
                echo "Delpoy my Code"
                sh "docker compose up -d"
            }
        }
    }
}
