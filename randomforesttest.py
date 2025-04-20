import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# STEP 1: Load your data
data = pd.read_csv("heart.csv")
print(data)
print(data["target"].unique())

# Replace '?' with NaN
data.replace('?', np.nan, inplace=True)

# Convert all columns to numeric
data = data.apply(pd.to_numeric, errors='coerce')

# Fill missing values with column means
data = data.fillna(data.mean())

# STEP 2: Split features and labels
X = data.drop("target", axis=1)
y = data["target"]

# STEP 3: Scale the features (optional for RF, but ok to keep)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# STEP 4: Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# STEP 5: Build and train the Random Forest
train_acc = []
test_acc = []
tree_range = range(1, 101)

for n in tree_range:
    model = RandomForestClassifier(n_estimators=n, random_state=42)
    model.fit(X_train, y_train)

    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)

    train_acc.append(train_score)
    test_acc.append(test_score)

# STEP 6: Predict and evaluate
y_pred = model.predict(X_test)

print("\nTest Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

import matplotlib.pyplot as plt

plt.plot(tree_range, train_acc, label="Training Accuracy")
plt.plot(tree_range, test_acc, label="Test Accuracy")
plt.title("Random Forest Accuracy vs Number of Trees")
plt.xlabel("Number of Trees (n_estimators)")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
