$(document).ready(function() {
    // popup mutil image "Goi Thieu Metiz"
    $('.popup-gallery').magnificPopup({
        delegate: 'img',
        type: 'image',
        tLoading: 'Đang tải ảnh #%curr%...',
        mainClass: 'mfp-img-mobile',
        gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0,1] // Will preload 0 - before current, and 1 after the current image
        },
        image: {
            tError: 'Lỗi tải ảnh.'
        },
        callbacks: {
            elementParse: function(qw) {
                qw.src = qw.el.attr('src');
            }
        }
    });

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
            crossDomain:false,
            context: this,
        })
        .done(function(response) {
            $('.post-detail-metiz li').removeClass('active');
            $(this).addClass('active');
            $('.title-about-metiz').html('<h1>'+ response.name +'</h1>');
            $('.content-seperator').html('<p>'+ response.content +'</p>');

            // popup mutil image "Goi Thieu Metiz" when use ajax
            $('.popup-gallery').magnificPopup({
                delegate: 'img',
                type: 'image',
                tLoading: 'Đang tải ảnh #%curr%...',
                mainClass: 'mfp-img-mobile',
                gallery: {
                    enabled: true,
                    navigateByImgClick: true,
                    preload: [0,1] // Will preload 0 - before current, and 1 after the current image
                },
                image: {
                    tError: 'Lỗi tải ảnh.'
                },
                callbacks: {
                    elementParse: function(qw) {
                        qw.src = qw.el.attr('src');
                    }
                }
            });
        })
        .fail(function() {
            alert("error");
        })
    });
});