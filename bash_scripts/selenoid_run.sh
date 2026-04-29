#!/bin/bash

pytest -v -n 3 --dist=loadscope --reruns 2 --alluredir=./allure-results --grid tests/test_main_page.py
