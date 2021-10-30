ludzie = {
    '/var/OCR/page_2.jpg': {'unsafe': 0.00913255475461483, 'safe': 0.9908673763275146},
    '/var/OCR/page_1.jpg': {'unsafe': 0.01096330489963293, 'safe': 0.9890367388725281},
    '/var/OCR/nude.py/examples/images/damita.jpg': {'safe': 0.08645060658454895, 'unsafe': 0.9135494232177734},
    '/var/OCR/nude.py/examples/images/test2.jpg': {'safe': 0.005279913544654846, 'unsafe': 0.9947201013565063},
    '/var/OCR/nude.py/examples/images/damita2.jpg': {'unsafe': 0.012305554002523422, 'safe': 0.9876943826675415},
    '/var/OCR/nude.py/examples/images/test6.jpg': {'safe': 0.13665150105953217, 'unsafe': 0.8633484840393066},
    '/var/OCR/source/page_8.jpg': {'unsafe': 0.01661510393023491, 'safe': 0.9833849668502808},
    '/var/OCR/source/page_7.jpg': {'unsafe': 0.027142908424139023, 'safe': 0.9728570580482483},
    '/var/OCR/source/page_2.jpg': {'unsafe': 0.02719378098845482, 'safe': 0.9728062152862549},
    '/var/OCR/source/page_6.jpg': {'unsafe': 0.027971455827355385, 'safe': 0.9720284938812256},
    '/var/OCR/source/page_4.jpg': {'unsafe': 0.01991395652294159, 'safe': 0.9800859689712524},
    '/var/OCR/source/page_3.jpg': {'unsafe': 0.019394567236304283, 'safe': 0.9806054830551147},
    '/var/OCR/source/page_5.jpg': {'unsafe': 0.02018631249666214, 'safe': 0.9798136353492737},
    '/var/OCR/source/page_1.jpg': {'unsafe': 0.02890695445239544, 'safe': 0.9710931181907654},
    '/var/OCR/test/page_2.jpg': {'unsafe': 0.00913255475461483, 'safe': 0.9908673763275146},
    '/var/OCR/test/page_1.jpg': {'unsafe': 0.01096330489963293, 'safe': 0.9890367388725281},
    '/var/OCR/imagenude/image4.jpeg': {'unsafe': 0.06310199201107025, 'safe': 0.9368979930877686},
    '/var/OCR/imagenude/image7.png': {'safe': 0.003055965295061469, 'unsafe': 0.996944010257721},
    '/var/OCR/imagenude/image6.jpeg': {'safe': 0.23160327970981598, 'unsafe': 0.7683966755867004},
    '/var/OCR/imagenude/image3.jpeg': {'unsafe': 0.01613936573266983, 'safe': 0.9838606119155884},
    '/var/OCR/imagenude/image1_censored.jpeg': {'unsafe': 0.03634943068027496, 'safe': 0.9636505842208862},
    '/var/OCR/imagenude/image5.png': {'safe': 2.1537833163165487e-05, 'unsafe': 0.9999784231185913},
    '/var/OCR/imagenude/image2.jpeg': {'unsafe': 0.10607864707708359, 'safe': 0.8939213752746582},
    '/var/OCR/imagenude/image1.jpeg': {'unsafe': 0.015926077961921692, 'safe': 0.9840738773345947},
}

for id, image in ludzie.items():
    print(id)
    for zmienne in image:
        if(zmienne=="safe"):
            print("bezpieczne")
        else:
            print("niebezpieczne")
        print(image[zmienne])
