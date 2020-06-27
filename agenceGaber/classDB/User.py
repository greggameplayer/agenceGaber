import agenceGaber.main as agm

class User :
    def __init__(self, login):
        self.email = login[0]
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

    def setId(self, variable):
        self.id= var
    
    def setRole(self, variable):
        if var == 1:
            self.role = 1 
        else:
            self.role = 0
    
    def findUserOnDB(self):
        login = (self.email, self.pw)
        agm.database.signIN(login)