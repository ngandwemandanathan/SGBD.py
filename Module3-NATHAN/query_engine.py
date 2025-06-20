from typing import List, Dict

def recherche_sequentielle(table: List[Dict], critere) -> List[Dict]:
    """Retourne les enregistrements qui satisfont le critère donné."""
    return [enr for enr in table if critere(enr)]

def filtrer_par_seuil(table: List[Dict], cle: str, seuil: int) -> List[Dict]:
    """Retourne les enregistrements où la valeur de la clé est supérieure au seuil."""
    return [enr for enr in table if enr.get(cle, 0) > seuil]

def construire_index(table: List[Dict], cle: str) -> Dict:
    """Construit un index basé sur une clé."""
    index = {}
    for item in table:
        index.setdefault(item.get(cle), []).append(item)
    return index

def recherche_indexee(index: Dict, seuil: int) -> List[Dict]:
    """Recherche dans l'index les enregistrements où la clé est supérieure au seuil."""
    return [enr for k in index for enr in index[k] if isinstance(k, int) and k > seuil]
