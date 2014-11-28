$(function () {
    setNavigation();
});

function setNavigation() {
    var path = window.location.pathname;
    path = path.replace(/\/$/, "");
    path = decodeURIComponent(path);

    $(".navbar-nav a").each(function () {
        var href = $(this).attr('href');
        if (path.substring(0, href.length) === href) {
            $(this).closest('a').addClass('current');
        }
    });
}


var center_img = function(img) {
    img.centerImage('inside');
};


$(document).ready(function(){
    $('.main-carousel').slick({
        dots: true,
        pauseOnDotsHover: true,
        pauseOnHover: true,
        fade: true,
        autoplay: false,
        autoplaySpeed: 5000,
        infinite: true,
        waitForAnimate: false,
    });
    $('.sec-carousel').slick({
        //dots: true,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        responsive: [
            {
                breakpoint: 970,
                settings: {
                slidesToShow: 2,
                slidesToScroll: 2
                }
            },
            {
                breakpoint: 750,
                settings: {
                slidesToShow: 1,
                slidesToScroll: 1
                }
            }
        ]
    });

    $('.product-carousel').slick({
        //dots: true,
        infinite: true,
        slidesToShow: 4,
        slidesToScroll: 4,
        responsive: [
            {
                breakpoint: 970,
                settings: {
                slidesToShow: 3,
                slidesToScroll: 3
                }
            },
            {
                breakpoint: 750,
                settings: {
                slidesToShow: 2,
                slidesToScroll: 2
                }
            }
        ]
    });
    
    
    
    $('.clients-carousel').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        arrows: false,
        autoplay: true,
        autoplaySpeed: 10000,
        pauseOnHover: true,
        //fade: true,
        responsive: [
            {
                breakpoint: 970,
                settings: {
                slidesToShow: 2,
                slidesToScroll: 2
                }
            },
            {
                breakpoint: 750,
                settings: {
                slidesToShow: 1,
                slidesToScroll: 1
                }
            }
        ]
    });


    


    center_img($('.slide-img img'));
    center_img($('.sec-slide-img img'));
    center_img($('.product-slide-img img'));
    center_img($('.clients-img img'));

    jQuery('a.gallery').colorbox({
        opacity: 1 ,
        rel: 'group1',
        maxWidth: "90%",
        maxHeight: "80%",
        transition:"fade",
    });
});


$(window).resize(function() {
    center_img($('.slide-img img'));
    center_img($('.sec-slide-img img'));
    center_img($('.product-slide-img img'));
    center_img($('.clients-img img'));
});
