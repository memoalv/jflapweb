from jflapweb import Blueprint

bp = Blueprint(
	'main',
	__name__,
	static_folder   = 'static',
	template_folder = 'templates',
	static_url_path = '/app/main/static',
)