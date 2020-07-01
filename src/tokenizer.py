# -*- coding: utf-8 -*-
# import
from src.parameters import Options
from ckiptagger import WS, POS, NER
import zipfile
import gdown
from os.path import join, exists
import argparse
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# class


class Tokenizer:
    """This class will tokenize the text by the ckip model.

    Arguments:
        data_path {str} -- the data path.
    """

    def __init__(self, data_path):
        if not exists(join(data_path, 'ckip_data')):
            self.download_ckip_data(data_path=data_path, remove=True)
        self.ws = WS(join(data_path, 'ckip_data'))
        self.pos = POS(join(data_path, 'ckip_data'))
        self.ner = NER(join(data_path, 'ckip_data'))

    def download_ckip_data(self, data_path, remove=True):
        """This function will download ckip data from google drive and remove the downloaded data.

        Args:
            data_path (str): the data path.
            remove (bool, optional): whether to remove the downloaded data. Defaults to True.
        """
        if not exists(data_path):
            os.makedirs(data_path, exist_ok=True)
        file_id = '1efHsY16pxK0lBD2gYCgCTnv1Swstq771'
        url = f'https://drive.google.com/uc?id={file_id}'
        data_zip = join(data_path, 'data.zip')
        gdown.download(url, data_zip, quiet=False)
        with zipfile.ZipFile(data_zip, 'r') as zip_ref:
            zip_ref.extractall(data_path)
        os.rename(data_zip[:-4], join(data_path, 'ckip_data'))
        if remove:
            os.remove(data_zip)

    def tokenize(self, text):
        ws_results = self.ws([text])
        pos_results = self.pos(ws_results)
        ner_results = self.ner(ws_results, pos_results)
        result = {'tokenize': ws_results[0],
                  'pos': pos_results[0],
                  'ner': ner_results[0]}
        return result


if __name__ == "__main__":
    # parameters
    opt = Options().parse()
    data_path = opt.datapath
    text = '我是楊明豪，目前在產學智慧辨識研究中心(Intelligent Recognition Industry Service Research Center, IRIS)擔任AI工程師。'

    # create tokenizer
    tokenizer = Tokenizer(data_path)

    # tokenize
    result = tokenizer.tokenize(text)
