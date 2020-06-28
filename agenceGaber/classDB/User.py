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

    def setInformations(self, infos):
        self.id= infos[0][0]
        self.name = str(infos[0][3])+ ' ' +str(infos[0][1])
        self.role = int(infos[1])
        self.auth = True
    
    def findUserOnDB(self):
        login = (self.email, self.pw)
        informations = agm.database.signIN(login)
        if len(informations)>0:
            self.setInformations(informations)
