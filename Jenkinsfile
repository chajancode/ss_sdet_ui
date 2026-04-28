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
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Код загружен из GitHub'
            }
        }
        stage('Диагностика Selenoid') {
            steps {
            sh """
            echo "=== Проверка на хосте ==="
            echo "Рабочая директория: ${WORKSPACE}"
            ls -la ${WORKSPACE}/selenoid/config/ || echo "❌ Директория config не найдена"
            
            echo "Содержимое config:"
            ls -la ${WORKSPACE}/selenoid/config/ -R || echo "❌ Нет файлов"
            
            echo "=== Проверка маунта в Docker ==="
            docker-compose config | grep -A 5 "selenoid:" || echo "❌ Не удалось проверить конфиг"
            
            echo "=== Временный контейнер для проверки ==="
            docker run --rm -v ${WORKSPACE}/selenoid/config:/test-data alpine ls -la /test-data/
        """
    }
}
        stage('Запуск тестов в докере') {
            steps {
                    sh """
                        echo "PROJECT_DIR=${env.PROJECT_DIR}" > .env
                        docker-compose down || true
                        docker-compose up --build --abort-on-container-exit --exit-code-from tests
                        TEST_EXIT_CODE=\$?
                        
                        # Диагностика - ищем результаты
                        echo "=== Поиск allure-results в контейнере ==="
                        docker-compose run --rm tests find /app -name "*.json" -type f 2>/dev/null | head -20
                        
                        echo "=== Поиск везде ==="
                        docker-compose run --rm tests find / -path "/proc" -prune -o -name "allure-results" -type d 2>/dev/null
                        
                        echo "=== Проверка смонтированной папки ==="
                        ls -la ./allure-results/ || echo "Папка пуста или не существует"
                        
                        exit \$TEST_EXIT_CODE
                    """
                }
            }
            post {
                always {
                    // sh 'docker-compose run --rm tests cp -r ./allure-results ./ || true'
                    archiveArtifacts artifacts: "${ALLURE_RESULTS}/**/*", fingerprint: true, allowEmptyArchive: true
                    sh 'docker-compose down || true'
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
                sh 'zip -r allure-results.zip allure-results'
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

