### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_customers',
                Field('f_name', type='string',
                      label=T('Name')),
                auth.signature,
                format='%(f_name)s',
                migrate=settings.migrate)

db.define_table('t_customers_archive', db.t_customers,
                Field('current_record', 'reference t_customers', readable=False, writable=False))

########################################
db.define_table('t_partners',
                Field('f_name', type='string',
                      label=T('Name')),
                auth.signature,
                format='%(f_name)s',
                migrate=settings.migrate)

db.define_table('t_partners_archive', db.t_partners,
                Field('current_record', 'reference t_partners', readable=False, writable=False))
########################################
db.define_table('t_checkup',
                Field('f_name', type='string',
                      label=T('Name')),
                Field('f_date', type='datetime',
                      label=T('Date')),
                Field('f_type', type='string',
                      label=T('Type')),
                Field('f_file', type='blob',
                      label=T('File')),
                Field('f_partner_link', "reference:t_partners",
                      label=T('Partner Link')),
                auth.signature,
                format='%(f_name)s',
                migrate=settings.migrate)

db.define_table('t_checkup_archive', db.t_checkup,
                Field('current_record', 'reference t_checkup', readable=False, writable=False))
