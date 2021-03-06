from flask import jsonify
import json

class Operations():
    
    def __init__(self):
        f = open('data.json',)
        self.data = json.load(f)

    # Fetch all data
    def fetch(self):
        return self.data

    # Fetch by returning all data with specific Id using spacial method next which returns the iterable as dictionary
    def fetchById(self, ids):
        return next(x for x in self.data if x['id'] == ids)
            
    # Adding Data given by User
    def add(self, dataByUser):
        self.data.append(dataByUser)
        
        #Writting Json Data
        js = json.dumps(self.data)
        with open('data.json', "w") as outfile:
            outfile.write(js)
            
        return self.data
    
    # Updating Data given by User
    def update(self, dataByUser):
        # next method takes the matched iterable and then update the data with the user data 
        next(x for x in self.data if x['id'] == dataByUser['id']).update(dataByUser)
        
        # for x in self.data:
        #     if x['id'] == dataByUser['id']:
        #
        #         # Getting Common keys in Data and dataByUser
        #         keys = list(set(list(x)).intersection(list(dataByUser)))
        #         for k in keys:
        #             x[k] = dataByUser[k]
                    
        # Writting Json Data
        js = json.dumps(self.data)
        with open("data.json", "w") as outfile:
            outfile.write(js)
            
        return self.data
 
    # Deleting Data of perticular Id spectified by User
    def delete(self, ids):
        
        # Taking those data into dataset which is not matched with the id
        # It is another way of deleting the data with same id
        self.data = [x for x in self.data if not x['id'] == ids]
        
        # for i, x in enumerate(self.data):
        #     if x['id'] == ids:
        #             del self.data[i]
        
        # Writting Json Data
        js = json.dumps(self.data)
        with open("data.json", "w") as outfile:
            outfile.write(js)
            
        return self.data
