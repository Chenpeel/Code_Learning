#!/bin/bash


if [ -f "./ins.sh" ]; then
    echo "yes"
elif [ -f "./test.sh" ]; then
    echo "no"
else
    echo "other"
fi