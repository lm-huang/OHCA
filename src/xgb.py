import data_helpers as data_helper
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay, classification_report, roc_curve, \
    auc
from sklearn.model_selection import train_test_split
from sklearn.metrics import RocCurveDisplay
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from sklearn.model_selection import RandomizedSearchCV

df = data_helper.get_cardiac_arrest_data()
df = df.sample(frac=0.1, random_state=42)
df = df[(df['call_to_patient_time'] > 0) & (df['call_to_patient_time'] < 25)]
df = data_helper.filter_age(df, 100)
X, y = data_helper.prepare(df)

def randomized_search_cv(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    params = {
        'max_depth': [7, 10],
        'learning_rate': [0.1, 0.5],
        'subsample': [0.6, 0.8]
    }
    pipe = XGBClassifier()

    search = RandomizedSearchCV(pipe, param_distributions=params, n_iter=8, n_jobs=-1, cv=3, random_state=42)
    search.fit(X_train, y_train)
    print(search.cv_results_)
    print("Tuned hyperparameters (best parameters): ", search.best_params_)
    print("Best accuracy:", search.best_score_)

    y_predict = search.predict(X_test)
    score = accuracy_score(y_predict, y_test)
    # Predict probabilities for the positive outcome only
    y_probs = search.predict_proba(X_test)[:, 1]  # Get probabilities for the positive class

    print("Accuracy score on hold out set: ", score)
    print(classification_report(y_test, y_predict))

    # Calculate ROC AUC
    fpr, tpr, _ = roc_curve(y_test, y_probs)
    roc_auc = auc(fpr, tpr)
    print("ROC AUC: ", roc_auc)

    # Display ROC Curve
    plt.figure(figsize=(8, 6))
    RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc, estimator_name='XGBClassifier').plot()
    plt.xlabel('False Positive Rate (1 - Specificity)')
    plt.ylabel('True Positive Rate (Sensitivity)')
    plt.title('ROC Curve for Survival Prediction')
    plt.savefig("figs/xgb1.png")
    plt.show()

    # Display Confusion Matrix
    cm = confusion_matrix(y_test, y_predict)
    plt.figure(figsize=(8, 6))
    ConfusionMatrixDisplay(cm, display_labels=['Died', 'Survived']).plot()
    plt.title('Confusion Matrix')
    plt.savefig("figs/xgb2.png")
    plt.show()

    return search.best_estimator_, X_test, y_test, y_probs

# Assuming 'X' and 'y' are already defined and preprocessed
best_model, X_test, y_test, y_probs = randomized_search_cv(X, y)
