om schema_manager import valider_enregistrement

def insertion_enregistrement(nom_table, enregistrement, tables):
    if nom_table not in tables:
        tables[nom_table] = []
    if valider_enregistrement(nom_table, enregistrement):
        tables[nom_table].append(enregistrement)
        print(f"Enregistrement ajouté à {nom_table}")
    else:
        print("Enregistrement invalide.")

def lire_enregistrements(nom_table, tables):
    if nom_table not in tables:
        print(f"La table {nom_table} n'existe pas.")
        return
    for enr in tables[nom_table]:
        print(enr)

def mise_a_jour_enregistrement(nom_table, condition, nouveau, tables):
    if nom_table not in tables:
        print(f"La table {nom_table} n'existe pas.")
        return
    modifie = False
    for enr in tables[nom_table]:
        if all(enr.get(k) == v for k, v in condition.items()):
            enr.update(nouveau)
            modifie = True
    print("Mise à jour effectuée." if modifie else "Aucun enregistrement mis à jour.")

def supprimer_enregistrement(nom_table, condition, tables):
    if nom_table not in tables:
        print(f"La table {nom_table} n'existe pas.")
        return
    original = len(tables[nom_table])
    tables[nom_table] = [enr for enr in tables[nom_table] if not all(enr.get(k) == v for k, v in condition.items())]
    supprimes = original - len(tables[nom_table])
    print(f"{supprimes} enregistrement(s) supprimé(s).")
