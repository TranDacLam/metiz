
		
	function buy(id, formkey) {
		/*
		* Check customer availability
		*/
		var login = '';
		if (login == 1) {
			$j.ajax({
				type: 'POST',
				url: '#',
				data: {id : id, form_key : formkey},
				beforeSend: function(){
					$j('#loading-mask').show();
				}
							}).done(function(response) {
				if (response.success == 1) {
					// var msg = response.message;
					// if (Object.isArray(msg)) {
						// msg = msg.join("\n").stripTags().toString();
					// }
					
					// if (msg) {
						// alert(msg);
					// }
					
					location.href = encodeURI('#');
					return;
				} else {
					var msg = response.error;
					if (Object.isArray(msg)) {
						msg = msg.join("\n").stripTags().toString();
					}
					
					if (msg) {
						alert(msg);
					}
				}
				
				$j('#loading-mask').hide();
			})
		} else {
			location.href = encodeURI('#');
			return;
		}
	}
		
		
	var phone = '2124771050',
	formatted = phone.substr(0, 3) + '****' + phone.substr(phone.length-3,3);
		  