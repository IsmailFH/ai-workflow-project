#!/usr/bin/env python
"""
logging a machine learning model to enable performance monitoring
"""

import time, os, csv, uuid
from datetime import date

MODEL_VERSION = 0.1
MODEL_VERSION_NOTE = "RandomForest model"
LOG_DIR_PATH = os.path.join(os.path.dirname(__file__), '..', 'logs')


def update_predict_log(country, y_pred, y_proba, target_date, runtime, model_version=MODEL_VERSION, test=False,
                       prefix='example'):

    today = date.today()
    logfile = os.path.join(LOG_DIR_PATH, "predict-{}-{}.log".format(today.year, today.month))

    header = ['unique_id', 'timestamp', 'country', 'y_pred', 'y_proba', 'target_date', 'model_version', 'runtime',
              'type']
    write_header = False

    if not os.path.exists(logfile):
        write_header = True
    with open(logfile, 'a+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        if write_header:
            writer.writerow(header)

        type = test and 'test' or 'prod'
        to_write = map(str,
                       [uuid.uuid4(), time.time(), country, y_pred, y_proba, target_date, model_version, runtime, type])
        writer.writerow(to_write)


def update_train_log(country, date_range, metric, runtime, model_version=MODEL_VERSION,
                     model_version_note=MODEL_VERSION_NOTE,
                     test=False):

    today = date.today()
    logfile = os.path.join(LOG_DIR_PATH, "train-{}-{}.log".format(today.year, today.month))
    header = ['unique_id', 'timestamp', 'country', 'date_range', 'metric', 'model_version', 'model_version_note',
              'runtime', 'type']
    write_header = False

    if not os.path.exists(logfile):
        write_header = True
    with open(logfile, 'a+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        if write_header:
            writer.writerow(header)

        mode = test and 'test' or 'prod'
        to_write = map(str, [uuid.uuid4(), time.time(), country, date_range, metric, model_version, model_version_note,
                             runtime, mode])
        writer.writerow(to_write)