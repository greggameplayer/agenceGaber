import agenceGaber.main as agm

class User :
    def __init__(self, login):
        self.email = login[0]
        self.name =''
        self.pw = login[1]
        self.id = ''
        self.role = ''
        self.auth = False

    def getId(self):
        return self.id
    def getRole(self):
        return self.role
    
    def isAuth(self):
        self.auth = True

    def setInformations(self, id, name, role):
        self.id= id
        self.name = name
        if role == 1:
            self.role = 1 
        else:
            self.role = 0
    
    def findUserOnDB(self):
        login = (self.email, self.pw)
        informations = agm.database.signIN(login)
        if len(informations)>0:
            self.setInformations(informations)
