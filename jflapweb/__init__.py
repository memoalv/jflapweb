from flask import Flask
from flask import Blueprint
from flask_talisman import Talisman
from flask_minify import minify as Minify

from jflapweb.config import Configuration
from jflapweb.config import settings_devel
from jflapweb.config import settings_production

minify        = Minify()
talisman      = Talisman()
configuration = Configuration()

def app_create(config):

	app = Flask(__name__)
	app.url_map.strict_slashes = False

	configuration.init_app(app)
	configuration.config_app(config)

	minify.init_app(app)

	minify.js   = True
	minify.css  = True
	minify.html = True

	talisman.init_app(app)

	talisman.force_https             = config.HTTPS_REDIRECT
	talisman.content_security_policy = config.CONTENT_SECURITY_POLICY

	from jflapweb.main import bp as main
	from jflapweb.errors import bp as errors

	app.register_blueprint(main)
	app.register_blueprint(errors)
	app.register_error_handler(Exception, routes.route_errors_generic)

	return app

def app_run(app, conf):

	app.run (
		host=conf.HOST,
		port=conf.PORT,
		debug=conf.DEBUG, 
		ssl_context=conf.SSL,
	)

from jflapweb import routes