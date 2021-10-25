import pathlib
import pandas


class Dataset:

    def __init__(self):
        self.dataset = pandas.read_csv(str(pathlib.Path(__file__).parent) + '/dataset.csv',
                                       names=['personagem_1', 'personagem_2', 'interacoes', 'livro'])

    def add(self, source: str, target: str, weight: str, book: str):
        df = pandas.DataFrame()
        df['personagem_1'] = [source]
        df['personagem_2'] = [target]
        df['interacoes'] = [weight]
        df['livro'] = [book]

        df = pandas.concat([self.dataset, df])

        df.to_csv(str(pathlib.Path(__file__).parent) + '/dataset2.csv', index=False)
        self.dataset = df
