var dataParams;
var bookingInfoDatatale;

function bookingInfoDatataleFunction() {
	if($("#booking_info_table").hasClass('dataTable')) {
		bookingInfoDatatale.ajax.reload();
	} else {
		// Init Datatable
	    bookingInfoDatatale= $('#booking_info_table').DataTable( {
	        "processing": false,
	        "serverSide": true,
	        "draw": 5,
	        "bFilter": false,
	        "bSort" : false,
	        "pagingType": "input",
	        ajax: {
	            url: '/booking-info-report/',
	            type: 'POST',
	            data: function (parameters) {
	            	parameters.order_id = $("#id_order_id").val().trim();
		            parameters.order_status = $("#id_order_status").val();
		            parameters.barcode =  $("#id_barcode").val().trim();
		            parameters.email = $("#id_email").val().trim();
		            var phone_val = $("#id_phone").val().trim();
		            if (phone_val.charAt(0) == 0) {
		            	phone_val = phone_val.substring(1);
		            }
		            parameters.phone = phone_val;
		            parameters.date_from =  $("#id_date_from").val().trim();
		            parameters.date_to = $("#id_date_to").val().trim();
		            dataParams = parameters;
	            },
		        error : function(jqXHR, textStatus, errorThrown) {
		            alert("Error: " + textStatus + ": " + errorThrown);
		        }
	        },
	        columns: [{
	            data: "order_id"
	        }, {
	            data: "order_desc"
	        }, {
	            data: "order_status"
	        }, {
	            data: "desc_transaction"
	        }, {
	            data: "barcode"
	        }, {
	            data: "amount",
	             render: $.fn.dataTable.render.number( ',' )
	        }, {
	            data: "email"
	        }, {
	            data: "phone"
	        }, {
	            data: "created_format"
	        }],
	        columnDefs: [{
				"className": "dt-right", 
				"targets": [5]
			}, {
				"className": "dt-center", 
				"targets": [2]
			}],
			"infoCallback": function( oSettings, iStart, iEnd, iMax, iTotal, sPre ) {
                if(iTotal > 0) {
                    $("#download-btn").prop( "disabled", false);
                } else {
                    $("#download-btn").prop( "disabled", true );
                    iStart = 0;
                }
                return "Showing "+iStart+" to "+iEnd+" of "+ iTotal +" entries";
            }
	    });
	}
}

$(document).ready(function() {
	// Before call ajax then disable search button
	$(document).bind("ajaxSend", function(e, xhr, settings) {
        $("#search-btn").prop( "disabled", true );
    }).bind("ajaxStop", function() {
        $("#search-btn").prop( "disabled", false);
    });

	/*Start Init datepicker*/
	$( "#id_date_from" ).datepicker({
      	changeMonth: true,
      	changeYear: true,
        dateFormat: "dd/mm/yy"
    });
	$( "#id_date_to" ).datepicker({
      	changeMonth: true,
      	changeYear: true,
        dateFormat: "dd/mm/yy"
  	});
  	/*Start Init datepicker*/
  	/*Set current date for from date and to date default*/
	$( "#id_date_from" ).datepicker("setDate", new Date());
  	$( "#id_date_to" ).datepicker("setDate", new Date());

  	 $("#id_date_from").blur(function(){
        $("#id_date_to").trigger('blur');
    })

    $("#id_amount_from").blur(function(){
        $("#id_amount_to").trigger('blur');
    })

    // Add validator
    $.formUtils.addValidator({
        name : 'compare',
        validatorFunction : function(value, $el, config, language, $form) {
            var startDate = $.datepicker.parseDate("dd/mm/yy",$('#id_date_from').val());
            var endDate = $.datepicker.parseDate("dd/mm/yy",$('#id_date_to').val());
   
            if($('#id_date_from').parent().hasClass('has-error') || $('#id_date_from').val() == '' || $('#id_date_to').val() == "") {
                return true;
            }
            return startDate <= endDate;
        },
        errorMessage : 'To Date must be greater than From Date',
        errorMessageKey: 'badEvenNumber'
    });

    // Init form validation
    $.validate({
	    modules : 'sanitize'
	 });

  	/*load data when init page*/
	bookingInfoDatataleFunction();
	// Click search button
	$("#search-btn").click(function() {
		// if form not error then call ajax to get data
		if($(".form-error").length < 1 ) {
			bookingInfoDatataleFunction();
		}
	});

	// Click download button then export to excel
	$("#download-btn").click(function() {
    	$.ajax({
			url: '/booking-info-export-to-excel/',
			type: 'POST',
			data: dataParams,
			success: function (data) {
				$(".dl-excel").attr("href", data.uri)[0].click();  
			},
	        error : function(jqXHR, textStatus, errorThrown) {
	            alert("Error: " + textStatus + ": " + errorThrown);
	        }
  		});
    });
} );