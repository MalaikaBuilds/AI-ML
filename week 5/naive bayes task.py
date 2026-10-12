import re
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
URL = ("https://raw.githubusercontent.com/Philipp-Sc/rust-bert-fraud-detection/"
       "embeddings-only/package/dataset/completeSpamAssassin.csv")
df = pd.read_csv(URL)[["Body", "Label"]]           # Label: 1 = spam, 0 = ham
df = df.dropna()
df = df[df["Body"].str.strip() != ""].drop_duplicates(subset="Body")
print("Emails after removing empty/duplicate rows:", len(df))
print(df["Label"].value_counts().rename({0: "ham", 1: "spam"}), "\n")
def clean(text):
    text = text.lower()
    text = re.sub(r"<[^>]+>", " ", text)                 # strip HTML tags
    text = re.sub(r"http\S+|www\.\S+", " url ", text)    # links -> 'url'
    text = re.sub(r"\S+@\S+", " emailaddr ", text)       # addresses -> 'emailaddr'
    text = re.sub(r"\d+", " num ", text)                 # numbers -> 'num'
    text = re.sub(r"[^a-z\s]", " ", text)                # remove punctuation/symbols
    return re.sub(r"\s+", " ", text).strip()
df["clean"] = df["Body"].apply(clean)
X_train, X_test, y_train, y_test = train_test_split(
    df["clean"], df["Label"], test_size=0.2, random_state=42, stratify=df["Label"]
)
def tfidf():
    return TfidfVectorizer(stop_words="english", ngram_range=(1, 2), min_df=2,
                           max_df=0.9, max_features=50000, sublinear_tf=True)
models = {
    "SVM (LinearSVC)":        Pipeline([("tfidf", tfidf()), ("clf", LinearSVC(C=1.0))]),
    "KNN (k=5, cosine)":      Pipeline([("tfidf", tfidf()),
                                        ("clf", KNeighborsClassifier(n_neighbors=5, metric="cosine",
                                                                     weights="distance", n_jobs=-1))]),
    "Naive Bayes (Multinom)": Pipeline([("tfidf", tfidf()), ("clf", MultinomialNB(alpha=0.1))]),
}
for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("=" * 55)
    print(f"{name}   ->   Accuracy: {accuracy_score(y_test, pred) * 100:.2f}%")
    print(classification_report(y_test, pred, target_names=["ham", "spam"], digits=4))
    print("Confusion matrix [rows=true, cols=pred]:\n", confusion_matrix(y_test, pred))
print("\n" + "=" * 55 + "\n5-fold cross-validation on the full dataset")
for name, model in models.items():
    scores = cross_val_score(model, df["clean"], df["Label"], cv=5, scoring="accuracy", n_jobs=-1)
    print(f"{name:24s} mean = {scores.mean() * 100:.2f}%  (+/- {scores.std() * 100:.2f})")
best = models["SVM (LinearSVC)"]
samples = [
    "Save up to 70% on life insurance!! FREE quote, click here http://cheap-quotes.biz now",
    "Hi Sam, thanks for the notes from the meeting. I'll send the updated schedule tomorrow.",
]
for s, p in zip(samples, best.predict([clean(s) for s in samples])):
    print(f"\n[{'SPAM' if p else 'HAM'}] {s[:70]}...")