INSERT INTO Ville (Libelle, CP)
VALUES  ('Paris', 75000),
		('Marseille', 13001),
		('Lille', 59000),
		('Bruille-Les-Marchiennes', 59490),
		('Allennes-Les-Marais', 59251),
		('Somain', 59490),
		('Marcq-en-Baroeul', 59700),
		('Rome', 00100),
		('Milan', 20019),
		('Venise', 30100),
		('Berlin', 12529),
		('Naples', 80100),
		('Madrid', 28039),
		('Barcelone', 08001),
		('Séville', 41940),
		('Lisbonne', 1250),
		('Budapest', 1007),
		('Porto', 4000);

INSERT INTO Pays (NomPays)
VALUES  ('France'),
		('Espagne'),
		('Portugal'),
		('Allemagne'),
		('Italie');

INSERT INTO LieuAvisiter (IdVille, NomPays, NomLieu, Descriptif, PrixVisite)
VALUES  (1, 'France', 'Tour Eiffel', 'La dame de fer', 40),
		(2, 'France', 'Vieux port', '...', 0),
		(3, 'France', 'Opéra', '.A.', 15),
		(4, 'France', 'Ferme du Muid', 'Chez moi', 10),
		(5, 'France', 'Ancienne distillerie', '&é"', 10),
		(6, 'France', 'Gare SNCF', 'azerty', 0),
		(7, 'France', 'Hippodrome', 'cours UUUUU', 2),
		(8, 'Italie', 'Collisé', 'C est beau', 25),
		(9, 'Italie', 'La Scala', 'Théâtre', 16),
		(10, 'Italie', 'Palais des doges', 'de l or', 20),
		(11, 'Allemagne', 'Porte de Brandebourg', 'Porte', 0),
		(12, 'Italie', 'Vesuve', 'Volcan', 0),
		(13, 'Espagne', 'Prado', 'Museum', 9);

INSERT INTO Circuit (DateDepart, NbrPlaceDisponible, Duree, PrixInscription, Descriptif, IdVilleDepart, IdVilleArrivee, NomPaysDepart, NomPaysArrivee)
VALUES  ('15/04/2020', 42, 7, 576, 'nice', 1, 11, 'France', 'Allemagne'),
		('20/05/2020', 22, 10, 755, 'le meilleur', 4, 12, 'France', 'Italie'),
		('25/06/2020', 66, 1, 111, 'bof', 13, 14, 'Espagne', 'Espagne'),
		('30/07/2020 ', 56, 7, 459, 'okok', 2, 15, 'France', 'Espagne');

INSERT INTO Etape (IdCircuit, Ordre, DateEtape, Duree, IdVille, NomPays, NomLieu)
VALUES  (1, 1, '16/04/2020', 240, 4, 'France', 'Ferme du Muid'),
		(1, 2, '17/04/2020', 160, 3, 'France', 'Opéra'),
		(1, 3, '21/04/2020', 240, 11, 'Allemagne', 'Porte de Brandebourg'),

		(2, 1, '21/05/2020', 160, 5, 'France', 'Ancienne distillerie'),
		(2, 2, '22/05/2020', 3600, 1, 'France', 'Tour Eiffel'),
		(2, 3, '25/05/2020', 3600, 8, 'Italie', 'Collisé'),
		(2, 4, '27/05/2020', 7200, 12, 'Italie', 'Vesuve'),

		(3, 1, '25/06/2020', 120, 13, 'Espagne', 'Prado');

INSERT INTO  Utilisateur (Nom, email, Prenom, DateDeNaissance)
VALUES	('Daouk', 'Jad.daouk@epsi.fr', 'Jad', '19-02-2001'),
		('Marit', 'Victor.Marit@epsi.fr', 'Victor', '27-02-1995'),
		('Hage', 'Gregoire.Hage@epsi.fr', 'Gregoire', '15-04-2001');

INSERT INTO  Membre (IdMembre)
VALUES (1);

INSERT INTO  Administrateur (IdAdmin, mdp, login)
VALUES (2, 'azerty', 'Victor.Marit');

INSERT INTO  Client (IdClient, mdp, login)
VALUES (3, 'azerty', 'Gregoire.Hage');

/*INSERT INTO  Réservation (NbrPlaceReserver, DateReservation, IdCircuit, IdClient)
VALUES (1, '01/04/2020', 1, 3);

INSERT INTO  DetailsReservation (IdMembre, IdReserv, Valider)
VALUES (1, 1, 1);*/