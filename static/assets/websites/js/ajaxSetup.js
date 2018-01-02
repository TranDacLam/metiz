
$(document).ready(function() {
    var csrftoken = getCookie('csrftoken');
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain:true, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                csrftoken = getCookie('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    }); 
    $.ajaxSetup({ cache: false });
    
    // FB init function
    FB.init({
        appId: fbAppId,
        version: 'v2.11',
        cookie     : true,
        xfbml      : true
    });

    (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = 'https://connect.facebook.net/vi_VN/sdk.js';
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));
});