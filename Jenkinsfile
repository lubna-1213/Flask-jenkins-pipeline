pipeline {
    agent any

    environment {
        VENV = "venv"
        DEPLOY_DIR = "C:\\Users\\Public\\jenkins-deploy"

    }

    stages {

      stage('Install Dependencies') {
    steps {
        bat '''
        python -m venv %VENV%
        call %VENV%\\Scripts\\activate
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest
        '''
    }
}

       stage('Run Unit Tests') {
    steps {
        bat '''
        call %VENV%\\Scripts\\activate
        set PYTHONPATH=%cd%
        python -m pytest tests
        '''
    }
}



        stage('Build Application') {
            steps {
                bat '''
                if not exist build mkdir build
                copy app.py build
                copy requirements.txt build
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                bat '''
                if not exist %DEPLOY_DIR% mkdir %DEPLOY_DIR%
                xcopy build %DEPLOY_DIR% /E /Y
                echo Application deployed to %DEPLOY_DIR%
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
