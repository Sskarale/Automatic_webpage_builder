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
    //verification
     
  var formData = new FormData();
  


  formData.append("txtAbout", $("#txtAbout").val());

  formData.append("businessWebsite", $("#businessWebsite").val());

  formData.append("txtServicesHeading1", $("#txtServicesHeading1").val());
  formData.append("txtServicesDescription1", $("#txtServicesDescription1").val());
  formData.append("txtServicesHeading2", $("#txtServicesHeading2").val());
  formData.append("txtServicesDescription2", $("#txtServicesDescription2").val());
  formData.append("txtServicesHeading3", $("#txtServicesHeading3").val());
  formData.append("txtServicesDescription3", $("#txtServicesDescription3").val());

  formData.append("txtHappyClients", $("#txtHappyClients").val());
  formData.append("txtProjects", $("#txtProjects").val());
  formData.append("txtHoursSupport", $("#txtHoursSupport").val());
  formData.append("txtHardWorkers", $("#txtHardWorkers").val());
  formData.append("txtCompanyDescription", $("#txtCompanyDescription").val());


  formData.append("txtPricing1", $("#txtPricing1").val());
  formData.append("txtPricing1Description", $("#txtPricing1Description").val());
  formData.append("txtPricing2", $("#txtPricing2").val());
  formData.append("txtPricing2Description", $("#txtPricing2Description").val());

  formData.append("txtFacility1", $("#txtFacility1").val());
  formData.append("txtFacility2", $("#txtFacility2").val());
  formData.append("txtFacility3", $("#txtFacility3").val());
  formData.append("txtFacility4", $("#txtFacility4").val());

  formData.append("txtTestimonial1", $("#txtTestimonial1").val());
  formData.append("txtTestimonial1Description", $("#txtTestimonial1Description").val());
  formData.append("txtTestimonial2", $("#txtTestimonial2").val());
  formData.append("txtTestimonial2Description", $("#txtTestimonial2Description").val());
  formData.append("txtTestimonial3", $("#txtTestimonial3").val());
  formData.append("txtTestimonial3Description", $("#txtTestimonial3Description").val());
    formData.append("txtTestimonial4", $("#txtTestimonial4").val());
  formData.append("txtTestimonial4Description", $("#txtTestimonial4Description").val());
    formData.append("txtTestimonial5", $("#txtTestimonial5").val());
  formData.append("txtTestimonial5Description", $("#txtTestimonial5Description").val());

  formData.append("txtLocation", $("#txtLocation").val());
  formData.append("txtEmail", $("#txtEmail").val());
  formData.append("txtPhoneNo", $("#txtPhoneNo").val());






  // formData.append("sliderImg1", lclSilderImage1);
  // formData.append("sliderImg2", lclSilderImage2);
  // formData.append("sliderImg3", lclSilderImage3);
  // formData.append("sliderImg4", lclSilderImage4);
  // formData.append("aboutImg1", lclAboutImage1);
  // formData.append("aboutImg2", lclAboutImage2);
  // formData.append("servicesImg1", lclServicesImage1);
  // formData.append("servicesImg2", lclServicesImage2);
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "add");

  // var table = $("#dataTables-example").DataTable();

  $.ajax({
    beforeSend: function () {
      $(".btn .spinner-border").show();
      $("#btn_add").attr("disabled", true);
    },
    url: "/business_website/",
    type: "POST",
    // headers: {'X-CSRFToken': '{{ csrf_token }}'},
    data: formData,
    processData: false,
    contentType: false,
    success: function (result) {

        alert(" Added Successfully");
        payment(5000, result[0].bw_id,result[0].bw_unique_id);

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

  // alert(uniqueId);

   var totalAmount = amount;
   var options = {
   "key": "rzp_test_aKbqVbQ3Ciq9KZ",
   // rzp_live_fAt71isKlJSzhX
   "amount": (totalAmount*100), // 2000 paise = INR 20
   "name": "Website",
   "description": "Payment",
   "handler": function (response) {
    if(uniqueId == 1){
    window.open("/first_business_details1/?id="+id,'_blank')

  }else{
    window.open("/second_business_details1/?id="+id,'_blank')

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

