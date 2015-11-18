# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    if auth.user:
        if auth.has_membership(5):
            redirect(URL('s_controller','student_home'))
        if auth.has_membership(4):
             redirect(URL('c_controller','company_home'))
        if auth.has_membership(27):
             redirect(URL('tpo','home'))
    #response.flash = T("")
    return dict(message=T('Welcome Placement App'))

def home():
    temp=request.args(0)
    if temp == 'c':
        session.flash=T("Invalid login")
        redirect(URL('c_controller','home'))
    if temp == 's':
        session.flash=T("Invalid login")
        redirect(URL('s_controller','home'))
    else:
        session.flash=T("Invalid login")
        redirect(URL('default','index'))
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def after_reg():
    x=session.user_grp
    if x=='s':
        auth.add_membership(5)
        redirect(URL('s_controller','step2_reg'))
    elif x=='c':
        auth.add_membership(4)
        redirect(URL('c_controller','step2_reg'))
    return locals()
def after_login():
    if auth.has_membership(group_id='student_group'):
        redirect(URL('s_controller','student_home'))
    if auth.has_membership(group_id='company_group'):
        redirect(URL('c_controller','company_home'))
    if auth.has_membership(group_id='TPO'):
        redirect(URL('tpo','home'))
    else:
        session.flash=('error login')
        redirect(URL('default','index'))
