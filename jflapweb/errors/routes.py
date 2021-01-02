from jflapweb.routes import abort
from jflapweb.routes import url_for
from jflapweb.routes import render_template

from jflapweb import config
from jflapweb.errors import bp as errors

@errors.errorhandler(Exception)
def route_errors_generic(error):
	return render_template('errors/error.html', error=error), error.code
