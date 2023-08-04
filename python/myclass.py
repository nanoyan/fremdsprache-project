class Vocab:
    def __init__(self, id , title, notation= None, description = None):
        self.id = id
        self.notation = notation
        self.title = title
        self.description = description
        self.children = []
    
    def add_child(self,child):
        self.children.append(child)
    
    def buildJson(self):
        self.json_string = {}
        self.json_string['id'] = self.id 
        if self.notation!=None:
            self.json_string['notation'] = self.notation
        self.json_string['title'] = self.title 
        if self.description!=None:
            self.json_string['description'] = self.description
        if len(self.children)>0:
            self.json_string['children'] = []
            for index,vocab in enumerate(self.children): 
                self.json_string['children'].append(vocab.buildJson())
        return self.json_string