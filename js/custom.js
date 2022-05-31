(function($) {
    "use strict";

    $(document).ready(function() {

        /*---------- Navigation ----------*/
        if ($('header').hasClass('full-width')) {
            $('header').attr('data-full', 'yes');
        }
        if ($('header').hasClass('alternative')) {
            $('header').attr('data-alt', 'yes');
        }

        function menumobile() {
            var winWidth = $(window).width();
            if (winWidth < 973) {
                $('#navigation').removeClass('menu');
                $('#navigation li').removeClass('dropdown');
                $('header').removeClass('full-width');
                $('#navigation').superfish('destroy');
            } else {
                $('#navigation').addClass('menu');
                if ($('header').data('full') === "yes") {
                    $('header').addClass('full-width')
                }
                $('#navigation').superfish({
                    delay: 300,
                    animation: { opacity: 'show' },
                    speed: 200,
                    speedOut: 50
                });
            }
            if (winWidth < 1272) {
                $('header').addClass('alternative').removeClass('full-width');
            } else {
                if ($('header').data('alt') === "yes") {} else {
                    $('header').removeClass('alternative');
                }
            }
        }

        $(window).resize(function() {
            menumobile();
        });
        menumobile();


        /*---------- Mobile Navigation ----------*/
        var jPanelMenu = $.jPanelMenu({
            menu: '#responsive',
            animated: false,
            duration: 200,
            keyboardShortcuts: false,
            closeOnContentClick: true
        });


        // desktop devices
        $('.menu-trigger').on('click', function() {
            var jpm = $(this);

            if (jpm.hasClass('active')) {
                jPanelMenu.off();
                jpm.removeClass('active');
            } else {
                jPanelMenu.on();
                jPanelMenu.open();
                jpm.addClass('active');
            }
            return false;
        });


        // Removes SuperFish Styles
        $('#jPanelMenu-menu').removeClass('sf-menu');
        $('#jPanelMenu-menu li ul').removeAttr('style');


        $(window).resize(function() {
            var winWidth = $(window).width();
            var jpmactive = $('.menu-trigger');
            if (winWidth > 990) {
                jPanelMenu.off();
                jpmactive.removeClass('active');
            }
        });



        /*---------- Stacktable ----------*/
        $('.responsive-table').stacktable();




        /*---------- Back to top ----------*/
        var pxShow = 400;
        var fadeInTime = 400;
        var fadeOutTime = 400;
        var scrollSpeed = 400;

        $(window).scroll(function() {
            if ($(window).scrollTop() >= pxShow) {
                $("#backtotop").fadeIn(fadeInTime);
            } else {
                $("#backtotop").fadeOut(fadeOutTime);
            }
        });

        $('#backtotop a').on('click', function() {
            $('html, body').animate({ scrollTop: 0 }, scrollSpeed);
            return false;
        });


        /*---------- Revolution Slider ----------*/
        $('.fullwidthbanner').revolution({
            delay: 9000,
            startwidth: 1180,
            startheight: 585,
            onHoverStop: "on",
            navigationType: "none",
            navigationArrows: "verticalcentered",
            navigationStyle: "none",
            touchenabled: "on",
            navOffsetHorizontal: 0,
            navOffsetVertical: 20,
            stopAtSlide: -1,
            stopAfterLoops: -1,
            fullWidth: "on",
        });



        /*---------- Flexslider ----------*/
        $('.testimonials-slider').flexslider({
            animation: "fade",
            controlsContainer: $(".custom-controls-container"),
            customDirectionNav: $(".custom-navigation a")
        });


        /*---------- Chosen Plugin ----------*/

        var config = {
            '.chosen-select': { disable_search_threshold: 10, width: "100%" },
            '.chosen-select-deselect': { allow_single_deselect: true, width: "100%" },
            '.chosen-select-no-single': { disable_search_threshold: 10, width: "100%" },
            '.chosen-select-no-results': { no_results_text: 'Oops, nothing found!' },
            '.chosen-select-width': { width: "95%" }
        };
        for (var selector in config) {
            $(selector).chosen(config[selector]);
        }


        /*---------- Checkboxes ----------*/

        $('.checkboxes').find('input:first').addClass('first')
        $('.checkboxes input').on('change', function() {
            if ($(this).hasClass('first')) {
                $(this).parents('.checkboxes').find('input').prop('checked', false);
                $(this).prop('checked', true);
            } else {
                $(this).parents('.checkboxes').find('input:first').not(this).prop('checked', false);
            }
        });


        /*---------- Magnific Popup ----------*/

        $('body').magnificPopup({
            type: 'image',
            delegate: 'a.mfp-gallery',

            fixedContentPos: true,
            fixedBgPos: true,

            overflowY: 'auto',

            closeBtnInside: true,
            preloader: true,

            removalDelay: 0,
            mainClass: 'mfp-fade',

            gallery: { enabled: true },

            callbacks: {
                buildControls: function() {
                    console.log('inside');
                    this.contentContainer.append(this.arrowLeft.add(this.arrowRight));
                }
            }
        });


        $('.popup-with-zoom-anim').magnificPopup({
            type: 'inline',

            fixedContentPos: false,
            fixedBgPos: true,

            overflowY: 'auto',

            closeBtnInside: true,
            preloader: false,

            midClick: true,
            removalDelay: 300,
            mainClass: 'my-mfp-zoom-in'
        });


        $('.mfp-image').magnificPopup({
            type: 'image',
            closeOnContentClick: true,
            mainClass: 'mfp-fade',
            image: {
                verticalFit: true
            }
        });


        /*---------- Tabs ----------*/

        var $tabsNav = $('.tabs-nav'),
            $tabsNavLis = $tabsNav.children('li');

        $tabsNav.each(function() {
            var $this = $(this);

            $this.next().children('.tab-content').stop(true, true).hide()
                .first().show();

            $this.children('li').first().addClass('active').stop(true, true).show();
        });

        $tabsNavLis.on('click', function(e) {
            var $this = $(this);

            $this.siblings().removeClass('active').end()
                .addClass('active');

            $this.parent().next().children('.tab-content').stop(true, true).hide()
                .siblings($this.find('a').attr('href')).fadeIn();

            e.preventDefault();
        });
        var hash = window.location.hash;
        var anchor = $('.tabs-nav a[href="' + hash + '"]');
        if (anchor.length === 0) {
            $(".tabs-nav li:first").addClass("active").show(); //Activate first tab
            $(".tab-content:first").show(); //Show first tab content
        } else {
            anchor.parent('li').trigger("click");
        }
    });

})(this.jQuery);