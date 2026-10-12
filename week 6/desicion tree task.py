import pandas as pd
import numpy as np

from sklearn.model_selection import (
    train_test_split,
    RandomizedSearchCV,
    cross_val_score
)

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from imblearn.over_sampling import SMOTE


url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/loan_prediction.csv"

df = pd.read_csv(url)

print("Original Shape:", df.shape)


df.drop("Loan_ID", axis=1, inplace=True)


for col in df.columns:

    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])

    else:
        df[col] = df[col].fillna(df[col].median())
df["Dependents"] = (
    df["Dependents"]
    .replace("3+", "3")
    .astype(int)
)

df["TotalIncome"] = (
    df["ApplicantIncome"] +
    df["CoapplicantIncome"]
)

df["Income_Loan_Ratio"] = (
    df["TotalIncome"] /
    (df["LoanAmount"] + 1)
)

df["EMI"] = (
    df["LoanAmount"] /
    (df["Loan_Amount_Term"] + 1)
)

df["LogIncome"] = np.log1p(df["TotalIncome"])

df["Loan_Status"] = (
    df["Loan_Status"]
    .map({"Y": 1, "N": 0})
)

X = pd.get_dummies(
    df.drop("Loan_Status", axis=1),
    drop_first=True
)

y = df["Loan_Status"]

print("Features Shape:", X.shape)


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
smote = SMOTE(random_state=42)

X_train_smote, y_train_smote = smote.fit_resample(
    X_train,
    y_train
)

print("After SMOTE:", X_train_smote.shape)


param_dist = {

    "n_estimators": [200,300,500,700,1000],

    "max_depth": [5,10,15,20,25,None],

    "min_samples_split": [2,5,10],

    "min_samples_leaf": [1,2,4],

    "max_features": ["sqrt","log2"],

    "bootstrap": [True, False]
}

rf = RandomForestClassifier(
    random_state=42
)

search = RandomizedSearchCV(
    estimator=rf,
    param_distributions=param_dist,
    n_iter=50,
    cv=5,
    scoring="accuracy",
    n_jobs=-1,
    random_state=42
)

search.fit(
    X_train_smote,
    y_train_smote
)

best_rf = search.best_estimator_

print("\nBest Parameters:")
print(search.best_params_)

cv_scores = cross_val_score(
    best_rf,
    X_train_smote,
    y_train_smote,
    cv=5,
    scoring="accuracy"
)

print("\nCross Validation Accuracy:")
print(cv_scores)
print("Average CV Accuracy:",
      round(cv_scores.mean(), 4))

y_pred = best_rf.predict(X_test)

print("\nTest Accuracy:")
print(round(
    accuracy_score(y_test, y_pred),
    4
))

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred
))

print("\nConfusion Matrix:")
print(confusion_matrix(
    y_test,
    y_pred
))


importance = pd.Series(
    best_rf.feature_importances_,
    index=X.columns
)

print("\nTop 15 Important Features:")
print(
    importance
    .sort_values(ascending=False)
    .head(15)
)
prob = best_rf.predict_proba(X_test)

print("\nSample Approval Probabilities:")
print(prob[:10])