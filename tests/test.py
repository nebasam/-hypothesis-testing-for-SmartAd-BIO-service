import unittest
import sys
import os
import pandas as pd
from pandas.core.frame import DataFrame
sys.path.append(os.path.abspath(os.path.join('../scripts/')))
sys.path.insert(1, 'scripts')

import main

class HypothesisTesting(unittest.TestCase):

    def setUp(self):
        self.path = '../Data/AdSmartABdata.csv'

    def test_read_proccessed_data(self):
        df = main.read_proccessed_data(self.path)
        assert type(df) is DataFrame

    def tearDown(self) -> None:
        print('Closed')

if __name__ == '__main__':
    unittest.main()
    