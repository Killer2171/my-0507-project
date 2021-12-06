properties([pipelineTriggers([pollSCM('* * * * *')])])
node{
    stage("clone"){
        git branch: 'main', url: 'https://github.com/Killer2171/my-0507-project.git'
    }
    stage("show files"){
        bat "dir"
    }
}
