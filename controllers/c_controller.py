# -*- coding: utf-8 -*-
# try something like
def home(): 
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
    else:
        pass
@auth.requires_login()
@auth.requires_membership('company_group')        
def posting():
    db.company_posting.c_id.writable=False
    db.company_posting.c_id.readable=False
    db.company_posting.display.writable=False
    db.company_posting.display.readable=False
    
    form_posting=SQLFORM(db.company_posting)
    cb1=TR(LABEL('B.Tech (CSE)'), INPUT(_name='bcse',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb1)
    cb2=TR(LABEL('B.Tech (ECE)'), INPUT(_name='bece',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb2)
    cb3=TR(LABEL('M.Tech (CSE)'), INPUT(_name='mcse',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb3)
    cb4=TR(LABEL('M.Tech (CSIS)'), INPUT(_name='mcsis',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb4)
    cb5=TR(LABEL('M.Tech (CL)'), INPUT(_name='mcl',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb5)
    cb6=TR(LABEL('M.Tech (VLSI)'), INPUT(_name='mvlsi',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb6)
    cb7=TR(LABEL('M.Tech (CASE)'), INPUT(_name='mcase',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb7)
    cb8=TR(LABEL('M.Tech (Bio Infomatics)'), INPUT(_name='mbio',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb8)
    cb9=TR(LABEL('MS (CSE)'), INPUT(_name='mscse',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb9)
    cb10=TR(LABEL('MS (ECE)'), INPUT(_name='msece',value=False,_type='checkbox'))
    form_posting[0].insert(-1,cb10)
    # if form_posting.process(onvalidation=myvalid).accepted:
    #    session.flash='accepted'
    if form_posting.process(onvalidation=form_valid).accepted:
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
            path=str("applications/scripting_project/uploads/"+string[1])
            db.csv_upload.import_from_csv_file(open(path,'rb'))
            query_to_retrive=db(db.csv_upload.c_id==auth.user_id).select(db.csv_upload.id.max())
            query_to_retrive=str(query_to_retrive)
            query_to_retrive=query_to_retrive.split()
            id_retrived=query_to_retrive[1]
            db(db.csv_upload.id==id_retrived).update(company_posting_id=cnt)
            pass
        response.flash='accepted'
    return locals()
