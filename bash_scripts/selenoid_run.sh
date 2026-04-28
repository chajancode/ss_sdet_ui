#!/bin/bash

pytest -n 3 --dist=loadscope --reruns 2 --alluredir=./app/allure-results --grid tests/test_main_page.py
