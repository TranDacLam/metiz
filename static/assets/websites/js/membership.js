
// Hiển thị nội dung khi click vào 1 tab cụ thể (dòng 4-7)
$j(document).ready(function(){
    $j( ".cgv-membership" ).tabs();
    $j( ".accordion" ).accordion({
        heightStyle: "content" // chiều cao của tab phụ thuộc vào nội dung
    });
    // dòng(10-14) click vào li của class cgv-membership
    // kiểm tra nếu trong li ko có thẻ a thì tìm đến thẻ a và kích hoạt action click
    $j('.cgv-membership > ul li').click(function(event) {
        if (!$j(event.target).is('a')) {
            $j(this).find("a").trigger('click');
        }
    });

    /* dòng 17-29 */
    var url = window.location.href; // tạo biến url =window.location.href
    var arr = url.split('?');// tách chuỗi url tại vị trí dấu ? thành 1 mảng arr[] chứa các phần tử 
    
    $j('#'+arr[1]).click();// nối kí từ # với phần tử vị trí thứ 1 rồi thực hiện click
    
    $j('.cgv-membership > ul').find('a').each(function() { //lặp qua mỗi phần tử a của class cgv-membership
        // kiểm tra nếu giá trị thuộc tính href của thẻ a = chuỗi '#'+id tại vị trí class lyt-history-content
        // thực hiện click
        if($j(this).attr('href') == '#'+$j('#'+arr[1]).parents('.lyt-history-content').attr('id')){
            $j(this).click(); 
        }
    });
});
                                    