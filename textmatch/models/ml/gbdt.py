# -*- coding:utf-8 -*-
'''
-------------------------------------------------
   Description :  GBDT
   Author :       machinelp
   Date :         2020-06-13
-------------------------------------------------

'''
import sys
import logging
import numpy as np
from textmatch.config.config import cfg
from textmatch.config.constant import Constant as const
from sklearn.ensemble import GradientBoostingClassifier

class GBDT:

    def __init__(self):
        #self.other_params = {'learning_rate': cfg.lr.learning_rate
        #                     }
        self.clf = GradientBoostingClassifier()
        pass

    def fit(self, train_x, train_y):
        self.clf.fit(train_x, train_y)
        return self

    def predict(self, X_test):
        predict = self.clf.predict_proba(X_test)[:,1]
        return predict

    def save_model(self):
        pass

    def load_model(self):
        pass
















