node ('HRMS'){
    properties([pipelineTriggers([pollSCM('* * * * *')])])
    stage("user input"){
        input message: "Do you want to continue"
    }
    stage ("SCM"){
        git "https://github.com/wakaleo/game-of-life.git"
    }
    stage ("build"){
        //this is the build step1 of done  jakjsa
        sh 'mvn clean package'
    }
    stage('publish result'){
        junit  "gameoflife-web/target/surefire-reports/*.xml"
    }
    stage('artifact'){
        archiveArtifacts artifacts: "gameoflife-web/target/*.war",followSymlinks: false
    }
}