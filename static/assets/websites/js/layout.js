$(document).ready(function() {
    // handle double click submit 
    $("form").submit(function() {
        // submit more than once return false
        $(this).submit(function() {
            return false;
        });
        // submit once return true
        return true;    
    });
});