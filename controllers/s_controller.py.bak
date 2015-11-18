# -*- coding: utf-8 -*-
# try something like
def home(): 
    session.user_grp=request.args(0)
    message=session.user_grp
    login_form=auth.login()
    
    return locals()
def reg_s():
    message=session.user_grp
    s_reg=auth.register()
    return locals()
def after_reg():
    message="sudent"
    return locals()
#@auth.requires_membership('student_group')
@auth.requires_login()
@auth.requires_membership('student_group')
def step2_reg():
    db.student.s_id.default=auth.user_id
    db.student.s_id.writable=False
    db.student.s_id.readable=False
    step2form=SQLFORM(db.student).process()
    if step2form.accepted:
        redirect(URL('s_controller','student_home'))
    #if step2form.accepted:
       # redirect
    return locals()
@auth.requires_login()
@auth.requires_membership('student_group')
def student_home():
    query=db.student.s_id==auth.user_id
    count_var=db(query).count()
    if count_var==0:
        redirect(URL('s_controller','step2_reg'))
    else:
        pass
    query=db.student.s_id==auth.user_id
    row=db(query).select().first()    # get the record 
    # set the default for all fields by ID 
    # for fieldname in db.student.fields: 
    #    if fieldname!='id': db.student[fieldname].default=row[fieldname] 
    db.student.id.readable=False
    db.student.s_id.writable=False
    db.student.s_id.readable=False
    form=SQLFORM(db.student,row)
    #for r in row:
     #   form.vars.roll_num=r.roll_num
    #  form.vars.ten_per=r.ten_per
    #    form.vars.twelve_per=r.twelve_per
    #    form.vars.year_passing=r.year_passing
    #    form.vars.cgpa=r.cgpa
    
    #db.student.course_id.writable=False
    #db.student.course_id.readable=False
    if form.process().accepted:
        response.flash="updated"
    return locals()
@auth.requires_login()
@auth.requires_membership('student_group')
def apply_for():
    query=db.student.s_id==auth.user_id
    count_var=db(query).count()
    if count_var==0:
        redirect(URL('s_controller','step2_reg'))
    else:
        pass
    # change id 
    listing_appliyed_for=db(db.student_select.sid==auth.user_id).select(db.student_select.posting_id)
    listing_appliyed_for_str=str(listing_appliyed_for)
    listing_appliyed_for_str=listing_appliyed_for_str.split()
    listing_appliyed_for_str=listing_appliyed_for_str[1:]
    courseid=db(db.student.s_id==auth.user_id).select(db.student.course_id)
    courseid=str(courseid)
    courseid=courseid.split()
    rows=db((db.jobs_posted.job==db.company_posting.id)&(db.jobs_posted.course_id==courseid[1])&(db.company_posting.c_id==db.auth_user.id)).select(db.auth_user.first_name,db.company_posting.Profile,db.company_posting.id)
    string=str(rows)
    string=string.split("\r\n")
    string=string[1:-1]
   
        #db.student_select.sid.default=auth.user_id
        #db.student_select..default
        
        #form=SQLFORM.factory(Field(db.student_select.sid,default=auth.user_id),Field(db.auth_user.first_name,default=company_details[0]),Field(db.student_select.posting_id,default=company_details[2]),Field(db.student_select.apply_))
    return locals()
@auth.requires_login()
@auth.requires_membership('student_group')
def apply_form():
    #change id
#    courseid=db(db.student.s_id==auth.user_id).select(db.student.course_id)
#    courseid=str(courseid)
#    courseid=courseid.split()
#    ids=db((db.jobs_posted.job==db.company_posting.id)&(db.jobs_posted.course_id==courseid[1])&(db.company_posting.c_id==db.auth_user.id)).select(db.company_posting.id)
#    ids=str(ids)
#    ids=ids.split()
#  for id in ids:
#        cb=id
    
    x=dict(request.vars)
    l=x.keys()
    for cid in l:
        db.student_select.insert(sid=auth.user_id,posting_id=cid,apply_=True)

           
    session.flash=x.values()
    redirect(URL('s_controller','student_home'))
    return locals()
