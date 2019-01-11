#!/bin/bash

# THIS FILE STARTS THE VIRTUAL ENV, SETS UP FLASK AND RUN'S IT for Babblizer

source venv/bin/activate

export FLASK_APP=babblizer/app

flask run