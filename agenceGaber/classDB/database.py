import os

try:
    import pyodbc
except ImportError:
    os.system('py -m pip install --upgrade pip')
    os.system('pip install pyodbc wheel')
    import pyodbc


class DATABASE:
    def __init__(self, ip, port, dbname, user, pwd):
        self.ip = ip
        self.port = port
        self.user = user
        self.pwd = pwd
        self.dbname = dbname

    def connectToDatabase(self):
        conn = pyodbc.connect(
            'Driver={MySQL ODBC 8.0 ANSI Driver};Server=' + self.ip + ';Port=' + self.port + ';Database=' + self.dbname + ';Uid=' + self.user + ';Pwd=' + self.pwd + ';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
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
        print(email, nom, prenom, birthdate, mdp)
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
                f"INSERT INTO utilisateur(Nom, email, Prenom, DateDeNaissance) VALUES('{nom}','{email}','{prenom}','{birthdate}')"
            )
            addcursor.commit()
            self.closeDatabase(addconn, addcursor)
            
            addconn2 = self.connectToDatabase()
            addcursor2 = addconn2.cursor()
            addcursor2.execute("select IdUtilisateur FROM utilisateur where email=?", email)
            lastId = addcursor2.fetchone()
            if len(lastId)>0:
                print(lastId)
                addconn3 = self.connectToDatabase()
                addcursor3 = addconn3.cursor()
                addcursor3.execute("INSERT INTO client(IdClient, mdp) VALUES(?, ?)", lastId[0], mdp
                )
                addcursor3.commit()
            else:
                return "error1"
            self.closeDatabase(addconn2, addcursor2)
            self.closeDatabase(addconn3, addcursor3)
            return "message"
        else:
            return "error"

    def signIN(self, credentials):
        resultat = []
        try:
            conn = self.connectToDatabase()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM utilisateur WHERE utilisateur.email=?", credentials[0])
            resultat = cursor.fetchone()
        except:
            print('fail to connect')
        finally:
            mdp = ""
            print(resultat)
            if len(resultat) > 0:
                if self.getUserGroup(resultat[0]) == 1:
                    cursor.execute("SELECT * FROM administrateur WHERE IdAdmin=?", resultat[0])
                    mdp = cursor.fetchone()[1]
                    list(resultat).append(1)
                    self.closeDatabase(conn, cursor)
                    if credentials[1] == mdp:
                        return [resultat, 1]
                    else:
                        return []
                else:
                    cursor.execute("SELECT * FROM client WHERE IdClient=?", resultat[0])
                    mdp = cursor.fetchone()[1]

                    self.closeDatabase(conn, cursor)
                    if credentials[1] == mdp:
                        return [resultat, 0]
                    else:
                        return []
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

    def allTrip(self):
        try:
            conn = self.connectToDatabase()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM circuit")
            result = cursor.fetchall()
        except:
            result = []
        finally:
            self.closeDatabase(conn, cursor)
            return result

    def featureTrip(self, id):
        try:
            conn = self.connectToDatabase()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM circuit WHERE IdCircuit=?", id)
            result = cursor.fetchone()
        except:
            result = []
        finally:
            self.closeDatabase(conn, cursor)
            return result

    def numberPlacesLeft(self, id):
        try:
            conn = self.connectToDatabase()
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(NbrPlaceReserver) FROM reservation WHERE IdCircuit=?", id)
            result = cursor.fetchone()[0]

            if result is None:
                result = '0'
        except:
            result = '0'
        finally:
            self.closeDatabase(conn, cursor)
            return result

    def citiesTrip(self, id):
        try:
            conn = self.connectToDatabase()
            cursor = conn.cursor()
            cursor.execute("SELECT SUM(NbrPlaceReserver) FROM etape WHERE IdCircuit=?", id)
            result = cursor.fetchone()
        except:
            result = ['0']
        finally:
            self.closeDatabase(conn, cursor)
            return result

    def etapesTrip(self, id):
        try:
            conn = self.connectToDatabase()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT etape.NomPays, etape.NomLieu, ville.Libelle FROM etape, ville WHERE ville.IdVille = "
                "etape.IdVille AND IdCircuit=?",
                id)
            results = cursor.fetchall()
        except:
            results = []
        finally:
            self.closeDatabase(conn, cursor)
            return results
    
    def allEtapes(self):
        try:
            conn = self.connectToDatabase()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM etape, ville WHERE ville.IdVille = etape.IdVille"
            )
            results = cursor.fetchall()
        except:
            results = []
        finally:
            self.closeDatabase(conn, cursor)
            return results
    
    def allTown(self):
        try:
            conn = self.connectToDatabase()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM ville"
            )
            results = cursor.fetchall()
        except:
            results = []
        finally:
            self.closeDatabase(conn, cursor)
            return results
    
    def allCountry(self):
        try:
            conn = self.connectToDatabase()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM pays"
            )
            results = cursor.fetchall()
        except:
            results = []
        finally:
            self.closeDatabase(conn, cursor)
            return results
    
    def getLieu(self, IdVille):
        try:
            conn = self.connectToDatabase()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM lieuavisiter WHERE IdVille=?", IdVille
            )
            results = cursor.fetchall()
        except:
            results = []
        finally:
            self.closeDatabase(conn, cursor)
            return results
    
    def getLieuxByVilleName(self, NameVille):
        try:
            conn = self.connectToDatabase()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM lieuavisiter, ville WHERE ville.Libelle=? and ville.IdVille=lieuavisiter.IdVille", NameVille
            )
            results = cursor.fetchall()
        except:
            results = []
        finally:
            self.closeDatabase(conn, cursor)
            return results

    def userTripSub(self, IdClient):
        try:
            print(IdClient)
            conn = self.connectToDatabase()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT reservation.NbrPlaceReserver, reservation.DateReservation, reservation.IdCircuit, circuit.DateDepart, circuit.Duree, circuit.PrixInscription, circuit.NomPaysDepart, circuit.NomPaysArrivee
                FROM reservation, circuit
                WHERE reservation.IdClient=?
                AND circuit.IdCircuit = reservation.IdCircuit""", IdClient
            )
            informationsreservations = cursor.fetchall()
        except:
            informationsreservations = []
        finally:
            self.closeDatabase(conn, cursor)
            return informationsreservations

    def ajoutReservation(self):
        pass