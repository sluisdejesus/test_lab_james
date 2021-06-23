class Pub:

    def __init__(self, pub_name, till):
        self.name = pub_name
        self.till = till
        self.drinks = []
    
    def drinks_count(self):
        return len(self.drinks)

     
