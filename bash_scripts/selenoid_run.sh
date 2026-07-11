#!/bin/bash

# bash_scripts/selenoid_run.sh
pytest -n 3 --dist=loadscope --reruns 2 --alluredir=./allure-results --grid --browser chrome,firefox