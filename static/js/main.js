
$(document).ready(function(){
	$('#slider').fadeIn('slow').delay(200);
	$("#sticker").sticky({topSpacing:0});
  });
  
  //https://dribbble.com/shots/3581904-HEALTHEX-Day-01
  
  //SMOOTH SCROLL MENU
  $(document).ready(function(){
	$("a").on('click', function(event) {
	  if (this.hash !== "") {  
		event.preventDefault();
  
		var hash = this.hash;
  
		$('html, body').animate({
		  scrollTop: $(hash).offset().top
		}, 1000, function(){
		  window.location.hash = hash;
		});
	  }
	});
  });
  
  //FIXED MENU COLORS
  $(document).ready(function(){
	$(window).trigger('scroll');
	$(window).bind('scroll', function () {
	  var pixels = 9999999999; //pixeles abajo
	  if ($(window).scrollTop() > pixels) {
	$('.nav').addClass('fixed');
		$('.menu a').css({"color":"#FEFFFF"});
		$('.logo').css({"color":"#FEFFFF"});
	  } else {
		$('.nav').removeClass('fixed');
		$('.menu a').css({"color":"#FEFFFF"});
		$('.logo').css({"color":"#FEFFFF"});
	  }
	}); 
  }); 
  
  /*
  $(document).ready(function(){
	$('a[href^="#"]').on('click',function (e){
	  e.preventDefault();
	  var target = this.hash;
	  var $target = $(target);
	  
	  //scroll con hash
	  $('html, body').animate({
		'scrollTop': $target.offset().top
	  }, 1000, 'swing', function(){
		window.location.hash = target;
	  });
	  
	 /* //scroll sin hash
	  $('html, body').animte({
		'scrollTop': $targer.offset().top
		}, 1000, 'swing');
	});
  });*/

  $(".custom-carousel").owlCarousel({
	autoWidth: true,
	loop: true
  });
  $(document).ready(function () {
	$(".custom-carousel .item").click(function () {
	  $(".custom-carousel .item").not($(this)).removeClass("active");
	  $(this).toggleClass("active");
	});
  });


  /* select box*/
  /* FORKED FROM https://codepen.io/yy/pen/vOYqYV */
$(".custom-select").each(function() {
	var classes = $(this).attr("class"),
	  id = $(this).attr("id"),
	  name = $(this).attr("name");
	var template = '<div class="' + classes + '">';
	template +=
	  '<span class="custom-select-trigger">' +
	  $(this).attr("placeholder") +
	  "</span>";
	template += '<div class="custom-options">';
	$(this).find("option").each(function() {
	  template +=
		'<span class="custom-option ' +
		$(this).attr("class") +
		'" data-value="' +
		$(this).attr("value") +
		'">' +
		$(this).html() +
		"</span>";
	});
	template += "</div></div>";
  
	$(this).wrap('<div class="custom-select-wrapper"></div>');
	$(this).hide();
	$(this).after(template);
  });
  $(".custom-option:first-of-type").hover(
	function() {
	  $(this).parents(".custom-options").addClass("option-hover");
	},
	function() {
	  $(this).parents(".custom-options").removeClass("option-hover");
	}
  );
  $(".custom-select-trigger").on("click", function() {
	$("html").one("click", function() {
	  $(".custom-select").removeClass("opened");
	});
	$(this).parents(".custom-select").toggleClass("opened");
	event.stopPropagation();
  });
  $(".custom-option").on("click", function() {
	$(this)
	  .parents(".custom-select-wrapper")
	  .find("select")
	  .val($(this).data("value"));
	$(this)
	  .parents(".custom-options")
	  .find(".custom-option")
	  .removeClass("selection");
	$(this).addClass("selection");
	$(this).parents(".custom-select").removeClass("opened");
	$(this)
	  .parents(".custom-select")
	  .find(".custom-select-trigger")
	  .text($(this).text());
  });

  console.clear();

  const loginBtn = document.getElementById('login');
  const signupBtn = document.getElementById('signup');
  
  loginBtn.addEventListener('click', (e) => {
	  let parent = e.target.parentNode.parentNode;
	  Array.from(e.target.parentNode.parentNode.classList).find((element) => {
		  if(element !== "slide-up") {
			  parent.classList.add('slide-up')
		  }else{
			  signupBtn.parentNode.classList.add('slide-up')
			  parent.classList.remove('slide-up')
		  }
	  });
  });
  
  signupBtn.addEventListener('click', (e) => {
	  let parent = e.target.parentNode;
	  Array.from(e.target.parentNode.classList).find((element) => {
		  if(element !== "slide-up") {
			  parent.classList.add('slide-up')
		  }else{
			  loginBtn.parentNode.parentNode.classList.add('slide-up')
			  parent.classList.remove('slide-up')
		  }
	  });
  });