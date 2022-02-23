# tp_facture
TP N1 - AWS reStart CMDLA1
L'objectif de ce premier TP est de créer une facture.

# Notions

Manipulation des dictionnaires
Utilisation du package copy
Manipulation des tableaux
Manipulation des boucles
Utilisation d'un dépôt public et création d'un fork git
Objectifs du TP
Vous devez créer un programme qui permettra à l'utilisateur d'entrer dans une liste de produits. Chaque produit est identifié par trois attributs. Ces attributs seront utilisés pour évaluer le coût total.

# Les attributs
Un nom
Un prix
La quantité
Les différents produits doivent être stockés dans un tableau. Le coût total sera calculé à partir de l'ensemble des produits présents dans le tableau

# Indication
Créer un fork de ce projet et décrypter son fonctionnement
Créer le modèle de dictionnaire avec les attributs ci-dessus
Ecrire du code permettant de récupérer les saisies utilisateurs. Ceci vous permettra de créer de nouvelles données sur la base du modèle créer en 2
Ajouter les données à un tableau
Calculer le prix total de la facture
Effectuez un git add . pour enregistrer les modifications
Effectuez un git commit -m "<votre_message>" pour créer une photo de votre projet
Poussez votre code sur votre dépôt github.

## Ce projet consiste en la réalisation d'un programme en python qui permettra à un utilisateur d'entrer un certain nombre (inconnu) de produits avec des informations (le nom, la quantité et le prix) sur ce dernier et nous nous servirons de ces informations pour créer une facture.

Pour ce faire nous allons réaliser une boucle while qui s'excécutera tant que l'utilisateur n'aura pas indiqué qu'il ne souhaite plus rajouter d'élements au tableau.
cette boucle exécura 3 input qui demanderons à l'utilisateur les information (nom, quatité et prix) créer chaque élements de type dictionnaire.
puis elle s'enservira pour créer l'élement et l'ajouter au tableau puis elle demandera à l'utilisateur s'il en ajouter un autre.
si la reponse est oui, la boucle sera réexécutée.
si la réponse est non, la variable de sortie sera passé en True, puis on sortira de la boucle.
un script lira les éléments constitutifs de la facture et des prints seront utilisés pour mettre cette dernière en forme.
