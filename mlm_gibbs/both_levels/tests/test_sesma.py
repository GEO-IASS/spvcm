from mlm_gibbs import both_levels as M
from mlm_gibbs.tests.utils import Model_Mixin
from mlm_gibbs.abstracts import Trace
import unittest as ut
import pandas as pd
from .make_data import FULL_PATH

class Test_SESMA(ut.TestCase, Model_Mixin):
    def setUp(self):
        super(Test_SESMA, self).build_self()
        self.cls = M.SESMA
        self.inputs['n_samples'] = 0
        self.instance = self.cls(**self.inputs)
        self.answer_trace = Trace.from_csv(FULL_PATH + '/data/sesma.csv')
