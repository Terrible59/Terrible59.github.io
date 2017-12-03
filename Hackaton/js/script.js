var logButton = $('.header-log-in-btn');
var close = $('.popup-close');
var message = $('.message-wrapp');
var messagePopup = $('.message-popup');
var messageClose = $('.message-popup-span');

logButton.on('click', function(event){
	$('.popup').fadeIn();
});
close.on('click', function(event){
	$('.popup').fadeOut();
});

function slowScroll (id) {
 	var offset = 0;
 	$('html, body').animate ({
  		scrollTop: $(id).offset ().top - offset
 	}, 500);
 	return false;
}

message.on('click',function(event){
	messagePopup.css('display','flex');
	message.fadeOut();
});

messageClose.on('click',function(event){
	messagePopup.fadeOut();
	message.fadeIn();
});



/*var p = $('.par');
var link = $('.link');

link.on('click',function(event){
	if(p.hasClass('closed')){
		p.slideDown();
		p.removeClass('closed');
	}
	else{
		p.slideUp();
		p.addClass('closed');
	}
});*/