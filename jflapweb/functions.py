from os import getenv


def default_version():

	'''
	returns the version string from the git tag
	finded on the system, at fail will return the
	string `production` as fallback.
	'''

	from version_query import predict_version_str
	
	version = 'v0.0.0'

	try:
		version = predict_version_str()
	except:
		return 'production'
	
	return str(version)


def default_secret_key(nbytes):

	'''
	returns a random url as the default password for
	the application with the length of `nbytes`.
	'''

	from secrets import token_urlsafe

	return token_urlsafe(int(nbytes))


def default_cpu_count():

	'''
	returns the default ammount of workers using the
	formula: (2N + 1) when N is the number of cores
	returned by `cpu_count()`.
	'''

	from multiprocessing import cpu_count

	return 2 * cpu_count() + 1


def default_certpath():

	'''
	returns the default search location for the
	certificate files.
	'''

	from os import getcwd

	return getcwd()


def default_certfile(path, file):

	'''
	returns the string of the `path + file` if the
	certificate file is valid.
	'''

	from os.path import join
	from os.path import isfile

	filename = join(str(path), str(file))

	return str(filename) if isfile(filename) else None


def default_ssl_context(keyfile, certfile):

	'''
	returns the proper ssl context if the existing
	certificates are valid.
	'''

	validcert = False
	validcert = (True if keyfile is not None else False)
	validcert = (True if certfile is not None else False)
	certfiles = (str(keyfile), str(certfile))
	
	return certfiles if validcert else 'adhoc'


def default_content_security_policy():

	'''
	returns the default and minimal `CSP` for the
	application to be able to work as intended.
	'''

	return { 
		'default-src': [
			'\'self\'',
			'\'unsafe-eval\'',
			'cjrtnc.leaningtech.com',
		],
		'img-src': [
			'\'self\'',
			'blob:',
			'cjrtnc.leaningtech.com',
		],
	}

from jflapweb.main import functions
