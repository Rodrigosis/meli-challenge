from fastapi import APIRouter
from typing import List, Dict

from src.infra.dataset import Dataset
from src.domain.common_friends import CommonFriends

router = APIRouter()
data = Dataset()


@router.get("/common-friends")
async def common_friends(source: str, target: str) -> Dict:
    return CommonFriends(data).get_common_friends(p1=source, p2=target)


@router.post("/interaction", status_code=201)
async def interaction(new_interaction: Dict):
    for i in ('source', 'target', 'weight', 'book'):
        if i not in new_interaction:
            raise ValueError('Parametro "' + i + '" nao encontrado')

    if not int(new_interaction['book']) == 4:
        raise ValueError('Somente interacoes do quarto livro podem ser inseridas')

    data.add(source=new_interaction['source'],
             target=new_interaction['target'],
             weight=new_interaction['weight'],
             book=new_interaction['book'])
