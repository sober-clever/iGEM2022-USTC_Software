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

var controller = new ScrollMagic.Controller();
gsap.registerPlugin(MotionPathPlugin);
gsap.to(".title", { y: 0, ease: "bounce", duration: 1 })
var path1 = gsap.to("#bubble1", {
	delay: 0,
	ease: "none",
	motionPath: {
		path: "#path1",
		align: "#path1",
		autoRotate: false,
		alignOrigin: [0.5, 0.5]
	}
});


var nav_scene = new ScrollMagic.Scene({
	triggerHook: 0,
	triggerElement: "#content"
}).setTween(gsap.to("#nav", { y: 0, duration: 0.5 }))
	.setClassToggle(".class-change", "active")
	.addTo(controller);

nav_scene.on("enter", function () { $("#progress").attr("width", "110"); $("#progress").attr("height", "110"); });
nav_scene.on("leave", function () { $("#progress").attr("width", "0"); $("#progress").attr("height", "0"); });

var scene1 = new ScrollMagic.Scene({
	triggerHook: 0,
	duration: $("#content").height() - $(window).height() + $("footer").height(),
	triggerElement: "#content"
})
	.addTo(controller);
scene1.on("progress", function () { process2Angle(($(document).scrollTop() - $("#top").height()) / scene1.duration()); });
scene1.on("leave", function () { process2Angle(0.999) });

var scene2 = new ScrollMagic.Scene({
	triggerElement: "#part03"
})
	.reverse(false)
	.addTo(controller)
	.setClassToggle(".sub-title", "active")
	


	var meshPath1 = gsap.to("#mesh-ball1", {
		delay: 0,
		ease: "none",
		motionPath: {
			path: "#mesh-path1",
			align: "#mesh-path1",
			autoRotate: false,
			alignOrigin: [0.5, 0.5]
		}
	});
	var meshBall1 = new ScrollMagic.Scene({
		triggerHook: 0.5,
		duration:($("#mesh-below").offset().top- $("#polygonal-mesh").offset().top )*0.5
	}).setTween(meshPath1)
		.addTo(controller)
		 
	meshBall1.triggerElement("#polygonal-mesh");
	
	var meshPath2 = gsap.to("#mesh-ball2", {
		delay: 0,
		ease: "none",
		motionPath: {
			path: "#mesh-path2",
			align: "#mesh-path2",
			autoRotate: false,
			alignOrigin: [0.5, 0.5]
		}
	});
	var meshBall2 = new ScrollMagic.Scene({
		triggerHook: 0.5,
		duration:($("#mesh-below").offset().top- $("#polygonal-mesh").offset().top )*0.5
	}).setTween(meshPath2)
		.addTo(controller)
		 
	meshBall2.triggerElement("#polygonal-mesh");
	
	var meshPath3 = gsap.to("#mesh-ball3", {
		delay: 0,
		ease: "none",
		motionPath: {
			path: "#mesh-path3",
			align: "#mesh-path3",
			autoRotate: false,
			alignOrigin: [0.5, 0.5]
		}
	});
	var meshBall3 = new ScrollMagic.Scene({
		triggerHook: 0.5,
		duration:($("#mesh-below").offset().top- $("#polygonal-mesh").offset().top )*0.5
	}).setTween(meshPath3)
		.addTo(controller)
		 
	meshBall3.triggerElement("#polygonal-mesh");
	
	var meshPath4 = gsap.to("#mesh-ball4", {
		delay: 0,
		ease: "none",
		motionPath: {
			path: "#mesh-path4",
			align: "#mesh-path4",
			autoRotate: false,
			alignOrigin: [0.5, 0.5]
		}
	});
	var meshBall4 = new ScrollMagic.Scene({
		triggerHook: 0.5,
		duration:($("#mesh-below").offset().top- $("#polygonal-mesh").offset().top )*0.5
	}).setTween(meshPath4)
		.addTo(controller)
		 
	meshBall4.triggerElement("#polygonal-mesh");
	
	

function refresh() {
	controller = new ScrollMagic.Controller();
	path1 = gsap.to("#bubble1", {
		delay: 0,
		ease: "none",
		motionPath: {
			path: "#path1",
			align: "#path1",
			autoRotate: false,
			alignOrigin: [0.5, 0.5]
		}
	});
	scene1 = new ScrollMagic.Scene({
		triggerHook: 0,
		duration: $("#content").height() - $(window).height() + $("footer").height(),
		triggerElement: "#content"
	})
		.addTo(controller);
	scene1.on("progress", function () { process2Angle(($(document).scrollTop() - $("#top").height()) / scene1.duration()); });
	scene1.on("leave", function () { process2Angle(0.999) });


	nav_scene = new ScrollMagic.Scene({
		triggerHook: 0,
		triggerElement: "#content"
	}).setTween(gsap.to("#nav", { y: 0, duration: 0.5 }))
		.setClassToggle(".class-change", "active")
		 
		.addTo(controller);

	nav_scene.on("enter", function () { $("#progress").attr("width", "110"); $("#progress").attr("height", "110"); });
	nav_scene.on("leave", function () { $("#progress").attr("width", "0"); $("#progress").attr("height", "0"); });

	scene2 = new ScrollMagic.Scene({
		triggerElement: "#part03"
	})
		.reverse(false)
		.addTo(controller)
		.setClassToggle(".sub-title", "active")
	scene3 = new ScrollMagic.Scene({
		triggerHook: 0.5,
		triggerElement: "#Ea"
	})
		.addTo(controller);
		 
	scene3.on("enter", function () {
		tl.play();
	});


	meshPath1 = gsap.to("#mesh-ball1", {
		delay: 0,
		ease: "none",
		motionPath: {
			path: "#mesh-path1",
			align: "#mesh-path1",
			autoRotate: false,
			alignOrigin: [0.5, 0.5]
		}
	});
	meshBall1 = new ScrollMagic.Scene({
		triggerHook: 0.5,
		duration:($("#mesh-below").offset().top- $("#polygonal-mesh").offset().top )*0.5
	}).setTween(meshPath1)
		.addTo(controller);
		 
	meshBall1.triggerElement("#polygonal-mesh");
	
	meshPath2 = gsap.to("#mesh-ball2", {
		delay: 0,
		ease: "none",
		motionPath: {
			path: "#mesh-path2",
			align: "#mesh-path2",
			autoRotate: false,
			alignOrigin: [0.5, 0.5]
		}
	});
	meshBall2 = new ScrollMagic.Scene({
		triggerHook: 0.5,
		duration:($("#mesh-below").offset().top- $("#polygonal-mesh").offset().top )*0.5
	}).setTween(meshPath2)
		.addTo(controller);
	meshBall2.triggerElement("#polygonal-mesh");
	
	meshPath3 = gsap.to("#mesh-ball3", {
		delay: 0,
		ease: "none",
		motionPath: {
			path: "#mesh-path3",
			align: "#mesh-path3",
			autoRotate: false,
			alignOrigin: [0.5, 0.5]
		}
	});
	meshBall3 = new ScrollMagic.Scene({
		triggerHook: 0.5,
		duration:($("#mesh-below").offset().top- $("#polygonal-mesh").offset().top )*0.5
	}).setTween(meshPath3)
		.addTo(controller)
	meshBall3.triggerElement("#polygonal-mesh");
	
	meshPath4 = gsap.to("#mesh-ball4", {
		delay: 0,
		ease: "none",
		motionPath: {
			path: "#mesh-path4",
			align: "#mesh-path4",
			autoRotate: false,
			alignOrigin: [0.5, 0.5]
		}
	});
	meshBall4 = new ScrollMagic.Scene({
		triggerHook: 0.5,
		duration:($("#mesh-below").offset().top- $("#polygonal-mesh").offset().top )*0.5
	}).setTween(meshPath4)
		.addTo(controller)
		
	meshBall4.triggerElement("#polygonal-mesh");
}

const debounce = (fn, delay) => {
	let timer;
	return function () {
		if (timer) {
			clearTimeout(timer);
		}
		timer = setTimeout(() => {
			controller = controller.destroy(true);
			nav_scene = nav_scene.destroy(true);
			scene1 = scene1.destroy(true);
			scene2 = scene2.destroy(true);
			scene3 = scene3.destroy(true);
			meshBall1 = meshBall1.destroy(true);
			meshBall2 = meshBall2.destroy(true);
			meshBall3 = meshBall3.destroy(true);
			meshBall4 = meshBall4.destroy(true);
			fn();

		}, delay);
	}
};

const cancalDebounce = debounce(refresh, 500);
window.addEventListener('resize', cancalDebounce);




var pathLength2 = document.getElementById('path7').getTotalLength();
var pathLength1 = document.getElementById('path6').getTotalLength();

gsap.registerPlugin(MotionPathPlugin);
var myEase = CustomEase.create("custom", "M0,0 C0.769,0.41 0.959,0.502 0.987,0.55 0.998,0.567 0.987,0.93 1,1 ");

var tl = gsap.timeline();
tl.to("#path7", { strokeDashoffset: 0,duration:1, ease: myEase });
tl.to("#path6", { strokeDashoffset: 0, duration:1,ease: myEase }, ">");
tl.to("#path7", { strokeDasharray: "3%,3%",duration:1, ease: "power1.out" }, "<");
tl.to("#down-arrow",{y:250,duration:1,ease:"bounce"},">");
tl.pause();
var scene3 = new ScrollMagic.Scene({
	triggerHook: 0.5,
	triggerElement: "#Ea"
})
	.addTo(controller)
	
scene3.on("enter", function () {
	tl.play();
});