#!/usr/bin/env bash

#PythonVersion=$(command -v python3.9 >/dev/null 2>&1 && echo Python 3 is installed)
#echo $PythonVersion
#if [[ -z "$PythonVersion" ]]
#then
#    echo "Installing Python3!"
#    brew install python3.9
#fi

# -> FairWeb (fairnlp(faircore), fairmongo)
pip3 install fairarticle>=4.1.4
pip3 install fairqt>=1.0.1
pip3 install fairresources>=4.0.3
pip3 install flask-socketio
pip3 install pyngrok