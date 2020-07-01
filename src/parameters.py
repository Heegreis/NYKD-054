# -*- coding: utf-8 -*-
# import
import argparse

# class


class Options:
    """The options of the NYKD-054.
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        self.parser.add_argument(
            '--datapath', type=str, default='./data/', help='the data path.')

    def parse(self):
        self.opt = self.parser.parse_args()
        return self.opt


if __name__ == "__main__":
    opt = Options().parse()
    print(opt)
