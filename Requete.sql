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
Where Etape.IdCircuit=1) AS NombreEtapes
FROM Circuit
WHere Circuit.IdCircuit=1

DELETE FROM LieuAvisiter FROM Ville, Pays
WHERE LieuAvisiter.NomLieu = '...'
AND Ville.Libelle = '...'
AND Pays.NomPays = '...'
AND LieuAvisiter.IdVille = Ville.IdVille
AND LieuAvisiter.NomPays = Pays.NomPays
AND LieuAvisiter.NomLieu NOT IN (
SELECT Etape.NomLieu
FROM Etape
);

SELECT PrixInscription + SUM(PrixVisite) AS 'Prix total'
FROM Circuit, LieuAvisiter, Etape
WHERE Circuit.IdCircuit = 2
AND LieuAvisiter.NomLieu = Etape.NomLieu
AND LieuAvisiter.NomPays = Etape.NomPays
AND LieuAvisiter.IdVille = Etape.IdVille
AND Etape.IdCircuit = Circuit.IdCircuit
Group By PrixInscription;

SELECT Circuit.IdCircuit, Circuit.PrixInscription, Circuit.DateDepart, Circuit.Duree
FROM Circuit, LieuAvisiter, Etape
WHERE LieuAvisiter.NomLieu = Etape.NomLieu
AND LieuAvisiter.NomPays = Etape.NomPays
AND LieuAvisiter.IdVille = Etape.IdVille
AND Circuit.DateDepart >= '...'
AND DATEADD (day, 
(
SELECT Circuit.Duree
FROM Circuit
WHERE Circuit.DateDepart >= '...'
)
, Circuit.DateDepart) <= '...'
AND Circuit.NbrPlaceDisponible >= '...'
Group By Circuit.IdCircuit, PrixInscription, Circuit.DateDepart, Circuit.Duree
HAVING '...' >= PrixInscription + SUM(PrixVisite);

DELETE FROM Etape FROM Circuit
WHERE Circuit.IdCircuit = '...'
AND Circuit.IdCircuit = Etape.IdCircuit
AND Etape.Ordre = '...';

DECLARE @count INT = 1;
WHILE @count <= 
(
SELECT COUNT(Ordre)
FROM Etape, Circuit
WHERE Circuit.IdCircuit = '...'
AND Circuit.IdCircuit = Etape.IdCircuit
)
BEGIN

	UPDATE Etape
	SET Etape.Ordre = @count
	FROM Circuit
	WHERE Circuit.IdCircuit = '...'
	AND Circuit.IdCircuit = Etape.IdCircuit
	AND Etape.Ordre = @count + 1;

	SET @count = @count+1;

END;
