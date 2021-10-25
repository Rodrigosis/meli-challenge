from unittest import TestCase
import pathlib
import pandas  # type: ignore

from src.domain.common_friends import CommonFriends


class TestCommonFriends(TestCase):

    def test_get_common_friends(self):
        test_1 = CommonFriends(Dataset()).get_common_friends('Tregar', 'Arya-Stark')
        self.assertEqual(test_1, {'common_friends': ['Eddard-Stark']})

        test_2 = CommonFriends(Dataset()).get_common_friends('Tregar', 'Coratt')
        self.assertEqual(test_2, {'common_friends': []})

    def test_get_friend(self):
        test = CommonFriends(Dataset()).get_friend('Tregar')

        self.assertEqual(test, ['Eddard-Stark'])


class Dataset:

    def __init__(self):
        self.dataset = pandas.read_csv(str(pathlib.Path(__file__).parent.parent.parent) + '/src/infra/dataset.csv',
                                       names=['personagem_1', 'personagem_2', 'interacoes', 'livro'])
