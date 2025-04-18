import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# STEP 1: Load your data
data = pd.read_csv("heart.csv")
print(data)
print(data["target"].unique())
# data.columns = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
#                 "thalach", "exang", "oldpeak", "slope", "ca", "thal", "condition"]

# df = pd.read_csv("heart+disease/processed.hungarian.data")  # header=None if it has no column names
#
# # OPTIONAL: assign the same columns if df2 has no headers
# df.columns = data.columns
#
# # Concatenate vertically (i.e., append)
# data = pd.concat([data, df], ignore_index=True)
#
# df = pd.read_csv("heart+disease/processed.switzerland.data")  # header=None if it has no column names
#
# # OPTIONAL: assign the same columns if df2 has no headers
# df.columns = data.columns
#
# # Concatenate vertically (i.e., append)
# data = pd.concat([data, df], ignore_index=True)
#
# df = pd.read_csv("heart+disease/processed.va.data")  # header=None if it has no column names
#
# # OPTIONAL: assign the same columns if df2 has no headers
# df.columns = data.columns
#
# # Concatenate vertically (i.e., append)
# data = pd.concat([data, df], ignore_index=True)


# Replace '?' with NaN
data.replace('?', np.nan, inplace=True)

# Convert all columns to numeric
data = data.apply(pd.to_numeric, errors='coerce')

# Fill missing values with column means
data = data.fillna(data.mean())

# STEP 2: Split features and labels
X = data.drop("target", axis=1)
y = data["target"]  # Multiclass (0–4)

# STEP 3: Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# STEP 4: Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# STEP 5: Build the neural network
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')  # sigmoid for binary classification
])

# STEP 6: Compile the model
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

# STEP 7: Train the model
model.fit(X_train, y_train, epochs=50, batch_size=16, validation_split=0.2)

# STEP 8: Evaluate on test set
loss, accuracy = model.evaluate(X_test, y_test)
print(f"\nTest Accuracy: {accuracy:.4f}")
