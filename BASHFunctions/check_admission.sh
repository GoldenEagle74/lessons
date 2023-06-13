#!/bin/bash

check_admission() {
    local score=$1
    if ((score > 50)); then
        echo "True"
    else
        echo "False"
    fi
}

check_admission "$1"

