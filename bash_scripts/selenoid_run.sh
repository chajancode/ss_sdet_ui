#1/bin/bash

pytest -n 1 --dist=loadscope --reruns 2 --alluredir=./allure-results --grid
