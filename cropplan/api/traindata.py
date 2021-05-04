from django.http import JsonResponse, HttpResponse
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from swarmlib import FireflyProblem, FUNCTIONS
from FireflyAlgorithm import *
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
import pickle, pdfkit, json, joblib

def train_data(request):
    no_iterations = int(request.GET['iteration'])
    data = pd.read_csv('frontend/src/assets/uploaded/cropdataset.csv')
    print(data.shape)
    plt.figure(figsize=(8, 6))
    sns.countplot(data['item'], label="Count")
    plt.savefig('frontend/src/assets/plots/countplot.png')
    plt.close()

    try:
      X = data.drop('item', axis=1)
      y = data['item']
      count=0
      for count in range(no_iterations):
          count+=1
          X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)
          fill_values = SimpleImputer(missing_values=np.nan, strategy='mean')
          X_train = fill_values.fit_transform(X_train).astype(str)
          X_test = fill_values.fit_transform(X_test).astype(str)

      xgb_model = XGBClassifier(gamma=0)
      xgb_model.fit(X_train, y_train)
      joblib_file = "frontend/src/assets/plots/xgbmodel.pkl"
      joblib.dump(xgb_model, joblib_file)
      xgb_pred = xgb_model.predict(X_test)
      xgb_accuracy = metrics.accuracy_score(y_test, xgb_pred)
      xgb_report = metrics.precision_recall_fscore_support(y_test, xgb_pred)
      xgb_dic_report = {
          "algorithm": 'XGBoost(Gradient Boost)',
          "accuracy": str(xgb_accuracy.round(2)),
          "precision": str(xgb_report[0][0].round(2)),
          "recall": str(xgb_report[1][0].round(2)),
          "f1_score": str(xgb_report[2][0].round(2)),
          "support": str(xgb_report[3][0])
      }

      svm_model = SVC()
      svm_model.fit(X_train, y_train)
      joblib_file_svm = "frontend/src/assets/plots/svmmodel.pkl"
      joblib.dump(svm_model, joblib_file_svm)
      svm_pred = svm_model.predict(X_test)
      svm_accuracy = metrics.accuracy_score(y_test, svm_pred)
      svm_report = metrics.precision_recall_fscore_support(y_test, svm_pred)
      svm_dic_report = {
          "algorithm": 'Support Vector Machine (SVM)',
          "accuracy": str(svm_accuracy.round(2)),
          "precision": str(svm_report[0][0].round(2)),
          "recall": str(svm_report[1][0].round(2)),
          "f1_score": str(svm_report[2][0].round(2)),
          "support": str(svm_report[3][0])
      }

      lgr_model = LogisticRegression()
      lgr_model.fit(X_train, y_train)
      joblib_file_lgr = "frontend/src/assets/plots/lgrmodel.pkl"
      joblib.dump(lgr_model, joblib_file_lgr)

      lgr_pred = lgr_model.predict(X_test)
      lgr_accuracy = metrics.accuracy_score(y_test, lgr_pred)
      lgr_report = metrics.precision_recall_fscore_support(y_test, lgr_pred)
      lgr_dic_report = {
          "algorithm": 'Logistic Regression',
          "accuracy": str(lgr_accuracy.round(2)),
          "precision": str(lgr_report[0][0].round(2)),
          "recall": str(lgr_report[1][0].round(2)),
          "f1_score": str(lgr_report[2][0].round(2)),
          "support": str(lgr_report[3][0])
      }

      feat_importances = pd.Series(xgb_model.feature_importances_, index=X.columns)
      plt.figure(figsize=(8, 6))
      feat_importances.nlargest(10).plot(kind='barh')
      plt.savefig('frontend/src/assets/plots/feat_importances.png')

      feedback = {
          'status': 'success',
          'confirmed': 'success',
          'msg': "Data was trained, model has been created and optimization is successful",
          'classname': 'alert alert-primary p-1 text-center',
          'xgb_report': xgb_dic_report,
          'svm_report': svm_dic_report,
          'lgr_report': lgr_dic_report,
      }
    except Exception as e:
        feedback = {
            'status': 'Failed',
            'msg': 'Error training data, please try again',
            'classname': 'alert alert-danger p-1 text-center',
        }
        print(e)
    return JsonResponse(feedback, safe=False)


def model_analysis():

    xgb_pred = xgb_model.predict(X_test)
    xgb_accuracy = metrics.accuracy_score(y_test, xgb_pred)
    xgb_report = metrics.precision_recall_fscore_support(y_test, xgb_pred)
    xgb_dic_report = {
        "algorithm": 'XGBoost(Gradient Boost)',
        "accuracy": str(xgb_accuracy.round(2)),
        "precision": str(xgb_report[0][0].round(2)),
        "recall": str(xgb_report[1][0].round(2)),
        "f1_score": str(xgb_report[2][0].round(2)),
        "support": str(xgb_report[3][0])
    }



def svm(X_train, y_train):
    # SVM_MODEL
    svm_model = SVC()
    svm_model.fit(X_train, y_train)
    svm_pred = svm_model.predict(X_test)
    svm_accuracy = metrics.accuracy_score(y_test, svm_pred)
    return JsonResponse(classification_report(y_test, svm_pred), safe=False)
    # ENd


def lgr(X_train, y_train):
    lgr_model = LogisticRegression()
    lgr_model.fit(X_train, y_train)
    lgr_pred = lgr_model.predict(X_test)
    lgr_accuracy = metrics.accuracy_score(y_test, lgr_pred)
    print('LGR', classification_report(y_test, lgr_pred))
    return JsonResponse(classification_report(y_test, lgr_pred), safe=False)
    # ENd
