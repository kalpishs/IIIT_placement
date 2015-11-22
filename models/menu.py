# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('Placement portal'),_class="brand",
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################


if auth.has_membership('student_group') and  not auth.has_membership('spc_group'):
    response.menu= [
         (T('Home'), False, URL('default', 'index'), []),
        (T('Apply'), False, URL('s_controller','apply_for'),[]
        ),(T('Spc'), False,URL('s_controller','spc'),[])
    ]
elif auth.has_membership('student_group') and auth.has_membership('spc_group'):
    response.menu= [
         (T('Home'), False, URL('default', 'index'), []),
        (T('Apply'), False, URL('s_controller','apply_for'),[]
        ),(T('View Student Deatils'), False, URL('s_controller','spc_view'),[]
        )]
elif auth.has_membership('company_group'):
    response.menu= [
         (T('Home'), False, URL('default', 'index'), []),
        (T('New Posting'), False,URL('c_controller','posting'),[]),
        (T('View Posting'), False,URL('c_controller','view_posting'),[])
        ]
elif auth.has_membership('TPO'):
    response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
        ]
else:
    response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Student Register'), False, URL('s_controller', 'reg_s'), []),
    (T('Company Register'), False, URL('c_controller', 'reg_c'), [])

    ]
DEVELOPMENT_MENU = True

if "auth" in locals(): auth.wikimenu()
