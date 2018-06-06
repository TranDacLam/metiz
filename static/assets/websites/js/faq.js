$(document).ready(function() {
    changeArrowQuestion();
});

// Change arrow down/up when click question
function changeArrowQuestion(){
    $('.question-toggle').on('click', function(){
        $('.question-toggle').find('span').removeClass('fa-chevron-circle-up, fa-chevron-circle-down');
        $('.question-toggle').find('span').addClass('fa-chevron-circle-down');
        if($(this).hasClass('collapsed')){
            $(this).find('span').removeClass('fa-chevron-circle-down');
            $(this).find('span').addClass('fa-chevron-circle-up');
        }else{
            $(this).find('span').removeClass('fa-chevron-circle-up');
            $(this).find('span').addClass('fa-chevron-circle-down');
        }
    });
}