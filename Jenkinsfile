pipeline {
    agent any

    parameters {
        string(name: 'BRANCH', defaultValue: 'alerts-tests', description: 'Ветка для сборки')
    }
    
    environment {
        PYTHON_VERSION = '3.10'
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
                    python3.10 --version
                    python3.10 -m venv venv
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
        }
        stage('Статы тестов') {
            steps {
                echo 'Добыча статов из allure-summary.json'
                script {
                    def summaryFile = 'allure-summary.json'
                    def summaryJson = readJSON file: summaryFile
                    def statistic = summaryJson.get('statistic', [:])
                    
                    env.TEST_TOTAL = statistic.get('total', 0).toString()
                    env.TEST_PASSED = statistic.get('passed', 0).toString()
                    env.TEST_FAILED = statistic.get('failed', 0).toString()
                    env.TEST_BROKEN = statistic.get('broken', 0).toString()
                    env.TEST_SKIPPED = statistic.get('skipped', 0).toString()
                    env.TEST_UNKNOWN = statistic.get('unknown', 0).toString()

                    echo """
                    Результаты прогона тестов:
                    Всего тестов: ${env.TEST_TOTAL}
                    Пройдено: ${env.TEST_PASSED}
                    Упало: ${env.TEST_FAILED}
                    Сломанные: ${env.TEST_BROKEN}
                    Пропущено: ${env.TEST_SKIPPED}
                    Неизвестно: ${env.TEST_UNKNOWN}
                    """
                    }
                }
            }
        }
    }
        post {
        always {
            echo 'Очистка временных файлов'
            cleanWs()
            script {
                def subject = "Результаты тестов${env.JOB_NAME} #${env.BUILD_NUMBER}"
                def body = """
                        Результаты прогона автотестов
                        Джоба: ${env.JOB_NAME}
                        Номер сборки: ${env.BUILD_NUMBER}
                        Ветка: ${params.BRANCH}
                        Запущено: ${env.BUILD_ID}

                        Статистика тестов:

                            Всего тестов: ${env.TEST_TOTAL}
                            Пройдено: ${env.TEST_PASSED}
                            Упало: ${env.TEST_FAILED}
                            Сломанные: ${env.TEST_BROKEN}
                            Пропущено: ${env.TEST_SKIPPED}
                            Неизвестно: ${env.TEST_UNKNOWN}
                        """
                emailext(
                    to: 'chajancode@gmail.com',
                    subject: subject,
                    body: body,
                    mimeType: 'text/html',
                    attachmentsPattern: 'allure-results.zip',
                    attachLog: false
                )
            }
        }
}
