pipeline {
    agent any

    triggers {
        cron('40 12 * * *')
    }

    parameters {
        string(name: 'BRANCH', defaultValue: 'task_ci4', description: 'Ветка для сборки')
        string(name: 'EMAILS', defaultValue: 'chajancode@gmail.com')
    }
    
    environment {
        PYTHON_VERSION = '3.10'
        ALLURE_RESULTS = 'allure-results'
        ALLURE_REPORT = 'allure-report'
        COMPOSE_PROJECT_NAME = 'ss_sdet_ui'
        PROJECT_DIR = "${WORKSPACE}"
        HOST_WORKSPACE = "/var/lib/docker/volumes/jenkins_home/_data/workspace/${JOB_NAME}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Код загружен из GitHub'
            }
        }
        stage('Запуск тестов в докере') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'UNSTABLE') {
                    sh """
                        echo "PROJECT_DIR=${env.PROJECT_DIR}" > .env
                        docker-compose down || true
                        docker-compose up --build --abort-on-container-exit --exit-code-from tests
                        docker cp \$(docker ps -aq -f name=tests):/app/${ALLURE_RESULTS}/. ${ALLURE_RESULTS}/ 
                        chmod -R 777 ${ALLURE_RESULTS}

                        TEST_EXIT_CODE=\$?
                        echo \$TEST_EXIT_CODE > test_exit_code.txt
                        docker-compose logs tests --no-color > pytest.log
                    """
                    script {
                        env.TEST_EXIT_CODE = readFile('test_exit_code.txt').trim()
                    }
                    archiveArtifacts artifacts: "${ALLURE_RESULTS}/**/*", fingerprint: true, allowEmptyArchive: true
                }
            }
            post {
                always {
                    script {
                        sh 'docker-compose down || true'
                    }
                    script {
                        echo "формирование отчета Allure"
                        if (fileExists(ALLURE_RESULTS)) {
                            sh "sudo chown -R jenkins:jenkins ${ALLURE_RESULTS} || true"
                            sh "chmod -R 755 ${ALLURE_RESULTS} || true"
                            allure([
                                includeProperties: false,
                                jdk: '',
                                properties: [],
                                reportBuildPolicy: 'ALWAYS',
                                results: [[path: "${ALLURE_RESULTS}"]]
                            ])
                        }
                    }
                }
                failure {
                    sh 'docker-compose logs tests || true'
                }
            }
        }
        stage('Статы тестов') {
            steps {
                echo 'Добыча статов из allure-summary.json'
                script {
                    def summaryFile = 'allure-report/widgets/summary.json'
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
    post {
        always {
            script {
                sh 'zip -r allure-results.zip allure-results || true'
                def failedLog = readFile('pytest.log')
                failedLog = failedLog.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                def subject = "Результаты тестов ${env.JOB_NAME} #${env.BUILD_NUMBER}"
                def body = """
                    <div><strong>Результаты прогона автотестов</strong></div>
                    <ul>
                    <li><span> Джоба: </span><span>${env.JOB_NAME}</span><span> </span></li>
                    <li><span> Номер сборки: </span><span>${env.BUILD_NUMBER}</span><span> </span></li>
                    <li><span> Ветка: </span><span>${params.BRANCH}</span><span> </span></li>
                    <li><span> ID сборки: </span><span>${env.BUILD_ID}</span><span> </span></li>
                    </ul>
                    <div><span> <strong>Статистика тестов:</strong></span></div>
                    <ul>
                    <li><span> Всего тестов: </span><span>${env.TEST_TOTAL}</span><span> </span></li>
                    <li><span> Пройдено: </span><span>${env.TEST_PASSED}</span><span> </span></li>
                    <li><span> Упало: </span><span>${env.TEST_FAILED}</span><span> </span></li>
                    <li><span> Сломанные: </span><span>${env.TEST_BROKEN}</span><span> </span></li>
                    <li><span> Пропущено: </span><span>${env.TEST_SKIPPED}</span><span> </span></li>
                    <li><span> Неизвестно: </span><span>${env.TEST_UNKNOWN}</span><span> </span></li>
                    </ul>
                    <div><span>&nbsp;</span></div>

                    <details>
                    <summary><strong>Лог тестов</strong></summary>
                    <pre>${failedLog}</pre>
                    </details>
                """
                emailext(
                    to: params.EMAILS,
                    subject: subject,
            body: body,
            mimeType: 'text/html',
            attachmentsPattern: 'allure-results.zip',
            attachLog: false
                )
            }
            cleanWs()
        }
    }
}