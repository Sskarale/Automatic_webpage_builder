$("#btn_submit").click(function() {
	if($("#bride").val() == "") {
		alert("Please Enter Bride Name");
		$("#bride").focus();
		return false;
	}
	if($("#groom").val() == "") {
		alert("Please your Groom Name");
		$("#groom").focus();
		return false;
	}
	if($("#date").val() == "") {
		alert("Please Enter your Date");
		$("#date").focus();
		return false;
	}
	if($("#time").val() == "") {
		alert("Please Enter your Time");
		$("#time").focus();
		return false;

	}
	if($("#venue").val() == "") {
		alert("Please select your venue");
		$("#venue").focus();
		return false;
	}
	
	let formData = new FormData();

	var lclFile = document.getElementById("InputUploadFile");
  	// lclImage = lclFile.files[0];
  
	  formData.append("bride", $("#bride").val());
	  // formData.append("InputUploadFile",lclImage);
	  formData.append("groom", $("#groom").val());
	  formData.append("date", $("#date").val());
	  formData.append("time", $("#time").val());
	  formData.append("venue", $("#venue").val());
	  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
	  formData.append("action", "add");

	  // console.log(typeof(formData));

	$.ajax({
	    beforeSend: function () {
	      $(".btn .spinner-border").show();
	      $("#btn_submit").attr("disabled", true);
	    },
	    url: "/webinvitation1/",
	    type: "POST",
	    data: formData,
	    processData: false,
	    contentType: false,
	    success: function (result) {

	     $("#visitpayment").show();
	    	$("#visitcard").hide();
	    	$("#txtName").text($("#bride").val());
	    	$("#txtName1").text($("#groom").val());
	    	$("#txtDate").text($("#date").val());
	    	$("#txtTime").text($("#time").val());
	    	$("#txtVenue").text($("#txtVenue").val());
	      
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
   let amount = 200;
          
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

