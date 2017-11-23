$(document).ready(function() {
    function getDate(applyDate){
        return applyDate.replace(/([0-9]{4})\-([0-9]{2})\-([0-9]{2})/g, '$3/$2/$1');
    }

    // *** LOAD MORE ***
    // movie html, need set data for movie html in movie_showing(movie)
    function movie_showing(newoffer){
        return  '<li class="item last">'
                    +'<a href="/new/detail/'+ newoffer.id +'">'
                        +'<div class="product-poster"">'
                            +'<div class="fun-new-offer">'
                                +'<div class="content-new-offer">'
                                   +'<div class="colum-left-new-offer">'
                                        +'<div class="poster-small-new-offer">'
                                            +'<img alt="" src="/media/'+ newoffer.image +'">'
                                            +'<div class="colum-right-new-offer">'
                                                +'<div class="format-new-offer release-day-new-offer">'
                                                    +'<h4>'+ getDate(newoffer.apply_date) 
                                                    +' - '+ check_end_date(newoffer) +'</h4>'
                                                +'</div>'
                                                +'<h2 class="product-name">'+ newoffer.name +'</h2>'
                                            +'</div>'
                                        +'</div>'
                                   +'</div>'
                                +'</div>'
                            +'</div>'
                        +'</div>'
                    +'</a>'
                +'</li>';
    }

    // Check time end_date of new 
    function check_end_date(newoffer){
        if(newoffer.end_date){
            return getDate(newoffer.end_date);
        }
        return "Áp Dụng Liên Tục";
    }

    // Check list news condition if < 12 remove button load more
    var coutNew = parseInt($('.load-more').attr('data-count-news'));
    if(coutNew < 12){
        $('.news-custom>.text-center button').remove();
    }

    $('#load-more-news').on('click', function(e){
        e.preventDefault();
        $(this).prop('disabled', true);
        var page = parseInt($(this).attr('data-page'));
        $.ajax({
            url: '/news/',
            type: 'get',
            data: {
                'page': page,
            },
            crossDomain:false,
            context: this,
        })
        .done(function(response) {
            // Check total page let remove button load more
            if(page >= response.total_page){
                $('.news-custom>.text-center button').remove();
            }
            
            // increase the value page +1
            $(this).attr('data-page',page + 1);
            var html = '';

            // for from data reponse set function movie_showing(movie)
            $.each(response.data, function(key, value) {
                html += movie_showing(value);
            });
            
            $('.news-custom>ul').append(html);

            $(this).prop('disabled', false);
        })
        .fail(function() {
            displayMsg();
            if(error.status == 400){
                $('.msg-result-js').html(msgResult(error.responseJSON.message, "danger"));
            }else{
                $('.msg-result-js').html(msgResult("Error load more news", "danger"));
            }
        });
    });
});