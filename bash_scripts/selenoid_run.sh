#!/bin/bash

pytest -n 3 --dist=loadscope --reruns 2 --alluredir=./app/allure-results --grid \
    test_frames_and_windows_page.py test_main_page.py test_basic_auth_page.py
