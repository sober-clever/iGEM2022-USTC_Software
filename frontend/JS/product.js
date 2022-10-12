initRDKitModule().then(function (instance) {
  RDKitModule = instance;
  console.log("version: " + RDKitModule.version());
  setTimeout(function(){document.getElementById('chem_search').contentWindow.$('customize').removeClassName('buttonDisabled');},700);
});
var searchC = document.getElementById("chem_search");
searchC.style.width = ($("#search-frame").width() - 1).toString() + "px";
searchC.style.height = "500px";
function resize(){
  if(parseInt($("#main-container").width() * 5 / 6) <= searchC.clientWidth || parseInt($("#main-container").width() * 5 / 6) <= 900){
    $("#search-frame").attr("class", "row m-0 p-0");
    $("#reactant_or_product").attr("class", "row m-0 pe-3");
    $("#reactant_or_product .selector").attr("class","btn-group-lg selector d-flex justify-content-around");
    $("#reactant_or_product .h4").attr("class","h4 text-center mb-lg-2 mt-lg-2");
    searchC.style.width = ($("#search-frame").width() - 1).toString() + "px";
  }
  else{
    $("#search-frame").attr("class", "col-8 m-0 p-0");
    $("#reactant_or_product").attr("class", "col-4 m-0 pe-0");
    $("#reactant_or_product .selector").attr("class","btn-group-vertical btn-group-lg selector my-lg-5");
    $("#reactant_or_product .h4").attr("class","h4 text-center mb-3 mt-lg-5");
    searchC.style.width = ($("#search-frame").width() - 1).toString() + "px";
  }
  for(i = 0; i < $(".svg-container").length; i++){
    if($(".svg-container")[i].clientHeight * $(window).width()/ 1200 <= 200)
      $(".svg-container")[i].style.transform = "scale(" + ($(window).width()/ 1200).toString() + ")";
    else
    $(".svg-container")[i].style.transform = "scale(1)";
  }
}

resize();
var flag = 0;
const debounce = (fn, delay) => {
    let timer;
    return function () {
      if (timer) {
        clearTimeout(timer);
      }
      timer = setTimeout(() => { 
        fn();
  
      }, delay);
    }
  };
const cancalDebounce = debounce(resize, 500);
window.addEventListener('resize', cancalDebounce);

nameMaximize = function(){
  for(var i = 0; i < $(".enzyme-name").length; i++){
    if($(".enzyme-name")[i].className.search(/maximum/) == -1)
      $(".enzyme-name")[i].className += " maximum";
  }
}

nameMinimize = function(){
  for(var i = 0; i < $(".enzyme-name").length; i++){
    if($(".enzyme-name")[i].className.search(/maximum/) != -1){
        $(".enzyme-name")[i].className = "enzyme-name";
    }
  }
}

nearMaximize = function(){
  for(var i = 0; i < $(".n-reaction").length; i++){
    if($(".n-reaction")[i].className.search(/maximum/) == -1)
      $(".n-reaction")[i].className += " maximum";
  }
}

nearMinimize = function(){
  for(var i = 0; i < $(".n-reaction").length; i++){
    if($(".n-reaction")[i].className.search(/maximum/) != -1)
      $(".n-reaction")[i].className = "n-reaction";
  }
}

listRerender = function(){
  if($("input#Max-radio").prop("checked"))
    nameMaximize();
  else
    nameMinimize();
  if($("input#nr-Max-radio").prop("checked"))
    nearMaximize();
  else
    nearMinimize();
}

// $("input#Max-radio").change(function(){alert($(this).val());nameMaximize();});
// $("input#Min-radio").change(function(){alert($(this).val());nameMinimize();});
$("#nearBtn").click(nearMaximize);
// $(".secRecBtn").on('click',function(){
//   showSecRec(this);
// });