from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay, classification_report, RocCurveDisplay
import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

def logistic_pipeline() -> Pipeline:
    """
    Create a pipeline with PCA and logistic regression
    """
    logistic_regression = LogisticRegression(random_state=42, solver='saga', max_iter=10000)
    pca = PCA()
    pipe = Pipeline(steps=[("pca", pca), ("logistic", logistic_regression)])
    return pipe

def logistic_param_grid() -> dict:
    """
    Parameter grid for logistic regression
    """
    c = [1, 0.1, 0.01, 0.001]
    param_grid = {
        "logistic__C": c,
    }
    return param_grid

def random_forest_pipeline() -> Pipeline:
    """
    Create a pipeline with PCA and random forest classifier
    """
    random_forest = RandomForestClassifier(random_state=42)
    pca = PCA()
    pipe = Pipeline(steps=[("pca", pca), ("random_forest", random_forest)])
    return pipe

def random_forest_param_grid() -> dict:
    """
    Parameter grid for random forest
    """
    params = {
        'random_forest__n_estimators': [100, 200, 300],
        'random_forest__max_depth': [10, 20, 30],
        'random_forest__max_features': ['sqrt'],
        'random_forest__min_samples_leaf': [1, 2, 4],
        'random_forest__min_samples_split': [2, 5, 10],
    }
    return params

def xgb_pipeline() -> Pipeline:
    """
    Create a pipeline with PCA and XGBoost classifier
    """
    xgb = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
    pca = PCA()
    pipe = Pipeline(steps=[("pca", pca), ("xgb", xgb)])
    return pipe

def xgb_params() -> dict:
    """
    Parameter grid for XGBoost
    """
    params = {
        'xgb__max_depth': [3, 5, 7],
        'xgb__learning_rate': [0.1, 0.01, 0.001],
        'xgb__subsample': [0.8, 0.9, 1.0],
        'xgb__n_estimators': [100, 200, 300],
    }
    return params

def grid_search_cv(X, y, model: str):
    """
    Grid search cross validation to find the best hyperparameters
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    if model == 'logistic':
        pipe = logistic_pipeline()
        params = logistic_param_grid()
    elif model == 'random_forest':
        pipe = random_forest_pipeline()
        params = random_forest_param_grid()
    elif model == 'xgb':
        pipe = xgb_pipeline()
        params = xgb_params()
    else:
        raise ValueError("Model not supported")

    search = GridSearchCV(pipe, param_grid=params, cv=5, n_jobs=-1, return_train_score=False)
    search.fit(X_train, y_train)

    y_predict = search.predict(X_test)  # Generate predictions

    return search, X_test, y_predict, y_test  # Correctly return four values

def roc_curve(search, X, y, title, file):
    """
    Plot ROC curve from the results of a GridSearchCV object
    """
    plt.figure(figsize=(10, 8))
    RocCurveDisplay.from_estimator(search.best_estimator_, X, y)
    plt.title(title)
    plt.savefig(file)
    plt.show()

def plot_confusion_matrix(search, y_true, y_predict, title, file):
    """
    Plot confusion matrix from the results of a GridSearchCV object
    """
    plt.figure(figsize=(10, 8))
    cm = confusion_matrix(y_true, y_predict, labels=search.best_estimator_.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=search.best_estimator_.classes_)
    disp.plot()
    plt.title(title)
    plt.savefig(file)
    plt.show()
