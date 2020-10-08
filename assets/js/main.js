(function($) {
    'use strict';
    const date = new Date();
    document.querySelector('.year').innerHTML = date.getFullYear();

    setTimeout(function () {
        $('#message').fadeOut('slow');
    }, 3000)
	/*  
		:: 5.0 Init Accordions
	*/
	initAccordions();
	function initAccordions() {
		if ($('.accordion').length) {
			var accs = $('.accordion');

			accs.each(function() {
				var acc = $(this);

				if (acc.hasClass('active')) {
					var panel = $(acc.next());
					// var panelH = panel.prop('scrollHeight') + 'px';

					if (panel.css('max-height') == '0px') {
						panel.css('max-height', panel.prop('scrollHeight') + 'px');
					} else {
						panel.css('max-height', '0px');
					}
				}

				acc.on('click', function() {
					if (acc.hasClass('active')) {
						acc.removeClass('active');
						var panel = $(acc.next());
						// var panelH = panel.prop('scrollHeight') + 'px';

						if (panel.css('max-height') == '0px') {
							panel.css('max-height', panel.prop('scrollHeight') + 'px');
						} else {
							panel.css('max-height', '0px');
						}
					} else {
						acc.addClass('active');
						var panel = $(acc.next());
						// var panelH = panel.prop('scrollHeight') + 'px';

						if (panel.css('max-height') == '0px') {
							panel.css('max-height', panel.prop('scrollHeight') + 'px');
						} else {
							panel.css('max-height', '0px');
						}
					}
				});
			});
		}
	}
})(jQuery);



