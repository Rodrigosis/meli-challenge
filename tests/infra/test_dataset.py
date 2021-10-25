from unittest import TestCase
import pandas  # type: ignore
import pathlib

from src.infra.dataset import Dataset


class TestDataset(TestCase):

    def test_add(self):
        data = Dataset()

        data.add('foo_1', 'foo_2', 'foo_interacoes', 'foo_livro')

        df = pandas.read_csv(str(pathlib.Path(__file__).parent.parent.parent) + '/src/infra/dataset2.csv',
                             names=['con1', 'con2', 'con3', 'con4'])

        test = df[df['con1'] == 'foo_1'].shape

        self.assertEqual(test[0], 1)
        self.assertEqual(test[1], 4)
