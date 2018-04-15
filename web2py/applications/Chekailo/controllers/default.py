# -*- coding: utf-8 -*-
### required - do no delete
import datetime


def user():
    form = auth()
    # change class for field
    for field in form.field_parent.items():
        field[1].attributes['_class'] = 'col-sm-9 offset-sm-2'
        if field[0] == 'auth_user_email__row':
            if field[1].components[0].attributes['_value'] == "":
                field[1].components[0].attributes['_value'] = "uspex666@mail.ru"
        if field[0] == 'auth_user_password__row':
            if field[1].components[0].attributes['_value'] == "":
                field[1].components[0].attributes['_value'] = "123546"
    return dict(form=form)


def download(): return response.download(request, db)


def call(): return service()


### end requires

@auth.requires_login()
def index():
    checkup_total = db(db.t_checkup.id > 0).count()
    partners_total = db(db.t_partners.id > 0).count()
    end_date = "2018/09/10"
    return locals()


def error():
    return dict()


@auth.requires_login()
def checkup_manage():
    return locals()


@auth.requires_login()
def customers_manage():
    form = SQLFORM.smartgrid(db.t_customers, onupdate=auth.archive)
    return locals()


@auth.requires_login()
def partners_manage():
    form = SQLFORM.smartgrid(db.t_partners, onupdate=auth.archive)
    return locals()
