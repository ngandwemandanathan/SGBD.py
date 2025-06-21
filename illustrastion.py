
# main_cli.py

from schema_manager import creer_schema, afficher_schemas
from crud_operations import (
    insertion_enregistrement, lire_enregistrements,
    mise_a_jour_enregistrement, supprimer_enregistrement
)
from query_engine import recherche_sequentielle, filtrer_par_seuil
from sort_engine import trier_table
from storage import charger, sauvegarder

# Chargement initial
tables, schemas = charger()

def menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Créer un schéma")
    print("2. Afficher les schémas")
    print("3. Ajouter un enregistrement")
    print("4. Afficher une table")
    print("5. Mettre à jour un enregistrement")
    print("6. Supprimer un enregistrement")
    print("7. Rechercher par critère")
    print("8. Filtrer par seuil")
    print("9. Trier une table")
    print("10. Sauvegarder")
    print("0. Quitter")

while True:
    menu()
    choix = input("Choisissez une option : ")

    if choix == "1":
        nom = input("Nom de la table : ")
        nb = int(input("Nombre de colonnes : "))
        colonnes = {}
        for _ in range(nb):
            champ = input("Nom du champ : ")
            typ = input("Type (str/int) : ")
            colonnes[champ] = typ
        creer_schema(nom, colonnes)

    elif choix == "2":
        afficher_schemas()

    elif choix == "3":
        table = input("Nom de la table : ")
        enreg = {}
        for champ in schemas.get(table, {}):
            val = input(f"{champ} ({schemas[table][champ]}): ")
            enreg[champ] = int(val) if schemas[table][champ] == "int" else val
        insertion_enregistrement(table, enreg, tables)

    elif choix == "4":
        table = input("Nom de la table à afficher : ")
        lire_enregistrements(table, tables)

    elif choix == "5":
        table = input("Table à modifier : ")
        champ_cond = input("Champ pour condition : ")
        val_cond = input("Valeur recherchée : ")
        champ_modif = input("Champ à modifier : ")
        nouvelle_val = input("Nouvelle valeur : ")
        condition = {champ_cond: int(val_cond) if val_cond.isdigit() else val_cond}
        nouveau = {champ_modif: int(nouvelle_val) if nouvelle_val.isdigit() else nouvelle_val}
        mise_a_jour_enregistrement(table, condition, nouveau, tables)

    elif choix == "6":
        table = input("Table à nettoyer : ")
        champ = input("Champ condition : ")
        val = input("Valeur à supprimer : ")
        condition = {champ: int(val) if val.isdigit() else val}
        supprimer_enregistrement(table, condition, tables)

    elif choix == "7":
        table = input("Table à rechercher : ")
        champ = input("Champ critère : ")
        val = input("Valeur du critère : ")
        resultat = recherche_sequentielle(tables[table], lambda r: str(r.get(champ)) == val)
        for r in resultat:
            print(r)

    elif choix == "8":
        table = input("Table à filtrer : ")
        cle = input("Clé numérique : ")
        seuil = int(input("Seuil minimum : "))
        resultat = filtrer_par_seuil(tables[table], cle, seuil)
        for r in resultat:
            print(r)

    elif choix == "9":
        table = input("Nom de la table à trier : ")
        cle = input("Clé de tri : ")
        try:
            trier_table(tables, schemas, table, cle)
        except Exception as e:
            print(f"Erreur : {e}")

    elif choix == "10":
        sauvegarder(tables, schemas)

    elif choix == "0":
        print("Au revoir !")
        break

    else:
        print("Option invalide.")
