import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

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

# STEP 3: Scale the features (Logistic Regression is sensitive to scaling)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# STEP 4: Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# STEP 5: Build and train the Logistic Regression model
log_model = LogisticRegression(max_iter=1000)  # increased iterations for convergence
log_model.fit(X_train, y_train)

# STEP 6: Predict and evaluate
y_pred = log_model.predict(X_test)

print("\nTest Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Reduce to 2D for visualization
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X_scaled)

# Re-train model on reduced features
log_model = LogisticRegression(max_iter=1)
log_model.fit(X_reduced, y)

# Meshgrid for decision surface
x_min, x_max = X_reduced[:, 0].min() - 1, X_reduced[:, 0].max() + 1
y_min, y_max = X_reduced[:, 1].min() - 1, X_reduced[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300),
                     np.linspace(y_min, y_max, 300))

Z = log_model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot
plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
scatter = plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, cmap='coolwarm', edgecolors='k')
plt.title('Logistic Regression Decision Boundary (PCA-reduced)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(scatter, label='Target')
plt.grid(True)
plt.tight_layout()
plt.show()






from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Initialize model
model = SGDClassifier(
    loss='log_loss',
    learning_rate='constant',
    eta0=0.01,
    random_state=42,
    max_iter=1,        # One step at a time
    tol=None,
    warm_start=False   # Don't restart, we’ll use partial_fit
)

# Prepare epoch tracking
n_epochs = 50
train_accs, test_accs = [], []

# Do one pass per epoch
for epoch in range(n_epochs):
    # Shuffle the training data
    indices = np.arange(len(X_train))
    np.random.shuffle(indices)
    X_epoch = X_train[indices]
    y_epoch = y_train.values[indices]

    # partial_fit (keeps learning across epochs)
    if epoch == 0:
        model.partial_fit(X_epoch, y_epoch, classes=np.unique(y))
    else:
        model.partial_fit(X_epoch, y_epoch)

    # Record accuracy
    train_accs.append(accuracy_score(y_train, model.predict(X_train)))
    test_accs.append(accuracy_score(y_test, model.predict(X_test)))

# Plot
plt.plot(train_accs, label="Training Accuracy")
plt.plot(test_accs, label="Test Accuracy")
plt.title("Logistic Regression Accuracy over Epochs (Fixed!)")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()