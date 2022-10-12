$(document).ready(function () {
	$("#wiki").click(function(){
        window.location.href="../homepage.html";
    })
    $("#product").click(function(){
        window.location.href="product.html";
    })

    var controller = new ScrollMagic.Controller();
    var tl1 = gsap.timeline();
    tl1.to("#pic1",{opacity:1,y:0,duration:1})
    .to("#title1",{opacity:1,x:0,duration:1},">")
    .to("#passage1",{opacity:1,y:0,duration:1},">")
    .to("#passage1 .text-emphasize",{y:0,duration:0.3,opacity:1,color:"#ff935e"},">+0.3")
    .pause();   
    var scene1 =  new ScrollMagic.Scene({
        triggerHook: 0.8,
	    triggerElement: "#content1"
    }).addTo(controller)
    scene1.on("enter", function () {
        tl1.play();
    });

    var tl2 = gsap.timeline();
    tl2.to("#pic2",{opacity:1,y:0,duration:1})
    .to("#title2",{opacity:1,x:0,duration:1},">")
    .to("#passage2",{opacity:1,y:0,duration:1},">")
    .to("#passage2 .text-emphasize",{y:0,duration:0.3,opacity:1,color:"#ff935e"},">+0.3")
    .pause();   
    var scene2 =  new ScrollMagic.Scene({
        triggerHook: 0.8,
	    triggerElement: "#content2"
    }).addTo(controller)
    scene2.on("enter", function () {
        tl2.play();
    });
    
    var tl3 = gsap.timeline();
    tl3.to("#pic3",{opacity:1,y:0,duration:1})
    .to("#title3",{opacity:1,x:0,duration:1},">")
    .to("#passage3",{opacity:1,y:0,duration:1},">")
    .to("#passage3 .text-emphasize",{y:0,duration:0.3,opacity:1,color:"#ff935e"},">+0.3")
    .pause();   
    var scene3 =  new ScrollMagic.Scene({
        triggerHook: 0.8,
	    triggerElement: "#content3"
    }).addTo(controller)
    scene3.on("enter", function () {
        tl3.play();
    });

    var tl4 = gsap.timeline();
    tl4.to("#pic4",{opacity:1,y:0,duration:1})
    .to("#title4",{opacity:1,x:0,duration:1},">")
    .to("#passage4",{opacity:1,y:0,duration:1},">")
    .to("#passage4 .text-emphasize",{y:0,duration:0.3,opacity:1,color:"#ff935e"},">+0.3")
    .pause();   
    var scene4 =  new ScrollMagic.Scene({
        triggerHook: 0.8,
	    triggerElement: "#content4"
    }).addTo(controller)
    scene4.on("enter", function () {
        tl4.play();
    });

    var tl5 = gsap.timeline();
    tl5.to("#pic5",{opacity:1,y:0,duration:1})
    .to("#title5",{opacity:1,x:0,duration:1},">")
    .to("#passage5",{opacity:1,y:0,duration:1},">")
    .to("#passage5 .text-emphasize",{y:0,duration:0.3,opacity:1,color:"#ff935e"},">+0.3")
    .pause();   
    var scene5 =  new ScrollMagic.Scene({
        triggerHook: 0.8,
	    triggerElement: "#content5"
    }).addTo(controller)
    scene5.on("enter", function () {
        tl5.play();
    });

    var tl6 = gsap.timeline();
    tl6.to(".Title-show",{y:0,opacity:1,duration:0.5})
    .to(".Title-hidden",{x:0,opacity:1,duration:0.5},">")
    .to(".title-hilight",{color:"#38a750",duration:0.3},">")
    .to("#main-img",{x:0,duration:0.5,opacity:1},"<")
    .to(".welcome",{x:0,opacity:1,duration:0.5},">")
    .to("#title-team-name",{color:"#38a750",duration:0.5},">")
    .to("#title-react",{color:"#6a97fd",duration:0.5},">")
    .to(".describe-icon",{duration:0.5,scale:1},">")
    .to(".describe-title",{duration:0.3,x:0},"<")
    .to(".describe-content",{duration:0.3,x:0},"<")
    .to(".describe-icon",{duration:0.5,color:"#68bfad"},">")
    .to(".describe-title-another",{duration:0.7,opacity:1,x:0},"<")
    .to(".describe-hilight",{duration:0.5,color:"#38a750"},">")
    var tl_nav = gsap.timeline();
    tl_nav.to("nav",{opacity:0,y:-20,duration:0.5})
    .to(".cir-nav",{opacity:1,x:0,duration:0.2},">")
    .pause();
    var i;
    for(i=1;i<=5;i++){
        new ScrollMagic.Scene({
            triggerElement:"#pic"+i,
            triggerHook:0.5,
            duration:$("#pic"+i).height()*0.5
        }).setTween(gsap.to("#anim-pic"+i, {y:60, ease: "none",duration:1}))
        .addTo(controller)
    }

    nav_scene = new ScrollMagic.Scene({
        triggerHook: 0,
        triggerElement: "#content"
    }).setTween(gsap.to("#nav", { y: 0, duration: 0.5 }))
        .setClassToggle(".class-change", "active")
        .addTo(controller);
    
    nav_scene.on("enter", function () { $("#progress").attr("width", "110"); $("#progress").attr("height", "110"); });
    nav_scene.on("leave", function () { $("#progress").attr("width", "0"); $("#progress").attr("height", "0"); });
    
    var scene6 = new ScrollMagic.Scene({
        triggerHook: 0,
        duration: $("#content").height() - $(window).height() + $("#enter-footer").height() - 1,
        triggerElement: "#content"
    })
        .addTo(controller);
    scene6.on("progress", function () {process2Angle(($(document).scrollTop() - $("#enter").height() - $("#nav").height() - parseInt($(".content").css("margin-top"))) / scene6.duration())});
    scene6.on("leave", function () { process2Angle(0.999) });

    process2Angle = function (process) {
        var angle = process * Math.PI * 2;
        if (process >= 0.5)
            majorArcFlag = 1;
        else
            majorArcFlag = 0;
        fx = (55 + Math.cos(Math.PI / 2 - angle) * 50).toFixed(3);
        fy = (55 - Math.sin(Math.PI / 2 - angle) * 50).toFixed(3);
        $("#path").attr("d", "M55,5 A50,50 0 " + majorArcFlag.toString() + ",1 " + fx.toString() + "," + fy.toString());
    }

    $(document).on("mousewheel DOMMouseScroll", function (e) {
        var delta = (e.originalEvent.wheelDelta && (e.originalEvent.wheelDelta > 0 ? 1 : -1)) ||  // chrome & ie
                    (e.originalEvent.detail && (e.originalEvent.detail > 0 ? -1 : 1));              // firefox
        s = $(window).scrollTop();
        if(s >= ($("#enter").height() - $("nav").height())){
            if (delta > 0) {
                // 向上滚      
                if(!tl_nav.isActive()){
                    tl_nav.reverse();
                }
            } else if (delta < 0) {
                 // 向下滚
                 if(!tl_nav.isActive()){
                    tl_nav.play(); 
                 }
            }
        }
    });
    $(".cir-nav").click(function(){
        tl_nav.reverse();
    });


	$('.navbar-toggler').click(function(){
		if($('button.navbar-toggler').hasClass('collapsed')){
			$('button.navbar-toggler').removeClass('collapsed');
			$('button.navbar-toggler').attr('aria-expanded','false');
			$('#navbarCollapse').removeClass('show');
			$('#navbarCollapse').css('display','none');
			$('.dropdown-toggle').off('mouseover',phonedropdownover);
			$('.dropdown-toggle').off('mouseout',phonedropdownout);
			$('ul.dropdown-menu').removeAttr('style');
		}else{
			$('button.navbar-toggler').addClass('collapsed');
			$('#navbarCollapse').css('display','inline-block');
			$('ul.dropdown-menu').css('display','none');
			$('.dropdown-toggle').on('mouseover',phonedropdownover);
			$('.dropdown-toggle').on('mouseout',phonedropdownout);
		}
		
	});
 
	function phonedropdownover(){
		this.nextElementSibling.style.display='inline-block';
	}
	
	function phonedropdownout(){
		this.nextElementSibling.style.display='none';
	}

window.addEventListener('resize',function(){
	if(document.body.clientWidth>576){
		$('.dropdown-toggle').off('mouseover',phonedropdownover);
		$('.dropdown-toggle').off('mouseout',phonedropdownout);
		$('ul.dropdown-menu').removeAttr('style');
	}
});


function refresh() {
    controller = new ScrollMagic.Controller();

    tl1 = gsap.timeline();
    tl1.to("#pic1",{opacity:1,y:0,duration:1})
    .to("#title1",{opacity:1,x:$("#titie1").width()*0.5,duration:1},">")
    .to("#passage1",{opacity:1,y:0,duration:1},">")
    .to("#passage1 .text-emphasize",{y:0,duration:0.3,opacity:1,color:"#ff935e"},">+0.3")
    .pause();   
    scene1 =  new ScrollMagic.Scene({
        triggerHook: 0.8,
	    triggerElement: "#content1"
    }).addTo(controller)
    scene1.on("enter", function () {
        tl1.play();
    });

    tl2 = gsap.timeline();
    tl2.to("#pic2",{opacity:1,y:0,duration:1})
    .to("#title2",{opacity:1,x:0,duration:1},">")
    .to("#passage2",{opacity:1,y:0,duration:1},">")
    .to("#passage2 .text-emphasize",{y:0,duration:0.3,opacity:1,color:"#ff935e"},">+0.3")
    .pause();   
    scene2 =  new ScrollMagic.Scene({
        triggerHook: 0.8,
	    triggerElement: "#content2"
    }).addTo(controller)
    scene2.on("enter", function () {
        tl2.play();
    });
    
    tl3 = gsap.timeline();
    tl3.to("#pic3",{opacity:1,y:0,duration:1})
    .to("#title3",{opacity:1,x:0,duration:1},">")
    .to("#passage3",{opacity:1,y:0,duration:1},">")
    .to("#passage3 .text-emphasize",{y:0,duration:0.3,opacity:1,color:"#ff935e"},">+0.3")
    .pause();   
    scene3 =  new ScrollMagic.Scene({
        triggerHook: 0.8,
	    triggerElement: "#content3"
    }).addTo(controller)
    scene3.on("enter", function () {
        tl3.play();
    });

    tl4 = gsap.timeline();
    tl4.to("#pic4",{opacity:1,y:0,duration:1})
    .to("#title4",{opacity:1,x:0,duration:1},">")
    .to("#passage4",{opacity:1,y:0,duration:1},">")
    .to("#passage4 .text-emphasize",{y:0,duration:0.3,opacity:1,color:"#ff935e"},">+0.3")
    .pause();   
    scene4 =  new ScrollMagic.Scene({
        triggerHook: 0.8,
	    triggerElement: "#content4"
    }).addTo(controller)
    scene4.on("enter", function () {
        tl4.play();
    });

    tl5 = gsap.timeline();
    tl5.to("#pic5",{opacity:1,y:0,duration:1})
    .to("#title5",{opacity:1,x:0,duration:1},">")
    .to("#passage5",{opacity:1,y:0,duration:1},">")
    .to("#passage5 .text-emphasize",{y:0,duration:0.3,opacity:1,color:"#ff935e"},">+0.3")
    .pause();   
    scene5 =  new ScrollMagic.Scene({
        triggerHook: 0.8,
	    triggerElement: "#content5"
    }).addTo(controller)
    scene5.on("enter", function () {
        tl5.play();
    });
    var i;
    for(i=1;i<=5;i++){
        new ScrollMagic.Scene({
            triggerElement:"#pic"+i,
            triggerHook:0.5,
            duration:$("#pic"+i).height()*0.5
        }).setTween(gsap.to("#anim-pic"+i, {y:60, ease: "none",duration:1}))
        .addTo(controller)
    }

    nav_scene = new ScrollMagic.Scene({
        triggerHook: 0,
        triggerElement: "#content"
    }).setTween(gsap.to("#nav", { y: 0, duration: 0.5 }))
        .setClassToggle(".class-change", "active")
        .addTo(controller);
    
    nav_scene.on("enter", function () { $("#progress").attr("width", "110"); $("#progress").attr("height", "110"); });
    nav_scene.on("leave", function () { $("#progress").attr("width", "0"); $("#progress").attr("height", "0"); });
    
    scene6 = new ScrollMagic.Scene({
        triggerHook: 0,
        duration: $("#content").height() - $(window).height() + $("#enter-footer").height() - 1,
        triggerElement: "#content"
    })
        .addTo(controller);
    scene6.on("progress", function () {process2Angle(($(document).scrollTop() - $("#enter").height() - $("#nav").height() - parseInt($(".content").css("margin-top"))) / scene6.duration())});
    scene6.on("leave", function () { process2Angle(0.999) });
}

const debounce = (fn, delay) => {
	let timer;
	return function () {
		if (timer) {
			clearTimeout(timer);
		}
		timer = setTimeout(() => {
			controller = controller.destroy(true);
            scene1 = scene1.destroy(true);
            scene2 = scene2.destroy(true);
            scene3 = scene3.destroy(true);
            scene4 = scene4.destroy(true);
            scene5 = scene5.destroy(true);
            scene6 = scene6.destroy(true);
            nav_scene = nav_scene.destroy(true);
			fn();

		}, delay);
	}
};

const cancalDebounce = debounce(refresh, 500);
window.addEventListener('resize', cancalDebounce);



});