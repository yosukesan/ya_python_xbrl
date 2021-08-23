#!/bin/bash

for src in $(ls *.py); 
do
    echo -e "\n=== start test unit"
    pyflakes3 $src
    echo -e "=== pyflakes3 end"
    mypy $src
    echo -e "=== mypy end"
done

pytest-3 test_unit.py
