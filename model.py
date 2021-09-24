from flask import jsonify
import json

class Operations():
    
    def __init__(self):
        
        f = open('data.json')
        self.data = json.load(f)
        
        
        
    def fetch(self):
        return self.data

    

    def fetchById(self, ids):
       
        for i, x in enumerate(self.data):
            for t in x:
    
                if x[t] == ids:
                    return self.data[i]
                        
        return None
        
        

    def add(self, dataByUser):
        
        self.data.append(dataByUser)
           
        js = json.dumps(self.data)
      
        with open('data.json', "w") as outfile:
            outfile.write(js)
            
        return self.data
    
    
    
    def update(self, dataByUser):
        
        for i, x in enumerate(self.data):
            for t in x:
    
                if x[t] == dataByUser['id']:
                          
                    if dataByUser.get('name') != None:
                        self.data[i]['name'] = dataByUser['name']
                        
                    if dataByUser.get('age') != None:
                        self.data[i]['age'] = dataByUser['age']
                        
                        
        js = json.dumps(self.data)
      
        with open("data.json", "w") as outfile:
            outfile.write(js)
            
        return self.data
    
    
    
    def delete(self, ids):
        
        for i, x in enumerate(self.data):
            for t in x:
    
                if x[t] == ids:
                    del self.data[i]
        
        
        js = json.dumps(self.data)
        
        with open("data.json", "w") as outfile:
            outfile.write(js)
            
        return self.data
        
        
        
        
        
        
        
        
        
        
        
            
        