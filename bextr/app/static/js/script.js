String.prototype.insertAt = function (index, string) {
    if (index > 0) {
        return this.substring(0, index) + string + this.substring(index, this.length);
    }
    else {
        return string + this;
    }
};

function fitCenter() {
        $('.fit-center').each(function() {
            $(this).position({
                my: 'center',
                at: 'center',
                of: $(this).parent()
             });
        });
}

function setMember() {
        $('.team-member').each(function(index) {
            var img = $(this).find('.member-img');
            var txt = $(this).find('.member-txt');
            if ((Modernizr.mq('only all') && Modernizr.mq('(min-width: 768px)'))
                || (!Modernizr.mq('only all') && document.body.clientWidth >= 768)) {
                $(img, txt).css('height', 'auto');
                $(img, txt).height(Math.max(img.height(), txt.height()));
                if(index % 2 == 0) {
                    txt.css('text-align', 'left');
                }
                else {
                    txt.css('text-align', 'right');
                }
            }
            else {
                console.log('bla');
                img.css('height', '150px');
                txt.css({'height': 'auto', 'text-align': 'center'});
            }
        });

}

function preloadImage(src) {
        $('<img/>').attr('src', src).css('display', 'none').appendTo('body');
    }

function setCurrentNav() {

    $('.navbar-nav a, .footer-menu a, .product-carousel a').each(function () {
        var href = this.href;
        if (window.location.href.substring(0, href.length) === href) {
            $(this).addClass('current');
        }
    });

    $('.product-carousel a').each(function () {
        var img = $(this).find('img');
        preloadImage(getCurrentProductNavImgSrc(img))
        if ($(this).hasClass('current')) {
            setCurrentProductNavImg(img);
            $('.product-carousel').slickGoTo($(this).parent().attr('index'));
        }
    });
}

function getCurrentProductNavImgSrc(item) {
    var imgPath = $(item).attr('src').replace('_current', '');
    var dotIndex = imgPath.lastIndexOf('.');
    return imgPath.insertAt(dotIndex, '_current');
}

function setCurrentProductNavImg(item) {
    $(item).attr('src', getCurrentProductNavImgSrc(item));
}

function unsetCurrentProductNavImg(item) {
    $(item).attr('src', $(item).attr('src').replace('_current', ''));
}




$(document).ready(function(){

    // swap svg with png if svg is not supported
    // http://caniuse.com/#feat=svg-img
    Modernizr.addTest('svgasimg', document.implementation
        .hasFeature('http://www.w3.org/TR/SVG11/feature#Image', '1.1'));
    if(!Modernizr.svgasimg) {
        $('img[src$=svg]').each(function() {
            $(this).attr('src', $(this).attr('src').replace('.svg', '.png'));
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
        rel: 'group-1',
        maxWidth: '90%',
        maxHeight: '90%',
    });

    $('a.video-gallery').colorbox({
        opacity: 0.5,
        iframe: true,
        maxWidth: '90%',
        maxHeight: '90%',
        innerWidth: 640,
        innerHeight: 390
    });

    if ($().bootstrapValidator) {
        $('.message-form').bootstrapValidator({
            message: 'This value is not valid.',
            feedbackIcons: {
                valid: 'glyphicon glyphicon-ok',
                invalid: 'glyphicon glyphicon-remove',
                validating: 'glyphicon glyphicon-refresh'
            },
            fields: {
                'message-name': {
                    message: 'The input is not valid.',
                    validators: {
                        notEmpty: {
                            message: 'The name is required and cannot be empty.'
                        },
                        stringLength: {
                            min: 1,
                            max: 200,
                            message: 'The name must be more than 1 and less than 200 characters long.'
                        }
                    }
                },
                'message-email': {
                    validators: {
                        notEmpty: {
                            message: 'The email is required and cannot be empty.'
                        },
                        stringLength: {
                            min: 1,
                            max: 200,
                            message: 'The email must be more than 1 and less than 200 characters long.'
                        },
                        emailAddress: {
                            message: 'The input is not a valid email address.'
                        },
                        regexp: {
                            regexp: '^[^@\\s]+@([^@\\s]+\\.)+[^@\\s]+$',
                            message: 'The input is not a valid email address.'
                        }
                    }
                },
                'message-text': {
                    message: 'The input is not valid.',
                    validators: {
                        notEmpty: {
                            message: 'The message is required and cannot be empty.'
                        },
                        stringLength: {
                            min: 1,
                            max: 500,
                            message: 'The message must be more than 1 and less than 500 characters long.'
                        }
                    }
                }
            }
        }).on('success.form.bv', function(e) {
            e.preventDefault();
            $.ajax({
                url: '/api/message',
                type: 'POST',
                accepts: 'text',
                dataType: 'text',
                data: $(e.target).serialize(),
                success: function (data, status, jqXHR) {
                    $('.msg-form-alert')
                        .addClass('alert-success')
                        .removeClass('alert-danger')
                        .removeClass('hide')
                        .text('Your message has been successfully sent.');
                },
                error: function (jqXHR, status, err) {
                    $('.msg-form-alert')
                        .addClass('alert-danger')
                        .removeClass('alert-success')
                        .removeClass('hide')
                        .text('Something went wrong, please try again.');
                }
            })
        }).on('error.validator.bv', function(e, data) {
            if (data.field === 'message-email') {
                data.element
                    .data('bv.messages')
                    .find('.help-block[data-bv-for="' + data.field + '"]').hide()
                    .filter('[data-bv-validator="' + data.validator + '"]').show();
            }
        });

        $('.subscribe-form').bootstrapValidator({
            message: 'This value is not valid.',
            feedbackIcons: {
                valid: 'glyphicon glyphicon-ok',
                invalid: 'glyphicon glyphicon-remove',
                validating: 'glyphicon glyphicon-refresh'
            },
            fields: {
                'subscribe-email': {
                    validators: {
                        notEmpty: {
                            message: 'The email is required and cannot be empty.'
                        },
                        stringLength: {
                            min: 1,
                            max: 200,
                            message: 'The email must be more than 1 and less than 200 characters long.'
                        },
                        emailAddress: {
                            message: 'The input is not a valid email address.'
                        },
                        regexp: {
                            regexp: '^[^@\\s]+@([^@\\s]+\\.)+[^@\\s]+$',
                            message: 'The input is not a valid email address.'
                        }
                    }
                }
            }
        }).on('success.form.bv', function(e) {
            e.preventDefault();
            $.ajax({
                url: '/api/subscribe',
                type: 'POST',
                accepts: 'text',
                dataType: 'text',
                data: $(e.target).serialize(),
                success: function (data, status, jqXHR) {
                    $('.subs-form-alert')
                        .addClass('alert-success')
                        .removeClass('alert-danger')
                        .removeClass('hide')
                        .text('Thank you for subscribing.');
                },
                error: function (jqXHR, status, err) {
                    var message = 'Something went wrong, please try again.'
                    if (err === 'CONFLICT') {
                        var message = 'Email address already subscribed.';
                    }
                    $('.subs-form-alert')
                        .addClass('alert-danger')
                        .removeClass('alert-success')
                        .removeClass('hide')
                        .text(message);
                }
            })
        }).on('error.validator.bv', function(e, data) {
            if (data.field === 'subscribe-email') {
                data.element
                    .data('bv.messages')
                    .find('.help-block[data-bv-for="' + data.field + '"]').hide()
                    .filter('[data-bv-validator="' + data.validator + '"]').show();
            }
        });
    }

    if ($().placeholder) {
        $('input, textarea').placeholder();
    }

});

$(window).load(function() {

    if ($(location).attr('pathname') === '/contact') {
        $.ajax({
            url: '/api/csrf-token',
            type: 'GET',
            accepts: 'text',
            dataType: 'text',
            success: function (data, status, jqXHR) {
                $('#message-csrf_token, #subscribe-csrf_token')
                    .attr('value', data);
            }
        });
    }

    setCurrentNav();

    setMember();

    fitCenter();

    $('.js-fouc').animate({'opacity': 1}, 100);

    $(window).resize(function() {
        fitCenter();
        setTimeout(setMember, 100);
        setTimeout(fitCenter, 500);
    });

});
