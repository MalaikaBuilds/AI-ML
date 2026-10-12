import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
df = pd.read_csv('wine.csv')
X = df.drop(columns=['wine_id', 'target', 'wine_class'])
Y = df['target'] 

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42, stratify=Y
)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)
for kernel in ['linear', 'rbf']:
    model = SVC(kernel=kernel, C=1.0)
    model.fit(X_train_s, Y_train)
    acc = accuracy_score(Y_test, model.predict(X_test_s))
    print(f'SVM ({kernel}) accuracy: {acc:.3f}')
raw = KNeighborsClassifier(n_neighbors=5).fit(X_train, Y_train)
print('KNN without scaling:', round(accuracy_score(Y_test, raw.predict(X_test)), 3))

for k in [1, 3, 5, 7, 9, 15, 25]:
    knn = KNeighborsClassifier(n_neighbors=k).fit(X_train_s, Y_train)
    acc = accuracy_score(Y_test, knn.predict(X_test_s))
    print(f'K={k:>2}: accuracy = {acc:.3f}')