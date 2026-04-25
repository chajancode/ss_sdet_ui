#1/bin/bash

pytest -n auto --dist=loadscope --reruns 2 --alluredir=./allure-results --grid
