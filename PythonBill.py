print("Bonjour et bienvenu dans notre programme de réalisation de facture")
print("tout ce que vous avez à faire est de nous renseigner le paramètre des éléments que vous souhaitez contabiliser")
print("et laisser la magie opérér")

achats = []
compteur = 1

while True:
    print("Ajoutons un nouvel élément à vos courses.")
    name = input("Merçi d'entrer le nom du produit: ")
    price = int(input("Merci d'entrer le prix du produit: "))
    quatity = int(input("Merci d'entrer les quantités du priduit: "))
    produit = "produit" + str(compteur)
    
    produit = {"name" : name,
               "price" : price,
               "quantity" : quatity}
    
    achats.append(produit)
    
    choix = input("Voulez-vous ajouter un nouvel élément à votre liste de courses ? ")
    
    if choix == "non":
        break
    
prixTotal = 0
    
for element in achats:
    prod = element
    nameProd = prod["name"]
    priceProd = prod["price"]
    qtyProd = prod["quantity"]
    somme = priceProd * qtyProd
    prixTotal += somme
    
    print(" {} - {} à {} = {} " . format(qtyProd, nameProd, priceProd, somme))
            
print("le total de votre facture est de : {} Fr CFA. Merci !" . format(prixTotal))