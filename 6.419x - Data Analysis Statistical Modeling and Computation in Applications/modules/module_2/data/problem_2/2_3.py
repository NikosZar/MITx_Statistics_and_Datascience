import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import seaborn as sns
import os

# Load the coefficients from our trained model
coef = np.load('models/logistic_regression_coef.npy')

# Calculate feature importance (maximum absolute value across classes)
feature_importance = np.max(np.abs(coef), axis=0)

# Get indices of top 100 features
top_indices = np.argsort(feature_importance)[-100:]

# Load evaluation data
X_train = np.load('/Users/nikos/Documents/GitHub/MITx_Statistics_and_Datascience/6.419x - Data Analysis Statistical Modeling and Computation in Applications/modules/module_2/data/p2_evaluation/X_train.npy')
y_train = np.load('/Users/nikos/Documents/GitHub/MITx_Statistics_and_Datascience/6.419x - Data Analysis Statistical Modeling and Computation in Applications/modules/module_2/data/p2_evaluation/y_train.npy')
X_test = np.load('/Users/nikos/Documents/GitHub/MITx_Statistics_and_Datascience/6.419x - Data Analysis Statistical Modeling and Computation in Applications/modules/module_2/data/p2_evaluation/X_test.npy')
y_test = np.load('/Users/nikos/Documents/GitHub/MITx_Statistics_and_Datascience/6.419x - Data Analysis Statistical Modeling and Computation in Applications/modules/module_2/data/p2_evaluation/y_test.npy')

# Apply log2 transform
X_train_log = np.log2(X_train + 1)
X_test_log = np.log2(X_test + 1)

print("Evaluation data shapes:")
print(f"X_train: {X_train.shape}")
print(f"y_train: {y_train.shape}")
print(f"X_test: {X_test.shape}")
print(f"y_test: {y_test.shape}")

# Function to train and evaluate a model with selected features
def evaluate_features(X_train, y_train, X_test, y_test, feature_indices, name):
    # Select features
    X_train_selected = X_train[:, feature_indices]
    X_test_selected = X_test[:, feature_indices]

    # Train logistic regression model
    model = LogisticRegression(max_iter=2000, random_state=42)
    model.fit(X_train_selected, y_train)

    # Evaluate on test set
    y_pred = model.predict(X_test_selected)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"{name} features accuracy: {accuracy:.4f}")

    return accuracy

# 1. Evaluate top features from logistic regression
top_accuracy = evaluate_features(X_train_log, y_train, X_test_log, y_test, top_indices, "Top")

# 2. Evaluate random features
np.random.seed(42)
random_indices = np.random.choice(X_train.shape[1], size=100, replace=False)
random_accuracy = evaluate_features(X_train_log, y_train, X_test_log, y_test, random_indices, "Random")

# 3. Evaluate high-variance features
# Calculate variance of each feature
feature_variances = np.var(X_train_log, axis=0)
high_var_indices = np.argsort(feature_variances)[-100:]
high_var_accuracy = evaluate_features(X_train_log, y_train, X_test_log, y_test, high_var_indices, "High-variance")

# Compare variances of selected features
top_variances = feature_variances[top_indices]
high_var_variances = feature_variances[high_var_indices]

# Plot histogram of variances
plt.figure(figsize=(12, 6))
sns.histplot(top_variances, alpha=0.5, label='Top features by coefficient', color='blue', bins=30)
sns.histplot(high_var_variances, alpha=0.5, label='Top features by variance', color='red', bins=30)
plt.xlabel('Variance', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.title('Distribution of Feature Variances', fontsize=14)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('images/feature_variance_comparison.png', dpi=300)
plt.show()

# Calculate overlap between the two feature sets
overlap = len(set(top_indices) & set(high_var_indices))
print(f"\nOverlap between top coefficient features and high variance features: {overlap} genes")

# Print summary of results
print("\nSummary of Results:")
print(f"Top coefficient features accuracy: {top_accuracy:.4f}")
print(f"Random features accuracy: {random_accuracy:.4f}")
print(f"High-variance features accuracy: {high_var_accuracy:.4f}")

# Calculate improvement percentages
improvement_over_random = ((top_accuracy - random_accuracy) / random_accuracy) * 100
improvement_over_variance = ((top_accuracy - high_var_accuracy) / high_var_accuracy) * 100

print(f"\nImprovement over random selection: {improvement_over_random:.2f}%")
print(f"Improvement over high-variance selection: {improvement_over_variance:.2f}%")