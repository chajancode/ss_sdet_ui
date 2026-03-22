echo "Запуск Selenium Hub. Порт: 4444."
echo
selenium-server hub --port 4444 &

sleep 5
echo
echo "Запуск ноды."
echo
selenium-server node --max-sessions 3 --detect-drivers true \
    --hub http://localhost:4444 &


sleep 5
echo
echo "Все сервисы запущены на хосте: http://localhost:4444"
echo
echo "Запуск тестов."
pytest -n 2 --dist=loadscope --alluredir=./allure-results --grid \
    --browser=all

echo "Тесты завершены."
echo
echo "Завершение работы сервера."
pkill -f selenium-server
