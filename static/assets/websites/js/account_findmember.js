	
		var theForm = new VarienForm('form-validate', true);
		// xử lý sự kiện khi nhập ngày tháng năm sinh (dòng 4-13)
		$j( document ).ready(function() {
			$j('#birthday').bind('keyup','keydown', function(event) {
			var inputLength = event.target.value.length;
			if(inputLength === 2 || inputLength === 5){
				var thisVal = event.target.value;
				thisVal += '/';
				$j(event.target).val(thisVal);
			}
		})
		});
		
		//trỏ đến trang account_forgot_password (từ dòng 16-21)
		function forgotpasswordf()
		{
			//var url = e.target.parentElement.action;
			var url = '#';
			window.location = url;
		}
		//trỏ đến trang account_login (từ dòng 23-28)
		function loginf()
		{
			//var url = e.target.parentElement.action;
			var url = '#';
			window.location = url;
		}

		// Hàm tìm account(từ dòng 31-62)
		function findaccount()
		{
			var f_name = $j.trim($j('input[name=\'first_name\']').val());
			var l_name = $j.trim($j('input[name=\'last_name\']').val());
			var b_day = $j.trim($j('input[name=\'birthday\']').val());
			var online_id = $j.trim($j('input[name=\'online_id\']').val());
			if(f_name !='' && l_name !='' || b_day!='' || online_id!=''){
				
				$j.ajax({
					type: 'POST',
					url: '#',
					data: {first_name : f_name, last_name :  l_name , birthday : b_day, online_id : online_id},
					beforeSend: function(){
						$j('#loading-mask').show();
						$j('#data_return').addClass('cgv-nodisplay');
					}
				}).done(function(result) {
					$j('#loading-mask').hide();
					if(result.code == 200) {
						$j('#data_return').removeClass('cgv-nodisplay');
						$j('.yourname').html(l_name + ' ' + f_name);
						$j('.youremail').html(result.data.EMAIL);
						$j('.yourid').html(result.data.HP_ID);
					}
					else {
						alert(result.error);
					}
				});
			}else{
				alert('Vui lòng nhập đúng thông tin');
			}
		}
	