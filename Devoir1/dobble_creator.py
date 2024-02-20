#Marianne Schmit Pemmerl, 20192143
#Kanty-Louange Gakima, 20184109

# cette classe sert a créer les cartes visuelles du jeu dans le dossier "results"
# this class is used to create the game visual cards in the "results" folder

from PIL import Image
import os
import random

# info :
# https://pillow.readthedocs.io/en/stable/reference/Image.html

class Creator():
    def __init__(self, pic_size=900, border_size=10):
        self.pic_size = pic_size
        self.border_size = border_size

    def read_images(self, folder):
        images = []
        for filename in os.listdir(folder):
            if filename.endswith(".png"):
                images.append(Image.open(os.path.join(folder, filename)))    
        return images


    def make_cards(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Creation des cartes visuelles***")

        # lecture des images à partir du dossier "images" : "1.png2, "2.png", "3.png", ... "<N>.png"
        # placement des images sur les cartes visuelles, rotations apreciees
        # ajout de la bordure sur les cartes visuelles
        # sauvegarde des cartes dans le dossier "results" : "card1.jpg", "card2.jpg", "card3.jpg", ... "card<N>.jpg"
            
        # reading images from the "images" folder: "1.png2, "2.png", "3.png", ..., "<N>.png"
        # placement of images on visual cards, rotations appreciated
        # added border on visual cards
        # save cards in the “results” folder : "card1.jpg", "card2.jpg", "card3.

        pic_size = self.pic_size

        # Lecture des images à partir du dossier "images"
        images = self.read_images("images")

        # Lecture des cartes depuis le fichier "cards_file"
        cards = []
        with open(cards_file, 'r') as f:
            for line in f:
                symbols = line.strip().split()
                cards.append([int(symbol) for symbol in symbols])

        order = len(cards[0]) - 1

        # Création des cartes visuelles
        results_folder = "results"
        if not os.path.exists(results_folder):
            os.makedirs(results_folder)

        for i, symbols in enumerate(cards):
            # Création d'une nouvelle image pour la carte
            card_image = Image.new('RGB', (pic_size + self.border_size, pic_size + self.border_size), color='white')
            symbol_width = pic_size // ( int(order ** 0.5)+1)  # 3 symboles horizontalement 
            symbol_height = pic_size // (int(order ** 0.5)+1) # 3 symboles verticalement

            # Placement des images correspondantes aux symboles sur la carte
            for j, symbol in enumerate(symbols):
                symbol_index = symbol - 1  # Index des symboles commence à 0
                image = images[symbol_index]

                #image = image.resize((symbol_width - 0, symbol_height - 60))

                row = j // ( int(order ** 0.5)+1)
                col = j % (int(order ** 0.5)+1)
                position = (col * symbol_width, row * symbol_height)

                # Rotation aléatoire de l'image
                angle = random.randint(0, 360)
                rotated_image = image.rotate(angle, expand=True)
                
                # Redimensionner l'image pour qu'elle s'adapte au symbole
                rotated_image = rotated_image.resize((symbol_width, symbol_height))

                # Création d'une image vierge de la même taille que l'image d'origine
                blank_image = Image.new('RGB', rotated_image.size, color='white')

                # Coller l'image tournée sur le fond blanc
                blank_image.paste(rotated_image, (0, 0), rotated_image)

                card_image.paste(blank_image, position)


            # Ajout de la bordure sur la carte
            border = Image.new('RGB', (pic_size + self.border_size * 2,  pic_size + self.border_size * 2 ),
                               color='white')
            border.paste(card_image, (self.border_size, self.border_size))

            # Sauvegarde de la carte dans le dossier "results"
            border.save(os.path.join(results_folder, f"card{i + 1}.jpg"))

# Exemple d'utilisation
creator = Creator()
creator.make_cards(verbose=True)
