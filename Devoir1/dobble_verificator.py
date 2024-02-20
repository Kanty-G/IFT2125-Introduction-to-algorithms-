#Marianne Schmit Pemmerl, 20192143
#Kanty-Louange Gakima, Matricule

# cette classe sert a verifier la validite de l'ensemble des cartes du jeu dans le fichier cartes.txt
# this class is used to check the validity  of the game cards set in the cartes.txt file

# doit retourner 0 si tout est correct, 1 si le jeu n'est pas optimal selon l'ordre et 2 si le jeu n'est pas valide
# should return 0 if everything is correct, 1 if the game set is not optimal according to the order and 2 if the game set is invalid

class Verificator():
    def __init__(self):
        pass

    def verify(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Verification des cartes***")
        
        cards = self.read_file(cards_file)

        symbols_split_cards = [] 

        for card in cards:
            symbols_split_cards.append(card.split())

        cards = symbols_split_cards

        order = self.findOrder(cards) #####################################################################

        # test : le nombre de carte devrait être optimal
        cardsno_isOptimal = self.verifyOptimalCardsno(cards, order)
      
        # test : le nombre de symboles par carte est le même pour chaque carte
        has_same_no_symbols =  self.verifySymbolsno(cards)
            
        # test : chaque paire de cartes partagent toujours un et un seul symbole en commun
        has_one_Common_Symbol= self.verifySymbolsperPair(cards)
            
        # test : le nombre de symbole total devrait être optimal
        symbolsno_isOptimal= self.verifyOptimalSymbolsno(cards, order)


        has_n_plus_one_Symbols= self.hasNplusOneSymbols(cards, order)


        # succes (0) si le jeu est valide et optimal
        # avertissement (1) si le jeu de carte n'est pas optimal
        # erreur (2) si le jeu de carte n'est pas valide
        
        if has_n_plus_one_Symbols and symbolsno_isOptimal and cardsno_isOptimal and has_same_no_symbols and has_one_Common_Symbol:
            return 0
        elif has_same_no_symbols and has_one_Common_Symbol:
            return 1
        else:
            return 2



    def verifyOptimalCardsno(self, cards, n):
        excepted_cards_n = n**2+n+1
        count_cards = len(cards)
        return count_cards==excepted_cards_n


    def verifyOptimalSymbolsno(self, cards, n):
        excepted_symbols_n = n**2+n+1
        symbols = []
        for card in cards:
            for symbol in card:
                if symbol not in symbols:
                    symbols.append(symbol)
        return len(symbols)==excepted_symbols_n
    

    #verify if every card has same symbols number
    def verifySymbolsno(self, cards): 
        first_card = cards[0]
        for card in cards[1:]:
            if len(first_card) != len(card):
                return False
        return True


    def hasOneCommonSymbol(self, card1, card2):
        # Find the intersection of symbols between card1 and card2
        common_symbols = set(card1) & set(card2)  
        return len(common_symbols) == 1

    #verify if each pair of cards shares only one common symbol
    def verifySymbolsperPair(self, cards):
        for card1 in range(len(cards)):
            for card2 in range(len(cards)):
                if card1 != card2:
                    if not self.hasOneCommonSymbol(cards[card1], cards[card2]):
                        return False
        return True
        
    #verify if each card has n+1 symbols 
    def hasNplusOneSymbols(self, cards, n): 

        for card in cards:
            if len(card) != n+1:
                return False
        return  True


    def read_file(self, input_file):
        file = open(input_file,"r")
        lines = file.readlines()
        file.close()
        return lines

    #calculate order
    def findOrder(self, cards):
        return len(cards[0])-1
