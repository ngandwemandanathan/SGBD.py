mport json
import os

FICHIER_JSON = "base_de_donnees.json"

def sauvegarder(tables, schemas, fichier=FICHIER_JSON):
    data = {
        "tables": tables,
        "schemas": schemas
    }
    try:
        with open(fichier, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("Sauvegarde effectuée avec succès.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")

def charger(fichier=FICHIER_JSON):
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print("Chargement effectué avec succès.")
        return data["tables"], data["schemas"]
    except FileNotFoundError:
        print("Aucun fichier de sauvegarde trouvé. Création d'une base vide.")
        return {}, {}
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")
        return {}, {}
