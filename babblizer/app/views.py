from app import app
from flask import render_template, flash, redirect, request
import requests
from .forms import LoginForm, DemoForm, AddForm, GimmeForm
import sys
import subprocess
from .ben_test import BenTest, NewBabble, GimmeBabble


path = "/Users/Gary/Music/Logic/"
test_active = "/Users/Gary/Desktop/test"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/babble', methods=['GET', 'POST'])
def testform():
    form = DemoForm()
    if form.validate_on_submit():
        words = BenTest(form.build.data).fnord()
        flash('{}'.format(words))
    return render_template('demo.html',title='Babblizer',form=form)

@app.route('/add_a_babble', methods=['GET', 'POST'])
def add_a_babble():
	form = AddForm()
	if form.validate_on_submit():
		result = NewBabble(form.yousay.data, form.isay.data).new_babble()
		print result
		flash('{}'.format(result))
	return render_template('add.html',title='Add a Babble',form=form)

@app.route('/gimme', methods=['GET', 'POST'])
def gimme_a_babble():
    form = GimmeForm()
    if request.form:
        print "Button Pressed"
        result = GimmeBabble(request.data).gimme_babble()
        print result
        flash('{}'.format(result))

    return render_template('gimme.html',title='Gimme a Babble', form=form)



