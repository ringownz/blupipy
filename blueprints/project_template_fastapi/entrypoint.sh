#!/bin/bash

set -e

function print_help {
    echo "Available options:"
    echo "create - Creates project on output folder"
    echo "bash - Starts bash"
}

case ${1} in
    create)
        mkdir "output" || true
        cookiecutter . -o output/ < answers.txt
        ;;
    bash)
        exec bash
        ;;
    *)
        print_help
        ;;
esac