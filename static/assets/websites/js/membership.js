
$j(document).ready(function(){
    $j( ".cgv-membership" ).tabs();
    $j( ".accordion" ).accordion({
        heightStyle: "content"
    });
    
    $j('.cgv-membership > ul li').click(function(event) {
        if (!$j(event.target).is('a')) {
            $j(this).find("a").trigger('click');
        }
    });
    
    var url = window.location.href;
    var arr = url.split('?');
    
    $j('#'+arr[1]).click();
    
    $j('.cgv-membership > ul').find('a').each(function() {
        if($j(this).attr('href') == '#'+$j('#'+arr[1]).parents('.lyt-history-content').attr('id')){
            $j(this).click();
        }
    });
});
                                    