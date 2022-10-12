$(document).ready(function () {


// var menuLeft = document.querySelector(".left-menu");
// menuLeft.style.height = ($(window).height() +$('#navbarCollapse').height()).toString() + "px";
// $('.progress-container').css('height', menuLeft.clientHeight );

// $('.part-circ')[0].style.top = (0.1 * $('.progress-container').height() + $('#navbarCollapse').height()).toString() + "px";
// for (i = 1; i < $('.part-circ').length - 1; i++)
// 	$('.part-circ')[i].style.top = ((0.1 + (i / ($('.part-circ').length - 1)) * 0.8) * $('.progress-container')
// 	.height() ).toString() + "px";
// $('.part-circ')[$('.part-circ').length - 1].style.top = (0.9 * $('.progress-container').height() )
// 	.toString() + "px";


// var controller = new ScrollMagic.Controller();

// var pinScene = new ScrollMagic.Scene({
// 	duration: $("body").height() - $("footer").height() - $(window).height()*2,
// 	offset:$(window).height(),
// }).setPin(menuLeft, {
// 	pushFollowers: false
// })
// .addIndicators()
// .addTo(controller);

// var tweenH = 0.1 * $('.progress-container').height();

// new ScrollMagic.Scene({
// 		triggerHook: 0.1,
// 		duration: $('.intro').outerHeight() - 0.1 * $(window).height(),
// 		offset: $(window).height()
// 	})
// 	.setTween(gsap.to(".progress.active", {
// 		height: tweenH,
// 		ease: "none"
// 	}))
// 	.addIndicators()
// 	.addTo(controller);

// for (i = 0; i < $('.part-circ').length - 1; i++) {
// 	tweenH += 0.8 * $('.progress-container').height() / ($('.part-circ').length - 1);
// 	var tween = gsap.to(".progress.active", {
// 		height: tweenH,
// 		ease: "none"
// 	});
// 	if (i > 0) {
// 		new ScrollMagic.Scene({
// 				triggerElement: $('.part')[i],
// 				triggerHook: 0.1,
// 				duration: $('.part')[i].clientHeight
// 			})
// 			.setClassToggle("#circ" + (i + 1).toString(), "active")
// 			.setTween(tween)
// 			.addTo(controller).addIndicators();

// 		new ScrollMagic.Scene({
// 				triggerElement: $('.part')[i],
// 				triggerHook: 0.1
// 			})
// 			.setClassToggle("#circ" + (i).toString(), "activated")
// 			.addIndicators()
// 			.addTo(controller);
// 	} else {
// 		new ScrollMagic.Scene({
// 				triggerElement: $('.part')[i],
// 				triggerHook: 0.1,
// 				duration: $('.part')[i].clientHeight
// 			}).addIndicators()
// 			.setClassToggle("#circ" + (i + 1).toString(), "active")
// 			.setTween(tween)
// 			.addTo(controller);
// 	}

// }

// new ScrollMagic.Scene({
// 		triggerElement: $('.part')[$('.part-circ').length - 1],
// 		triggerHook: 0.1,
// 		duration: $("#part0" + $('.part-circ').length.toString()).outerHeight() + $("footer").height() - $(window)
// 			.height() * 0.9 + 20
// 	})
// 	.setClassToggle("#circ" + ($('.part-circ').length).toString(), "active")
// 	.setTween(gsap.to(".progress.active", {
// 		height: $('.progress-container').height(),
// 		ease: "none"
// 	}))
// 	.addIndicators()
// 	.addTo(controller);

// new ScrollMagic.Scene({
// 		triggerElement: $('.part')[$('.part-circ').length - 1],
// 		triggerHook: 0.1
// 	})
// 	.setClassToggle("#circ" + ($('.part-circ').length - 1).toString(), "activated")
// 	.addIndicators()
// 	.addTo(controller);



var menuLeft = document.querySelector(".left-menu");
menuLeft.style.height = $(window).height().toString() + "px";
$('.progress-container').css('height',menuLeft.clientHeight);

$('.part-circ')[0].style.top = (0.1 * $('.progress-container').height()).toString() + "px";
for(i = 1;i < $('.part-circ').length - 1; i++)
  $('.part-circ')[i].style.top = ((0.1 + (i / ($('.part-circ').length - 1)) * 0.8) * $('.progress-container').height()).toString() + "px";
$('.part-circ')[$('.part-circ').length - 1].style.top = (0.9 * $('.progress-container').height()).toString() + "px";

var controller = new ScrollMagic.Controller();

var pinScene = new ScrollMagic.Scene({
  duration: $("body").height() - $("footer").height() - $(window).height()*2,
  offset:$(window).height(),
}).setPin(menuLeft, {pushFollowers: false}).addTo(controller);

var tweenH = 0.1 * $('.progress-container').height();

new ScrollMagic.Scene({
	offset:$(window).height(),
  	triggerHook: 0.1,
  	duration: $('.intro').outerHeight() - 0.1 * $(window).height()
})
  .setTween(gsap.to(".progress.active", {height: tweenH, ease: "none"}))
  
  .addTo(controller);

for(i = 0;i < $('.part-circ').length - 1; i++){
  tweenH += 0.8 * $('.progress-container').height() / ($('.part-circ').length - 1);
  var tween = gsap.to(".progress.active", {height: tweenH, ease: "none"});
  if(i > 0){
    new ScrollMagic.Scene({
      triggerElement: $('.part')[i],
      triggerHook: 0.1,
      duration: $('.part')[i].clientHeight
    })
    .setClassToggle("#circ" + (i+1).toString(), "active")
    .setTween(tween)
    .addTo(controller);

    new ScrollMagic.Scene({
      triggerElement: $('.part')[i],
      triggerHook: 0.1
    })
    .setClassToggle("#circ" + (i).toString(), "activated")
    
    .addTo(controller);
  }
  else{
    new ScrollMagic.Scene({
      triggerElement: $('.part')[i],
      triggerHook: 0.1,
      duration: $('.part')[i].clientHeight
    })
    .setClassToggle("#circ" + (i+1).toString(), "active")
    .setTween(tween)
    .addTo(controller);
  }
    
}

new ScrollMagic.Scene({
  triggerElement: $('.part')[$('.part-circ').length - 1],
  triggerHook: 0.1,
  duration: $("#part0" + $('.part-circ').length.toString()).outerHeight()+$("footer").height() - $(window).height() * 0.9 + 20})
.setClassToggle("#circ" + ($('.part-circ').length).toString(), "active")
.setTween(gsap.to(".progress.active", {height: $('.progress-container').height(), ease: "none"}))

.addTo(controller);

new ScrollMagic.Scene({
  triggerElement: $('.part')[$('.part-circ').length - 1],
  triggerHook: 0.1
})
.setClassToggle("#circ" + ($('.part-circ').length - 1).toString(), "activated")

.addTo(controller);

//######

// $("img").each(function() {
//     var dfd = $.Deferred();

//     $(this).load(dfd.resolve);
//     defereds.push(dfd);
// });
// $.when.apply(null, defereds).done(function() {
//   controller = controller.destroy(true);
//   pinScene = pinScene.destroy(true);
//   refresh();
// });



function refresh() {
	document.documentElement.style.setProperty('--subpageImgWidth', $('.subpage-img').width()+'px');
	menuLeft = document.querySelector(".left-menu");
	menuLeft.style.height = $(window).height().toString() + "px";
	$('.progress-container').css('height',menuLeft.clientHeight);

$('.part-circ')[0].style.top = (0.1 * $('.progress-container').height()).toString() + "px";
for(i = 1;i < $('.part-circ').length - 1; i++)
  $('.part-circ')[i].style.top = ((0.1 + (i / ($('.part-circ').length - 1)) * 0.8) * $('.progress-container').height()).toString() + "px";
$('.part-circ')[$('.part-circ').length - 1].style.top = (0.9 * $('.progress-container').height()).toString() + "px";


controller = new ScrollMagic.Controller();

pinScene = new ScrollMagic.Scene({
  duration: $("body").height() - $("footer").height() - $(window).height()*2,
  offset:$(window).height(),
}).setPin(menuLeft, {pushFollowers: false}).addTo(controller);

tweenH = 0.1 * $('.progress-container').height();

new ScrollMagic.Scene({
	triggerElement:".main-container",
  	triggerHook: 0.1,
  	duration: $('.intro').outerHeight()- 0.1 * $(window).height()
})
  .setTween(gsap.to(".progress.active", {height: tweenH, ease: "none"}))
  
  .addTo(controller);

for(i = 0;i < $('.part-circ').length - 1; i++){
  tweenH += 0.8 * $('.progress-container').height() / ($('.part-circ').length - 1);
  tween = gsap.to(".progress.active", {height: tweenH, ease: "none"});
  if(i > 0){
    new ScrollMagic.Scene({
      triggerElement: $('.part')[i],
      triggerHook: 0.1,
      duration: $('.part')[i].clientHeight
    })
    .setClassToggle("#circ" + (i+1).toString(), "active")
    .setTween(tween)
    .addTo(controller);

    new ScrollMagic.Scene({
      triggerElement: $('.part')[i],
      triggerHook: 0.1
    })
    .setClassToggle("#circ" + (i).toString(), "activated")
    
    .addTo(controller);
  }
  else{
    new ScrollMagic.Scene({
      triggerElement: $('.part')[i],
      triggerHook: 0.1,
      duration: $('.part')[i].clientHeight
    })
    .setClassToggle("#circ" + (i+1).toString(), "active")
    .setTween(tween)
    .addTo(controller);
  }
    
}

new ScrollMagic.Scene({
  triggerElement: $('.part')[$('.part-circ').length - 1],
  triggerHook: 0.1,
  duration: $("#part0" + $('.part-circ').length.toString()).outerHeight()+$("footer").height() - $(window).height() * 0.9 + 20})
.setClassToggle("#circ" + ($('.part-circ').length).toString(), "active")
.setTween(gsap.to(".progress.active", {height: $('.progress-container').height(), ease: "none"}))

.addTo(controller);

new ScrollMagic.Scene({
  triggerElement: $('.part')[$('.part-circ').length - 1],
  triggerHook: 0.1
})
.setClassToggle("#circ" + ($('.part-circ').length - 1).toString(), "activated")

.addTo(controller);
	
}

// function leftMenuChange() {
// 	if ($(window).width() <= 576) {
// 		$(".left-menu").addClass("col-3")
// 		$(".left-menu").removeClass("col-2")
// 		$(".main-body").addClass("col-9")
// 		$(".main-body").removeClass("col-10")
// 	} else {
// 		$(".left-menu").addClass("col-2")
// 		$(".left-menu").removeClass("col-3")
// 		$(".main-body").addClass("col-10")
// 		$(".main-body").removeClass("col-9")
// 	}
// }

const debounce = (fn, delay) => {
	let timer;
	return function() {
		if (timer) {
			clearTimeout(timer);
		}
		timer = setTimeout(() => {
		//alert();
			// leftMenuChange();
			controller = controller.destroy(true);
			pinScene = pinScene.destroy(true);
			fn();

		}, delay);
	}
};
const cancalDebounce = debounce(refresh, 500);
window.addEventListener('resize', cancalDebounce);

var dropdownDisplay = true;

$('.navbar-toggler').click(function() {
	if ($('button.navbar-toggler').hasClass('collapsed')) {
		$('button.navbar-toggler').removeClass('collapsed');
		$('button.navbar-toggler').attr('aria-expanded', 'false');
		$('#navbarCollapse').removeClass('show');
		$('#navbarCollapse').css('display', 'none');
		$('.dropdown-toggle').off('mouseover', phonedropdownover);
		$('.dropdown-toggle').off('mouseout', phonedropdownout);
		$('ul.dropdown-menu').removeAttr('style');
    $("#nav-list").removeClass("flex-column");
	} else {
		$('button.navbar-toggler').addClass('collapsed');
		$('#navbarCollapse').css('display', 'inline-block');
		$('ul.dropdown-menu').css('display', 'none');
		$('.dropdown-toggle').on('mouseover', phonedropdownover);
		$('.dropdown-toggle').on('mouseout', phonedropdownout);
    $("#nav-list").addClass("flex-column");
	}

});

function phonedropdownover() {
  if(dropdownDisplay)
	  this.nextElementSibling.style.display = 'inline-block';
}

function phonedropdownout() {
  if(!dropdownDisplay)
	this.nextElementSibling.style.display = 'none';
}

window.addEventListener('resize', function() {
	if (document.body.clientWidth > 576) {
		$('.dropdown-toggle').off('mouseover', phonedropdownover);
		$('.dropdown-toggle').off('mouseout', phonedropdownout);
		$('ul.dropdown-menu').removeAttr('style');
    // phonedropdownout();
    $("#nav-list").removeClass("flex-column");
	}
	if(document.body.clientWidth >= 780){
    $(".left-menu").css("opacity","1");
  }
  else{
    $(".left-menu").css("opacity","0");
  }
});

var tl_nav = gsap.timeline();
tl_nav.to("nav", {
		opacity: 0,
		y: -20,
		duration: 0.5
	})
	.to(".cir-nav", {
		opacity: 1,
		x: 0,
		duration: 0.2
	}, ">")
	.pause();


	
$(document).on("mousewheel DOMMouseScroll", function(e) {

	var delta = (e.originalEvent.wheelDelta && (e.originalEvent.wheelDelta > 0 ? 1 : -1)) || // chrome & ie
		(e.originalEvent.detail && (e.originalEvent.detail > 0 ? -1 : 1)); // firefox
	s = $(window).scrollTop();
	if (s >= ($(window).height() - $("nav").height())) {
		if (delta > 0) {
			// 向上滚      
			if (!tl_nav.isActive()) {
				tl_nav.reverse();
			}
		} else if (delta < 0) {
			// 向下滚
			if (!tl_nav.isActive()) {
				tl_nav.play();
			}
		}
	}

});
$(".cir-nav").click(function() {
  // $("body").css("width",$("body").width()-1);
	tl_nav.reverse();
});


//window.getComputedStyle(document.querySelector('.subpage-img','::before'))

//document.documentElement.style.setProperty()
document.documentElement.style.setProperty('--subpageImgWidth', $('.subpage-img').width()+'px');

});