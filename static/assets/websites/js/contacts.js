$(document).ready(function() {
    var val_required = 'Trường này là bắt buộc';
    $("#contactForm").validate({
        rules: {
            name: { 
                required: true,
            },
            email:{
                required: true,
            },
            comment:{
                required: true,
            }
        },
        messages:{
            name: {
                required: val_required,
            },
            email: {
                required: val_required,
            },
            comment:{
                required: val_required,
            },
        }
    });
});