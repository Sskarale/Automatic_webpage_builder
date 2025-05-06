from django.db import models

# Create your models here.

class Resume1(models.Model):
	re_id = models.AutoField(primary_key=True, unique = True)
	re_about = models.CharField(max_length=250)
	re_name = models.CharField(max_length=100)
	re_skill1 = models.CharField(max_length=100,default="")
	re_skill2 = models.CharField(max_length=100,default="")
	re_skill3 = models.CharField(max_length=100,default="")
	re_skill4 = models.CharField(max_length=100,default="")
	re_education1 = models.CharField(max_length=100)
	re_education2 = models.CharField(max_length=100)
	re_education3 = models.CharField(max_length=100)
	re_education4 = models.CharField(max_length=100)
	re_experience1 = models.CharField(max_length=100)
	re_experience2 = models.CharField(max_length=100)
	re_experience3 = models.CharField(max_length=100)
	re_experience4 = models.CharField(max_length=100)
	re_address = models.CharField(max_length=100)
	re_phone = models.CharField(max_length=100)
	re_email = models.CharField(max_length=100)
	re_resume  = models.ImageField(upload_to="app/static/web/media/resumedata")
	re_image = models.ImageField(upload_to="app/static/web/media/images")
	re_status = models.IntegerField(default=0)
	re_created_by = models.CharField(max_length=100, default="")

class Resume2(models.Model):
	re_id = models.AutoField(primary_key=True, unique = True)
	re_about = models.CharField(max_length=250)
	re_name = models.CharField(max_length=100)
	re_skill1 = models.CharField(max_length=100)
	re_skill2 = models.CharField(max_length=100)
	re_skill3 = models.CharField(max_length=100)
	re_skill4 = models.CharField(max_length=100)
	re_education1 = models.CharField(max_length=100)
	re_education2 = models.CharField(max_length=100)
	re_education3 = models.CharField(max_length=100)
	re_education4 = models.CharField(max_length=100)
	re_experience1 = models.CharField(max_length=100)
	re_experience2 = models.CharField(max_length=100)
	re_experience3 = models.CharField(max_length=100)
	re_experience4 = models.CharField(max_length=100)
	re_address = models.CharField(max_length=100)
	re_phone = models.CharField(max_length=100)
	re_email = models.CharField(max_length=100)
	re_resume  = models.ImageField(upload_to="app/static/web/media/resumedata")
	re_image = models.ImageField(upload_to="app/static/web/media/images")
	re_status = models.IntegerField(default=0)
	re_created_by = models.CharField(max_length=100, default="")

class Resume3(models.Model):
	re_id = models.AutoField(primary_key=True, unique = True)
	re_about = models.CharField(max_length=250)
	re_name = models.CharField(max_length=100)
	re_skill1 = models.CharField(max_length=100)
	re_skill2 = models.CharField(max_length=100)
	re_skill3 = models.CharField(max_length=100)
	re_skill4 = models.CharField(max_length=100)
	re_education1 = models.CharField(max_length=100)
	re_education2 = models.CharField(max_length=100)
	re_education3 = models.CharField(max_length=100)
	re_education4 = models.CharField(max_length=100)
	# re_experience1 = models.CharField(max_length=100)
	# re_experience2 = models.CharField(max_length=100)
	# re_experience3 = models.CharField(max_length=100)
	# re_experience4 = models.CharField(max_length=100)
	re_address = models.CharField(max_length=100)
	re_phone = models.CharField(max_length=100)
	re_email = models.CharField(max_length=100)
	re_resume  = models.ImageField(upload_to="app/static/web/media/resumedata")
	re_image = models.ImageField(upload_to="app/static/web/media/images")
	re_status = models.IntegerField(default=0)
	re_created_by = models.CharField(max_length=100, default="")		
# ============================================================================================
class Visit1(models.Model):
	vi_id = models.AutoField(primary_key=True, unique = True)
	vi_name = models.CharField(max_length=100)
	vi_address = models.CharField(max_length=100)
	vi_phone = models.CharField(max_length=100)
	vi_phone1 = models.CharField(max_length=100)
	vi_email = models.CharField(max_length=100)
	vi_image = models.ImageField(upload_to="app/static/web/media/images")
	vi_status = models.IntegerField(default=0)
	vi_created_by = models.CharField(max_length=100, default="")		

class Visit2(models.Model):
	vi_id = models.AutoField(primary_key=True, unique = True)
	vi_name = models.CharField(max_length=100)
	vi_address = models.CharField(max_length=100)
	vi_phone = models.CharField(max_length=100)
	vi_phone1 = models.CharField(max_length=100)
	vi_email = models.CharField(max_length=100)
	vi_image = models.ImageField(upload_to="app/static/web/media/images")
	vi_status = models.IntegerField(default=0)
	vi_created_by = models.CharField(max_length=100, default="")

class Visit3(models.Model):
	vi_id = models.AutoField(primary_key=True, unique = True)
	vi_name = models.CharField(max_length=100)
	vi_address = models.CharField(max_length=100)
	vi_phone = models.CharField(max_length=100)
	vi_phone1 = models.CharField(max_length=100)
	vi_email = models.CharField(max_length=100)
	vi_image = models.ImageField(upload_to="app/static/web/media/images")
	vi_status = models.IntegerField(default=0)
	vi_created_by = models.CharField(max_length=100, default="")	

# ============================================================================================

class Invitation1(models.Model):
	in_id = models.AutoField(primary_key=True, unique = True)
	in_bride = models.CharField(max_length=100)
	in_invitation_id = models.CharField(max_length=100,default = "")
	in_groom = models.CharField(max_length=100)
	in_date = models.CharField(max_length=100)
	in_time = models.CharField(max_length=100)
	in_venue = models.CharField(max_length=100)
	# in_image = models.ImageField(upload_to="app/static/web/media/images")
	in_status = models.IntegerField(default=0)
	in_created_by = models.CharField(max_length=100, default="")		

class Invitation2(models.Model):
	in_id = models.AutoField(primary_key=True, unique = True)
	in_bride = models.CharField(max_length=100)
	in_invitation_id = models.CharField(max_length=100,default = "")

	in_groom = models.CharField(max_length=100)
	in_date = models.CharField(max_length=100)
	in_time = models.CharField(max_length=100)
	in_venue = models.CharField(max_length=100)
	# in_image = models.ImageField(upload_to="app/static/web/media/images")
	in_status = models.IntegerField(default=0)
	in_created_by = models.CharField(max_length=100, default="")		

class Invitation3(models.Model):
	in_id = models.AutoField(primary_key=True, unique = True)
	in_bride = models.CharField(max_length=100)
	in_invitation_id = models.CharField(max_length=100,default = "")

	in_groom = models.CharField(max_length=100)
	in_date = models.CharField(max_length=100)
	in_time = models.CharField(max_length=100)
	in_venue = models.CharField(max_length=100)
	# in_image = models.ImageField(upload_to="app/static/web/media/images")
	in_status = models.IntegerField(default=0)
	in_created_by = models.CharField(max_length=100, default="")

class Registration(models.Model):
	us_id = models.AutoField(primary_key=True, unique = True)
	us_name = models.CharField(max_length=100)
	us_mobile = models.CharField(max_length=100)
	us_email = models.CharField(max_length=100)
	us_password = models.CharField(max_length=100)
	us_secret_key = models.CharField(max_length=100, default="")
	us_status = models.CharField(max_length=100)
	us_created_by = models.CharField(max_length=100)

class Payment(models.Model):
	py_id = models.AutoField(primary_key=True, unique = True)
	py_card_id = models.CharField(max_length=100)
	py_user_name =  models.CharField(max_length=100,default='')
	py_user_email = models.CharField(max_length=100)
	py_amount = models.CharField(max_length=100)
	py_status = models.IntegerField(default = 0)
	py_created_by = models.CharField(max_length=100)

class AdminMaster(models.Model):
	ad_id = models.AutoField(primary_key=True, unique = True)
	ad_name = models.CharField(max_length=100)
	ad_mobile = models.CharField(max_length=100)
	ad_email = models.CharField(max_length=100)
	ad_password = models.CharField(max_length=100)
	# ad_role = models.CharField(max_length=100)
	ad_status = models.IntegerField(default=0)
	ad_created_by = models.CharField(max_length=100, default="")

class BusinessWebsite(models.Model):
	bw_id = models.AutoField(primary_key=True, unique = True)
	bw_unique_id = models.CharField(max_length=100)
	bw_about = models.CharField(max_length=100,default = "")

	bw_services_heading1 = models.CharField(max_length=100,default = "")
	bw_services_description1 = models.CharField(max_length=100,default = "")

	bw_services_heading2 = models.CharField(max_length=100,default = "")
	bw_services_description2 = models.CharField(max_length=100,default = "")

	bw_services_heading3 = models.CharField(max_length=100,default = "")
	bw_services_description3 = models.CharField(max_length=100,default = "")

	bw_happy_clients = models.CharField(max_length=100,default = "")
	bw_hours = models.CharField(max_length=100,default = "")

	bw_hard_workers = models.CharField(max_length=100,default = "")
	bw_company_description = models.CharField(max_length=100,default = "")
	bw_pricing1 = models.CharField(max_length=100,default = "")
	bw_pricing1_description = models.CharField(max_length=100,default = "")
	bw_pricing2 = models.CharField(max_length=100,default = "")
	bw_pricing2_description = models.CharField(max_length=100,default = "")

	bw_facility1 = models.CharField(max_length=100,default = "")
	bw_facility2 = models.CharField(max_length=100,default = "")
	bw_facility3 = models.CharField(max_length=100,default = "")
	bw_facility4 = models.CharField(max_length=100,default = "")

	bw_testimonial1 = models.CharField(max_length=100,default = "")
	bw_testimonial1_description = models.CharField(max_length=100,default = "")

	bw_testimonial2 = models.CharField(max_length=100,default = "")
	bw_testimonial2_description = models.CharField(max_length=100,default = "")

	bw_testimonial3 = models.CharField(max_length=100,default = "")
	bw_testimonial3_description = models.CharField(max_length=100,default = "")


	bw_testimonial4 = models.CharField(max_length=100,default = "")
	bw_testimonial4_description = models.CharField(max_length=100,default = "")

	bw_testimonial5 = models.CharField(max_length=100,default = "")
	bw_testimonial5_description = models.CharField(max_length=100,default = "")


	bw_location = models.CharField(max_length=100,default = "")
	bw_email = models.CharField(max_length=100,default = "")
	bw_phone = models.CharField(max_length=100,default = "")
	bw_projects = models.CharField(max_length=100,default = "")


	# bw_seimage1 = models.FileField(upload_to="app/static/media/images")
	bw_user_name = models.CharField(max_length=100,default = "")
	bw_user_email = models.CharField(max_length=100,default = "")
	bw_amount = models.CharField(max_length=100,default = "")
	bw_status = models.IntegerField(default=0)
	bw_created_by = models.CharField(max_length=100)
	bw_created_at = models.DateTimeField(auto_now=True, null=True)


class PersonalWebsite(models.Model):
	pw_id = models.AutoField(primary_key=True, unique = True)
	pw_unique_id = models.CharField(max_length=100)
	pw_image = models.ImageField(upload_to="app/static/media/images/" ,default="True")
	pw_name = models.CharField(max_length=100,default = "")
	pw_designation1 = models.CharField(max_length=100,default = "")
	pw_designation2 = models.CharField(max_length=100,default = "")
	pw_designation3 = models.CharField(max_length=100,default = "")

	# bw_slimage1 = models.FileField(upload_to="app/static/media/images")
	# bw_slimage2 = models.FileField(upload_to="app/static/media/images")
	# bw_slimage3 = models.FileField(upload_to="app/static/media/images")
	# bw_slimage4 = models.FileField(upload_to="app/static/media/images")
	# bw_abimage1 = models.FileField(upload_to="app/static/media/images")
	# bw_abimage2 = models.FileField(upload_to="app/static/media/images")
	pw_about = models.CharField(max_length=100,default = "")

	pw_skill1 = models.CharField(max_length=100,default = "")
	pw_skill2 = models.CharField(max_length=100,default = "")
	pw_skill3 = models.CharField(max_length=100,default = "")
	pw_skill4 = models.CharField(max_length=100,default = "")
	pw_skill5 = models.CharField(max_length=100,default = "")
	pw_skill6 = models.CharField(max_length=100,default = "")

	pw_skill1_per = models.CharField(max_length=100,default = "")
	pw_skill2_per = models.CharField(max_length=100,default = "")
	pw_skill3_per = models.CharField(max_length=100,default = "")
	pw_skill4_per = models.CharField(max_length=100,default = "")
	pw_skill5_per = models.CharField(max_length=100,default = "")
	pw_skill6_per = models.CharField(max_length=100,default = "")

	pw_service1 = models.CharField(max_length=100,default = "")
	pw_service2 = models.CharField(max_length=100,default = "")
	pw_service3 = models.CharField(max_length=100,default = "")
	pw_service4 = models.CharField(max_length=100,default = "")
	pw_service5 = models.CharField(max_length=100,default = "")
	pw_service6 = models.CharField(max_length=100,default = "")

	pw_education1 = models.CharField(max_length=100,default = "")
	pw_education2 = models.CharField(max_length=100,default = "")
	pw_education3 = models.CharField(max_length=100,default = "")

	pw_experience1 = models.CharField(max_length=100,default = "")
	pw_experience2 = models.CharField(max_length=100,default = "")
	pw_experience3 = models.CharField(max_length=100,default = "")

	pw_mobile = models.CharField(max_length=100,default = "")
	pw_email = models.CharField(max_length=100,default = "")
	pw_address = models.CharField(max_length=100,default = "")

	pw_company_description = models.CharField(max_length=100,default = "")


	pw_experience_years = models.CharField(max_length=100,default = "")
	pw_freelance = models.CharField(max_length=100,default = "")
	pw_user_name = models.CharField(max_length=100,default = "")
	pw_user_email = models.CharField(max_length=100,default = "")
	pw_amount = models.CharField(max_length=100,default = "")
	# bw_seimage1 = models.FileField(upload_to="app/static/media/images")
	# bw_seimage2 = models.FileField(upload_to="app/static/media/images")
	# bw_services = models.CharField(max_length=100)
	pw_status = models.IntegerField(default=0)
	pw_created_by = models.CharField(max_length=100,default = "")
	pw_created_at = models.DateTimeField(auto_now=True, null=True)




	

