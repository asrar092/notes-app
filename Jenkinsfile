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
                script{
                    Code_Cloning("https://github.com/asrar092/notes-app.git","main")
                }
                echo "Sussessfully Clone code"
            }
        }
        stage("build"){
            steps{
                script{
                    build("note-app","latest","asrar092")
                }
            }
        }
        stage("Images Push in Docker Hub"){
            steps{
                script{
                    push_dockerhub("note-app")
                }
                echo "It is Done Bro!!"
            }
        }
        stage("Deploy"){
            steps{
                echo "Delpoy my Code"
                sh "docker compose down && docker compose up -d"
            }
        }
    }
}
