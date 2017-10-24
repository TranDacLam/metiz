$(document).ready(function() {
    //  load more
    // data demo
    var list_news = [
        {
            "id": 1,
            "apply_date": "Ngày 20 tháng 11 năm 2017",
            "image": "/assets/websites/images/news/Kingsman_350_X_495.jpg",
        },
        {
            "id": 2,
            "apply_date": "Ngày 15 tháng 11 năm 2017",
            "image": "/assets/websites/images/news/Kingsman_350_X_495.jpg",
        }
    ];

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
            $(this).attr('data-page',page + 1);
            var html = '';

            // for from data reponse set function movie_showing(movie)
            $.each(list_news, function(key, value) {
                html += movie_showing(value);
            });
            
            $('.news-custom>ul').append(html);

            $(this).prop('disabled', false);
        })
        .fail(function() {
            alert("error");
        });
    });
});