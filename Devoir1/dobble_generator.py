#Kanty-Louange Gakima, Matricule
#Marianne Schmit Pemmerl, 20192143

import random

class Generator:
    def __init__(self, order=7):
        self.order = order

    def generate(self, cards_file="cartes.txt", verbose=False):
        if verbose:
            print("*** Génération des cartes ***")
        
        order = self.order
        total_symbols = order ** 2 + order + 1

        #generates symbols for the horizon
        horizon = []
        for i in range(self.order + 1):
            horizon.append([k + (self.order) * i for k in range(1,self.order+1)])
            horizon[i].append(self.order ** 2 + self.order+1) # add last symbol to horizon

        #generates symbols for the main matrix
        matrix = [[[] for _ in range(self.order)] for _ in range(self.order)]
        
        symbols = [i for i in range(1, total_symbols)]
        
        #add cards horizontally
        for i in range(order):
            for j in range(order):
                matrix[i][j].append(symbols[0])
            symbols.pop(0) 


        #add cards vertically    
        for j in range(order):
            for i in range(order):
                matrix[i][j].append(symbols[0])
            symbols.pop(0)  # Remove the first element from symbols


        #add cards diagonally #1
        #diagonals premier sens
        for i in range(order):
            for j in range(order):  
                matrix[j][((j+1)+i)%order].append(symbols[0])
            symbols.pop(0)

        #pour n=2 on a trois directions: horizontal, vertical et diagonal
        #a partir de n= 3 on a 4 directions (inclus la deuxieme direction de la diagonal)
        if(order>2):

            #add cards diagonally #2
            #diagonals deuxieme sens
            for j in range(order):
                for i in range(order):
                    matrix[i][((order-i)+j)%order].append(symbols[0])
                symbols.pop(0)

        #les autres directions commencent a partir de n >= 5
        if(order>=5):
            directions = (order+1)-4 #-4 directions deja trouvé
            for direction in range(directions):

                for i in range(order):
                    for j in range(order):  
                        matrix[j][((j*(2+direction))+i)%order].append(symbols[0])
                    symbols.pop(0)

        cards = []
        for card in matrix:
            if isinstance(card, list):
                cards.extend(card)

        for row in horizon:
            cards.append(row)

        for card in cards:
            random.shuffle(card)

        content = self.file_content(cards)
        self.write(cards_file, content)

    def write(self,fileName, content):
        #écrire la sortie dans un fichier/write output in file
        file = open(fileName, "w")
        file.write(content)
        file.close()

    def file_content(self,cards):
        # Write the cards to the file
        content = ""
        for card_set in cards:
            if isinstance(card_set[0], list):
                for card in card_set:
                    symbols_str = " ".join(str(symbol) for symbol in card)
                    content += symbols_str + "\n"
            else:
                symbols_str = " ".join(str(symbol) for symbol in card_set)
                content += symbols_str + "\n"

        return content
