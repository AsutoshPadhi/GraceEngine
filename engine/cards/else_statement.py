from engine.cards.card import Card
from engine.cards.sticker import Sticker
from engine.cards.display import Display

# from card import Card
# from sticker import Sticker
# from display import Display

class ElseStatement(Card):

    '''
    For information on card and attributes and methods, 
    refer parent class Card in card.py
    '''

    def __init__(self, card_number:int):
        card_id = "else_statement"
        card_type = [True, False, False, False, False, True, 0]
        super(ElseStatement,self).__init__(card_id,card_type,card_number)

    def generate_card(self):
        self.card_dict["card_id"] = self.card_id
        self.card_dict["card_number"] = self.card_number
        self.card_dict["card_type"] = self.card_type
        self.card_dict["card_color"] = "color_logic"
        else_text = {
            "val_type":"text",
            "text":"else"
        }
        self.card_dict["display"] =[else_text]
        self.card_dict["external_dependant"] = {}
        if not self.children:
            self.card_dict["children"] = []

        return self.card_dict

    def generate_code(self, nesting_level = 0):
        nesting_level += 1
        self.code = "else:\n"
        if not self.children:
            self.code += "    " * nesting_level
            self.code += "pass"
        else:
            for child in self.children:
                self.code += "    " * nesting_level 
                self.code += child.generate_code(nesting_level)
        return self.code  

    def add_child(self,child, position):
        if position is None:
            self.children.append(child)
            self.card_dict["children"].append(child.generate_card())
        else:
            self.children.insert(position, child)
            self.card_dict["children"].insert(position, child.generate_card())
        
if __name__ == "__main__":
    test_card = ElseStatement(0)

    print("Card: \n",test_card.generate_card())
    print("Code: \n",test_card.generate_code())

    test_card_ch1 = Display(("text","Hello World!"), 0)
    test_card.add_child(test_card_ch1, None)
    test_card_ch2 = Display(("variable","count"), 0)
    test_card.add_child(test_card_ch2, None)


    print("Card: \n",test_card.generate_card())
    print("Code: \n",test_card.generate_code())