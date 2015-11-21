# -*- coding: utf-8 -*-
# try something like
def home(): 
    if auth.has_membership('student_group'):
        redirect(URL('s_controller','student_home'))
    if auth.has_membership('company_group'):
        redirect(URL('c_controller','company_home'))
    if auth.has_membership('TPO'):
        redirect(URL('tpo','home'))
    auth.settings.register_next = URL('c_controller','after_reg', args='company')
    session.user_grp=request.args(0)
    message=session.user_grp
    login_form=auth.login()
    return locals()


def reg_c():
    def Myfuc2(form):
            s='@'+form.vars.first_name
            pos2 = form.vars.email.find(s)
            if pos2 == -1:
                form.errors.email='not valid company email'
    message=session.user_grp
    auth.settings.register_onvalidation.append(Myfuc2)
    c_reg=auth.register()
    return locals()

@auth.requires_login()
def after_reg():
    message="hello"
    return locals()
@auth.requires_login()
@auth.requires_membership('company_group')
def step2_reg():
    db.company.c_id.writable=False
    db.company.c_id.readable=False
    step2form=SQLFORM(db.company).process()
    if step2form.accepted:
        redirect(URL('c_controller','company_home'))
    return locals()
@auth.requires_login()
@auth.requires_membership('company_group')
def company_home():
    session.flag_add_more=1
    query=db.company.c_id==auth.user_id
    count_var=db(query).count()
    if count_var==0:
        redirect(URL('c_controller','step2_reg'))
    else:
        pass
    mssage="company Home"
    return locals()

def myvalid(form_posting):
    x=form_posting.vars.cb1
    if x:
        response.flash='btech cse'
    else:
        response.flash='none'
        
def form_valid(form_posting):
    rows=db(db.company_posting.id).select(db.company_posting.id.max())
    rows=str(rows)
    rows=rows.split()
    cnt=rows[1]
    cnt=int(cnt)+1
#    session.flash=cnt
#    response.flash=cnt
    if form_posting.vars.bcse:
        db.jobs_posted.insert(course_id=6,job=cnt)
    if form_posting.vars.bece:
        db.jobs_posted.insert(course_id=7,job=cnt)
    if form_posting.vars.mcse:
        db.jobs_posted.insert(course_id=8,job=cnt)
    if form_posting.vars.mcsis:
        db.jobs_posted.insert(course_id=9,job=cnt)
    if form_posting.vars.mcl:
        db.jobs_posted.insert(course_id=10,job=cnt)
    if form_posting.vars.mvlsi:
        db.jobs_posted.insert(course_id=11,job=cnt)
    if form_posting.vars.mcase:
        db.jobs_posted.insert(course_id=12,job=cnt)
    if form_posting.vars.mbio:
        db.jobs_posted.insert(course_id=13,job=cnt)
    if form_posting.vars.mscse:
        db.jobs_posted.insert(course_id=14,job=cnt)
    if form_posting.vars.msece:
        db.jobs_posted.insert(course_id=15,job=cnt)
    if form_posting.vars.add_more:
        session.flag_add_more=1
    else:
        session.flag_add_more=0
@auth.requires_login()
@auth.requires_membership('company_group')        
def posting():
#    if session.flag_posting=="1":
#        session.flash="flag set"
#        response.flash="flag set"
#    else:
#        session.flash="flag not set"
#        response.flash="flag set"
    db.company_posting.status.writable=False
    db.company_posting.status.readable=False
    db.company_posting.posted_on.writable=False
    db.company_posting.posted_on.readable=False
    db.company_posting.c_id.writable=False
    db.company_posting.c_id.readable=False
    db.company_posting.display.writable=False
    db.company_posting.display.readable=False
    form_posting=SQLFORM(db.company_posting)
    #TR(div(_class="form-group",_id="company_posting_Location__row"))
    cb1=TR(LABEL('B.Tech (CSE)',_class='control-label col-sm-3'), INPUT(_name='bcse',_class='col-sm-9',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb1)

    cb2=TR(LABEL('B.Tech (ECE)',_class='control-label col-sm-3'), INPUT(_name='bece',_class='col-sm-9',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb2)
    cb3=TR(LABEL('M.Tech (CSE)',_class='control-label col-sm-3'), INPUT(_name='mcse',_class='col-sm-9',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb3)
    cb4=TR(LABEL('M.Tech (CSIS)',_class='control-label col-sm-3'), INPUT(_name='mcsis',_class='col-sm-9',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb4)
    cb5=TR(LABEL('M.Tech (CL)',_class='control-label col-sm-3'), INPUT(_name='mcl',_class='col-sm-9',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb5)
    cb6=TR(LABEL('M.Tech (VLSI)',_class='control-label col-sm-3'), INPUT(_name='mvlsi',_class='col-sm-9',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb6)
    cb7=TR(LABEL('M.Tech (CASE)',_class='control-label col-sm-3'), INPUT(_name='mcase',_class='col-sm-9',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb7)
    cb8=TR(LABEL('M.Tech (Bio Infomatics)',_class='control-label col-sm-3'), INPUT(_name='mbio',_class='col-sm-9',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb8)
    cb9=TR(LABEL('MS (CSE)',_class='control-label col-sm-3'), INPUT(_name='mscse',_class='col-sm-9',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb9)
    cb10=TR(LABEL('MS (ECE)',_class='control-label col-sm-3'), INPUT(_name='msece',_class='col-sm-9',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb10)
    cb11=TR(LABEL('add More',_id='l_add_more',_class='control-label col-sm-3'), INPUT(_name='add_more',_class='col-sm-9',value=False,_type='checkbox',_id='add_more'))
    form_posting[0].insert(-1,cb11)
    # if form_posting.process(onvalidation=myvalid).accepted:
    #    session.flash='accepted'
    if form_posting.process(onvalidation=form_valid,keepvalues=True).accepted:
        rows=db(db.company_posting.c_id==auth.user_id).select(db.company_posting.id.max())
        rows=str(rows)
        rows=rows.split()
        cnt=rows[1]
        query_filename=db(db.company_posting.id==cnt).select(db.company_posting.CSV)
        string=str(query_filename)
        string=string.split()
        if string[1]=='""':
            pass
            #flaging
        else:
            path=str("applications/IIIT_placement/uploads/"+string[1])
            db.csv_upload.import_from_csv_file(open(path,'rb'))
            query_to_retrive=db(db.csv_upload.c_id==auth.user_id).select(db.csv_upload.id.max())
            query_to_retrive=str(query_to_retrive)
            query_to_retrive=query_to_retrive.split()
            id_retrived=query_to_retrive[1]
            db(db.csv_upload.id==id_retrived).update(company_posting_id=cnt)
            pass
    if session.flag_add_more!=1:
#        query_for_posting_id=db(db.company_posting.c_id==auth.user_id).select(db.company_posting.id.max())
#        query_for_posting_id=str(query_for_posting_id)
#        query_for_posting_id=query_for_posting_id.split()
#        max_id=int(query_for_posting_id[1])
#        row_select_details=db(db.company_posting.id==max_id).select()
#        form_posting=SQLFORM(db.company_posting)
#session.flag_posting=1
        redirect(URL('c_controller','company_home'))
        session.flash="old form"
        response.flash="old form"
    else:
#        session.flash="new form"
#        response.flash="new form"
        pass
        #response.flash= session.flag_add_more
    return locals()
