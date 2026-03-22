echo "Запуск Selenium Hub. Порт: 4444."
echo
selenium-server hub --port 4444 &

sleep 5
echo
echo "Запуск ноды с Chrome."
echo
selenium-server node --max-sessions 5 --driver-implementation \
        "chrome" --hub http://localhost:4444 &

sleep 5
echo
echo "Все сервисы запущены на хосте: http://localhost:4444"
echo
echo "Запуск упавших тестов. Попыток перезапуска 2."
echo "Задержка между перезапусками 2 сек."
echo
pytest -n auto --lf --reruns 2 --reruns-delay 2 \
        --dist=loadscope --alluredir=./allure-results
echo
echo "Тесты завершены."
echo
echo "Завершение работы сервера."
pkill -f selenium-server