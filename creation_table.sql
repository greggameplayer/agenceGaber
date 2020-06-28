CREATE TABLE Pays(
   NomPays VARCHAR(50),
   PRIMARY KEY(NomPays)
);

CREATE TABLE Ville(
   IdVille INT  AUTO_INCREMENT,
   Libelle VARCHAR(50),
   CP INT,
   Longitude INT,
   PRIMARY KEY(IdVille)
);

CREATE TABLE Utilisateur(
   IdUtilisateur INT  AUTO_INCREMENT,
   Nom VARCHAR(50),
   email VARCHAR(50) UNIQUE,
   Prenom VARCHAR(50),
   DateDeNaissance DATE,
   PRIMARY KEY(IdUtilisateur)
);

CREATE TABLE Circuit(
   IdCircuit INT  AUTO_INCREMENT,
   DateDepart DATE,
   NbrPlaceDisponible INT,
   Duree INT,
   PrixInscription INT,
   Descriptif VARCHAR(50),
   IdVilleDepart INT NOT NULL,
   IdVilleArrivee INT NOT NULL,
   NomPaysDepart VARCHAR(50) NOT NULL,
   NomPaysArrivee VARCHAR(50) NOT NULL,
   PRIMARY KEY(IdCircuit),
   FOREIGN KEY(IdVilleDepart) REFERENCES Ville(IdVille),
   FOREIGN KEY(IdVilleArrivee) REFERENCES Ville(IdVille),
   FOREIGN KEY(NomPaysDepart) REFERENCES Pays(NomPays),
   FOREIGN KEY(NomPaysArrivee) REFERENCES Pays(NomPays)
);

CREATE TABLE LieuAvisiter(
   IdVille INT,
   NomPays VARCHAR(50),
   NomLieu VARCHAR(50),
   Descriptif VARCHAR(50),
   PrixVisite INT,
   PRIMARY KEY(IdVille, NomPays, NomLieu),
   FOREIGN KEY(IdVille) REFERENCES Ville(IdVille),
   FOREIGN KEY(NomPays) REFERENCES Pays(NomPays)
);

CREATE TABLE Client(
   IdClient INT,
   mdp VARCHAR(1000),
   login VARCHAR(50),
   PRIMARY KEY(IdClient),
   FOREIGN KEY(IdClient) REFERENCES Utilisateur(IdUtilisateur)
);

CREATE TABLE Administrateur(
   IdAdmin INT,
   mdp VARCHAR(1000),
   login VARCHAR(50),
   PRIMARY KEY(IdAdmin),
   FOREIGN KEY(IdAdmin) REFERENCES Utilisateur(IdUtilisateur)
);

CREATE TABLE Membre(
   IdMembre INT,
   PRIMARY KEY(IdMembre),
   FOREIGN KEY(IdMembre) REFERENCES Utilisateur(IdUtilisateur)
);

CREATE TABLE Reservation(
   IdReserv INT IDENTITY (1,1),
   NbrPlaceReserver INT,
   DateReservation DATE,
   IdCircuit INT NOT NULL,
   IdClient INT NOT NULL,
   PRIMARY KEY(IdReserv),
   FOREIGN KEY(IdCircuit) REFERENCES Circuit(IdCircuit),
   FOREIGN KEY(IdClient) REFERENCES Client(IdClient)
);

CREATE TABLE Etape(
   IdCircuit INT,
   Ordre INT,
   DateEtape DATE,
   Duree INT,
   IdVille INT NOT NULL,
   NomPays VARCHAR(50) NOT NULL,
   NomLieu VARCHAR(50) NOT NULL,
   PRIMARY KEY(IdCircuit, Ordre),
   FOREIGN KEY(IdCircuit) REFERENCES Circuit(IdCircuit),
   FOREIGN KEY(IdVille, NomPays, NomLieu) REFERENCES LieuAvisiter(IdVille, NomPays, NomLieu)
);

CREATE TABLE DetailsReservation(
   IdMembre INT,
   IdReserv INT,
   Valider BIT DEFAULT 1,
   DateAnnulation DATE,
   PRIMARY KEY(IdMembre, IdReserv),
   FOREIGN KEY(IdMembre) REFERENCES Membre(IdMembre),
   FOREIGN KEY(IdReserv) REFERENCES Reservation(IdReserv)
);
