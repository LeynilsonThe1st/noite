$(() => {
    $(window).on('scroll', function () {
        var header = $('header').height();
        var y = $(window).scrollTop();
        var nav = $("nav");
        var activador = $('.activador').offset().top

        if ((y + nav.height() >= activador) && (y < header)) {
            nav.fadeOut('fast');
        } else {
            if (y + nav.height() <= activador) {
                nav.removeClass('on').fadeIn('fast');
            } else {
                nav.addClass('on').fadeIn('fast');
            }
        }
    });
});
