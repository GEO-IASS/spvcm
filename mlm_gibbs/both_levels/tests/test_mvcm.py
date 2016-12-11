from mlm_gibbs import both_levels as M
from mlm_gibbs.tests.utils import Model_Mixin
from mlm_gibbs.abstracts import Trace
import unittest as ut
import pandas as pd
from .make_data import FULL_PATH

class Test_MVCM(ut.TestCase, Model_Mixin):
    def setUp(self):
        super(Test_MVCM, self).build_self()
        self.cls = M.MVCM
        del self.inputs['M']
        del self.inputs['W']
        self.inputs['n_samples'] = 0
        self.instance = self.cls(**self.inputs)
        self.answer_trace = Trace.from_csv(FULL_PATH + '/data/mvcm.csv')
