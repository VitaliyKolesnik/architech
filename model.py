import pickle

class Model:

    def __init__(self, file_name):
        self.matches = []
        self.load(file_name)

    def load(self, file_name):
        try:
            with open(file_name, 'rb') as f:
                self.matches = pickle.load(f)
        except:
            self.matches = []

    def save(self, file_name):
        with open(file_name, 'wb') as f:
            pickle.dump([self.matches], f)



    def add_contact(self, name, score):
        if  self.matches == []:
            id = 0
        else:
            id = self.matches[-1]['id']+1
        self.matches.append({'id':id,'name':name,'score':score})