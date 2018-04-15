from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Chekailo'
settings.subtitle = 'Scorpa'
settings.author = 'Scorpa'
settings.author_email = 'Scorpa@e.com'
settings.keywords = ''
settings.description = ''
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = 'ca4a2aa1-8408-4fa1-871e-60ce1269c8bc'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
