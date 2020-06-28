import os

try:
    import pyodbc
except ImportError:
    os.system('py -m pip install --upgrade pip')
    os.system('pip install pyodbc wheel')
    import pyodbc

class DATABASE:
    def __init__(self,ip,port,dbname,user,pwd):
        self.ip = ip
        self.port = port
        self.user = user
        self.pwd = pwd
        self.dbname = dbname

    def connectToDatabase(self):
        conn = pyodbc.connect('Driver={MySQL ODBC 8.0 ANSI Driver};Server=' + self.ip +';Port=' + self.port +';Database=' + self.dbname +';Uid=' + self.user + ';Pwd=' + self.pwd +';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
        conn.setencoding(encoding='utf-8')
        return conn


    def closeDatabase(self, conn, cursor):
        cursor.close()
        conn.close()


    def circuitInfos(self, IdGiven):
        conn = self.connectToDatabase()
        cursor = conn.cursor()
        cursor.execute(
        """
        Select
        Circuit.IdCircuit, Circuit.Descriptif,
        (SELECT Ville.Libelle
        FROM Circuit, Ville
        WHERE Circuit.IdVilleDepart=Ville.IdVille AND Circuit.IdCircuit=1) AS VilleDepart,
        (SELECT Ville.Libelle
        FROM Circuit, Ville
        WHERE Circuit.IdVilleArrivee=Ville.IdVille AND Circuit.IdCircuit=1) AS VilleArrivee,
        (SELECT COUNT(*)
        from Etape
        Where Etape.IdCircuit=?) AS NombreEtapes
        FROM Circuit
        WHere Circuit.IdCircuit=?
        """, IdGiven, IdGiven)
        rows = cursor.fetchall()
        self.closeDatabase(conn, cursor)
        return rows
    
    def signUP(self, email, nom, prenom, birthdate, mdp):
        conn = self.connectToDatabase()
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT * FROM utilisateur WHERE email = ?
            """, email
        )
        connlength = len(list(cursor.fetchall()))
        self.closeDatabase(conn, cursor)
        if connlength == 0:
            addconn = self.connectToDatabase()
            addcursor = addconn.cursor()
            addcursor.execute(
                """
                INSERT INTO utilisateur(Nom, email, Prenom, DateDeNaissance)
                VALUES(?,?,?,?)
                """,
                nom, email, prenom, birthdate
            )
            addcursor.execute("select SCOPE_IDENTITY()")
            lastId = addcursor.fetchone()
            if len(list(addcursor.fetchall())) != []:
                addcursor.execute(
                    """
                        INSERT INTO client(IdClient, mdp) VALUES(?, ?)
                    """, lastId[0], mdp
                )
            else:
                return {"error": "Il y a eu un problème lors de la création de l'utilisateur"}
            self.closeDatabase(addconn, addcursor)
            return {"message": "L'utilisateur a été créé avec succés"}
        else:
            return {"error": "Un utilisateur posséde déjà cet email"}
    
    def signIN(self, credentials):
        resultat=[] 
        try :
            conn = self.connectToDatabase()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM utilisateur WHERE utilisateur.email=?",credentials[0])
            resultat = cursor.fetchone()
        except:
            print('fail to connect')
        finally:
            mdp = ""
            if self.getUserGroup(resultat[0]) == 1:
                cursor.execute("SELECT * FROM administrateur WHERE IdAdmin=?",resultat[0])
                mdp = cursor.fetchone()[1]
                list(resultat).append(1)
                self.closeDatabase(conn, cursor)
                if credentials[1] == mdp:
                    return [resultat, 1]
                else:
                    return []
            else:
                cursor.execute("SELECT * FROM client WHERE IdClient=?",resultat[0])
                mdp = cursor.fetchone()[1]
                
                self.closeDatabase(conn, cursor)
                if credentials[1] == mdp:
                    return [resultat, 0]
                else:
                    return []
            
    
    def getUserGroup(self, UserID):
        results = []
        test = 0
        try:
            conn = self.connectToDatabase()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM client WHERE IdClient=?", UserID)
            results = cursor.fetchone()[0]
        except:
            test = 1
        finally:
            self.closeDatabase(conn, cursor)

            return test