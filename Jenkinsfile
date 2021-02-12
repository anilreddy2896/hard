node ('HRMS'){
    properties([pipelineTriggers([pollSCM('* * * * *')])])
    stage ("SCM"){
        git "https://github.com/wakaleo/game-of-life.git"
    }
    stage ("build"){
        //this is the build step
        sh 'mvn clean package'
    }
    stage('publish result'){
        junit  "gameoflife-web/target/surefire-reports/*.xml"
    }
    stage('artifact'){
        archiveArtifacts artifacts: "gameoflife-web/target/*.war",followSymlinks: false
    }
}