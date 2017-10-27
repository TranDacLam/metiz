$(document).ready(function() {
    //  load more
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
                                                    +'<h3 class="glyphicon glyphicon-calendar">'
                                                    +'<h4>'+ newoffer.apply_date +'</h4></h3>'
                                                +'</div>'
                                            +'</div>'
                                        +'</div>'
                                   +'</div>'
                                +'</div>'
                            +'</div>'
                        +'</div>'
                    +'</a>'
                +'</li>';
    }

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
            if(response.length < 12){
                $('.news-custom>.text-center button').remove();
            }
            
            $(this).attr('data-page',page + 1);
            var html = '';

            // for from data reponse set function movie_showing(movie)
            $.each(response, function(key, value) {
                html += movie_showing(value);
            });
            
            $('.news-custom>ul').append(html);

            $(this).prop('disabled', false);
        })
        .fail(function() {
            displayMsg();
            $('.msg-result-js').html(msgResult("Error load more news", "danger"));
        });
    });
});