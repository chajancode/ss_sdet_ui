pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.10.19'
        ALLURE_RESULTS = 'allure-results'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Код загружен из GitHub'
            }
        }
        
        stage('Setup Python') {
            steps {
                echo 'Настройка Python'
                sh '''
                    python3 --version
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Запуск тестов с Allure') {
            steps {
                echo 'Запуск автотестов с генерацией Allure results'
                sh '''
                    . venv/bin/activate
                    bash_scripts/grid_run_tests.sh
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: "${ALLURE_RESULTS}/**/*", fingerprint: true
                }
            }
        }

                stage('Генерация Allure отчёта') {
            steps {
                echo 'Генерация Allure отчета'
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: "${ALLURE_RESULTS}"]]
                ])
            }
            post {
                always {
                    publishHTML([
                        reportDir: 'allure-report',
                        reportFiles: 'index.html',
                        reportName: 'Allure Report'
                    ])
                }
            }
        }
    }
        post {
        always {
            echo 'Очистка временных файлов'
            cleanWs()
        }
        success {
            echo 'Tесты успешно пройдены'
        }
        failure {
            echo 'Некоторые тесты упали'
        }
    }
}