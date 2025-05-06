function validateEmail(paramEmailID) {
    var filter = /^[0-9a-z.]+\@[a-z0-9]+\.[a-zA-z0-9]{2,4}$/;
  
    if (filter.test(paramEmailID)) {
      return true;
    } else {
      return false;
    }
  }
  
  // alert("Hello");

  
  $("#btn_add").click(function (e) {
   

  var formData = new FormData();


  formData.append("lclImage","0");
  formData.append("personalWebsite", $("#personalWebsite").val());
  formData.append("txtName1", $("#txtName1").val());
  formData.append("txtDesignation1", $("#txtDesignation1").val());
  formData.append("txtDesignation2", $("#txtDesignation2").val());
  formData.append("txtDesignation3", $("#txtDesignation3").val());
  formData.append("txtAbout", $("#txtAbout").val());
  formData.append("txtSkill1", $("#txtSkill1").val());
  formData.append("txtSkill2", $("#txtSkill2").val());
  formData.append("txtSkill3", $("#txtSkill3").val());
  formData.append("txtSkill4", $("#txtSkill4").val());
  formData.append("txtSkill5", $("#txtSkill5").val());
  formData.append("txtSkill6", $("#txtSkill6").val());
  formData.append("txtService1", $("#txtService1").val());
  formData.append("txtService2", $("#txtService2").val());
  formData.append("txtService3", $("#txtService3").val());
  formData.append("txtService4", $("#txtService4").val());
  formData.append("txtService5", $("#txtService5").val());
  formData.append("txtService6", $("#txtService6").val());
  formData.append("txtEducation1", $("#txtEducation1").val());
  formData.append("txtEducation2", $("#txtEducation2").val());
  formData.append("txtEducation3", $("#txtEducation3").val());
  formData.append("txtExperience1", $("#txtExperience1").val());
  formData.append("txtExperience2", $("#txtExperience2").val());
  formData.append("txtExperience3", $("#txtExperience3").val());
  formData.append("txtMobile", $("#txtMobile").val());
  formData.append("txtEmail", $("#txtEmail").val());
  formData.append("txtAddress", $("#txtAddress").val());
  formData.append("txtExperienceCount", $("#txtExperienceCount").val());
  formData.append("txtFreelance", $("#txtFreelance").val());
  


  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "add");

  // var table = $("#dataTables-example").DataTable();

  $.ajax({
    beforeSend: function () {
      $(".btn .spinner-border").show();
      $("#btn_add").attr("disabled", true);
    },
    url: "/personal_website_details/",
    type: "POST",
    // headers: {'X-CSRFToken': '{{ csrf_token }}'},
    data: formData,
    processData: false,
    contentType: false,
    success: function (result) {

        alert(" Added Successfully");
        payment(5000, result[0].pw_id,result[0].pw_unique_id);



    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {
      $(".btn .spinner-border").hide();
      $("#btn_add").attr("disabled", false);
    },
  });
});




  

 function payment(amount, id,uniqueId) {

   var totalAmount = amount;
   var options = {
   "key": "rzp_test_aKbqVbQ3Ciq9KZ",
   // rzp_live_fAt71isKlJSzhX
   "amount": (totalAmount*100), // 2000 paise = INR 20
   "name": "Website",
   "description": "Payment",
   "handler": function (response) {
    if(uniqueId == 1){
     window.open("/first_personal_details1/?id="+id,'_blank')

  }else{
     window.open("/second_personal_details1/?id="+id,'_blank')

  }
    // resumeDetails1(id);

   },
   "prefill": {
       "contact": $("#txtMobileNo").val(),
       "email":   $("#txtEmail").val(),
   },
    
   "theme": {
       "color": "#4caf50"
   }
 };
 var rzp1 = new Razorpay(options);
 rzp1.open();
 // preventDefault();
 // });

}
