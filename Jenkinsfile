pipeline{ 
    agent{ 'any ' }
    triggers{ pollSCM( '* * * * *' )}
    stages{
        stage("git"){
            steps{
                git "https://github.com/wakaleo/game-of-life.git"
            }
        stage("build"){
            steps{
                sh 'mvn clean package'
            }
        }   
    }
    
}