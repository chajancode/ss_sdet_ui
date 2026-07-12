# Что автоматизировано

**UI1. Главная страница + авторизация** (по чек-листу)
- Проверить открытие главной страницы: отображаются хедер, блок навигации, список курсов, футер → [`test_main_page.py::test_main_page_elements`](../tests/test_main_page.py)
- Проверить, что меню навигации остаётся видимым при скроллинге страницы вниз → [`test_main_page.py::test_navbar_on_scroll`](../tests/test_main_page.py)
- Перейти по меню навигации на страницу Lifetime Membership Club, проверить переход и заголовок → [`test_main_page.py::test_transition_through_navbar`](../tests/test_main_page.py)
- Проверить поля формы авторизации: Username и Password отображаются, кнопка Login задизейблена при пустых полях → [`test_login_page.py::test_authentication_fields`](../tests/test_login_page.py)
- Ввести валидные данные, проверить сообщение об успешной авторизации → [`test_login_page.py::test_login`](../tests/test_login_page.py)
- Ввести невалидные данные, проверить сообщение об ошибке → [`test_login_page.py::test_login`](../tests/test_login_page.py)
- Разлогиниться, проверить, что снова отображаются поля для входа → [`test_login_page.py::test_login`](../tests/test_login_page.py)

**UI2. Allure**
- Отчёты Allure, аннотация Severity к каждому тест-кейсу, Step к каждому публичному методу Page Object, аннотации Epic/Feature/Story → [`pages/`](../pages), [`tests/`](../tests)

**UI3. DataProvider**
- Универсальный тест авторизации на разных данных (в том числе некорректных), источник параметров - параметризация → [`test_login_page.py::test_login`](../tests/test_login_page.py), [`login_test_data_sets.py`](../test_data/login_test_data_sets.py)

**UI4. Screenshots**
- Скриншот при падении теста → [`conftest.py`](../tests/conftest.py)

**UI5. Cookies**
- Запись куков в файл и считывание куков из него → [`utils/cookie_tools.py`](../utils/cookie_tools.py)
- Тест, авторизующийся при первом запуске и использующий куки при втором → [`test_login_sqlex.py`](../tests/test_login_sqlex.py)

**UI6. JavaScriptExecutor**
- Убрать фокус из поля ввода и определить наличие скролла на странице, код вынесен в отдельные Step-функции → [`utils/java_script_executor.py`](../utils/java_script_executor.py), [`test_js_sqlex.py`](../tests/test_js_sqlex.py)

**UI7. Параллельный запуск тестов**
- Многопоточный запуск (минимум два потока), скрипты для развёртывания Selenium Grid (hub и node) → [`grid_start.sh`](../bash_scripts/grid_start.sh)

**UI8. Перезапуск упавших тестов**
- Автоматический повтор упавших кейсов (2 попытки), скрипт для выполнения только упавших кейсов с предыдущего прогона → [`grid_rerun_failed.sh`](../bash_scripts/grid_rerun_failed.sh)

**UI9. Браузеры**
- Запуск на разных браузерах с Grid и без, класс DriverFactory, создающий WebDriver по входным параметрам → [`config/drivers.py`](../config/drivers.py)

**UI10. Drag-n-Drop**
- Перетащить элемент в принимающий, убедиться, что текст принимающего элемента изменился → [`test_droppable_page.py`](../tests/test_droppable_page.py)

**UI11. Tabs**
- Нажать на ссылку, перенести фокус на новую вкладку, нажать ссылку, убедиться, что открылась третья вкладка → [`test_frames_and_windows_page.py`](../tests/test_frames_and_windows_page.py)

**UI12. Alerts**
- Нажать Input Alert, ввести кастомный текст, подтвердить, убедиться, что текст применился → [`test_alert_page.py`](../tests/test_alert_page.py)

**UI13. Basic auth**
- Нажать Display Image, пройти авторизацию (httpwatch/httpwatch), убедиться, что авторизация прошла успешно → [`test_basic_auth_page.py`](../tests/test_basic_auth_page.py)
