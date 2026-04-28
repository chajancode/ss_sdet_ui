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
                sh """
                    echo "PROJECT_DIR=${env.PROJECT_DIR}" > .env
                    docker-compose down || true
                    echo "👀 завершил работу контейнеров"
                    echo "🚀 Запуск тестов в докере"
                    docker-compose up --build --abort-on-container-exit --exit-code-from tests
            TEST_EXIT_CODE=\$?
            echo \$TEST_EXIT_CODE > test_exit_code.txt

            # Меняем владельца папки с результатами
            sudo chown -R jenkins:jenkins allure-results || true
                """
                env.TEST_EXIT_CODE = readFile('test_exit_code.txt').trim()
                archiveArtifacts artifacts: "${ALLURE_RESULTS}/**/*", fingerprint: true, allowEmptyArchive: true
            }
            post {
                always {
                    script {
                        sh """
                            echo "👀 Текущая директория: \$(pwd)"
                            echo "👀 Содержимое текущей директории:"
                            ls -la
                        """

                        // Проверка существования папки allure-results средствами Groovy
                        if (fileExists(ALLURE_RESULTS)) {
                            echo "✅ Папка ${ALLURE_RESULTS} существует"
                        } else {
                            echo "❌ Папка ${ALLURE_RESULTS} не найдена"
                        }

                        echo "👀 завершение работы"
                        sh 'docker-compose down || true'
                    }
                }
                failure {
                    sh 'docker-compose logs tests || true'
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
                def subject = "Результаты тестов ${env.JOB_NAME} #${env.BUILD_NUMBER}"
                def body = """
                Результаты прогона автотестов \n
                Джоба: ${env.JOB_NAME} \n
                Номер сборки: ${env.BUILD_NUMBER}\n
                Ветка: ${params.BRANCH}\n
                ID сборки: ${env.BUILD_ID}\n
                \n
                Статистика тестов:\n
                \n
                    Всего тестов: ${env.TEST_TOTAL}\n
                    Пройдено: ${env.TEST_PASSED}\n
                    Упало: ${env.TEST_FAILED}\n
                    Сломанные: ${env.TEST_BROKEN}\n
                    Пропущено: ${env.TEST_SKIPPED}\n
                    Неизвестно: ${env.TEST_UNKNOWN}\n
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
            echo 'Очистка временных файлов'
            cleanWs()
        }
    }
}
