ef creer_schema(nom_table, colonnes_types):
    schemas[nom_table] = colonnes_types
    print(f"Schéma créé pour {nom_table}: {colonnes_types}")

def afficher_schemas():
    for table, champs in schemas.items():
        print(f"{table}: {champs}")

def valider_enregistrement(nom_table, enregistrement):
    schema = schemas.get(nom_table)
    if schema is None:
        print(f"Erreur : la table {nom_table} n'existe pas.")
        return False

    for champ, type_attendu in schema.items():
        if champ not in enregistrement:
            print(f"Erreur : le champ '{champ}' est manquant.")
            return False

        if type_attendu == "int" and not isinstance(enregistrement[champ], int):
            print(f"Erreur : le champ '{champ}' doit être un entier (int).")
            return False
        elif type_attendu == "str" and not isinstance(enregistrement[champ], str):
            print(f"Erreur : le champ '{champ}' doit être une chaîne (str).")
            return False

    return True
