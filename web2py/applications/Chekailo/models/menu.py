response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
    (T('🏠 ' + 'Home'), URL('default', 'index') == URL(), URL('default', 'index'), []),
    (T('➕' + 'Add CheckUP'), URL('default', 'checkup_manage') == URL(), URL('default', 'checkup_manage'), [])
]
