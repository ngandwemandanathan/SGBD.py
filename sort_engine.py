from typing import List, Dict
from storage import sauvegarder

def tri_selection(data: List[Dict], cle: str) -> List[Dict]:
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j][cle] < data[min_idx][cle]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

def valider_cle_schema(schema: Dict[str, str], cle: str) -> bool:
    return cle in schema

def trier_table(tables: Dict[str, List[Dict]], schemas: Dict[str, Dict], nom: str, cle: str) -> List[Dict]:
    if nom not in tables or not valider_cle_schema(schemas[nom], cle):
        raise ValueError("Table ou clé invalide.")
    tables[nom] = tri_selection(tables[nom][:], cle)
    sauvegarder(tables, schemas)
    return tables[nom]
