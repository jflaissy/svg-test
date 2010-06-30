# -*- coding: utf-8 -*-
"""Module de recalibrage des captures d'ecran."""
import Image
import random


def go(input_file, output_prefix, parameters=None):
	"""Il detecte les coordonnees et la taille du rectangle rouge entourant l'image svg,
	puis il recherche les coordonnees de l'image svg a l'interieur de la zone rouge
	et enfin il enregistre le rendu de l'image svg dans une nouvelle image """
	print 'Postprocessing statique in:', input_file, 'output_p:', output_prefix
	#chargement image
	im = Image.open(input_file)

	#parametres generaux
	(width,height)= im.size#largeur et hauteur du screenshot
	pix=im.load()#objet d'acces des pixels
	pas=2#pas de recherche de la zone rouge
	colorref=[221,0,0]#couleur de references[rouge,vert,bleu]

	#parametres detection zone rouge
	posyr=0
	zoneRougeTrouve= 0
	n=0
	pas=2#pas de recherche de la zone rouge
	poshyr=0#ordonnee segment superieur cadre rouge
	posbyr=0#ordonnee segment inferieur cadre rouge
	posgxr=0#abscisse segment lateral gauche cadre rouge
	posdxr=0#abscisse segment lateral droit cadre rouge

	#parametres detection image svg
	zoneImageTrouve= 0
	poshyi= 0#ordonnee segment superieur image svg
	posbyi= 0#ordonnee segment inferieur image svg
	posgxi= 0#abscisse segment lateral gauche image svg
	posdxi= 0#abscisse segment lateral droit image svg

	#recherche zone rouge et abscisse segment lateral gauche cadre rouge
	while(zoneRougeTrouve==0):
		posyr=random.randint(1,height-1)
		posgxr=0
		color= pix[posgxr,posyr]
		while(posgxr+pas<width):
			if(color[0]==colorref[0] and color[1]==colorref[1] and color[2]==colorref[2]):
				zoneRougeTrouve=1
				break
			posgxr=posgxr+pas
			color= pix[posgxr,posyr]
		if n>400 :
			output= "%s.bmp" % output_prefix
			im.save(output)
			return output
		n=n+1

	#recherche ordonnee segment superieur cadre rouge
	poshyr=posyr
	while(color[0]==colorref[0] and color[1]==colorref[1] and color[2]==colorref[2] and poshyr-pas>0):
		poshyr=poshyr-pas

		color= pix[posgxr,poshyr]
	poshyr=poshyr+pas

	#recherche ordonnee segment inferieur cadre rouge
	posbyr=posyr
	color= pix[posgxr,posbyr]
	while(color[0]==colorref[0] and color[1]==colorref[1] and color[2]==colorref[2] and posbyr+pas<height):
		posbyr=posbyr+pas
		color= pix[posgxr,posbyr]
	posbyr=posbyr-pas

	#recherche abscisse segment lateral droit cadre rouge
	posdxr=posgxr
	color= pix[posdxr,poshyr]
	while(color[0]==colorref[0] and color[1]==colorref[1] and color[2]==colorref[2] and posdxr+pas<width):
		posdxr=posdxr+pas
		color= pix[posdxr,poshyr]
	posdxr=posdxr-pas

	#parmetres image svg
	poshyi= poshyr
	posbyi= posbyr
	posgxi=posgxr
	posdxi=posdxr

	#recherche zone image svg et abscisse segment lateral gauche image svg
	while(zoneImageTrouve==0):
		posyi=random.randint(poshyi,posbyi)
		posgxi=posgxr
		color= pix[posgxi,posyi]
		while(posgxi+1<posdxi):
			if(not (color[0]==colorref[0] and color[1]==colorref[1] and color[2]==colorref[2])):
				zoneImageTrouve=1
				break
			posgxi=posgxi+1
			color= pix[posgxi,posyi]

	#recherche ordonnee segment superieur image svg
	poshyi=posyi
	color= pix[posgxi,poshyi]
	while(not (color[0]==colorref[0] and color[1]==colorref[1] and color[2]==colorref[2])):
		poshyi=poshyi-1
		color= pix[posgxi,poshyi]
	poshyi=poshyi+1
	#recherche ordonnee segment inferieur image svg
	posbyi=posyi
	color= pix[posgxi,posbyi]
	while(not (color[0]==colorref[0] and color[1]==colorref[1] and color[2]==colorref[2])):
		posbyi=posbyi+1
		color= pix[posgxi,posbyi]
	posbyi=posbyi-1

	#recherche abscisse segment lateral droit image svg
	posdxi=posgxi
	color= pix[posdxi+1,posbyi]
	while(not (color[0]==colorref[0] and color[1]==colorref[1] and color[2]==colorref[2])):
		posdxi=posdxi+1
		color= pix[posdxi,posbyi]
	posdxi=posdxi-1

	#Recuperation de l'image svg
	box = (posgxi, poshyi, posdxi, posbyi)
	imout = im.crop(box)
	output= "%s.bmp" % output_prefix
	imout.save(output)
	return output
