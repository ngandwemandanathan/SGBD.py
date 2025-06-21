from typing import List, Dict

def recherche_sequentielle(table: List[Dict], critere) -> List[Dict]:
    return [enr for enr in table if critere(enr)]

def filtrer_par_seuil(table: List[Dict], cle: str, seuil: int) -> List[Dict]:
    return [enr for enr in table if enr.get(cle, 0) > seuil]

def construire_index(table: List[Dict], cle: str) -> Dict:
    index = {}
    for item in table:
        index.setdefault(item.get(cle), []).append(item)
    return index

def recherche_indexee(index: Dict, seuil: int) -> List[Dict]:
    return [enr for k in index for enr in index[k] if isinstance(k, int) and k > seuil]


