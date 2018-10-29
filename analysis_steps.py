# coding: utf-8

import pandas
import pandas as pd
pd.read_csv("2015Q2-house-disburse-detail-updated.csv")
dataset = pd.read_csv("2015Q2-house-disburse-detail-updated.csv")
dataset.sum
dataset.AMOUNT
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
list(map(locale.atof, dataset.AMOUNT))
amount_column_float = list(map(locale.atof, dataset.AMOUNT))
sum(amount_column_float)
dataset = pd.read_csv("2015Q2-house-disburse-detail-updated.csv")
from dateutil.parser import parse
dataset['COVERAGE_PERIOD'] = dataset.apply(lambda row: (parse(row['END DATE']) - parse(row['START DATE'])).days, axis=1)
dataset.COVERAGE_PERIOD.std()
sum(map(locale.atof, dataset.AMOUNT))
list(map(locale.atof, dataset.AMOUNT))
list(map(locale.atof, dataset.AMOUNT))[-5:-1]
dataset.COVERAGE_PERIOD
list(map(locale.atof, dataset.AMOUNT))[-5:]
list(map(locale.atof, dataset.AMOUNT))[-5:]
sum(map(locale.atof, dataset.AMOUNT))
sum(map(lambda x: abs(locale.atof(x)), dataset.AMOUNT))
dataset['AMOUNT_FLOAT'] = pd.Series(list(map(locale.atof, dataset.AMOUNT))).values
positive_dataset = dataset[dataset.AMOUNT_FLOAT > 0]
dataset['START_PARSED'] = pd.Series(list(map(parse, dataset['START DATE']))).values
positive_dataset = dataset.query('AMOUNT_FLOAT > 0')
sum(positive_dataset[(positive_dataset.START_PARSED >= parse('1/1/2010')) &( positive_dataset.START_PARSED <= parse('2016-12-31'))].AMOUNT_FLOAT) / 7


