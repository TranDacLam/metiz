$(document).ready(function() {
	history.pushState(null, null, location.href);
    window.onpopstate = function () {
        $("#back_warning").modal('show');
        history.go(1);
    };
})
