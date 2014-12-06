String.prototype.insertAt = function (index, string) {
  if (index > 0)
    return this.substring(0, index) + string + this.substring(index, this.length);
  else
    return string + this;
};


function fitCenter(){
      $('.fit-center').each(function(){
            $(this).position({
                my: 'center',
                at: 'center',
                of: $(this).parent(),
             });
        });
}


function setMember(){

        $('.team-member').each(function(index){
            var img = $(this).find('.member-img');
            var txt = $(this).find('.member-txt');
            if(Modernizr.mq('(min-width: 768px)')) {
                img.css('height', 'initial');
                txt.css('height', 'initial');
                var heightImg = img.height();
                var heightTxt = txt.height();
                var maxHeight = Math.max(heightImg, heightTxt);
                img.height(maxHeight);
                txt.height(maxHeight);
                if(index % 2 == 0) {
                    txt.css('text-align', 'left');
                }
                else {
                    txt.css('text-align', 'right');
                }
            }
            else {
                img.css('height', '150px');
                txt.css({'height': 'initial', 'text-align': 'center'});
            }
        });

}

function setCurrentNav() {
    var path = window.location.pathname;
    path = path.replace(/\/$/, '');
    path = decodeURIComponent(path);

    $('.navbar-nav a, .footer-menu a').each(function () {
        var href = $(this).attr('href');
        if (path.substring(0, href.length) === href) {
            $(this).addClass('current');
        }
    });

    $('.product-carousel a').each(function () {
        var href = $(this).attr('href');
        if (path.substring(0, href.length) === href) {
            $(this).addClass('current');
            setCurrentProductNavImg($(this).find('img'));
            $('.product-carousel').slickGoTo($(this).parent().attr('index'));
        }
    });
}


function setCurrentProductNavImg(item) {
    var imgPath = $(item).attr('src')
    var dotIndex = imgPath.lastIndexOf('.');
    $(item).attr('src', imgPath.insertAt(dotIndex, '_current'));
}

function unsetCurrentProductNavImg(item) {
    var imgPath = $(item).attr('src')
    $(item).attr('src', imgPath.replace('_current', ''));
}


$(document).ready(function(){

    // swap svg with png if svg is not supported
    // http://caniuse.com/#feat=svg-img
    if(!Modernizr.svgasimg) {
        $('img[src$=svg]').each(function() {
            $(this).attr('src').replace('.svg', '.png');
        });
    }

    $('.product-carousel a').hover(
        function() {
            if (!$(this).hasClass('current')) {
                setCurrentProductNavImg($(this).find('img'));
            }
        },
        function() {
            if (!$(this).hasClass('current')) {
                unsetCurrentProductNavImg($(this).find('img'));
            }
        }
    );

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

    var sec_slide_count = $('.sec-carousel > div').length;
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

    var client_slide_count = $('.client-carousel > div').length;
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
        maxWidth: '90%',
        maxHeight: '90%',
    });

    $('a.video-gallery').colorbox({
        opacity: 0.5,
        rel: 'group2',
        iframe: true,
        maxWidth: '90%',
        maxHeight: '90%',
        innerWidth: 640,
        innerHeight: 390
    });

    setCurrentNav();

});


$(window).load(function() {

    setMember();

    fitCenter();

    $('.product-carousel, .main-carousel').animate({'opacity': 1}, 100);

    $(window).resize(function() {
        fitCenter();
        setTimeout(setMember, 100);
        setTimeout(fitCenter, 500);
    });

});
