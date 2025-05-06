from django.shortcuts import render
from app.models import Resume1
from app.models import Resume2
from app.models import Resume3
from app.models import Visit1
from app.models import Payment
from app.models import Invitation1
from app.models import PersonalWebsite
from app.models import BusinessWebsite
from app.models import AdminMaster
from django.core.files.storage import FileSystemStorage





from django.http import HttpResponse

from django.http import JsonResponse
from app.models import Registration
from mailjet_rest import Client




# Create your views here.

def openHome(request):
    return render(request, 'web/index.html');

def viewTemplates(request):
    return render(request, 'web/Template.html');

def viewWebsites(request):
    return render(request, 'web/websites.html');

def viewFirstPersonal(request):
    if 'web_email' in request.session:
        return render(request, 'web/first_personal_website.html');
    else:
        return render(request, 'web/login.html');

def viewSecondPersonal(request):
    if 'web_email' in request.session:
        return render(request, 'web/second_personal_website.html');
    else:
        return render(request, 'web/login.html');

def viewFirstBusiness(request):
    if 'web_email' in request.session:
        return render(request, 'web/first_business_website.html');
    else:
        return render(request, 'web/login.html');

def viewSecondBusiness(request):
    if 'web_email' in request.session:
        return render(request, 'web/second_business_website.html');
    else:
        return render(request, 'web/login.html');

def viewGpdemo(request):
    return render(request, 'web/websites/gp_business/index.html');

def viewVisiting(request):
    return render(request, 'web/Visit-cards.html');

def viewFirstVisitingForm(request):
    if 'web_email' in request.session:
        return render(request, 'web/visitform1.html');
    else:
        return render(request, 'web/login.html');

def viewSecondVisitingForm(request):
    if 'web_email' in request.session:
        return render(request, 'web/visitform2.html');
    else:
        return render(request, 'web/login.html');

def viewThirdVisitingForm(request):
    if 'web_email' in request.session:
        return render(request, 'web/visitform3.html');
    else:
        return render(request, 'web/login.html');

def viewFourthVisitingForm(request):
    if 'web_email' in request.session:
        return render(request, 'web/visitform4.html');
    else:
        return render(request, 'web/login.html');

def viewInvitation(request):
    return render(request, 'web/invitation.html');

def viewFirstInvitation(request):
    return render(request, 'web/first_invitation_form.html');

def viewSecondInvitation(request):
    return render(request, 'web/second_invitation_form.html');

def viewThirdInvitation(request):
    return render(request, 'web/third_invitation_form.html');

def viewAbout(request):
    return render(request, 'web/about.html');


def viewLogin(request):
    return render(request, 'web/login.html');

def viewRegister(request):
    return render(request, 'web/register.html');

def openPersonalWebsite1(request):
    return render(request, 'web/websites/personal_website1/index.html');

def viewResumepage(request):
    return render(request, 'web/resume-page1.html');

def viewResume(request):
    return render(request, 'web/resume.html');

def viewResume1(request):
    return render(request, 'web/resume1.html');

def viewResume2(request):
    return render(request, 'web/resume2.html');

def viewResume3(request):
    return render(request, 'web/resume3.html');

def viewRindex1(request):
    return render(request, 'web/resumeindex1.html');

def viewRindex2(request):
    return render(request, 'web/resumeindex2.html');

def viewRindex3(request):
    return render(request, 'web/resumeindex3.html');

def personalWebsite1(request):
    return render(request,'web/first_personal_website.html');


 #WebResume===================================================
def viewsWebResume1(request):
    if request.POST['action'] == "add":
        Resume1.objects.create(
            re_about = request.POST['InputAboutMe'],
            re_name = request.POST['InputName'],
            re_skill1 = request.POST['InputSkill1'],
            re_skill2 = request.POST['InputSkill2'],
            re_skill3 = request.POST['InputSkill3'],
            re_skill4 = request.POST['InputSkill4'],
            re_education1 = request.POST['InputEduction1'],
            re_education2 = request.POST['InputEduction2'],
            re_education3 = request.POST['InputEduction3'],
            re_education4 = request.POST['InputEduction4'],
            re_experience1 = request.POST['InputExperience1'],
            re_experience2 = request.POST['InputExperience2'],
            re_experience3 = request.POST['InputExperience3'],
            re_experience4 = request.POST['InputExperience4'],
            re_address = request.POST['InputAddress'],
            re_phone = request.POST['InputAlterNumber'],
            re_email = request.POST['InputEmail'],
            re_image = request.FILES['InputUploadFile'],
            re_created_by = request.session['web_email']
        )
        # data = Visit1.objects.last();
        data = Resume1.objects.filter(re_created_by=request.session['web_email']).values();
        data = list(data)
        dictValue = data[-1]
        # print(dictValue);
        return HttpResponse(dictValue['re_id']); 


def viewsWebResume2(request):
    if request.POST['action'] == "add":
        Resume2.objects.create(
            re_about = request.POST['InputAboutMe'],
            re_name = request.POST['InputName'],
            # re_skill1 = request.POST['InputSkill1'],
            # re_skill2 = request.POST['InputSkill2'],
            # re_skill3 = request.POST['InputSkill3'],
            # re_skill4 = request.POST['InputSkill4'],
            re_education1 = request.POST['InputEduction1'],
            re_education2 = request.POST['InputEduction2'],
            re_education3 = request.POST['InputEduction3'],
            re_education4 = request.POST['InputEduction4'],
            re_experience1 = request.POST['InputExperience1'],
            re_experience2 = request.POST['InputExperience2'],
            re_experience3 = request.POST['InputExperience3'],
            re_experience4 = request.POST['InputExperience4'],
            re_address = request.POST['InputAddress'],
            re_phone = request.POST['InputAlterNumber'],
            re_email = request.POST['InputEmail'],
            re_image = request.FILES['InputUploadFile'],
            re_created_by = request.session['web_email']
        )
        data = Resume2.objects.filter(re_created_by=request.session['web_email']).values();
        data = list(data)
        dictValue = data[-1]
        # print(dictValue);
        return HttpResponse(dictValue['re_id']); 

def viewsWebResume3(request):
    if request.POST['action'] == "add":
        Resume3.objects.create(
            re_about = request.POST['InputAboutMe'],
            re_name = request.POST['InputName'],
            re_skill1 = request.POST['InputSkill1'],
            re_skill2 = request.POST['InputSkill2'],
            re_skill3 = request.POST['InputSkill3'],
            re_skill4 = request.POST['InputSkill4'],
            re_education1 = request.POST['InputEduction1'],
            re_education2 = request.POST['InputEduction2'],
            re_education3 = request.POST['InputEduction3'],
            re_education4 = request.POST['InputEduction4'],
            # re_experience1 = request.POST['InputExperience1'],
            # re_experience2 = request.POST['InputExperience2'],
            # re_experience3 = request.POST['InputExperience3'],
            # re_experience4 = request.POST['InputExperience4'],
            re_address = request.POST['InputAddress'],
            re_phone = request.POST['InputAlterNumber'],
            re_email = request.POST['InputEmail'],
            re_image = request.FILES['InputUploadFile'],
            re_created_by = request.session['web_email']
        )
        data = Resume2.objects.filter(re_created_by=request.session['web_email']).values();
        data = list(data)
        dictValue = data[-1]
        # print(dictValue);
        return HttpResponse(dictValue['re_id']);
# =========================================================================  Visit  ====================

def viewsWebVisit1(request):
    if request.POST['action'] == "add":
        Visit1.objects.create(
            vi_name = request.POST['InputName'],
            vi_email = request.POST['InputEmail1'],
            vi_phone = request.POST['InputAlterNumber'],
            vi_phone1 = request.POST['InputAlterNumber1'],
            vi_address = request.POST['InputAddress'],
            vi_image = request.FILES['InputUploadFile'],
            vi_created_by = request.session['web_email']
        )
        # data = Visit1.objects.last();
        data = Visit1.objects.filter(vi_created_by=request.session['web_email']).values();
        # print(data);
        # last_ten_in_ascending_order = reversed(data)
        data = list(data)
        dictValue = data[-1]
        # print(dictValue);
        return HttpResponse(dictValue['vi_image']); 

def viewsWebVisit2(request):
    if request.POST['action'] == "add":
        Visit1.objects.create(
            vi_name = request.POST['InputName'],
            vi_email = request.POST['InputEmail1'],
            vi_phone = request.POST['InputAlterNumber'],
            vi_phone1 = request.POST['InputAlterNumber1'],
            vi_address = request.POST['InputAddress'],
            vi_image = request.FILES['InputUploadFile']
        )
        data = Visit1.objects.filter(vi_created_by=request.session['web_email']).values();
        # print(data);
        # last_ten_in_ascending_order = reversed(data)
        data = list(data)
        dictValue = data[-1]
        # print(dictValue);
        return HttpResponse(dictValue['vi_image']);  

def viewsWebVisit3(request):
    if request.POST['action'] == "add":
        Visit3.objects.create(
            vi_name = request.POST['InputName'],
            vi_email = request.POST['InputEmail1'],
            vi_phone = request.POST['InputAlterNumber'],
            vi_phone1 = request.POST['InputAlterNumber1'],
            vi_address = request.POST['InputAddress'],
            vi_image = request.FILES['InputUploadFile']
        )
        return HttpResponse(); 
 
def viewsWebVisit4(request):
    if request.POST['action'] == "add":
        Visit4.objects.create(
            vi_name = request.POST['InputName'],
            vi_email = request.POST['InputEmail1'],
            vi_phone = request.POST['InputAlterNumber'],
            vi_phone1 = request.POST['InputAlterNumber1'],
            vi_address = request.POST['InputAddress'],
            vi_image = request.FILES['InputUploadFile']
        )
        return HttpResponse(); 

#============================================================================ Invitation =================
def webinvitation1(request):
    if request.POST['action'] == "add":
        Invitation1.objects.create(
            in_bride = request.POST['bride'],
            in_groom = request.POST['groom'],
            in_date = request.POST['date'],
            in_time = request.POST['time'],
            in_venue = request.POST['venue'],
            in_created_by = request.session['web_email'],
            # in_image = request.FILES['InputUploadFile']
        )
        return HttpResponse(); 

def webinvitation2(request):
    if request.POST['action'] == "add":
        Visit3.objects.create(
            in_bride = request.POST['bride'],
            in_groom = request.POST['groom'],
            in_date = request.POST['date'],
            in_time = request.POST['time'],
            in_venue = request.POST['venue'],
            # in_image = request.FILES['InputUploadFile']
        )
        return HttpResponse(); 

def webinvitation3(request):
    if request.POST['action'] == "add":
        Visit3.objects.create(
            in_bride = request.POST['bride'],
            in_groom = request.POST['groom'],
            in_date = request.POST['date'],
            in_time = request.POST['time'],
            in_venue = request.POST['venue'],
            # in_image = request.FILES['InputUploadFile']
        )
        return HttpResponse(); 

def registerDetails(request):
    if Registration.objects.filter(us_email=request.POST['txtEmail'], us_status='0').exists():
        return HttpResponse("1")
    else:
        lclID = Registration.objects.count()
        status = "0"
    

        lclNewID = lclID + 1

        Registration.objects.create (
            us_id = lclNewID,
            us_name = request.POST['txtName'],
            us_email = request.POST['txtEmail'],
            us_password = request.POST['txtPassword'],
            us_mobile = request.POST['txtMobileNo'],  
            us_secret_key = request.POST['txtSecretKey'],    
            us_status = status,
            # ad_created_by = request.session['email']

        )

        return HttpResponse(request.POST['txtEmail'])

def userLoginValidate(request):
    if Registration.objects.filter(us_email=request.POST['txtEmail'], us_password=request.POST['txtPassword'], us_status='0').exists():
        products_json = Registration.objects.filter(us_email=request.POST['txtEmail']).values()
        data = list(products_json)
        dictValue = data[0]
        request.session['web_email'] = dictValue['us_email']
        request.session['web_name'] = dictValue['us_name']
        request.session['web_phone'] = dictValue['us_mobile']
        return HttpResponse("1")
    else:
        return HttpResponse("0")

def visitPayment(request):
     Payment.objects.create (
        py_card_id = request.POST['visit1'],
        py_user_name = request.session['web_name'],
        py_user_email = request.session['web_email'],
        py_amount = request.POST['amount'],

    )
     api_key = 'aac6730a0dc8a5b7c81cf4c35f650567'
     api_secret = '5f1c7d8729dd7e93b78796ad6ba7697f'
     mailjet = Client(auth=(api_key, api_secret), version='v3.1')
     data = {
     'Messages': [
     {
     "From": {
     "Email": "shaheenkadakol@gmail.com",
     "Name": "Digital Card Generator"
     },
     "To": [
     {
     "Email": request.session['web_email'],
     "Name": request.session['web_name']
     }
     ],
     "Subject": "Greetings from Digital Card Generator.",
     "TextPart": "FoodDonation",
     "HTMLPart": "<h3> Payment of ₹" +  request.POST['amount'] + "successful. Thank you",
     "CustomID": "AppGettingStartedTest"
     }
     ]
     }
     result = mailjet.send.create(data=data)
     print(result.status_code)
     print(result.json())
     return HttpResponse("0")

def resumeDetails1(request):

    

    # context = {};

    # context['re_id'] = dictValue['re_id'];
    # context['re_about'] = dictValue['re_about'];
    # context['re_name'] = dictValue['re_name'];
    # context['re_skill1'] = dictValue['re_skill1'];
    # context['re_skill2'] = dictValue['re_skill2'];
    # context['re_skill3'] = dictValue['re_skill3'];
    # context['re_skill4'] = dictValue['re_skill4'];

    # context['re_education1'] = dictValue['re_education1'];
    # context['re_education2'] = dictValue['re_education2'];
    # context['re_education3'] = dictValue['re_education3'];
    # context['re_education4'] = dictValue['re_education4'];

    # context['re_experience1'] = dictValue['re_experience1'];
    # context['re_experience2'] = dictValue['re_experience2'];
    # context['re_experience3'] = dictValue['re_experience3'];
    # context['re_experience4'] = dictValue['re_experience4'];

    # context['re_address'] = dictValue['re_address'];
    # context['re_phone'] = dictValue['re_phone'];
    # context['re_email'] = dictValue['re_email'];
    # context['re_resume'] = dictValue['re_resume'];
    # context['re_image'] = dictValue['re_image'];

    return render(request, 'web/resume_details1.html');

def resumeDetailsAjax1(request):
    data = Resume1.objects.filter(re_id=request.POST['id']).values();
    data = list(data)
    value = JsonResponse(data, safe=False)
    return value

def resumeDetails2(request):
    return render(request, 'web/resume_details2.html');

def resumeDetailsAjax2(request):
    data = Resume2.objects.filter(re_id=request.POST['id']).values();
    data = list(data)
    value = JsonResponse(data, safe=False)
    return value

def resumeDetails3(request):
    return render(request, 'web/resume_details3.html');

def resumeDetailsAjax3(request):
    data = Resume3.objects.filter(re_id=request.POST['id']).values();
    data = list(data)
    value = JsonResponse(data, safe=False)
    return value

def adminMasterDetails(request):
    if request.POST['action'] == "add":
        AdminMaster.objects.create(ad_name = request.POST['txtName'],ad_mobile = request.POST['txtNumber'],ad_email = request.POST['txtEmail'],ad_password = request.POST['txtPassword']) 

    elif request.POST['action'] == "getData":
        data = AdminMaster.objects.filter(ad_status='0').values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values
        
    elif request.POST['action'] == "update":
        data = AdminMaster.objects.filter(ad_id=request.POST['id']).update(ad_name = request.POST['txtName1'],ad_mobile = request.POST['txtContact1'],ad_email = request.POST['txtEmail1'],ad_password = request.POST['txtPassword1']);
        
    elif request.POST['action'] == "delete":
        data = AdminMaster.objects.filter(ad_id=request.POST['id']).update(ad_status='1')
    
    return HttpResponse()

def viewAdminIndex(request):
    data1 = Registration.objects.filter(us_status = 0).count()
    data2 = PersonalWebsite.objects.filter(pw_status = 0).count()
    data3 = BusinessWebsite.objects.filter(bw_status = 0).count()

    context = {};
    context['users'] = data1;
    context['personalwebsitepayment'] = data2;
    context['businesswebsitepament'] = data3;


    return render(request, 'admin/adminindex.html',context);

def adminlog(request):
    return render(request, 'admin/adminlogin.html');

def viewManageUser(request):
    return render(request, 'admin/manageuser.html');

def viewPayment(request):
    return render(request, 'admin/payment.html');

def viewAdmin_Master(request):
    return render(request, 'admin/admin_master.html');

def getPayment(request):
    data = Payment.objects.filter().values();
    data = list(data)
    value = JsonResponse(data, safe=False)
    return value

# websites
def personalWebsite1Demo(request):
    return render(request, 'web/Personal_Website/index.html');

def personalWebsite2Demo(request):
    return render(request, 'web/personal_website1/index.html');

def businessWebsite1Demo(request):
    return render(request, 'web/presento_business/index.html');

def businessWebsite2Demo(request):
    return render(request, 'web/gp_business/index.html');

# website form
def businessWebsite(request):
    if request.POST['action'] == "add":
        BusinessWebsite.objects.create(bw_unique_id = request.POST['businessWebsite'], 
        bw_about = request.POST['txtAbout'],
        bw_services_heading1  = request.POST['txtServicesHeading1'],
        bw_services_description1  = request.POST['txtServicesDescription1'],
        bw_services_heading2  = request.POST['txtServicesHeading2'],
        bw_services_description2  = request.POST['txtServicesDescription2'],
        bw_services_heading3  = request.POST['txtServicesHeading3'],
        bw_services_description3  = request.POST['txtServicesDescription3'],

        bw_happy_clients  = request.POST['txtHappyClients'],
        bw_projects  = request.POST['txtProjects'],    
        bw_hours  = request.POST['txtHoursSupport'],
        bw_hard_workers  = request.POST['txtHardWorkers'],
        bw_company_description  = request.POST['txtCompanyDescription'],
        bw_pricing1  = request.POST['txtPricing1'],
        bw_pricing1_description  = request.POST['txtPricing1Description'],
        bw_pricing2  = request.POST['txtPricing2'],
        bw_pricing2_description  = request.POST['txtPricing2Description'],
        bw_facility1  = request.POST['txtFacility1'],
        bw_facility2  = request.POST['txtFacility2'],
        bw_facility3  = request.POST['txtFacility3'],
        bw_facility4  = request.POST['txtFacility4'],
        bw_testimonial1  = request.POST['txtTestimonial1'],
        bw_testimonial1_description  = request.POST['txtTestimonial1Description'],
        bw_testimonial2  = request.POST['txtTestimonial2'],
        bw_testimonial2_description  = request.POST['txtTestimonial2Description'],
        bw_testimonial3  = request.POST['txtTestimonial3'],
        bw_testimonial3_description  = request.POST['txtTestimonial3Description'],
        bw_testimonial4  = request.POST['txtTestimonial4'],
        bw_testimonial4_description  = request.POST['txtTestimonial4Description'],
        bw_testimonial5  = request.POST['txtTestimonial5'],
        bw_testimonial5_description  = request.POST['txtTestimonial5Description'],
        bw_location  = request.POST['txtLocation'],
        bw_email  = request.POST['txtEmail'],
        bw_phone  = request.POST['txtPhoneNo'],
        bw_created_by = request.session['web_email'], 
        bw_user_name = request.session['web_email'], 
        bw_user_email = request.session['web_name'], 
        bw_amount = 5000, 
        ) 

        api_key = 'aac6730a0dc8a5b7c81cf4c35f650567'
        api_secret = '5f1c7d8729dd7e93b78796ad6ba7697f'
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
          'Messages': [
            {
              "From": {
                "Email": "shaheenkadakol@gmail.com",
                "Name": "Web Page Builder"
              },
              "To": [
                {
                  "Email": request.session['web_email'],
                  "Name": request.session['web_name']
                }
              ],
              "Subject": "Greetings from Web Page Builder.",
              "TextPart": "Web Page Builder",
              "HTMLPart": "<h3>Dear Customer,Thank you for payment",
              "CustomID": "AppGettingStartedTest"
            }
          ]
        }
        result = mailjet.send.create(data=data)
        print(result.status_code)
        print(result.json())   

        data = BusinessWebsite.objects.filter(bw_created_by=request.session['web_email']).values();
        data = list(data)
        dictValue = data[-1]
        # print(dictValue);
        list1 = [{"bw_id":dictValue['bw_id'],"bw_unique_id":dictValue['bw_unique_id']}]
        return JsonResponse(list1,safe = False) 

def personalWebsite(request):
    if request.POST['action'] == "add":
        PersonalWebsite.objects.create(pw_unique_id = request.POST['personalWebsite'],
        pw_image =  request.FILES['lclImage'],           
        pw_name =  request.POST['txtName1'],
        pw_about = request.POST['txtAbout'],
        pw_designation1 = request.POST['txtDesignation1'],
        pw_designation2 = request.POST['txtDesignation2'],
        pw_designation3 = request.POST['txtDesignation3'],
        pw_skill1 = request.POST['txtSkill1'],
        pw_skill2 = request.POST['txtSkill2'],
        pw_skill3 = request.POST['txtSkill3'],
        pw_skill4 = request.POST['txtSkill4'],
        pw_skill5 = request.POST['txtSkill5'],
        pw_skill6 = request.POST['txtSkill6'],
        pw_service1 = request.POST['txtService1'],
        pw_service2 = request.POST['txtService2'],
        pw_service3 = request.POST['txtService3'],
        pw_service4 = request.POST['txtService4'],
        pw_service5 = request.POST['txtService5'],
        pw_service6 = request.POST['txtService6'],
        pw_education1 = request.POST['txtEducation1'],
        pw_education2 = request.POST['txtEducation2'],
        pw_education3 = request.POST['txtEducation3'],
        pw_experience1 = request.POST['txtExperience1'],
        pw_experience2 = request.POST['txtExperience2'],
        pw_experience3 = request.POST['txtExperience3'],
        pw_mobile = request.POST['txtMobile'],
        pw_email = request.POST['txtEmail'],
        pw_address = request.POST['txtAddress'],
        pw_experience_years = request.POST['txtExperienceCount'],
        pw_freelance = request.POST['txtFreelance'],
        pw_created_by = request.session['web_email'],
        pw_user_name = request.session['web_email'], 
        pw_user_email = request.session['web_name'], 
        pw_amount = 5000, 

        )

        api_key = 'aac6730a0dc8a5b7c81cf4c35f650567'
        api_secret = '5f1c7d8729dd7e93b78796ad6ba7697f'
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
        'Messages': [
        {
        "From": {
        "Email": "shaheenkadakol@gmail.com",
        "Name": "Web Page Builder"
        },
        "To": [
        {
        "Email": request.session['web_email'],
        "Name": request.session['web_name']
        }
        ],
        "Subject": "Greetings from Web Page Builder.",
        "TextPart": "Web Page Builder",
        "HTMLPart": "<h3>Dear Customer,Thank you for payment",
        "CustomID": "AppGettingStartedTest"
        }
        ]
        }
        result = mailjet.send.create(data=data)
        print(result.status_code)
        print(result.json())    
    
        data = PersonalWebsite.objects.filter(pw_created_by=request.session['web_email']).values();
        data = list(data)
        dictValue = data[-1]
        # print(dictValue);
        list1 = [{"pw_id":dictValue['pw_id'],"pw_unique_id":dictValue['pw_unique_id']}]
        
        return JsonResponse(list1,safe = False) 

def personalWebsiteDetails(request):
    if request.POST['action'] == "add":
        PersonalWebsite.objects.create(pw_unique_id = request.POST['personalWebsite'],         
        pw_name =  request.POST['txtName1'],
        pw_about = request.POST['txtAbout'],
        pw_designation1 = request.POST['txtDesignation1'],
        pw_designation2 = request.POST['txtDesignation2'],
        pw_designation3 = request.POST['txtDesignation3'],
        pw_skill1 = request.POST['txtSkill1'],
        pw_skill2 = request.POST['txtSkill2'],
        pw_skill3 = request.POST['txtSkill3'],
        pw_skill4 = request.POST['txtSkill4'],
        pw_skill5 = request.POST['txtSkill5'],
        pw_skill6 = request.POST['txtSkill6'],
        pw_service1 = request.POST['txtService1'],
        pw_service2 = request.POST['txtService2'],
        pw_service3 = request.POST['txtService3'],
        pw_service4 = request.POST['txtService4'],
        pw_service5 = request.POST['txtService5'],
        pw_service6 = request.POST['txtService6'],
        pw_education1 = request.POST['txtEducation1'],
        pw_education2 = request.POST['txtEducation2'],
        pw_education3 = request.POST['txtEducation3'],
        pw_experience1 = request.POST['txtExperience1'],
        pw_experience2 = request.POST['txtExperience2'],
        pw_experience3 = request.POST['txtExperience3'],
        pw_mobile = request.POST['txtMobile'],
        pw_email = request.POST['txtEmail'],
        pw_address = request.POST['txtAddress'],
        pw_experience_years = request.POST['txtExperienceCount'],
        pw_freelance = request.POST['txtFreelance'],
        pw_created_by = request.session['web_email'],
        pw_user_name = request.session['web_email'], 
        pw_user_email = request.session['web_name'], 
        pw_amount = 5000, 

        )

        api_key = 'aac6730a0dc8a5b7c81cf4c35f650567'
        api_secret = '5f1c7d8729dd7e93b78796ad6ba7697f'
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')
        data = {
        'Messages': [
        {
        "From": {
        "Email": "shaheenkadakol@gmail.com",
        "Name": "Web Page Builder"
        },
        "To": [
        {
        "Email": request.session['web_email'],
        "Name": request.session['web_name']
        }
        ],
        "Subject": "Greetings from Web Page Builder.",
        "TextPart": "Web Page Builder",
        "HTMLPart": "<h3>Dear Customer,Thank you for payment",
        "CustomID": "AppGettingStartedTest"
        }
        ]
        }
        result = mailjet.send.create(data=data)
        print(result.status_code)
        print(result.json())    
    
        data = PersonalWebsite.objects.filter(pw_created_by=request.session['web_email']).values();
        data = list(data)
        dictValue = data[-1]
        # print(dictValue);
        list1 = [{"pw_id":dictValue['pw_id'],"pw_unique_id":dictValue['pw_unique_id']}]
        return JsonResponse(list1,safe = False) 

# invitation form
def invitationForm(request):
    if request.POST['action'] == "add":
        Invitation.objects.create(in_unique_id = request.POST['invitation'], 
        in_bride = request.POST['bride'],
        in_groom = request.POST['groom'],
        in_date = request.POST['date'], 
        in_time = request.POST['time'],
        in_venue = request.POST['venue'])   
    
    return HttpResponse()


# visiting cards
def visitingForm(request):
    if request.POST['action'] == "add":
        Visiting.objects.create(vi_unique_id = request.POST['visitingCard'], 
        vi_name = request.POST['name'],
        vi_email = request.POST['email'],
        vi_number = request.POST['number'], 
        vi_altnumber = request.POST['altNumber'],
        vi_logo = request.FILES['txtImage'],
        vi_address = request.POST['address'])   
    
    return HttpResponse()

def registerForm(request):
    if request.POST['action'] == "add":
        Register.objects.create(re_name = request.POST['name'],
        re_username = request.POST['uname'],
        re_number = request.POST['number'], 
        re_email = request.POST['email'],
        re_password = request.POST['password'])
    
    return HttpResponse()

def firstPersonalDetails1(request):
    return render(request, 'web/Personal_Website/index.html');

def firstPersonalDetailsAjax1(request):
    data = PersonalWebsite.objects.filter(pw_id=request.POST['id']).values();
    data = list(data)
    value = JsonResponse(data, safe=False)
    return value

def secondPersonalDetails1(request):
    return render(request, 'web/Personal_Website1/index.html');

def secondPersonalDetailsAjax1(request):
    data = PersonalWebsite.objects.filter(pw_id=request.POST['id']).values();
    data = list(data)
    value = JsonResponse(data, safe=False)
    return value

def firstBusinessDetails1(request):
    return render(request, 'web/presento_business/index.html');

def firstBusinessDetailsAjax1(request):
    data = BusinessWebsite.objects.filter(bw_id=request.POST['id']).values();
    data = list(data)
    value = JsonResponse(data, safe=False)
    return value

def secondBusinessDetails1(request):
    return render(request, 'web/gp_business/index.html');

def secondBusinessDetailsAjax1(request):
    data = BusinessWebsite.objects.filter(bw_id=request.POST['id']).values();
    data = list(data)
    value = JsonResponse(data, safe=False)
    return value

def adminLogin(request):
    return render(request, 'admin/adminlogin.html');

def adminLoginValidate(request):
    if AdminMaster.objects.filter(ad_email=request.POST['txtEmail'], ad_password=request.POST['txtPassword'], ad_status='0').exists():
        products_json = AdminMaster.objects.filter(ad_email=request.POST['txtEmail']).values()
        data = list(products_json)
        dictValue = data[0]
        request.session['email'] = dictValue['ad_email']
        request.session['name'] = dictValue['ad_name']
        request.session['phone'] = dictValue['ad_mobile']
        return HttpResponse("1")
    else:
        return HttpResponse("0")



def userDetails(request):
    data = Registration.objects.filter(us_status='0').values();
    data = list(data)
    value = JsonResponse(data, safe=False)
    return value

def openUserDetails(request):
    return render(request, 'admin/manageuser.html');

def paymentDetails(request):
    data = PersonalWebsite.objects.filter(pw_status='0').values();
    data = list(data)
    value = JsonResponse(data, safe=False)
    return value


def webLogout(request):
    request.session.delete()
    return render(request,'web/index.html')

def getPersonalWebsiteData(request):
    data = PersonalWebsite.objects.filter(pw_id= request.POST['id'],pw_created_by = request.session['web_email'],pw_status='0',pw_unique_id=request.POST['uniqueId']).values()
    data = list(data)
    value = JsonResponse(data, safe=False)
    return value

def checkUserSession(request):
    if "web_email" in request.session:
        return HttpResponse(1)
    else:
        return HttpResponse(0)

def profile(request):
    return render(request,'web/profile.html')


def getPersonalWebsiteProfile(request):
    data = PersonalWebsite.objects.filter(pw_created_by = request.session['web_email'],pw_status='0',pw_unique_id=request.POST['uniqueId']).values()
    data = list(data)
    value = JsonResponse(data, safe=False)
    return value

def getPersonalWebsiteProfile1(request):
    data = PersonalWebsite.objects.filter(pw_created_by = request.session['web_email'],pw_status='0',pw_unique_id=request.POST['uniqueId']).values()
    data = list(data)
    value = JsonResponse(data, safe=False)
    return value

def getBusinessWebsiteProfile1(request):
    data = BusinessWebsite.objects.filter(bw_created_by = request.session['web_email'],bw_status='0',bw_unique_id=request.POST['uniqueId']).values()
    data = list(data)
    value = JsonResponse(data, safe=False)
    return value

def getBusinessWebsiteProfile2(request):
    data = BusinessWebsite.objects.filter(bw_created_by = request.session['web_email'],bw_status='0',bw_unique_id=request.POST['uniqueId']).values()
    data = list(data)
    value = JsonResponse(data, safe=False)
    return value

def personalWebsite1Update(request):
    if request.POST['imgText'] == "":
        profile_pic = request.FILES['lclImage']
        fs = FileSystemStorage()
        filename = fs.save("app/static/media/images/" + profile_pic.name, profile_pic)
        image_path = fs.url(filename);
        image_path = image_path[1:];
        data = PersonalWebsite.objects.filter(pw_id=request.POST['id']).update(
            pw_image =  image_path,           
            pw_name =  request.POST['txtName1'],
            pw_about = request.POST['txtAbout'],
            pw_designation1 = request.POST['txtDesignation1'],
            pw_designation2 = request.POST['txtDesignation2'],
            pw_designation3 = request.POST['txtDesignation3'],
            pw_skill1 = request.POST['txtSkill1'],
            pw_skill2 = request.POST['txtSkill2'],
            pw_skill3 = request.POST['txtSkill3'],
            pw_skill4 = request.POST['txtSkill4'],
            pw_skill5 = request.POST['txtSkill5'],
            pw_skill6 = request.POST['txtSkill6'],
            pw_service1 = request.POST['txtService1'],
            pw_service2 = request.POST['txtService2'],
            pw_service3 = request.POST['txtService3'],
            pw_service4 = request.POST['txtService4'],
            pw_service5 = request.POST['txtService5'],
            pw_service6 = request.POST['txtService6'],
            pw_education1 = request.POST['txtEducation1'],
            pw_education2 = request.POST['txtEducation2'],
            pw_education3 = request.POST['txtEducation3'],
            pw_experience1 = request.POST['txtExperience1'],
            pw_experience2 = request.POST['txtExperience2'],
            pw_experience3 = request.POST['txtExperience3'],
            pw_mobile = request.POST['txtMobile'],
            pw_email = request.POST['txtEmail'],
            pw_address = request.POST['txtAddress'],
            pw_experience_years = request.POST['txtExperienceCount'],
            pw_freelance = request.POST['txtFreelance'],
            pw_created_by = request.session['web_email'],
            pw_user_name = request.session['web_email'], 
            pw_user_email = request.session['web_name'], 
            pw_amount = 5000, 
            )
        data = PersonalWebsite.objects.filter(pw_created_by=request.session['web_email']).values();
        data = list(data)
        dictValue = data[-1]
        list1 = [{"pw_id":dictValue['pw_id'],"pw_unique_id":dictValue['pw_unique_id']}]
        return JsonResponse(list1,safe = False) 
    else:
        data = PersonalWebsite.objects.filter(pw_id=request.POST['id']).update(
            pw_image =  image_path,           
            pw_name =  request.POST['txtName1'],
            pw_about = request.POST['txtAbout'],
            pw_designation1 = request.POST['txtDesignation1'],
            pw_designation2 = request.POST['txtDesignation2'],
            pw_designation3 = request.POST['txtDesignation3'],
            pw_skill1 = request.POST['txtSkill1'],
            pw_skill2 = request.POST['txtSkill2'],
            pw_skill3 = request.POST['txtSkill3'],
            pw_skill4 = request.POST['txtSkill4'],
            pw_skill5 = request.POST['txtSkill5'],
            pw_skill6 = request.POST['txtSkill6'],
            pw_service1 = request.POST['txtService1'],
            pw_service2 = request.POST['txtService2'],
            pw_service3 = request.POST['txtService3'],
            pw_service4 = request.POST['txtService4'],
            pw_service5 = request.POST['txtService5'],
            pw_service6 = request.POST['txtService6'],
            pw_education1 = request.POST['txtEducation1'],
            pw_education2 = request.POST['txtEducation2'],
            pw_education3 = request.POST['txtEducation3'],
            pw_experience1 = request.POST['txtExperience1'],
            pw_experience2 = request.POST['txtExperience2'],
            pw_experience3 = request.POST['txtExperience3'],
            pw_mobile = request.POST['txtMobile'],
            pw_email = request.POST['txtEmail'],
            pw_address = request.POST['txtAddress'],
            pw_experience_years = request.POST['txtExperienceCount'],
            pw_freelance = request.POST['txtFreelance'],
            pw_created_by = request.session['web_email'],
            pw_user_name = request.session['web_email'], 
            pw_user_email = request.session['web_name'], 
            pw_amount = 5000, 
            )
        data = PersonalWebsite.objects.filter(pw_created_by=request.session['web_email']).values();
        data = list(data)
        dictValue = data[-1]
        list1 = [{"pw_id":dictValue['pw_id'],"pw_unique_id":dictValue['pw_unique_id']}]
        return JsonResponse(list1,safe = False) 

def deleteUserPersonalWebsite(request):
    PersonalWebsite.objects.filter(pw_id = request.POST['id']).update(pw_status = "1")
    return HttpResponse()

def getBusinessWebsiteData(request):
    data = BusinessWebsite.objects.filter(bw_id= request.POST['id'],bw_created_by = request.session['web_email'],bw_status='0',bw_unique_id=request.POST['uniqueId']).values()
    data = list(data)
    value = JsonResponse(data, safe=False)
    return value

def businessWebsiteUpdate(request):
    data = BusinessWebsite.objects.filter(bw_id=request.POST['id']).update(
        bw_about = request.POST['txtAbout'],
        bw_services_heading1  = request.POST['txtServicesHeading1'],
        bw_services_description1  = request.POST['txtServicesDescription1'],
        bw_services_heading2  = request.POST['txtServicesHeading2'],
        bw_services_description2  = request.POST['txtServicesDescription2'],
        bw_services_heading3  = request.POST['txtServicesHeading3'],
        bw_services_description3  = request.POST['txtServicesDescription3'],

        bw_happy_clients  = request.POST['txtHappyClients'],
        bw_projects  = request.POST['txtProjects'],    
        bw_hours  = request.POST['txtHoursSupport'],
        bw_hard_workers  = request.POST['txtHardWorkers'],
        bw_company_description  = request.POST['txtCompanyDescription'],
        bw_pricing1  = request.POST['txtPricing1'],
        bw_pricing1_description  = request.POST['txtPricing1Description'],
        bw_pricing2  = request.POST['txtPricing2'],
        bw_pricing2_description  = request.POST['txtPricing2Description'],
        bw_facility1  = request.POST['txtFacility1'],
        bw_facility2  = request.POST['txtFacility2'],
        bw_facility3  = request.POST['txtFacility3'],
        bw_facility4  = request.POST['txtFacility4'],
        # bw_testimonial1  = request.POST['txtTestimonial1'],
        # bw_testimonial1_description  = request.POST['txtTestimonial1Description'],
        # bw_testimonial2  = request.POST['txtTestimonial2'],
        # bw_testimonial2_description  = request.POST['txtTestimonial2Description'],
        # bw_testimonial3  = request.POST['txtTestimonial3'],
        # bw_testimonial3_description  = request.POST['txtTestimonial3Description'],
        # bw_testimonial4  = request.POST['txtTestimonial4'],
        # bw_testimonial4_description  = request.POST['txtTestimonial4Description'],
        # bw_testimonial5  = request.POST['txtTestimonial5'],
        # bw_testimonial5_description  = request.POST['txtTestimonial5Description'],
        bw_location  = request.POST['txtLocation'],
        bw_email  = request.POST['txtEmail'],
        bw_phone  = request.POST['txtPhoneNo'],
        bw_created_by = request.session['web_email'], 
        bw_user_name = request.session['web_email'], 
        bw_user_email = request.session['web_name'], 
        bw_amount = 5000, 
        )
    data = BusinessWebsite.objects.filter(bw_id = request.POST['id'],bw_created_by=request.session['web_email']).values();
    data = list(data)
    dictValue = data[-1]
    list1 = [{"bw_id":dictValue['bw_id'],"bw_unique_id":dictValue['bw_unique_id']}]
    return JsonResponse(list1,safe = False) 

def deleteUserBusinessWebsite(request):
    BusinessWebsite.objects.filter(bw_id = request.POST['id']).update(bw_status = "1")
    return HttpResponse()

def forgotPassword(request):
	return render(request, 'web/forgot_password.html');

def updatePassword(request):
	return render(request, 'web/update_password.html');


def checkPassword(request):
    if Registration.objects.filter(us_email=request.POST['txtEmail'], us_secret_key=request.POST['txtSecretKey']).exists():
        request.session['forgot_email'] = request.POST['txtEmail']
        return HttpResponse("1")
    else:
        return HttpResponse("10")

def resetPassword(request):
    if request.POST['action'] == "update":
        data = Registration.objects.filter(us_status='0',us_email=request.session['forgot_email']).update(
			
			# re_role = request.POST['txtRole1'],
			us_password = request.POST['txtPassword1'],
			
			);

    return HttpResponse()

def personalWebsite1Update1(request):

    data = PersonalWebsite.objects.filter(pw_id=request.POST['id']).update(          
        pw_name =  request.POST['txtName1'],
        pw_about = request.POST['txtAbout'],
        pw_designation1 = request.POST['txtDesignation1'],
        pw_designation2 = request.POST['txtDesignation2'],
        pw_designation3 = request.POST['txtDesignation3'],
        pw_skill1 = request.POST['txtSkill1'],
        pw_skill2 = request.POST['txtSkill2'],
        pw_skill3 = request.POST['txtSkill3'],
        pw_skill4 = request.POST['txtSkill4'],
        pw_skill5 = request.POST['txtSkill5'],
        pw_skill6 = request.POST['txtSkill6'],
        pw_service1 = request.POST['txtService1'],
        pw_service2 = request.POST['txtService2'],
        pw_service3 = request.POST['txtService3'],
        pw_service4 = request.POST['txtService4'],
        pw_service5 = request.POST['txtService5'],
        pw_service6 = request.POST['txtService6'],
        pw_education1 = request.POST['txtEducation1'],
        pw_education2 = request.POST['txtEducation2'],
        pw_education3 = request.POST['txtEducation3'],
        pw_experience1 = request.POST['txtExperience1'],
        pw_experience2 = request.POST['txtExperience2'],
        pw_experience3 = request.POST['txtExperience3'],
        pw_mobile = request.POST['txtMobile'],
        pw_email = request.POST['txtEmail'],
        pw_address = request.POST['txtAddress'],
        pw_experience_years = request.POST['txtExperienceCount'],
        pw_freelance = request.POST['txtFreelance'],
        pw_created_by = request.session['web_email'],
        pw_user_name = request.session['web_email'], 
        pw_user_email = request.session['web_name'], 
        pw_amount = 5000, 
        )
    data = PersonalWebsite.objects.filter(pw_id = request.POST['id'],pw_created_by=request.session['web_email']).values();
    data = list(data)
    dictValue = data[-1]
    list1 = [{"pw_id":dictValue['pw_id'],"pw_unique_id":dictValue['pw_unique_id']}]
    return JsonResponse(list1,safe = False) 