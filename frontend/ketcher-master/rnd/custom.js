if(!window.rnd){
    throw new Error("rnd should be defined prior to loading this file");
}

rnd.custom = [];


//var countCustomGroups=0;
setTimeout(function(){
	
	var buttonlist=[];
	for(let i=0;i<4;i++){
		var newbutton = document.createElement("td");
		newbutton.className="toolButton buttonDisabled";
		//newbutton.style.width='32px';
		newbutton.style.textAlign='center';
		newbutton.style.fontSize='1.2rem'
		 //toolButtonCell toolButton stateButton modeButton sideButton
		newbutton.setAttribute('selid',('custom_'+i))  ;
		newbutton.id = 'custom_'+i;
		newbutton.appendChild(document.createTextNode(i+1));
		$('main_toolbar').appendChild(newbutton);
		buttonlist[i]=newbutton;
	}
	
	if(localStorage.getItem('count') != '0'){
		let effectiveButtonList=[];
	for(let i = 0; i < parseInt(localStorage.getItem('count')); i++){
		rnd.custom[i]={
			name:("Custom group "+(i+1)),
			molfile:localStorage.getItem('custom_'+i) ,
			bid: 0,
			aid: 0
			};
			$('custom_'+i).removeClassName('buttonDisabled');
			effectiveButtonList[i]=buttonlist[i];
	}
effectiveButtonList.each(function (el)
	{
	    ui.initButton(el);
	    if (el.identify() != 'atom_table' && el.identify() != 'atom_reagenerics')
	        el.observe('click', ui.onClick_SideButton); // TODO need some other way, in general tools should be pluggable
	});
}


countCustomGroups=rnd.custom.length;

},700);


