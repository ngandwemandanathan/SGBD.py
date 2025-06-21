# SGBD.py
# README - Système Modulaire de Gestion de Données en Python

Ce projet implémente un mini SGBD (Système de Gestion de Base de Données) à l'aide du langage Python. Il repose sur une architecture modulaire pour assurer la clarté, la maintenabilité et l'évolutivité du code.

---

## Table des Matières

* [Prérequis](#prérequis)
* [Structure du projet](#structure-du-projet)
* [Détails des Modules](#détails-des-modules)

  * [1. schema\_manager.py](#1-schema_managerpy)
  * [2. crud\_operations.py](#2-crud_operationspy)
  * [3. query\_engine.py](#3-query_enginepy)
  * [4. sort\_engine.py](#4-sort_enginepy)
  * [5. storage.py](#5-storagepy)
* [Comment utiliser](#comment-utiliser)

---

## Prérequis

* Python 3.7 ou plus récent
* Aucune bibliothèque externe requise (tout est basé sur les modules standards)

---

## Structure du projet

```bash
/mon_sgbd_modulaire
├── schema_manager.py       # Module de gestion des schémas de table
├── crud_operations.py      # Module des opérations CRUD
├── query_engine.py         # Module de recherche et filtrage
├── sort_engine.py          # Module d'algorithmes de tri
├── storage.py              # Module de sauvegarde/chargement JSON
├── main_cli.py             # Interface utilisateur (non obligatoire)
├── base_de_donnees.json    # Fichier de sauvegarde
```

---

## Détails des Modules

### 1. schema\_manager.py

Ce module permet de :

* Créer un schéma de table (dictionnaire des colonnes et types de données)
* -Valider qu'un enregistrement respecte bien la définition du schéma
* Afficher les schémas disponibles

Structure utilisée :

```python
schemas = {
    "etudiants": {"nom": "str", "age": "int"}
}
```

### 2. crud\_operations.py

Fonctionnalités :

* Ajouter un enregistrement dans une table (après validation)
* Lire tous les enregistrements d'une table
* Mettre à jour des enregistrements correspondant à une condition
* Supprimer des enregistrements selon une condition

Exemple :

```python
insertion_enregistrement("etudiants", {"nom": "Paul", "age": 22}, tables)
```

### 3. query\_engine.py

Contient des fonctions de recherche et filtrage :

* `recherche_sequentielle`: retourne les éléments selon une fonction critère
* `filtrer_par_seuil`: exemple spécifique où une valeur de clé doit dépasser un seuil
* `construire_index` et `recherche_indexee`: permettent des recherches plus rapides via index

### 4. sort\_engine.py

Fonction de tri :

* `tri_selection`: implémentation de tri par sélection sur une clé
* `trier_table`: applique le tri et met à jour la table, puis sauvegarde

Peut être étendu à d'autres algorithmes : insertion, fusion, etc.

### 5. storage.py

Responsable de la persistance des données :

* `sauvegarder`: écrit les tables + schémas dans un fichier JSON
* `charger`: lit et retourne les tables + schémas du fichier

Fichier utilisé : `base_de_donnees.json`

---

## Comment utiliser

1. Créez un schéma via `creer_schema(...)`
2. Ajoutez des données via `insertion_enregistrement(...)`
3. Affichez ou modifiez les données avec `lire_enregistrements`, `mise_a_jour_enregistrement`, `supprimer_enregistrement`
4. Appliquez un tri ou une recherche si nécessaire
5. Sauvegardez ou rechargez les données avec `storage.py`

---

N'hésitez pas à étendre les modules avec plus de types, opérations, ou à y ajouter une interface graphique ou web si besoin.
