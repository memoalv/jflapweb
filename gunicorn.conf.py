from wsgi import configuration as current

errorlog  = '-'
accesslog = '-'
loglevel  = 'info'

bind    = "%s:%s" % (current.HOST,current.PORT)
reload  = current.DEBUG
workers = current.WORKERS

#? https support
ssl_version = 'TLS'

keyfile  = current.KEYFILE
certfile = current.CERTFILE

#? low traffic specific values
timeout   = 120
keepalive = 120

#? This fix the runit log not capturing properly
capture_output = True
