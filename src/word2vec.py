# -*- coding: utf-8 -*-
# import
from src.parameters import Options
import numpy as np
from os.path import join

# class


class Word2Vec:
    """The word2vec will convert the word to vector.

    Arguments:
        data_path {str} -- the data path.
    """

    def __init__(self, data_path):
        self.token = np.load(
            join(data_path, 'ckip_data/embedding_word/token_list.npy'))
        self.vector = np.load(
            join(data_path, 'ckip_data/embedding_word/vector_list.npy')).astype(np.float16)

    def transform(self, text):
        vec = []
        for t in text:
            if t in self.token:
                idx = np.argwhere(self.token == t)[0, 0]
                vec.append(self.vector[idx])
            else:
                temp = np.zeros(300, dtype=np.float16)
                for c in t:
                    if c in self.token:
                        idx = np.argwhere(self.token == c)[0, 0]
                        temp += self.vector[idx]
                vec.append(temp)
        return np.array(vec)


if __name__ == "__main__":
    # parameters
    opt = Options().parse()
    data_path = opt.datapath
    text = ['楊', '明', '豪', '楊明豪']

    # create word2vec
    w2v = Word2Vec(data_path=data_path)

    # transform
    vec = w2v.transform(text=text)
