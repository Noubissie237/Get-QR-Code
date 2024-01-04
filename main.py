import qrcode
from PIL import Image

def give_qrcode(world : str, fileName : str): 

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,)

    qr.add_data(world)

    qr.make(fit=True)

    image = qr.make_image(fill_color="black", black_color="while")

    image.save(fileName + '.png')

    return image


try:

    name = input("\nEntrez le text dont vous souhaitez générer le qrcode : ")

    fichier = input("\nEntrer le nom du fichier qui sera sauvegardé : ")

    give_qrcode(name, fichier)

    print("\nGénération éffectué avec succèss ! ")

except:
    
    print("\n Une erreur s'est produite ")
