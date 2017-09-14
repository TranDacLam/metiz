// đặt class 'odd','even','first','last' vao phan tu 'ul.products-grid' 
// funtion trong varien/js.js
// Nhưng em nghĩ như thế này mới đúng: decorateGeneric($$('ul.products-grid li'), ['odd','even','first','last']); 
// em thêm thẻ li vào thì nó add các class 'odd','even','first','last' vào thẻ li
    decorateGeneric($$('ul.products-grid'), ['odd','even','first','last']);