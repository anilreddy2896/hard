node ('HRMS' && 'DEV'){
    properties([pipelineTriggers([corn('* * * * *')])])
    stage ("SCM"){
        git "https://github.com/wakaleo/game-of-life.git"
    }
    stage ("build"){
        sh 'mvn clean package'
    }
    stage('publish result'){
        junit  "gameoflife-web/target/surefire-reports/*.xml"
    }
    stage('artifact'){
        archiveArtifacts artifacts: "gameoflife-web/target/*.war",followSymlinks: false
    }
}