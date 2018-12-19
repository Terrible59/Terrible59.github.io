var popup1 = $('#popup-1');
var popup2 = $('#popup-2');
var popup3 = $('#popup-3');
var popup4 = $('#popup-4');
var popup5 = $('#popup-5');
var popup6 = $('#popup-6');

var popup = $('.popup');

var btn1 = $('#popup-1-btn');
var btn2 = $('#popup-2-btn');
var btn3 = $('#popup-3-btn');
var btn4 = $('#popup-4-btn');
var btn5 = $('#popup-5-btn');
var btn6 = $('#popup-6-btn');

var ph1 = $('#phot1');
var ph2 = $('#phot2');
var ph3 = $('#phot3');
var ph4 = $('#phot4');
var ph5 = $('#phot5');
var ph6 = $('#phot6');

var ph_popup1 = $('#ph-popup1');
var ph_popup2 = $('#ph-popup2');
var ph_popup3 = $('#ph-popup3');
var ph_popup4 = $('#ph-popup4');
var ph_popup5 = $('#ph-popup5');
var ph_popup6 = $('#ph-popup6');

var close = $('.popup-close');

btn1.on('click', function(event){
	popup1.fadeIn();
});

btn2.on('click', function(event){
	popup2.fadeIn();
});

btn3.on('click', function(event){
	popup3.fadeIn();
});

btn4.on('click', function(event){
	popup4.fadeIn();
});

btn5.on('click', function(event){
	popup5.fadeIn();
});

btn6.on('click', function(event){
	popup6.fadeIn();
});

close.on('click', function(event){
	popup.fadeOut();
});



ph1.on('click', function(event){
	ph_popup1.fadeIn();
});
ph2.on('click', function(event){
	ph_popup2.fadeIn();
});
ph3.on('click', function(event){
	ph_popup3.fadeIn();
});
ph4.on('click', function(event){
	ph_popup4.fadeIn();
});
ph5.on('click', function(event){
	ph_popup5.fadeIn();
});
ph6.on('click', function(event){
	ph_popup6.fadeIn();
});


$('.menu-toggle').on('click', function() {
  $(this).toggleClass('is-active');
  $('.main-menu-list').toggleClass('main-active');
});