from flask_blog import app
from flask import request, redirect, url_for, render_template

@app.route('/')

def show_entries():
	return render_template('./entries/index.html')