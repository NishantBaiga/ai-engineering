
# Machine Learning

## What is machine learning?

Machine learning (ML) is a field of artificial intelligence in which computers learn patterns from data to make predictions or decisions. Rather than programming every rule by hand, we train a model on examples so it can apply what it has learned to new cases.

## Why do we use machine learning?

We use ML to find useful patterns in large amounts of data, automate tasks, and make predictions when explicit rules are difficult to write or maintain. Examples include spam detection, recommendations, fraud detection, image recognition, and demand forecasting.


## Types of machine learning

- **Supervised learning:** Learns from labeled examples. It is used for classification (such as spam or not spam) and regression (such as predicting a price).
	- **Classification:** Predicts a category or class, such as whether an email is spam.
		- **Binary classification:** Predicts one of two classes, such as spam or not spam.
		- **Multiclass classification:** Predicts one of three or more mutually exclusive classes, such as an animal species.
		- **Multilabel classification:** Assigns multiple labels to one example, such as tagging an image with several objects.
	- **Regression:** Predicts a continuous numerical value, such as a house price.
		- **Linear regression:** Models a linear relationship between input features and a numerical target.
		- **Polynomial regression:** Models nonlinear relationships by adding powers of input features.
		- **Regularized regression:** Uses penalties, such as L1 (Lasso) or L2 (Ridge), to limit model complexity.
- **Unsupervised learning:** Finds patterns in unlabeled data, such as grouping similar items into clusters.
	- **Clustering:** Groups similar data points, such as segmenting customers by behavior.
	- **Dimensionality reduction:** Reduces the number of features while preserving important information, such as with principal component analysis (PCA).
	- **Association rule learning:** Finds relationships between items, such as products frequently purchased together.
	- **Anomaly detection:** Identifies unusual data points that differ from typical patterns.
- **Semi-supervised learning:** Combines a small set of labeled examples with a larger set of unlabeled data.
- **Reinforcement learning:** Learns which actions to take by receiving rewards or penalties from its environment.


# Supervised learning

Supervised learning trains a model on examples that pair input data (features) with known answers (labels or targets). The model learns patterns linking the inputs to those answers, then uses what it learned to predict answers for new examples. For instance, it can learn from emails labeled “spam” or “not spam” to classify incoming emails.

Use supervised learning when you have enough representative, reliably labeled data and a clear outcome to predict. It is suited to classification tasks, which predict categories, and regression tasks, which predict numerical values. Examples include identifying fraudulent transactions, diagnosing a condition from test results, and estimating a home's price. If labeled data is unavailable or you want to find patterns without predicting a specific outcome, supervised learning may not be the right choice; consider unsupervised learning instead.

## Regression

Regression is a type of supervised learning that predicts a continuous numerical value instead of a category. In regression, the model learns the relationship between input features and a target value, then uses that pattern to estimate values for new examples.

For example, regression can predict:

- A house price based on its size, location, and age
- A company's sales for the next month
- The temperature for a specific day
- A student's score based on study time and past performance

Unlike classification, which gives labels such as "spam" or "not spam," regression produces numbers. The model tries to minimize the difference between its predictions and the actual values in the training data. Common regression techniques include linear regression, polynomial regression, and regularized regression.

Regression is useful when the output is a numeric value and the goal is to estimate a quantity rather than assign a class.

## Linear regression

Linear regression is a supervised learning method that predicts a continuous numerical target by modeling it as a linear combination of input features. “Linear” means the prediction is linear in the model's coefficients; features themselves may be transformed before they are used.

### The model

With one feature, the model is:

```text
ŷ = b₀ + b₁x
```

Here, `x` is the input feature, `ŷ` is the predicted target, `b₀` is the intercept (the predicted value when `x` is zero), and `b₁` is the slope (the predicted change in the target for a one-unit increase in `x`). For example, a model predicting a home's price from its size might estimate a baseline price with `b₀` and an additional amount per square foot with `b₁`.

With multiple features, the model becomes:

```text
ŷ = b₀ + b₁x₁ + b₂x₂ + ... + bₚxₚ
```

Each `xⱼ` is a feature and each `bⱼ` is its coefficient. A positive coefficient means the prediction increases as that feature increases, while a negative coefficient means it decreases, assuming the other features stay fixed. Coefficients describe associations in the fitted model; they do not by themselves prove cause and effect.

### How it learns

During training, the algorithm chooses coefficients that make predictions close to the known target values. A common approach is ordinary least squares, which minimizes the sum of squared residuals:

```text
residual = actual value - predicted value
```

Squaring makes positive and negative errors both contribute positively and gives larger errors more weight. Once fitted, the model applies the learned coefficients to the features of a new example to produce a prediction.

### Evaluating a model

Evaluate linear regression on data that was not used to fit it. Common metrics include:

- **Mean absolute error (MAE):** The average absolute prediction error, in the target's units.
- **Mean squared error (MSE):** The average squared error; it penalizes large errors more heavily.
- **Root mean squared error (RMSE):** The square root of MSE, expressed in the target's units.
- **R-squared (R²):** Measures how much variation in the target is explained by the model relative to a baseline. A higher value can indicate a better fit, but does not guarantee accurate predictions on new data.

### Assumptions and limitations

Linear regression is most appropriate when the relationship between the features and target is reasonably represented by the chosen linear form. For statistical inference, ordinary least squares also relies on assumptions about errors, including independence and constant variance; normally distributed errors are often assumed for certain confidence intervals and tests. Strong outliers can substantially affect the fitted coefficients, and highly correlated features can make individual coefficients unstable. A straight-line model may underfit a curved relationship, while adding too many features can overfit the training data. Check residuals and performance on held-out data, and consider feature transformations, regularization, or a different model when needed.

## Cost function and Gradient Descent

A **cost function** (also called a loss or objective function) measures how far a model's predictions are from the known target values. For linear regression, a common choice is the mean squared error (MSE):

```text
J(b) = (1 / n) Σᵢ (ŷᵢ - yᵢ)²
```

Here, `n` is the number of training examples, `yᵢ` is the actual target, and `ŷᵢ` is the prediction. Training aims to find coefficients `b` that minimize `J(b)`. Some definitions use half the MSE, which changes its scale but not the minimizing coefficients.

**Gradient descent** is an iterative way to reduce the cost. It computes the gradient, which points toward the direction of steepest increase, then updates each coefficient in the opposite direction:

```text
bⱼ ← bⱼ - α · ∂J/∂bⱼ
```

The learning rate `α` sets the update size. Repeat the update until the cost or coefficients change very little, or a chosen iteration limit is reached. If the learning rate is too large, the cost may increase or diverge; if it is too small, learning may be slow. Scaling features with very different ranges can help.

### Gradient descent convergence

For linear regression with squared-error cost, the objective is convex, so every local minimum is a global minimum. A standard convergence result states that for a differentiable convex objective with a Lipschitz-continuous gradient, gradient descent using a sufficiently small fixed learning rate (for example, at most `1/L`, where `L` is the gradient's Lipschitz constant) converges in objective value to the global minimum. The guarantee depends on these conditions and the step size; arbitrary update rules are not guaranteed to converge. If several coefficient vectors achieve the minimum, the cost can converge even when the coefficients are not unique. In practice, monitor the cost and evaluate the model on held-out data.

