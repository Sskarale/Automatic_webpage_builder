"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.openHome),
    path("index/", views.openHome),
    path("Template/", views.viewTemplates),
    path("websites/", views.viewWebsites),
    path("first_personal_website/", views.viewFirstPersonal),
    path("second_personal_website/", views.viewSecondPersonal),
    path("first_business_website/", views.viewFirstBusiness),
    path("second_business_website/", views.viewSecondBusiness),
    path("index.html/", views.viewGpdemo),
    path("Visit-cards/", views.viewVisiting),
    path("visitform1/", views.viewFirstVisitingForm),
    path("visitform2/", views.viewSecondVisitingForm),
    path("visitform3/", views.viewThirdVisitingForm),
    path("visitform4/", views.viewFourthVisitingForm),
    path("invitation/", views.viewInvitation),
    path("first_invitation_form/", views.viewFirstInvitation),
    path("second_invitation_form/", views.viewSecondInvitation),
    path("third_invitation_form/", views.viewThirdInvitation),
    path("about/", views.viewAbout),
    path("login/", views.viewLogin),
    path("register/", views.viewRegister),
    path("personal_website1/", views.openPersonalWebsite1),
    path("resume/", views.viewResume),
    path("resumepage/", views.viewResumepage),
    path("resume1/", views.viewResume1),
    path("resume2/", views.viewResume2),
    path("resume3/", views.viewResume3),
    path("rindex1/", views.viewRindex1),
    path("rindex2/", views.viewRindex2),
    path("rindex3/", views.viewRindex3),



    path("visit_payment/", views.visitPayment),



# Web Backend====================================================================================

    path('webresume1/',views.viewsWebResume1),
    path('webresume2/',views.viewsWebResume2),
    path('webresume3/',views.viewsWebResume3),
    path('webvisit1/',views.viewsWebVisit1),
    path('webvisit2/',views.viewsWebVisit2),
    path('webvisit3/',views.viewsWebVisit3),
    path('webvisit4/',views.viewsWebVisit4),
    path('webinvitation1/',views.webinvitation1),
    path('webinvitation2/',views.webinvitation2),
    path('webinvitation3/',views.webinvitation3),


    path('register_details/',views.registerDetails),
    path('user_login_validate/', views.userLoginValidate),
    path('resume_details1/', views.resumeDetails1, name=''),

    path('resume_details_ajax1/', views.resumeDetailsAjax1, name=''),

    path('resume_details2/', views.resumeDetails2, name=''),
    path('resume_details_ajax2/', views.resumeDetailsAjax2, name=''),

    path('resume_details3/', views.resumeDetails3, name=''),
    path('resume_details_ajax3/', views.resumeDetailsAjax3, name=''),

    path('adminindex/', views.viewAdminIndex),
    path('manageuser/', views.viewManageUser),
    path('payment/', views.viewPayment),
    path('admin_master/', views.viewAdmin_Master), 

    path('aadmin_master/', views.adminMasterDetails),
    path('get_payment/', views.getPayment),

    # webistes
   path("personal_website1/",views.personalWebsite1),

   path("personal_website1_demo/",views.personalWebsite1Demo),
   path("personal_website2_demo/",views.personalWebsite2Demo),

   path("business_website1_demo/",views.businessWebsite1Demo),
   path("business_website2_demo/",views.businessWebsite2Demo),

   path("business_website/", views.businessWebsite),
   path("personal_website/", views.personalWebsite),
   path("invitaion_form/", views.invitationForm),
   path("visiting_form/", views.visitingForm),
   path("register_form/", views.registerForm),

   path("first_personal_details1/", views.firstPersonalDetails1),
   path('first_personal_details_ajax1/', views.firstPersonalDetailsAjax1, name=''),

   path("second_personal_details1/", views.secondPersonalDetails1),
   path('second_personal_details_ajax1/', views.secondPersonalDetailsAjax1, name=''),

   path("first_business_details1/", views.firstBusinessDetails1),
   path('first_business_details_ajax1/', views.firstBusinessDetailsAjax1, name=''),

   path("second_business_details1/", views.secondBusinessDetails1),
   path('second_business_details_ajax1/', views.secondBusinessDetailsAjax1, name=''),

   path('admin_login/', views.adminLogin, name=''),

   path('admin_login_validate/', views.adminLoginValidate, name=''),
   path('user_details/', views.userDetails, name=''),

   path('open_user_details/', views.openUserDetails, name=''),
   path('payment_details/', views.paymentDetails, name=''),

   path('logout/', views.webLogout, name=''),
   path('get_personal_website_data/',views.getPersonalWebsiteData),
   path('check_user_session/',views.checkUserSession),
   path('profile/',views.profile),
   path('get_personal_website_profile/',views.getPersonalWebsiteProfile),
   path('get_personal_website_profile1/',views.getPersonalWebsiteProfile1),
   path('get_business_website_profile1/',views.getBusinessWebsiteProfile1),
   path('get_business_website_profile2/',views.getBusinessWebsiteProfile2),
   path('personal_website1_update/',views.personalWebsite1Update),
   path('delete_user_personal_website/',views.deleteUserPersonalWebsite),
   path('get_business_website_data/',views.getBusinessWebsiteData),
   path('business_website_update/',views.businessWebsiteUpdate),

   path('delete_user_business_website/',views.deleteUserBusinessWebsite),
    path('forgot_password/', views.forgotPassword),
  path('check_password/',views.checkPassword),
   path('update_password/',views.updatePassword),
   path('reset_password/',views.resetPassword),

   path('personal_website_details/',views.personalWebsiteDetails),

   path('personal_website1_update1/',views.personalWebsite1Update1),

























]
