# -*- coding: utf-8 -*-
# try something like
def index():
    return dict(message="hello from tpo.py")
@auth.requires_login()
@auth.requires_membership('TPO')
def home():
    query_filename = db(db.auth_user.id==db.company_posting.c_id).select(db.company_posting.CSV,db.auth_user.first_name,db.company_posting.id)
    string=str(query_filename)
    string=string.split()
    query_rows=db((db.csv_upload.company_posting_id==db.company_posting.id)&(db.company_posting.c_id==db.auth_user.id)).select(db.csv_upload.Profile,db.csv_upload.Location,db.csv_upload.CTC,db.auth_user.first_name,db.company_posting.id,db.csv_upload.Bond_month)
    rows=str(query_rows)
    rows=rows.split()
  
    #   if string[1]=='""':
    #db((db.csv_upload.company_posting_id==db.company_posting.id/)&(db.company_posting.c_id==db.auth_user.id)).select()
    #x="home"
    return locals()
def selected():
    x=dict(request.vars)
    l=x.keys()
    #for ids_l in l:
    # db(db.company_posting.id==ids_l).update(db.company_posting.display=True)
    session.flash=x.values()

    redirect(URL('tpo','home'))
    return locals()
