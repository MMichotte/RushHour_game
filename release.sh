#!/bin/bash

unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac

if [[ ${machine} == "Mac" ]]
then
    python3 OSX_setup.py py2app  
    rm -rf build && rm -rf .eggs
    cd dist && zip -r RushHour.zip Rush-Hour.app
    cd .. && rm -rf dist/Rush-Hour.app
    mv dist/RushHour.zip release/
    rm -rf dist
fi 