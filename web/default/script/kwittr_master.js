$(function fixedHeader() {
    "use strict";
    var header = $(".static");
    $(window).scroll(function () {
        var scroll = $(window).scrollTop();

        if (scroll >= 1) {
            header.removeClass('static').addClass("scrolled");
        } else {
            header.removeClass("scrolled").addClass('static');
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

function parallax() {
	var primaryHero = document.getElementById("homeHero");
	var yPos = window.pageYOffset / primaryHero.dataset.speed;
	yPos = -yPos;
	var coords = '0% '+ yPos + 'px';
	primaryHero.style.backgroundPosition = coords;
}
window.addEventListener("scroll", function(){
	parallax();	
}); 
