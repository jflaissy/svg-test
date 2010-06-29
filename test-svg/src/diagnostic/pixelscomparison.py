"""Module de comparaison d'image pixel par pixel."""
# -*- coding: utf-8 -*-

import Image

def go(comparison, output_prefix, diagnostic):
    """Il compare une capture avec une image de reference s'il y en a une(mode "separate")
    ou avec une autre capture(mode "les uns contres les autres")"""
    print 'Diagnostic Pixel à Pixel. '
    input_file1=comparison['instances'][0]['postprocessing']['output']
    #choix de la deuxieme image
    if(len(comparison['instances'])>1):
        input_file2=comparison['instances'][1]['postprocessing']['output']
    else:
        input_file2=diagnostic['reference']
    
    im1 = Image.open(input_file1)
    im2 = Image.open(input_file2)
    nbPixelErreur=0
    
    pixels1=im1.getdata()
    pixels2=im2.getdata()
    
    #test si la taille des images est la même
    if(im1.size!=im2.size or im1.getbands()!=im2.getbands()):
        comparison['result'] = { 'valid' : False,
                                 'message' : 'taille des images differente' }
        return
    #compare les images pixel a pixel
    for i in range(len(pixels1)):
        if(pixels1[i]!=pixels2[i]):
            nbPixelErreur=nbPixelErreur+1
    #exporte le resultat
    if nbPixelErreur>0:
        comparison['result'] = { 'valid' : False,
                                 'message' : 'nombre de pixels differents : %s' % nbPixelErreur }
    else:
        comparison['result'] = { 'valid': True,
                                 'message': 'Egalité pixel à pixel.' }
