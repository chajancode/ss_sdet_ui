#!/bin/bash

pytest -n 3 --dist=loadscope --reruns 2 --alluredir=./allure-results --grid