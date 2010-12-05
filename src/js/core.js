$(window).load(function() {
	$('.click h1').click(function() {
		$(this).next('div').slideToggle(600);
	}).css('cursor', 'pointer').hover(function() {
		$(this).stop().animate( {
			'opacity' : 0.75
		}, 500);
	}, function() {
		$(this).stop().animate( {
			'opacity' : 1
		}, 500);
	});

	$('#1-clic div').toggle();

	$('textarea').supertextarea( {
		maxl : 300,
		dsrm : {
			use : true,
			text : 'caràcters restants',
			css : {
				'color' : '#0BA034',
				'font-size' : 'small'
			}
		}
	});
});