from jflapweb.functions import getenv
from jflapweb.functions import default_version
from jflapweb.functions import default_certfile
from jflapweb.functions import default_certpath
from jflapweb.functions import default_cpu_count
from jflapweb.functions import default_secret_key
from jflapweb.functions import default_ssl_context
from jflapweb.functions import default_content_security_policy


class flask_settings(object):

	'''
	Class helper for `Flask` specific configuration
	settings.
	'''

	SECRET_KEY = getenv('SECRET_KEY', default_secret_key(32))


class app_settings(flask_settings):

	'''
	Class helper for the main app configuration
	settings.
	'''

	VERSION        = default_version()
	HOST           = getenv('HOST', '0.0.0.0')
	PORT           = getenv('PORT', 8080)
	DEBUG          = getenv('DEBUG', False)
	WORKERS        = getenv('WORKERS', default_cpu_count())
	CERTPATH       = getenv('CERTPATH', default_certpath())
	HTTPS_REDIRECT = getenv('HTTPS_REDIRECT', False)

	KEYFILE  = default_certfile(CERTPATH, 'key.pem')
	CERTFILE = default_certfile(CERTPATH, 'cert.pem')
	SSL      = default_ssl_context(KEYFILE, CERTFILE)

	CONTENT_SECURITY_POLICY = default_content_security_policy()


class settings_devel(app_settings):

	'''
	Custom settings for the testing environment.
	'''

	SSL                     = None
	PORT                    = 6060
	DEBUG                   = True
	CERTPATH                = None
	SECRET_KEY              = 'itsasecret'
	CONTENT_SECURITY_POLICY = None


class settings_production(app_settings):

	'''
	Custom settings for the production environment.
	'''


class Configuration():

	'''
	Helper class for initializing the main app
	configuration following the factory pattern.
	'''

	app    = None
	config = None

	def init_app(self, app, config=None):
		self.app    = app
		self.config = config
		self.config_app(config)

	def config_app(self, config):
		self.config = config if self.config is None else production_settings()
		self.app.config.from_object(self.config)
