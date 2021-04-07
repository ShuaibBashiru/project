from django.http import JsonResponse, HttpResponse
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from swarmlib import FireflyProblem, FUNCTIONS
from FireflyAlgorithm import *
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn import metrics
import pickle
import SwarmPackagePy
# from sklearn.externals import joblib
# If the glucose level of the patient
# is greater than 125 mg/dL and his/her
# blood pressure is between 129 and 225
# mmHg, then the patient is diabetic.
# Index(['Pregnancies', 'glucose', 'bloodPressure', 'skinThickness', 'insulin',
#        'bmi', 'diabetesPedigreeFunction', 'age', 'Outcome'],
#       dtype='object')

def Fun(x):
    return 5


def testing():
    # svm_model = Ssifier(gamma=0)
    # svm_model.fit(X_train, y_train)
    # svm_pred = svm_model.predict(X_test)
    # svm_accuracy = metrics.accuracy_score(y_test, svm_pred)
    # svm_prediction = svm_model.predict_proba(X_test)
    # svm_report = metrics.precision_recall_fscore_support(y_test, svm_pred)
    # svm_dic_report = {
    #     "algorithm": 'SVM',
    #     "accuracy": str(svm_accuracy.round(2)),
    #     "precision": str(svm_report[0][0].round(2)),
    #     "recall": str(svm_report[1][0].round(2)),
    #     "f1_score": str(svm_report[2][0].round(2)),
    #     "support": str(svm_report[3][0])
    # }
    #
    # lgr_model = LogisticRegression()
    # lgr_model.fit(X_train, y_train)
    # lgr_pred = lgr_model.predict(X_test)
    # lgr_accuracy = metrics.accuracy_score(y_test, lgr_pred)
    # svm_prediction = lgr_model.predict_proba(X_test)
    # lgr_report = metrics.precision_recall_fscore_support(y_test, lgr_pred)
    # svm_dic_report = {
    #     "algorithm": 'LGR',
    #     "accuracy": str(lgr_accuracy.round(2)),
    #     "precision": str(lgr_report[0][0].round(2)),
    #     "recall": str(lgr_report[1][0].round(2)),
    #     "f1_score": str(lgr_report[2][0].round(2)),
    #     "support": str(lgr_report[3][0])
    # }


    1
# testing()