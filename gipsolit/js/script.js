$(document).ready(function(){

	var popup = $('popup');

	$('.popup-open').on('click',function(event){
		$('.popup').fadeIn();
	});

	$('.popup-close').on('click',function(event){
		$('.popup').fadeOut();
	});
});