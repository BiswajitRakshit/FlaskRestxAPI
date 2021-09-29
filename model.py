from flask import jsonify
import json

class Operations():
    
    def __init__(self):
        f = open('data.json',)
        self.data = json.load(f)

    #
    def fetch(self):
        return self.data

    #
    def fetchById(self, ids):
        for x in self.data:
            if any(map(lambda m: x[str(m)] == ids, list(x))):
                return x
     
    #
    def add(self, dataByUser):
        self.data.append(dataByUser)
        
        #Writting Json Data
        js = json.dumps(self.data)
        with open('data.json', "w") as outfile:
            outfile.write(js)
            
        return self.data
     
    #
    def update(self, dataByUser):
        for x in self.data:
            if any(map(lambda m: x[str(m)] == dataByUser['id'], list(x))):
                          
                if dataByUser.get('name') != None:
                    x['name'] = dataByUser['name']
                    
                if dataByUser.get('age') != None:
                    x['age'] = dataByUser['age']
                    
        #Writting Json Data
        js = json.dumps(self.data)
        with open("data.json", "w") as outfile:
            outfile.write(js)
            
        return self.data
 
    #
    def delete(self, ids):
        
        for i, x in enumerate(self.data):
            if any(map(lambda m: x[str(m)] == ids, list(x))):
    
                    del self.data[i]
        
        #Writting Json Data
        js = json.dumps(self.data)
        with open("data.json", "w") as outfile:
            outfile.write(js)
            
        return self.data