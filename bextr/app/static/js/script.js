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

var center_img = function() {
    $('.slide-img img').centerImage('inside');
    $('.sec-slide-img img').centerImage('inside');
    $('.product-slide-img img').centerImage('inside');
    $('.client-img img').centerImage('inside');
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

    var sec_slide_count = $('.sec-carousel > div').length
    $('.sec-carousel').slick({
        //dots: true,
        infinite: true,
        slidesToShow: Math.min(sec_slide_count, 3),
        slidesToScroll: Math.min(sec_slide_count, 3),
        responsive: [
            {
                breakpoint: 970,
                settings: {
                slidesToShow: Math.min(sec_slide_count, 2),
                slidesToScroll: Math.min(sec_slide_count, 2)
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

    var client_slide_count = $('.client-carousel > div').length
    $('.client-carousel').slick({
        infinite: true,
        slidesToShow: Math.min(client_slide_count, 3),
        slidesToScroll: Math.min(client_slide_count, 3),
        arrows: false,
        autoplay: true,
        autoplaySpeed: 10000,
        pauseOnHover: true,
        //fade: true,
        responsive: [
            {
                breakpoint: 970,
                settings: {
                slidesToShow: Math.min(client_slide_count, 2),
                slidesToScroll: Math.min(client_slide_count, 2)
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

    $('a.image-gallery').colorbox({
        opacity: 0.5,
        rel: 'group1',
        maxWidth: "90%",
        maxHeight: "90%",
    });

    $('a.video-gallery').colorbox({
        opacity: 0.5,
        rel: 'group2',
        iframe: true,
        maxWidth: "90%",
        maxHeight: "90%",
        innerWidth: 640,
        innerHeight: 390
    });

    center_img();

    $('.product-carousel, .main-carousel').animate({"opacity": 1}, 100);

});

$(window).resize(function() {
	setTimeout(center_img, 500);
});
