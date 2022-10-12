


$(document).ready(function () {
	$(".dropdown").mouseover(function () {
		$(".dropdown").children(".dropdown-toggle").addClass("show");
		$(".dropdown").children(".dropdown-toggle").attr("aria-expanded", "true");
		$(".dropdown").children(".dropdown-menu").addClass("show");
		$(".dropdown").children(".dropdown-menu").attr("data-bs-popper", "none");
	})
	$(".navbar").mouseout(function () {
		$(".dropdown").children(".dropdown-toggle").removeClass("show");
		$(".dropdown").children(".dropdown-toggle").attr("aria-expanded", "false");
		$(".dropdown").children(".dropdown-menu").removeClass("show");
		$(".dropdown").children(".dropdown-menu").attr("data-bs-popper", "false");
	})

	var goDown = function () {
		if ($(window).scrollTop() < 10 && event.deltaY > 0) {
			event.preventDefault();
			var content = $('#content').offset().top;
			window.scrollTo({
				top: content,
				behavior: "smooth"
			});
		}
		else {

		}
	};

	document.getElementById('top').addEventListener('wheel', goDown, false);
});



