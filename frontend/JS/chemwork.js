$(document).ready(function(){
	var sample = [];
	var secSample = {
		km1_range:[0,100000],
		km2_range:[0,100000],
		kcat1_range:[0,100000],
		kcat2_range:[0,100000]
	};
	// for(var i = 0; i < 39 ; i++){
	// 	sample[i] = {};
	// 	sample[i].ECnum = 'EC.'+ i + '.' + i + '.' + i + '.' + i;
	// 	sample[i].name = 'Enzymeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee' + (i+1);
	// 	sample[i].link = ['BRENDA' + (i+1),'Uniprot' + (i+1),'PDB' + (i+1),'PubMed' + (i+1)];
	// 	sample[i].percent = (100 - i*2.5)+'%';
	// 	sample[i].nearestReact = "C1CCCCC1CCCCCCCCCCCCCCCC>>C1CCC(=O)C1";
	// 	sample[i].organism = "Classssss";
	// 	sample[i].ph = (6.8 + 0.01 * i).toFixed(2);
	// 	sample[i].temper = 37;
	// 	if(i % 2 == 0)
	// 	sample[i].cofactor = false;
	// 	else
	// 	sample[i].cofactor = "NADP+";
	// }

var ECcode;
var cofact;
	const resultApp = {
		data() {
			return {
				Data: {
					response : sample,
					flag : 0,
					seen : true,
					choice : true,
					display : false,
					second : false,
					secRes : secSample
				}
			}
		},
		methods:{
			length(){
				if(this.Data.flag * 10 > this.Data.response.length){
        			this.Data.seen = false;
        			this.Data.flag = this.Data.response.length / 10;
    			}
    		flag = this.Data.flag;
    		if(!this.Data.choice){
    			setTimeout(function(){svgRender(10 * flag)},700);
    		}
    		else{
        		setTimeout(listRerender,70);
    		}
    		},
    		radioCheck(){
      			this.Data.choice = $("#cards")[0].checked;
      			if(!this.Data.choice){
        		setTimeout(function(){svgRender(10 * flag)},700);
				$("#modeId").html("Card")
      		}
			else{
				$("#modeId").html("List")
			}

    		},
			showSecRec(button){
				if($(button.target).html() == "Show" || $(button.target).html() == "Show Auxiliary Reaction"){
					$(".secRecBtn").html("Show")
					$(".window-out .ph-choice").empty();
					$(".window-out .temp-choice").empty();
					$(".window-out .sec-choice").empty();
					var index = $("tbody .result-item").index($(button.target).parent().parent());
					ECcode = this.Data.response[index].ECnum;
					cofact = this.Data.response[index].cofactor
					var l = this.Data.response[index].substrate_info.length;
					for(j = 0;j < l; j++){
						$(".window-out .sec-choice").append($("<option></option>").html(this.Data.response[index].substrate_info[j]));
					}
					arr = this.Data.response[index].ph.flat();
					l = arr.length;
					for(j = 0;j < l; j++){
						$(".window-out .ph-choice").append($("<option></option>").html(arr[j].toString()));
					}
					arr = this.Data.response[index].temper.flat();
					l = arr.length;
					for(j = 0;j < l; j++){
						$(".window-out .temp-choice").append($("<option></option>").html(arr[j].toString()));
					}
					$(button.target).parent().append($(".window-out"));
					$(".window-out").css("left",'').css("display","block").css("position","absolute").css("right","5%");
					$(button.target).html("Hide");
				}
				else{
					$(".window-out").css("display","none").css("right",'');
					$(button.target).html("Show");
				}
			},
			showSecRecCard(button){
				if($(button.target).html() == "Show Auxiliary Reaction"){
					$(".btn-sec-card").html("Show Auxiliary Reaction");
					$(".window-out .sec-choice").empty();
					$(".window-out .temp-ph-choice").empty();
					var index = $("#result-card-list .card").index($(button.target).parent().parent().parent().parent());
					var l = this.Data.response[index].substrate_info.length;
					for(j = 0;j < l; j++){
						$(".window-out .sec-choice").append($("<option></option>").html(this.Data.response[index].substrate_info[j]));
					}
					arr = this.Data.response[index].ph.flat();
					l = arr.length;
					for(j = 0;j < l; j++){
						$(".window-out .ph-choice").append($("<option></option>").html(arr[j].toString()));
					}
					arr = this.Data.response[index].temper.flat();
					l = arr.length;
					for(j = 0;j < l; j++){
						$(".window-out .temp-choice").append($("<option></option>").html(arr[j].toString()));
					}
					$(button.target).parent().append($(".window-out"));
					$(".window-out").css("right",'').css("display","block").css("position","absolute").css("left","20%").css("z-index","114");
					$(button.target).html("Hide Auxiliary Reaction");
				}
				else{
					$(".window-out").css("display","none").css("left",'');
					$(button.target).html("Show Auxiliary Reaction");
				}
			},
			nameRender(){
				if($("input#Max-radio").prop("checked")){
					for(var i = 0; i < $(".enzyme-name").length; i++){
						if($(".enzyme-name")[i].className.search(/maximum/) == -1)
						  $(".enzyme-name")[i].className += " maximum";
				}
			}
				else{
					for(var i = 0; i < $(".enzyme-name").length; i++){
						if($(".enzyme-name")[i].className.search(/maximum/) != -1){
							$(".enzyme-name")[i].className = "enzyme-name";
					  }
					}
				  }
					},
			nearRender(){
				if($("input#nr-Max-radio").prop("checked")){
					for(var i = 0; i < $(".n-reaction").length; i++){
					  if($(".n-reaction")[i].className.search(/maximum/) == -1)
						$(".n-reaction")[i].className += " maximum";
					}
				}
				else{
					for(var i = 0; i < $(".n-reaction").length; i++){
						if($(".n-reaction")[i].className.search(/maximum/) != -1)
						  $(".n-reaction")[i].className = "n-reaction";
					  }
				}
			},
			kineticShow(button){
				if($(button.target).next().css("display") == "none"){
					$(button.target).next().css("display",'block')
				}
				else{
					$(button.target).next().css("display",'none')
				}
			}
		}
	};
	const vm = Vue.createApp(resultApp).mount('#result');

	function svgRender(flag) { 
		for(var i = 0; i < parseInt(flag); i++){
		  for(var j = 0;j < vm.Data.response[i].nearestReact.length;j++){
		  if(vm.Data.response[i].nearestReact[j] == ">")
			break;
		  }
		var reactantSMILES = vm.Data.response[i].nearestReact.substring(0,j);
		var productSMILES = vm.Data.response[i].nearestReact.substring(j+2);
		var mol = RDKitModule.get_mol(reactantSMILES);
		var dest = document.querySelectorAll(".svg-container")[i];
		var svg = mol.get_svg();
		dest.innerHTML = "<div>" + svg + "</div>" + "<i class='bi bi-arrow-right reaction-arr'></i>";
		mol = RDKitModule.get_mol(productSMILES);
		dest = document.querySelectorAll(".svg-container")[i];
		mol.get_aromatic_form();
		svg = mol.get_svg();
		dest.innerHTML += "<div>" + svg + "</div>";
		}
		}

	var chem = {};
	chem.chemdraw = document.getElementById('chem_search').contentWindow; 
	chem.reactant = document.getElementById('reactant');
	chem.product = document.getElementById('product');
	chem.searchbutton = document.getElementById('search_button');
	chem.typeselect = document.getElementById('type_list');
	chem.value = {};
	chem.value.product = {};
	chem.value.reactant = {};
	chem.value.product.entiretyflag = false;
	chem.value.reactant.entiretyflag = false;
	chem.value.product.partflag = 0;
	chem.value.reactant.partflag = 0;
	chem.value.type = 0;
	chem.value.cofactors = [];
	chem.value.organism = '';
	var nowdraw = true;
	
	chem.changetype = function(type) {
		if(type)
		{
			if(chem.chemdraw.ui.ctab.atoms._map._count == 0){
				chem.value.product.entiretyflag = false;
			}else{
				chem.value.product.entiretyflag = true;
			}
			var product = chem.chemdraw.ui.saveSmilesFile();
			chem.value.product.smiles = product.smiles;
			chem.value.product.reactionAtoms = product.reactionAtoms;
			chem.value.product.partflag = product.count;
		}else{
			if(chem.chemdraw.ui.ctab.atoms._map._count == 0){
				chem.value.reactant.entiretyflag = false;
			}else{
				chem.value.reactant.entiretyflag = true;
			}
			var reactant = chem.chemdraw.ui.saveSmilesFile();
			chem.value.reactant.smiles = reactant.smiles;
			chem.value.reactant.reactionAtoms = reactant.reactionAtoms;
			chem.value.reactant.partflag = reactant.count;
		}
		
		return true;
	}
	
	chem.typeR = function(){
		nowdraw = true;
		return chem.changetype(true);
	}
	
	chem.typeP = function(){
		nowdraw = false;
		return chem.changetype(false);
	}
	
	chem.onClick_searchbutton = function(){
		vm.$data.Data.flag = 0;
		vm.$data.Data.seen = true;
		vm.$data.Data.choice = true;
		vm.$data.Data.display = false;
		$('.text-info').remove();
		$("#search_button").removeClass("is-invalid").removeClass("is-valid");
		$(".invalid").remove();
		$(".valid").remove();
		if(nowdraw == true){
			chem.changetype(false);
		}
		if(nowdraw == false){
			chem.changetype(true);
		}
		
		if(chem.value.product.entiretyflag == false && chem.value.reactant.entiretyflag == false){
			$("#search_button").addClass("is-invalid");
			$("#info-container").append('<div class="invalid mt-2">Please enter compounds.</div>');
			return;
		}
		else{
			if(chem.value.product.entiretyflag == false){
				$("#search_button").addClass("is-invalid");
				$("#info-container").append('<div class="invalid mt-2">Please enter product.</div>');
				return;
			}else if(chem.value.product.partflag == 0){
				$("#search_button").addClass("is-invalid");
				$("#info-container").append('<div class="invalid mt-2">Please select the groups involved in the reaction on the product.</div>');
				return;
			}
			
			if(chem.value.reactant.entiretyflag == false){
				$("#search_button").addClass("is-invalid");
				$("#info-container").append('<div class="invalid mt-2">Please enter reactant.</div>');
				return;
			}else if(chem.value.reactant.partflag == 0){
				$("#search_button").addClass("is-invalid");
				$("#info-container").append('<div class="invalid mt-2">Please select the groups involved in the reaction on the reactant.</div>');
				return;
			}
		}
		
		chem.value.type = chem.typeselect.options[chem.typeselect.selectedIndex].value;
		$("input.cofactors-check:checked").each(function(i, n){ 
			chem.value.cofactors[i] = $(this).val();
		})
		chem.value.organism= $("input#classtype").val()
		if(chem.value.type == 0){
			$("#search_button").addClass("is-invalid");
			$("#info-container").append('<div class="invalid mt-2">Please select the reaction type.</div>')
			return;
		}
		$("#search_button").addClass("is-valid");
		$("#info-container").append('<div class="valid mt-2">OK</div>')
		chem.searchbutton.innerHTML += '<div class="spinner-border" style="color:#0fa0a0; background-color: rgba(25, 135, 84,0.2)"></div>';
		chem.searchbutton.disabled = true;
		 $.ajax({
			url:'http://1.117.223.64:9100/api/prescreen/query',
			type:'post',
			contentType: 'application/json',
			data: JSON.stringify(chem.value),
			success: function(data){
				console.log(JSON.parse(data));
				var repo = JSON.parse(data);
				var j = 0;
				for (let i in repo){
					if(i.search(/[0-9]/) != -1){
						vm.$data.Data.response[j] = {};
						vm.$data.Data.response[j].ECnum = i;
						if(repo[i].kinetic)
							l = repo[i].kinetic.length;
						else
							l = 0;
						if(l == 0){
							vm.$data.Data.response[j].ph = [0];
							vm.$data.Data.response[j].temper = [0];
							vm.$data.Data.response[j].refer = [0];
						}
						else{
							vm.$data.Data.response[j].ph = new Array(l);
							vm.$data.Data.response[j].temper = new Array(l);
							vm.$data.Data.response[j].refer = new Array(l);
							for(k = 0; k<l; k++){
								vm.$data.Data.response[j].ph[k] = JSON.parse(repo[i].kinetic[k][0]);
								vm.$data.Data.response[j].temper[k] = JSON.parse(repo[i].kinetic[k][1]);
								vm.$data.Data.response[j].refer[k] = repo[i].kinetic[k][2];
							}
						}
						vm.$data.Data.response[j].nearestReact = repo[i].most_similar_reaction;
						vm.$data.Data.response[j].percent = repo[i].similarity.toFixed(2);
						vm.$data.Data.response[j].name = repo[i].name ? repo[i].name : "None.";
						vm.$data.Data.response[j].link = repo[i].link ? repo[i].link : ["link","link","link","link"];
						vm.$data.Data.response[j].cofactor = repo[i].cofactor ? repo[i].cofactor : false;
						vm.$data.Data.response[j].substrate_info = repo[i].substrate_info ? repo[i].substrate_info : false;
						j++;
					}
				}
				vm.$data.Data.display = true;
				$("#search_button").removeClass("is-valid");
				$(".valid").remove();
				$("#info-container").append('<div class="text-info mt-2" style="text-align:center">Data returned.</div>')
				chem.searchbutton.innerHTML = 'Search';
				chem.searchbutton.disabled = false;
			},
			error: function(errorMsg){
				$("#search_button").removeClass("is-valid").addClass("is-invalid");
				$(".valid").remove();
				chem.searchbutton.innerHTML = ' &nbsp; Search &nbsp; ';
				chem.searchbutton.disabled = false;
				$("#info-container").append('<div class="invalid mt-2">Network Problem.</div>');
			}
		}) 
		return;
	}
	
	chem.reactionType = function(type){
		chem.value.type = type;
		return true;
	}

	function anotherSearch(){
		second = {};
		vm.$data.Data.second = false;
		second.ph = $(".ph-choice").val();
		second.temp = $(".temp-choice").val();
		second.substrate_info = $(".sec-choice").val();
		second.organism = chem.value.organism;
		second.ec_num = ECcode;
		second.cofactor2 = cofact;
		$(".another-search").attr("disabled",true);
		$(".another-search").append('<div class="spinner-border" style="width:16px; height:16px; color:#0fa0a0; background-color: rgba(25, 135, 84,0.2)"></div>');
		$.ajax({
		url:'http://1.117.223.64:9100/api/prescreen/second_query',
		type:'post',
		contentType: 'application/json',
		data: JSON.stringify(second),
		success:function(data){
		console.log(JSON.parse(data));
		vm.$data.Data.second = true;
		$(".another-search").html("Search!");
		$(".another-search").attr("disabled",false);
		vm.$data.Data.secRes = JSON.parse(data);
		},
	})
	}

	chem.reactant.addEventListener('click',chem.typeR,false);
	chem.product.addEventListener('click',chem.typeP,false);
	chem.searchbutton.addEventListener('click',chem.onClick_searchbutton,false);
	$(".another-search").click(function(){anotherSearch()});
});

$('#go-back').on('mousedown',function(){
	 $(window).on('mousemove',function(e){
		 var Sx =e.clientX;
		 var Sy =e.clientY;
		 var newsx =Sx-$('#go-back').width()/2;
		 var newsy =Sy-$('#go-back').height()/2;
		 $('#go-back').css({left:newsx+'px',top:newsy+'px'})

	 })
});

$('#go-back').on('mouseup',function(){
	$(window).off('mousemove');
});