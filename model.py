from flask import jsonify
import json

class Operations():
    
    def __init__(self):
        
        f = open('data.json')
        self.data = json.load(f)
        
        
        
    def fetch(self):
        return self.data

    

    def fetchById(self, jsonFile):
        
    
        for ids, x in enumerate(self.data):
            for i in x:
    
                if x[i] == jsonFile['id']:
                          
                    return self.data[ids]
                        
        return None
        
        

    def add(self, jsonFile):
        
        self.data.append(jsonFile)
           
        js = json.dumps(self.data)
      
        with open('data.json', "w") as outfile:
            outfile.write(js)
            
        return self.data
    
    
    
    def update(self, jsonFile):
        
        for ids, x in enumerate(self.data):
            for i in x:
    
                if x[i] == jsonFile['id']:
                          
                    if jsonFile.get('name') != None:
                        self.data[ids]['name'] = jsonFile['name']
                        
                    if jsonFile.get('age') != None:
                        self.data[ids]['age'] = jsonFile['age']
                        
                        
        js = json.dumps(self.data)
      
        with open("data.json", "w") as outfile:
            outfile.write(js)
            
        return self.data
    
    
    
    def delete(self, jsonFile):
        
        for ids, x in enumerate(self.data):
            for i in x:
    
                if x[i] == jsonFile['id']:
                    del self.data[ids]
        
        
        js = json.dumps(self.data)
        
        with open("data.json", "w") as outfile:
            outfile.write(js)
            
        return self.data
        
        
        
        
        
        
        
        
        
        
        
            
        