$(document).ready(function(){ 
$('.selectcsv').on('click', function(){
    $('.form').slideToggle('slow');
})

$(".tablelist td:contains('Suspicious')").each(function(i){
        $(this).addClass('red');
})
$(".tablelist td:contains('Accurate')").each(function(i){
    $(this).addClass('blue');
})
});