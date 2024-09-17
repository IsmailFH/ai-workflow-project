#!/usr/bin/env python
"""
model tests
"""

import os, sys
import unittests
from ast import literal_eval
import pandas as pd
from datetime import date
LOG_DIR ="Logs/"
LOG_PREFIX = 'unittests'
sys.path.insert(1, os.path.join('..', os.getcwd()))


from logger import update_train_log, update_predict_log


class LoggerTest(unittests.TestCase):
    def test_01_train(self):

        today = date.today()
        log_file = os.path.join(LOG_DIR, "{}-train-{}-{}.log".format(LOG_PREFIX, today.year, today.month))
        if os.path.exists(log_file):
            os.remove(log_file)

        country = 'all'
        date_range = ('2017-11-29', '2019-05-24')
        metric = {'rmse': 0.5}
        runtime = "00:00:01"
        model_version = 0.1
        model_version_note = "test model"

        update_train_log(country, date_range, metric, runtime,
                         model_version, model_version_note, test=True, prefix=LOG_PREFIX)

        self.assertTrue(os.path.exists(log_file))

    def test_02_train(self):
        today = date.today()
        log_file = os.path.join(LOG_DIR, "{}-train-{}-{}.log".format(LOG_PREFIX, today.year, today.month))

        ## update the log
        country = 'all'
        date_range = ('2017-11-29', '2019-05-24')
        metric = {'rmse': 0.5}
        runtime = "00:00:01"
        model_version = 0.1
        model_version_note = "test model"

        update_train_log(country, date_range, metric, runtime,
                         model_version, model_version_note, test=True, prefix=LOG_PREFIX)
        df = pd.read_csv(log_file)
        logged_metric = [literal_eval(i) for i in df['metric'].copy()][-1]
        self.assertEqual(metric, logged_metric)

    def test_03_predict(self):
        """
        ensure log file is created
        """

        log_file = os.path.join("logs", "predict-test.log")
        if os.path.exists(log_file):
            os.remove(log_file)

        y_pred = [0]
        y_proba = [0.6, 0.4]
        runtime = "00:00:02"
        model_version = 0.1
        country = "all"
        target_date = '2017-03-06'

        update_predict_log(country, y_pred, y_proba, target_date, runtime,
                           model_version, test=True, prefix=LOG_PREFIX)

        self.assertTrue(os.path.exists(log_file))
    def test_04_predict(self):
        """
        ensure that content can be retrieved from log file
        """

        log_file = os.path.join("logs", "predict-test.log")

        y_pred = [0]
        y_proba = [0.6, 0.4]
        runtime = "00:00:02"
        model_version = 0.1
        country = "all"
        target_date = '2017-03-06'

        update_predict_log(country, y_pred, y_proba, target_date, runtime,
                           model_version, test=True, prefix=LOG_PREFIX)

        df = pd.read_csv(log_file)
        logged_y_pred = [literal_eval(i) for i in df['y_pred'].copy()][-1]
        self.assertEqual(y_pred, logged_y_pred)

if __name__ == '__main__':
    unittests.main()

