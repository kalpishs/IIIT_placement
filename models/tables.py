# -*- coding: utf-8 -*-
db.define_table('company',
                Field('contact_person'),
                Field('address',requires=IS_NOT_EMPTY()),
                Field('c_id','reference auth_user',default=auth.user_id)
               )
db.define_table('company_posting',
                Field('c_id','reference auth_user',default=auth.user_id),
                Field('Location',requires=IS_NOT_EMPTY()),
                Field('Profile',requires=IS_NOT_EMPTY()),
                Field('Job_discription','text'),
                Field('ctc'),
                Field('CSV','upload'),
                Field('display','boolean',default=False),
                Field('posted_on','datetime',default=request.now),
                Field('status','boolean',default=True)
               )
db.define_table('csv_upload',
                Field('Profile'),
                Field('Location'),
                Field('CTC'),
                Field('Bond_month'),
                Field('c_id','reference auth_user',default=auth.user_id),
                Field('company_posting_id','reference company_posting',requires=IS_IN_DB(db, db.company_posting.id, '%(id)s'))
                #job_posting
               )
db.define_table('course',
                Field('course_name',requires=IS_NOT_EMPTY())
               )
db.define_table('jobs_posted',
                Field('course_id','reference course',requires=IS_IN_DB(db, db.course.id, '%(course_name)s')),
                Field('job')
                )
db.define_table('student',
                Field('roll_num',requires=IS_NOT_EMPTY()),
                Field('course_id','reference course',requires=IS_IN_DB(db, db.course.id, '%(course_name)s')),
                Field('ten_per',requires=IS_NOT_EMPTY()),
                Field('twelve_per',requires=IS_NOT_EMPTY()),
                Field('year_passing',requires=IS_NOT_EMPTY()),
                Field('cgpa'),
                Field('resume','upload'),
                Field('s_id','reference auth_user')
                )
db.define_table('student_select',
                   Field('sid','reference auth_user',default=auth.user_id),
                   Field('posting_id','reference company_posting',requires=IS_IN_DB(db, db.company_posting.id, '%(Profile)s')),
                   Field('apply_','boolean')
               )
