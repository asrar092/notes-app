pipeline{
    agent { label "ashif"}
    
    stages{
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
                sh "docker login -u asrar092 -p dckr_pat_BxvMH3bakYxwOGEw-4vLs8UQy1"
                sh "docker tag note-app asrar092/note-app"
                sh "docker push asrar092/note-app"
                echo "It is Done Bro!!"
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
