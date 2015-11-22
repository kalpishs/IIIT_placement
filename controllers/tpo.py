# -*- coding: utf-8 -*-
# try something like
from gluon.tools import Mail
mail = Mail()

def index():
    
    return dict(message="hello from tpo.py")
@auth.requires_login()
@auth.requires_membership('TPO')
def home():
    if auth.has_membership('student_group'):
        redirect(URL('s_controller','student_home'))
    if auth.has_membership('company_group'):
        redirect(URL('c_controller','company_home'))
    query_filename = db(db.auth_user.id==db.company_posting.c_id).select(db.company_posting.CSV,db.auth_user.first_name,db.company_posting.id,db.company_posting.status,db.company_posting.display,db.auth_user.email)
    string=str(query_filename)
    string=string.split()
    query_rows=db((db.csv_upload.company_posting_id==db.company_posting.id)&(db.company_posting.c_id==db.auth_user.id)).select(db.csv_upload.Profile,db.csv_upload.Location,db.csv_upload.CTC,db.auth_user.first_name,db.company_posting.id,db.company_posting.status,db.company_posting.display,db.auth_user.email,db.csv_upload.Bond_month)
    rows=str(query_rows)
    rows=rows.split()
  
    #   if string[1]=='""':
    #db((db.csv_upload.company_posting_id==db.company_posting.id/)&(db.company_posting.c_id==db.auth_user.id)).select()
    #x="home"
    return locals()
@auth.requires_login()
@auth.requires_membership('TPO')
def selected():
    x=dict(request.vars)
    l=x.keys()
    rows1=db(db.company_posting).select(db.company_posting.id)
    rows=str(rows1)
    rows=rows.split()
    rows=rows[1:]
    for ids_l in rows:
        if ids_l in l:
            db(db.company_posting.id==ids_l).update(display=True)
        else:
            db(db.company_posting.id==ids_l).update(display=False)
        
    session.flash="Updated"

    redirect(URL('tpo','home'))
    return locals()
mail.settings.server = 'smtp.gmail.com:587'
mail.settings.sender = 'tpo.iiith@gmail.com'
mail.settings.login =  'tpo.iiith@gmail.com:luhkkykzvwnkljiq'
@auth.requires_login()
@auth.requires_membership('TPO')
def email():
    email_id=request.vars.emailid
    email_id=str(email_id)
    form = SQLFORM.factory(
    Field('email', requires =[ IS_EMAIL(error_message='invalid email!'), IS_NOT_EMPTY() ],default=email_id),
    Field('subject', requires=IS_NOT_EMPTY(),default="IIIT-Hydrabad Placements"),
    Field('message', requires=IS_NOT_EMPTY(), type='text',default="Hello this is an email send to you regarding placement drives at IIIT-H ")
    )
    if form.process().accepted:
            x = mail.send(to=[form.vars.email],
            subject=form.vars.subject,
            message=form.vars.message
        )

            if x == True:
                response.flash = 'email sent sucessfully.'
                session.flash='email sent sucessfully.'
                redirect(URL('home'))
            else:
                response.flash = 'fail to send email sorry!'

        #response.flash = 'form accepted.'
    elif form.errors:
        response.flash='form has errors.'

        
    return dict(form=form)
def display_details():
    x=request.vars.id
    y=request.vars.name
    query_rows=db(db.company_posting.id==x).select()
    c_id=query_rows[0].c_id
    c_location=query_rows[0].Location
    c_csv=query_rows[0].CSV
    if c_csv=="":
        flag=0
        pass
    else:
        flag=1
        query_csv=db(db.csv_upload.company_posting_id==x).select()
#     rows=str(query_rows)
#     rows=rows.split('\r\n')
#     rows=rows[1:]
    return locals()
