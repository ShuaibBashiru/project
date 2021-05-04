(function(document, window, $){
    $(document).ready(function(){ 
 $(".slideshow").slick({
     slidesToShow: 1,
     prevArrow: '.prevdiv',
     nextArrow: '.nextdiv',
     speed: 3000,
     autoplay: true
 });
        });
 
 })(document, window, jQuery)
 