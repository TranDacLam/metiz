$(document).ready(function() {
    // get param query url
    var urlParams;
    (window.onpopstate = function () {
        var match,
            pl     = /\+/g,  // Regex for replacing addition symbol with a space
            search = /([^&=]+)=?([^&]*)/g,
            decode = function (s) { return decodeURIComponent(s.replace(pl, " ")); },
            query  = window.location.search.substring(1);

        urlParams = {};
        while (match = search.exec(query))
           urlParams[decode(match[1])] = decode(match[2]);
    })();
    
    // add active for tab from tag footer redirect page posts 
    var kq_post = urlParams['key_query'];
    $('.post-detail-metiz li[data-post-detail="'+ kq_post +'"]').addClass('active')

    // active and ajax in page posts
    $('.post-detail-metiz li').click(function(e){
        e.preventDefault();
        post_detail_kq = $(this).attr('data-post-detail');
        $.ajax({
            url: '?key_query=' + post_detail_kq,
            type: 'get',
            dataType: 'json',
            context: this,
        })
        .done(function(response) {
            $('.post-detail-metiz li').removeClass('active');
            $(this).addClass('active');
            $('.title-about-metiz').html('<h1>'+ response.name +'</h1>');
            $('.content-seperator').html('<p>'+ response.content +'</p>');
        })
        .fail(function() {
            alert("error");
        })
    });
});