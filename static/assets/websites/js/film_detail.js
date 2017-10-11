$(document).ready(function() {
    function getId(url) {
        var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
        var match = url.match(regExp);

        if (match && match[2].length == 11) {
            return match[2];
        } else {
            return 'error';
        }
    }
    var youtubeurl = $('#trailer-film-detail').attr('data-youtube');
    yturltoken = getId(youtubeurl);
    $('#trailer-film-detail').html('<iframe width="560" height="315" src="//www.youtube.com/embed/' + yturltoken + '" frameborder="0" allowfullscreen></iframe>');
});