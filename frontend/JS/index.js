
$(".dropdown").mouseover(function(){
  $(".dropdown").children(".dropdown-toggle").addClass("show");
  $(".dropdown").children(".dropdown-toggle").attr("aria-expanded","true");
  $(".dropdown").children(".dropdown-menu").addClass("show");
  $(".dropdown").children(".dropdown-menu").attr("data-bs-popper","none");
})
$(".navbar").mouseout(function(){
  $(".dropdown").children(".dropdown-toggle").removeClass("show");
  $(".dropdown").children(".dropdown-toggle").attr("aria-expanded","false");
  $(".dropdown").children(".dropdown-menu").removeClass("show");
  $(".dropdown").children(".dropdown-menu").attr("data-bs-popper","false");
})      

$(window).scroll(function(){
  var height=document.documentElement.scrollTop;
  if(height>=100){
    $("#go-top").css("display","block");
  }
  else{
    $("#go-top").css("display","none");
  }
})
$("#go-top").click(function(){
  window.scrollTo({
    top:0,
    behavior:"smooth"
  })
})



var menuLeft = document.querySelector(".left-menu");
$('.our-logo').css('height',menuLeft.clientWidth);
menuLeft.style.height = $(window).height().toString() + "px";
$('.progress-container').css('height',menuLeft.clientHeight - menuLeft.clientWidth);

$('.part-circ')[0].style.top = (0.1 * $('.progress-container').height()+menuLeft.clientWidth).toString() + "px";
for(i = 1;i < $('.part-circ').length - 1; i++)
  $('.part-circ')[i].style.top = ((0.1 + (i / ($('.part-circ').length - 1)) * 0.8) * $('.progress-container').height() + menuLeft.clientWidth).toString() + "px";
$('.part-circ')[$('.part-circ').length - 1].style.top = (0.9 * $('.progress-container').height() + menuLeft.clientWidth).toString() + "px";


var controller = new ScrollMagic.Controller();

var pinScene = new ScrollMagic.Scene({
  duration: $("body").height() - $("footer").height() - $(window).height()
}).setPin(menuLeft, {pushFollowers: false}).addTo(controller);

var tweenH = 0.1 * $('.progress-container').height();

new ScrollMagic.Scene({
  triggerHook: 0.1,
  duration: $('.intro').outerHeight() + $('#nav').outerHeight() - 0.1 * $(window).height()
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


function refresh(){
  $('.our-logo').css('height',menuLeft.clientWidth);
  menuLeft.style.height = $(window).height().toString() + "px";
  $('.progress-container').css('height',menuLeft.clientHeight - menuLeft.clientWidth);
  
  $('.part-circ')[0].style.top = (0.1 * $('.progress-container').height()+menuLeft.clientWidth).toString() + "px";
  for(i = 1;i < $('.part-circ').length - 1; i++)
    $('.part-circ')[i].style.top = ((0.1 + (i / ($('.part-circ').length - 1)) * 0.8) * $('.progress-container').height() + menuLeft.clientWidth).toString() + "px";
  $('.part-circ')[$('.part-circ').length - 1].style.top = (0.9 * $('.progress-container').height() + menuLeft.clientWidth).toString() + "px";
  
  //ScrollMagic
  controller = new ScrollMagic.Controller();
  
  pinScene = new ScrollMagic.Scene({
    duration: $("body").height() - $("footer").height() - $(window).height()
  }).setPin(menuLeft, {pushFollowers: false}).addTo(controller);
  
  tweenH = 0.1 * $('.progress-container').height();
  
  new ScrollMagic.Scene({
    triggerHook: 0.1,
    duration: $('.intro').outerHeight() + $('#nav').outerHeight() - 0.1 * $(window).height()
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
}
function leftMenuChange(){
  if($(window).width()<=576){
    $(".left-menu").addClass("col-3")
    $(".left-menu").removeClass("col-2") 
    $(".main-body").addClass("col-9")
    $(".main-body").removeClass("col-10")
  }
  else{
    $(".left-menu").addClass("col-2")
    $(".left-menu").removeClass("col-3")
    $(".main-body").addClass("col-10")
    $(".main-body").removeClass("col-9")
  }
}

const debounce = (fn, delay) => {
  let timer;
  return function () {
    if (timer) {
      clearTimeout(timer);
    }
    timer = setTimeout(() => {

      leftMenuChange();
      controller = controller.destroy(true);
      pinScene = pinScene.destroy(true);      
      fn();

    }, delay);
  }
};
const cancalDebounce = debounce(refresh, 500);
window.addEventListener('resize', cancalDebounce);
