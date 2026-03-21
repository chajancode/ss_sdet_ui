echo "Запуск Selenium Hub. Порт: 4444."
echo
selenium-server hub --port 4444 &

sleep 5
echo
echo "Запуск ноды с Chrome."
echo
selenium-server node --max-sessions 5 --hub http://localhost:4444 \
        --detect-drivers true &

sleep 5
echo
echo "Все сервисы запущены на хосте: http://localhost:4444"
echo