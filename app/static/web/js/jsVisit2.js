$("#btn_submit").click(function() {
	if($("#InputName").val() == "") {
		alert("Please Enter Name");
		$("#InputName").focus();
		return false;
	}
	if($("#InputEmail1").val() == "") {
		alert("Please your Email");
		$("#InputEmail1").focus();
		return false;
	}
	if($("#InputAlterNumber").val() == "") {
		alert("Please Enter your Phone number");
		$("#InputAlterNumber").focus();
		return false;
	}
	if($("#InputAlterNumber1").val() == "") {
		alert("Please Enter your Phone number");
		$("#InputAlterNumber1").focus();
		return false;

	}
	if($("#InputUploadFile").val() == "") {
		alert("Please select your InputUpload Image");
		$("#InputUploadFile").focus();
		return false;
	}
	if($("#InputAddress").val() == "") {
		alert("Please select your Address");
		$("#InputAddress").focus();
		return false;
	}
	

		let formData = new FormData();

		var lclFile = document.getElementById("InputUploadFile");
  	lclImage = lclFile.files[0];
  
	  formData.append("InputName", $("#InputName").val());
	  formData.append("InputUploadFile",lclImage);
	  formData.append("InputEmail1", $("#InputEmail1").val());
	  formData.append("InputAlterNumber", $("#InputAlterNumber").val());
	  formData.append("InputAlterNumber1", $("#InputAlterNumber1").val());
	  formData.append("InputAddress", $("#InputAddress").val());
	  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
	  formData.append("action", "add");

	  // console.log(typeof(formData));

	$.ajax({
	    beforeSend: function () {
	      $(".btn .spinner-border").show();
	      $("#btn_submit").attr("disabled", true);
	    },
	    url: "/webvisit2/",
	    type: "POST",
	    data: formData,
	    processData: false,
	    contentType: false,
	    success: function (result) {

	        $("#visitpayment").show();
	    	$("#visitcard").hide();
	    	$("#visitingName").text($("#InputName").val());
	    	$("#phone").text($("#InputAlterNumber").val());
	    	$("#AlterNumber").text($("#InputAlterNumber1").val());
	    	$("#email").text($("#InputEmail1").val());
	    	$("#address").text($("#InputAddress").val());
	    	let img = result.substring(3);
	    	$("#img-profile").attr('src', img);
	      
	    },
	    error: function (request, error) {
	      console.error(error);
	    },
	    complete: function () {
	      $(".btn .spinner-border").hide();
	      $("#btn_submit").attr("disabled", false);
	    },
	  });

});

$("#btnPayment").click(function (e) {
           //verification
   let amount = 100;
          
   var formData = new FormData();
   
   formData.append("visit1", $("#visit1").val());
   formData.append("amount", amount);

   formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
     $.ajax({
     beforeSend: function () {
       $(".btn .spinner-border").show();
       $("#btn_add").attr("disabled", true);
     },
     url: "/visit_payment/",
     type: "POST",
     // headers: {'X-CSRFToken': '{{ csrf_token }}'},
     data: formData,
     processData: false,
     contentType: false,
     success: function (result) {

         payment(100);
       
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

 function payment(amount) {

   var totalAmount = amount;
   var options = {
   "key": "rzp_test_aKbqVbQ3Ciq9KZ",
   // rzp_live_fAt71isKlJSzhX
   "amount": (totalAmount*100), // 2000 paise = INR 20
   "name": "Visiting Card",
   "description": "Payment",
   "handler": function (response) {
    // alert(response.razorpay_payment_id);
    // submitRegDetails(response.razorpay_payment_id);
    // window.location.href = '/pay_success/'
    // alert(response);
    $(".downloadPdf").show();
    $("#btnPayment").hide();

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