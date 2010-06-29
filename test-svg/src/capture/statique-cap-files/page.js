//window.onload=initialize();

function initialize(){
	var hauteur = 700;
	var largeur=1000; 
	window.innerHeight=hauteur;
	window.innerWidth=largeur;
	var largeur_image=document.getElementById('cadre').offsetWidth;
	var hauteur_image=document.getElementById('cadre').offsetHeight;
	document.getElementById('cadre').style.left=(largeur/2-largeur_image/2)+"px";
	document.getElementById('cadre').style.top=(hauteur/2-hauteur_image/2)+"px";

	}