$(function fixedHeader() {
    "use strict";
    var header = $(".static");
    $(window).scroll(function () {
        var scroll = $(window).scrollTop();

        if (scroll >= 150) {
            header.removeClass('static').addClass("scrolled");
        } else {
            header.removeClass("scrolled").addClass('static');
        }
    });
});

$(function headerTrigger(){
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        var os = $('#header-trigger').offset().top;
        var ht = $('#header-trigger').height();
        if(scroll > os + ht){
            $('#navbar-main').addClass('color-change');
        }
        else {
            $('#navbar-main').removeClass('color-change');
        }
    });
});

var acc = document.getElementsByClassName("accordion-toggle");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    } 
  });
}

var acc = document.getElementsByClassName("nav-toggle");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
      panel.style.opacity = 0;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
      panel.style.opacity = 1;
    } 
  });
}

function parallax() {
	var primaryHero = document.getElementById("parallaxObject");
	var yPos = window.pageYOffset / primaryHero.dataset.speed;
	yPos = -yPos;
	var coords = '0% '+ yPos + 'px';
	primaryHero.style.backgroundPosition = coords;
}
window.addEventListener("scroll", function(){
	parallax();	
}); 

