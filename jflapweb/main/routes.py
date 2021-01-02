from jflapweb.main import bp as main

from jflapweb.routes import request
from jflapweb.routes import url_for
from jflapweb.routes import redirect
from jflapweb.routes import render_template
from jflapweb.routes import send_from_directory


@main.route('/')
def route_root():

	return redirect(url_for('main.route_home'))


@main.route('/home')
def route_home():

	return render_template('jflap.html')


@main.route('/about')
def route_about():

	return render_template('about.html')


@main.route('/resources/<path:file>')
def route_resources(file):

	return send_from_directory(main.static_folder, filename=file)
