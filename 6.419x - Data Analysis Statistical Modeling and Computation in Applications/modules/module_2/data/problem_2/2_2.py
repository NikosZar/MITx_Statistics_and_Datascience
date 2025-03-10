import numpy as np
from sklearn.linear_model import LogisticRegressionCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import os

# Load the data from the reduced dataset to avoid memory issues
x = np.load('/Users/nikos/Documents/GitHub/MITx_Statistics_and_Datascience/6.419x - Data Analysis Statistical Modeling and Computation in Applications/modules/module_2/data/p2_unsupervised_reduced/X.npy')

# Create log2 transformed data
x_log2 = np.log2(x + 1)

# Load the cluster labels we created
cluster_labels = np.load('images/subtype_labels.npy')

print("Shape of X:", x_log2.shape)
print("Number of clusters:", len(np.unique(cluster_labels)))

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(
    x_log2, cluster_labels, test_size=0.2, random_state=42, stratify=cluster_labels
)

print(f"Training set size: {X_train.shape[0]}")
print(f"Validation set size: {X_val.shape[0]}")

# Try different regularization types
for penalty in ['l1', 'l2']:  # Removed elasticnet as it's causing convergence issues
    print(f"\nTraining with {penalty} regularization:")

    # Use LogisticRegressionCV to automatically find the best C value
    # We'll use 5-fold cross-validation
    lr = LogisticRegressionCV(
        cv=5,
        penalty=penalty,
        solver='liblinear',  # liblinear is faster for l1 and l2
        max_iter=2000,  # Increased from 1000 to 2000
        random_state=42,
        n_jobs=-1  # use all available cores
    )

    # Fit the model
    lr.fit(X_train, y_train)

    # Print the best C value
    print(f"Best C: {lr.C_[0]}")

    # Evaluate on validation set
    y_val_pred = lr.predict(X_val)
    val_accuracy = accuracy_score(y_val, y_val_pred)
    print(f"Validation accuracy: {val_accuracy:.4f}")

    # If this is the best model so far, save it
    if not 'best_val_accuracy' in locals() or val_accuracy > best_val_accuracy:
        best_val_accuracy = val_accuracy
        best_model = lr
        best_penalty = penalty

# Print the best model details
print("\nBest model:")
print(f"Regularization: {best_penalty}")
print(f"C value: {best_model.C_[0]}")
print(f"Validation accuracy: {best_val_accuracy:.4f}")

# Get detailed classification report for the best model
y_val_pred = best_model.predict(X_val)
print("\nClassification Report:")
print(classification_report(y_val, y_val_pred))

# Plot the confusion matrix
from sklearn.metrics import confusion_matrix
import seaborn as sns

plt.figure(figsize=(10, 8))
cm = confusion_matrix(y_val, y_val_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.savefig('images/confusion_matrix.png', dpi=300)
plt.show()

# Save the best model for later use
import joblib
os.makedirs('models', exist_ok=True)
joblib.dump(best_model, 'models/logistic_regression_model.pkl')

# Extract and save the coefficients for feature selection
coef = best_model.coef_
np.save('models/logistic_regression_coef.npy', coef)

print("\nModel and coefficients saved.")