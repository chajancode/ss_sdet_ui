#!/bin/bash

pytest -n 3 --dist=loadscope --reruns 2 --alluredir=./allure-results --grid tests/test_js_sqlex.py
