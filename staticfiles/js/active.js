var jQuery, window, document;
(function ($) {
	"use strict";

    $(document).ready(function(){
        $(".testimonial-carousel").owlCarousel({
            
            nav: false,
            dots: true,
            autoplay: false,
            loop: true,
            responsive:{
                0:{
                    items: 1,
                    margin: 0
                },
                600:{
                    items: 2,
                    margin: 30
                },
                1000:{
                    items: 2,
                    margin: 30
                }
            }
        });
        $(".testimonial-carousel-2").owlCarousel({
            items: 1,
            nav: false,
            dots: true,
            autoplay: false,
            loop: true,
            margin: 0
        });
        
        $(".work-slider").owlCarousel({
            items: 1,
            nav: true,
            dots: true,
            autoplay: false,
            loop: true,
            navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
        });
        
        var homepageSlides = $(".homepage-slides");
        
        homepageSlides.owlCarousel({
            items: 1,
            nav: true,
            dots: false,
            autoplay: false,
            loop: true,
            navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            mouseDrag: false,
            touchDrag: false,
        });
        
        homepageSlides.on("translate.owl.carousel", function(){
            $(".single-homepage-slide h2, .single-homepage-slide p").removeClass("animated fadeInDown").css("opacity", "0");
            $(".single-homepage-slide .slide-simple-btn").removeClass("animated fadeInUp").css("opacity", "0");
        });
        
        homepageSlides.on("translated.owl.carousel", function(){
            $(".single-homepage-slide h2, .single-homepage-slide p").addClass("animated fadeInDown").css("opacity", "1");
            $(".single-homepage-slide .slide-simple-btn").addClass("animated fadeInUp").css("opacity", "1");
        });
        
        
        $(".big-play-icon").magnificPopup({
            type: 'video'
        });
        
        $(".single-project-gallery").magnificPopup({
            type: 'image',
            gallery: {
                enabled: true
            }
        });
        
        $("ul#navigation").slicknav({
            prependTo: ".responsive-menu-wrap"
        });
        
        $(".mega-faqs-wrapper").perfectScrollbar();
        
        var window_width = $(window).width();
        
        if(window_width > 767){
            new WOW().init();
        }
        
        var deviceAgent = navigator.userAgent.toLowerCase();
        var agentID = deviceAgent.match(/(iphone|ipod|ipad|android)/);
        if (agentID) {

            $("body").addClass("mega-touch-device");
            $(".header-area .col-md-3").removeClass("col-md-3").addClass("col-md-12");

        }

    });


    $(window).on('load', function(){
        jQuery(".mega-slide-preloader-wrap, .mega-site-preloader-wrap").fadeOut(500);
    });


})(jQuery);	