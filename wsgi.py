from jflapweb import app_run
from jflapweb import app_create
from jflapweb import settings_devel
from jflapweb import settings_production

configuration = settings_production()
application   = app_create(configuration)

if __name__ == "__main__":
	app_run(application, configuration)