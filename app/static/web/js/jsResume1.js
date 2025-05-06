$("#btn_submit").click(function() {
	if($("#InputAboutMe").val() == "") {
		alert("Please Enter About");
		$("#InputAboutMe").focus();
		return false;
	}
	if($("#InputUploadFile").val() == "") {
		alert("Please Upload-File");
		$("#InputUploadFile").focus();
		return false;
	}
	if($("#InputEduction1").val() == "") {
		alert("Please Enter your Eduction-1");
		$("#InputEduction1").focus();
		return false;

	}
	if($("#InputEduction2").val() == "") {
		alert("Please Enter your Eduction-2");
		$("#InputEduction2").focus();
		return false;
	}
	if($("#InputEduction3").val() == "") {
		alert("Please select your Eduction-3");
		$("#InputEduction3").focus();
		return false;
	}
	if($("#InputEduction4").val() == "") {
		alert("Please select your Eduction-4");
		$("#InputEduction4").focus();
		return false;
	}
	if($("#InputSkill1").val() == "") {
		alert("Please Enter your Eduction-1");
		$("#InputSkill1").focus();
		return false;

	}
	if($("#InputSkill2").val() == "") {
		alert("Please Enter your Eduction-2");
		$("#InputSkill2").focus();
		return false;
	}
	if($("#InputSkill3").val() == "") {
		alert("Please select your Eduction-3");
		$("#InputSkill3").focus();
		return false;
	}
	if($("#InputSkill4").val() == "") {
		alert("Please select your Eduction-4");
		$("#InputSkill4").focus();
		return false;
	}
	if($("#InputExperience1").val() == "") {
		alert("Please Enter your Eduction-1");
		$("#InputExperience1").focus();
		return false;

	}
	if($("#InputExperience2").val() == "") {
		alert("Please Enter your Eduction-2");
		$("#InputExperience2").focus();
		return false;
	}
	if($("#InputExperience3").val() == "") {
		alert("Please select your Eduction-3");
		$("#InputExperience3").focus();
		return false;
	}
	if($("#InputExperience4").val() == "") {
		alert("Please select your Eduction-4");
		$("#InputExperience4").focus();
		return false;
	}
	if($("#InputName").val() == "") {
		alert("Please select your Name");
		$("#InputName").focus();
		return false;
	}
	if($("#InputJobTitle").val() == "") {
		alert("Please select your Job-Title");
		$("#InputJobTitle").focus();
		return false;
	}
	if($("#InputEmail").val() == "") {
		alert("Please select your Email");
		$("#InputEmail").focus();
		return false;
	}
	if($("#InputAlterNumber").val() == "") {
		alert("Please select your Phone number");
		$("#InputAlterNumber").focus();
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
  
	  formData.append("InputAboutMe", $("#InputAboutMe").val());
	  formData.append("InputUploadFile",lclImage);
	  formData.append("InputEduction1", $("#InputEduction1").val());
	  formData.append("InputEduction2", $("#InputEduction2").val());
	  formData.append("InputEduction3", $("#InputEduction3").val());
	  formData.append("InputEduction4", $("#InputEduction4").val());

	  formData.append("InputSkill1", $("#InputSkill1").val());
	  formData.append("InputSkill2", $("#InputSkill2").val());
	  formData.append("InputSkill3", $("#InputSkill3").val());
	  formData.append("InputSkill4", $("#InputSkill4").val());

	  formData.append("InputExperience1", $("#InputExperience1").val());
	  formData.append("InputExperience2", $("#InputExperience2").val());
	  formData.append("InputExperience3", $("#InputExperience3").val());
	  formData.append("InputExperience4", $("#InputExperience4").val());
	  formData.append("InputName", $("#InputName").val());
	  formData.append("InputJobTitle", $("#InputJobTitle").val());
	  formData.append("InputEmail", $("#InputEmail").val());
	  formData.append("InputAlterNumber", $("#InputAlterNumber").val());
	  formData.append("InputAddress", $("#InputAddress").val());
	  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
	  formData.append("action", "add");

	  // console.log(typeof(formData));

	$.ajax({
	    beforeSend: function () {
	      $(".btn .spinner-border").show();
	      $("#btn_submit").attr("disabled", true);
	    },
	    url: "/webresume1/",
	    type: "POST",
	    data: formData,
	    processData: false,
	    contentType: false,
	    success: function (result) {

	      alert(" Added Successfully");

	      payment(300, result);
	      // location.reload();
	      $("#btn_submit").modal('hide');
	      
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


 function payment(amount, id) {

   var totalAmount = amount;
   var options = {
   "key": "rzp_test_aKbqVbQ3Ciq9KZ",
   // rzp_live_fAt71isKlJSzhX
   "amount": (totalAmount*100), // 2000 paise = INR 20
   "name": "Visiting Card",
   "description": "Payment",
   "handler": function (response) {
    window.location = "/resume_details1/?id="+id
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



// $("#btn_submit").click(function() {
// 	if($("#InputName").val() == "") {
// 		alert("Please Enter Name");
// 		$("#InputName").focus();
// 		return false;
// 	}

// 	if($("#InputEmail1").val() == "") {
// 		alert("Please Enter Email");
// 		$("#InputEmail1").focus();
// 		return false;
// 	}
// 	if($("#InputAlterNumber").val() == "") {
// 		alert("Please Enter your Mobile number");
// 		$("#InputAlterNumber").focus();
// 		return false;

// 	}
// 	if($("#InputAddress").val() == "") {
// 		alert("Please Enter your Address");
// 		$("#InputAddress").focus();
// 		return false;
// 	}
// 	if($("#InputEduction").val() == "") {
// 		alert("Please select your Eduction");
// 		$("#InputEduction").focus();
// 		return false;
// 	}
// 	if($("#InputSkills").val() == "") {
// 		alert("Please select your Skills");
// 		$("#InputSkills").focus();
// 		return false;
// 	}
// 	if($("#InputUploadFile").val() == "") {
// 		alert("Please select your Upload-file");
// 		$("#InputUploadFile").focus();
// 		return false;
// 	}

// 		let formData = new FormData();
  
	 
// 	  formData.append("InputName", $("#InputName").val());
// 	  formData.append("InputEmail1", $("#InputEmail1").val());
// 	  formData.append("InputAlterNumber", $("#InputAlterNumber").val());
// 	  formData.append("InputAddress", $("#InputAddress").val());
// 	  formData.append("InputEduction", $("#InputEduction").val());
// 	  formData.append("InputSkills", $("#InputSkills").val());
// 	  formData.append("InputUploadFile", $("#InputUploadFile").val());
// 	  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
// 	  formData.append("action", "update");


// 	  // console.log(typeof(formData));

// 	$.ajax({
// 	    beforeSend: function () {
// 	      $(".btn .spinner-border").show();
// 	      $("#btn_add").attr("disabled", true);
// 	    },
// 	    url: "/webresume1/",
// 	    type: "POST",
// 	    data: formData,
// 	    processData: false,
// 	    contentType: false,
// 	    success: function (result) {

// 	      alert("Admin Updated Successfully");
// 	      location.reload();
// 	      $("#add_modal").modal('hide');
	      
// 	    },
// 	    error: function (request, error) {
// 	      console.error(error);
// 	    },
// 	    complete: function () {
// 	      $(".btn .spinner-border").hide();
// 	      $("#btn_add").attr("disabled", false);
// 	    },
// 	  });

// });

// $("#btn_delete").click(function() {--------

// 		let formData = new FormData();
  
// 	  formData.append("id", $("#delete_id").val());
// 	  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
// 	  formData.append("action", "delete");

// 	  // console.log(typeof(formData));

// 	$.ajax({
// 	    beforeSend: function () {
// 	      $(".btn .spinner-border").show();
// 	      $("#btn_add").attr("disabled", true);
// 	    },
// 	    url: "/webresume1/",
// 	    type: "POST",
// 	    data: formData,
// 	    processData: false,
// 	    contentType: false,
// 	    success: function (result) {

// 	      alert("Admin Deleted Successfully");
// 	      location.reload();
// 	      $("#add_modal").modal('hide');
	      
// 	    },
// 	    error: function (request, error) {
// 	      console.error(error);
// 	    },
// 	    complete: function () {
// 	      $(".btn .spinner-border").hide();
// 	      $("#btn_add").attr("disabled", false);
// 	    },
// 	  });

// });

// function getData() {
//   // alert("1");
//   var formData = new FormData();
//   formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
//   formData.append("action", "getData");

//   $.ajax({

//       url: "/webresume1/",
//       type: "POST",
//       data: formData,
//       processData: false,
//       contentType: false,
//       success: function (response) {
//         $("#tableData tr:gt(0)").remove();
//         for(var i = 0; i < response.length; i++) {
//           var j = i + 1;
//           $("#tableData").append('<tr><td>'+j+
//           	'</td><td style="display: none;">'+response[i].re_id+
//           	'</td><td>'+response[i].re_name+
//           	'</td><td>'+response[i].re_mobile+
//           	'</td><td>'+response[i].re_email+
//           	'</td><td>'+response[i].re_eduction+
//           	'</td><td>'+response[i].re_address+
//           	'</td><td>'+response[i].re_skill+
//           	'</td><td><div class="d-flex" style="justify-content: space-evenly;">'+
//           	'<a href="javascript:void(0);" id="edit_row" title="View/Edit" data-toggle="modal" data-target="#edit_modal" class="text-primary" onClick="getRowsUpdate();"> <i class="fa fa-edit"></i></a>'+
//           	'<a href="javascript:void(0);" title="Delete" data-toggle="modal" data-target="#delete_modal" class="text-danger" id="delete_row" onClick="getRowsDelete();"> <i class="far fa-trash-alt"></i></a></div></td></tr>');
//         }
//       },
//       error: function (request, error) {
//         console.error(error);
//       },
//       complete: function () {

//       },
//     });

// }

// getData();


// function getRowsUpdate() {
//   $("#tableData tr").click(function() {
//       var currentRow = $(this).closest("tr");
//       var lclID = currentRow.find("td:eq(1)").text();
//       var lclName = currentRow.find("td:eq(2)").text();
//       var lclEmail = currentRow.find("td:eq(4)").text();
//       var lclEduction = currentRow.find("td:eq(3)").text();
//       var lclAddress = currentRow.find("td:eq(5)").text();
//       var lclSkill = currentRow.find("td:eq(6)").text();
//       // alert(lclName);
//       $("#txtName1").val(lclName);
//       $("#txtEmail1").val(lclEmail);
//       $("#txtMobileNo1").val(lclMobile);
//       $("#selRole1").val(lclRole);
//       $("#edit_id").val(lclID);

//       $("#edit_modal").modal('show');

//   });
// }


// function getRowsDelete() {
//   $("#tableData tr").click(function() {
//       var currentRow = $(this).closest("tr");
//       var lclID = currentRow.find("td:eq(1)").text();
//       // alert(lclID);
//       $("#delete_id").val(lclID);
//       $("#delete_modal").modal('show');

//   });
// }