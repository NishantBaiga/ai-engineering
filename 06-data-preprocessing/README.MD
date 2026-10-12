# Steps

1. **Collect and inspect data** — understand its structure, types, and quality.
2. **Clean the data** — fix inconsistencies, remove duplicates, and correct invalid values.
3. **Handle missing values** — remove incomplete records or impute missing values appropriately.
4. **Handle outliers** — investigate unusual values and decide whether to retain, transform, cap, or remove them.
5. **Transform data** — encode categorical features and scale numeric features when needed.
6. **Select or create features** — keep relevant variables and derive useful features.
7. **Split the data** — create training, validation, and test sets.
8. **Validate the processed data** — check that values and formats are suitable and that no information leaks across splits.

Fit preprocessing transformations on the training set only, then apply them to the validation and test sets.



# Introduction

## What is data preprocessing?

Data preprocessing is the process of preparing raw data for analysis or machine learning. It includes inspecting and cleaning the data, handling missing values and outliers, transforming features, and splitting the data into datasets for training and evaluation.

## What is data cleaning?

Data cleaning is a step within data preprocessing that detects and addresses inaccurate, inconsistent, duplicated, or incomplete data. Common tasks include correcting invalid values, standardizing formats, removing duplicate records, and handling missing values.

## Raw data vs. clean data

| Raw data | Clean data |
| --- | --- |
| Data in its original form, as collected from its source. | Data reviewed and prepared for analysis or machine learning. |
| May contain missing values, duplicates, errors, and inconsistent formats. | Problems are addressed and formats are standardized where appropriate. |
| May not be reliable or ready for direct use. | Is more consistent and suitable for analysis, while preserving the meaning of the original data. |

Keep an unchanged copy of the raw data so cleaning decisions can be reviewed and the process can be repeated.

## Features, labels, and observations

- **Features** are the input information a model uses to make a prediction. In a table, features are usually columns such as age, temperature, or account balance.
- **A label** is the value a model is trained to predict, also called the target. For example, in a dataset about house sales, the sale price can be the label. Labels are used in supervised learning.
- **An observation** is one individual example or record in a dataset. In a table, an observation is usually a row containing feature values and, when available, its label.

For example, each house sale is an observation; its size and location are features; and its sale price is the label.

## Numerical and categorical data

- **Numerical data** represents quantities as numbers, such as age, temperature, or account balance. It can be discrete (counts) or continuous (measurements). Many models can use numerical features directly, though scaling or other preprocessing may be useful.
- **Categorical data** represents groups or labels, such as color, country, or product type. Categories can be nominal (no natural order) or ordinal (a meaningful order). Many models require categories to be encoded, for example with one-hot encoding. For nominal categories, arbitrary numeric codes can misleadingly imply an order or distance.

Numerical and categorical are common feature types, especially in tabular data, but they are not the only data used in machine learning. Text, images, audio, and time series can also be used. They need representations suited to their structure: text may be tokenized, images represented as pixel arrays, audio as waveforms or spectrograms, and time series as ordered sequences. Some models handle particular data types directly; others require preprocessing to convert them into suitable inputs. The appropriate representation depends on the data, model, and task.

## What is a data preprocessing pipeline?

A data preprocessing pipeline is a repeatable sequence of steps that converts raw data into inputs suitable for analysis or a machine-learning model. A typical pipeline:

Think of it as a recipe for preparing data: it applies the same ordered operations every time, so training data and future data are handled consistently.

1. **Inspects and cleans** the data, addressing errors, duplicates, and inconsistent formats.
2. **Separates features and label** and splits the data into training, validation, and test sets. Choose a split that respects time or groups when relevant.
3. **Fits transformations using the training set**, such as imputing missing values, encoding categories, and scaling numeric features.
4. **Applies those fitted transformations** to each split and checks that the results are valid. Do not fit transformations on validation or test data; doing so can leak information and produce misleading evaluation results.
5. **Feeds the processed data to the model** and retains the fitted steps so the same processing can be applied consistently to future data.

The exact steps depend on the dataset and model. A defined, reusable pipeline makes processing reproducible and helps prevent data leakage.

For example, when predicting house prices, a pipeline can fill missing values, encode property types, and scale numeric features. It learns the values needed for these transformations from the training set, then reuses them for validation, test, and future records. This avoids allowing evaluation data to influence how the model is prepared and makes predictions on new records comparable to training inputs.

## Common problems in real-world datasets

Real-world datasets often contain issues that make model training harder or less reliable. Some common problems include:

- **Missing values** — records may be incomplete because of survey non-response, broken sensors, or skipped fields.
- **Duplicate records** — repeated entries can distort counts, summaries, and model learning.
- **Inconsistent formatting** — dates, text labels, units, and categories may vary across sources or time periods.
- **Outliers** — unusually large or small values may reflect real events or measurement errors and can strongly affect model performance.
- **Incorrect or noisy values** — typos, invalid codes, and bad measurements can introduce false patterns.
- **Class imbalance** — some target classes may be much rarer than others, which can bias a model toward the majority class.
- **Data leakage** — information from the future or validation/test data can accidentally influence preprocessing or training.
- **Schema drift** — the meaning or structure of a feature may change over time, such as a category being renamed or a field becoming optional.
- **Irrelevant or redundant features** — unrelated variables can add noise and increase complexity without improving prediction quality.
- **Small or uneven sample sizes** — limited data can make it difficult to estimate patterns reliably or compare splits fairly.

These problems are why preprocessing is essential: it helps turn messy raw data into a more reliable form for analysis and modeling.





# Data Cleaning

## Duplicate Values 

Duplicate records can inflate counts and cause a model to give repeated examples too much weight. Before removing them, check whether repeated rows are genuinely redundant or represent valid events.

### Find duplicates with pandas

Use `duplicated()` to identify repeated rows. By default, it marks later occurrences and compares all columns:

```python
import pandas as pd

df = pd.read_csv("data.csv")
duplicates = df[df.duplicated()]
print(f"Duplicate rows: {len(duplicates)}")
print(duplicates)
```

To check duplicates based on specific columns, pass them to `subset`:

```python
duplicates = df[df.duplicated(subset=["email"], keep=False)]
```

`keep=False` marks every row in each duplicate group. Choose columns that identify a record; matching only one field, such as a name, may incorrectly treat distinct records as duplicates.

### Remove duplicates

After reviewing the matches, use `drop_duplicates()` to keep the first occurrence:

```python
df = df.drop_duplicates()
```

To deduplicate by selected columns, while keeping the most recent record according to a timestamp:

```python
df = (df.sort_values("updated_at")
	.drop_duplicates(subset=["email"], keep="last"))
```

Check the result and retain the original raw data so the cleaning step can be reviewed or repeated:

```python
print(f"Rows after deduplication: {len(df)}")
```

## Correct invalid and inconsistent data

Inspect column types and example values before making changes. Define valid values and formats using the source documentation and domain knowledge. A value that looks unusual is not necessarily wrong, so investigate it before correcting or removing it.

### Wrong data types

Convert values to the type they represent. Parse dates explicitly and convert numeric text after handling known formatting. With `errors="coerce"`, unparseable values become missing, so inspect them rather than silently accepting the conversion:

```python
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["amount"] = pd.to_numeric(
	df["amount"].astype("string").str.replace(",", "", regex=False),
	errors="coerce",
)

print(df[["date", "amount"]].isna().sum())
```

Review failed conversions and correct them from a trusted source, mark them missing, or exclude affected records as appropriate. Keep identifiers as strings when numeric operations are not meaningful or leading zeros matter.

### Invalid values and inconsistent formats

Check values against documented rules, allowed categories, expected units, and formats. Standardize only values known to mean the same thing. For example, trim whitespace and map verified spelling variants to a canonical category:

```python
df["city"] = df["city"].astype("string").str.strip()
df["city"] = df["city"].replace({
	"New Yrok": "New York",
	"new york": "New York",
})

print(df["city"].value_counts(dropna=False))
```

For dates, units, and codes, confirm the meaning of each source format before converting it. Do not merge categories based only on similar spelling; verify that they refer to the same value.

### Impossible or implausible values

Use domain rules to flag impossible values and investigate them. For example, if age is expected to be between 0 and 120:

```python
invalid_age = df["age"].notna() & ~df["age"].between(0, 120)
print(df.loc[invalid_age, "age"])
```

Correct a value only when its intended value is known. Otherwise, mark it missing, retain it with an explanatory flag, or remove the record based on the task; document the decision. Recheck data types, allowed values, ranges, and missing-value counts after cleaning.




# Handling Missing Values

Missing values are entries in a dataset where the value is absent, unknown, not recorded, or not applicable. In pandas, they commonly appear as `NaN`, `None`, or `null`. They often happen because of incomplete surveys, broken sensors, skipped form fields, merged data sources, or records that were never fully captured.

Missing values are important because many analysis and machine learning methods cannot work with them directly. If they are ignored, they can cause errors, bias the results, or reduce the amount of usable information in the dataset. At the same time, a missing value is not always a mistake; sometimes it reflects a real condition, such as a field that does not apply to a record.

### Why this matters

- Some models do not accept missing values.
- Missing data can distort summaries and statistics.
- Dropping too much data may remove useful patterns.
- Filling in values incorrectly can create false relationships.

### Common ways to handle missing values

- Remove rows or columns with too many missing entries.
- Fill missing values with a statistic such as the mean, median, or mode.
- Use domain knowledge to replace values with a realistic default.
- For time-based data, use forward or backward fill when appropriate.
- Keep a flag that records that a value was missing when missingness itself is informative.

### Example with pandas

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df.isna().sum())

# Fill numeric missing values with the median
for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].median())

# Drop rows where a required field is missing
# (example: a customer email or target variable)
df = df.dropna(subset=["email"])

print(df.isna().sum())
```

The best method depends on the dataset, the feature type, and the task. A good preprocessing decision is based on understanding why the data is missing and choosing a strategy that preserves data quality without introducing bias.


### What are missing values?

Missing values are entries where a data point is absent, unknown, not recorded, or not applicable. In pandas, they often appear as `NaN`, `None`, or `null`. They can happen because of skipped survey answers, failed sensors, merged sources, or fields that simply do not apply to a record.

Missing values matter because many analysis and machine learning methods cannot work with them directly. If they are ignored, they can cause errors, distort summaries, or reduce the usable information in the dataset. The right preprocessing step depends on why the value is missing and on the task: rows may be removed, values may be filled with a statistic or default, or the missingness may be tracked as useful information in itself. 




## Detect missing values

Use pandas `isna()` (or its alias, `isnull()`) to identify missing entries. Count them by column, check whether any are present, or select rows containing missing values:

```python
missing_by_column = df.isna().sum()
print(missing_by_column)

print("Any missing values:", df.isna().any().any())
rows_with_missing_values = df[df.isna().any(axis=1)]
print(rows_with_missing_values)
```

Calculate the percentage of missing values in each column with `df.isna().mean().mul(100)`. Pandas recognizes values such as `NaN`, `None`, and `NaT` as missing. Empty strings and placeholders like `"N/A"` or `"unknown"` are not automatically recognized; standardize them first if they represent absent data.


## Removal Rows and Columns  
Remove rows that contain at least one missing value with `dropna()`. Use `subset` to limit the check to required columns:

```python
# Drop every row with one or more missing values
df_rows_removed = df.dropna()

# Drop rows only when the required email value is missing
df_required_removed = df.dropna(subset=["email"])
```

Remove columns that contain missing values with `axis=1`:

```python
# Drop every column with one or more missing values
df_columns_removed = df.dropna(axis=1)
```

By default, `dropna()` returns a new DataFrame and keeps rows or columns only when they meet the selected criteria. Removal can discard useful data, so use it when the amount of missing data and the task make dropping records or features appropriate.

## Numerical imputation

For numeric columns, fill missing values using a central tendency such as the mean or median, or a fixed value when that makes sense for the data:

```python
# Fill with the column mean
df["age"] = df["age"].fillna(df["age"].mean())

# Fill with the column median when the distribution is skewed
df["income"] = df["income"].fillna(df["income"].median())

# Fill with a business-specific default
df["score"] = df["score"].fillna(0)

# Forward fill from the previous row, or backward fill from the next row
df["status"] = df["status"].ffill()
df["status"] = df["status"].bfill()

# Fill a categorical column with a constant value
df["category"] = df["category"].fillna("Unknown")
```

Use the mean for roughly symmetric data, the median for skewed distributions or outlier-heavy columns, and a constant only when zero or another sentinel is meaningful. In machine learning workflows, fit imputation parameters on the training set and apply them to validation/test data to avoid data leakage.

Forward fill (`ffill()`) uses the last observed value; backward fill (`bfill()`) uses the next observed value. These methods are useful for ordered data when adjacent values are meaningful, so sort rows appropriately first. A constant can be numeric or categorical and should be chosen to make sense for the column.

For a scikit-learn approach, `SimpleImputer` handles this cleanly:

```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="median")
df[["age", "income"]] = imputer.fit_transform(df[["age", "income"]])
```

## Categorical imputation

For categorical features, missing values are usually filled with the most common category, a custom label like `"Unknown"`, or a domain-specific value. This keeps the column valid for grouping, encoding, and model training without losing rows.

```python
# Fill with the most frequent category
city_mode = df["city"].mode()[0]
df["city"] = df["city"].fillna(city_mode)

# Fill with a custom category for missing values
df["segment"] = df["segment"].fillna("Unknown")

# Fill a categorical column with the previous valid value
# Use this carefully and only for ordered data
df["status"] = df["status"].ffill()
```

When categories are unordered, `mode` or a sentinel such as `"Unknown"` is usually the safest choice. If the missingness itself is meaningful, you can also create a separate indicator column before imputation so the model can learn this pattern.

For machine learning pipelines, `SimpleImputer` can handle categorical columns with `strategy="most_frequent"` or `strategy="constant"`:

```python
from sklearn.impute import SimpleImputer

cat_imputer = SimpleImputer(strategy="most_frequent")
df[["city", "segment"]] = cat_imputer.fit_transform(df[["city", "segment"]])

constant_imputer = SimpleImputer(strategy="constant", fill_value="Unknown")
df[["segment"]] = constant_imputer.fit_transform(df[["segment"]])
```

In practice, do not fit the imputer on the full dataset before splitting into train/validation/test. Fit it only on the training data and then apply it to the holdout sets to avoid data leakage.





## Outlier Detection and Treatment

An **outlier** is an observation that is unusually far from the rest of the data. It may result from a data-entry or measurement error, or it may be a valid but rare event. Investigate its cause before removing or changing it.

Outliers can:

- Pull the mean and standard deviation away from typical values, distorting summaries and scaling.
- Skew visualizations and statistical analyses.
- Have a disproportionate effect on models sensitive to extreme values, such as linear regression and k-nearest neighbors.
- Represent important signals, such as fraud or equipment failure, so removing them blindly can discard useful information.

Their impact depends on the data and method. Use domain context to decide whether to correct, cap, transform, or retain an outlier.


## Ways To Detect Outlier 
Outliers can be detected using statistical rules and visualizations. These methods flag unusual observations; they do not prove that a value is an error. Investigate flagged values in context.

### Statistical Methods

- **Interquartile range (IQR):** Calculate `IQR = Q3 - Q1`. Values below `Q1 - 1.5 * IQR` or above `Q3 + 1.5 * IQR` are commonly flagged. This robust rule is a heuristic, not a universal cutoff.
- **Z-score:** Calculate `z = (x - mean) / standard deviation`. A common rule flags `|z| > 3`. It is most appropriate for roughly normal data and can be distorted by extreme values.
- **Modified Z-score:** Use the median and median absolute deviation (MAD): `0.6745 * (x - median) / MAD`. An absolute score above `3.5` is a common flag and is more robust than the standard z-score.
- **Percentile thresholds:** Flag values below or above selected percentiles, such as the 1st and 99th. Choose cutoffs based on the data and domain.
- **Multivariate methods:** For unusual combinations of features, consider Mahalanobis distance (when its assumptions are appropriate) or algorithms such as isolation forest. These can detect patterns missed by checking one feature at a time.

### Graphical Methods

- **Box plot:** Shows the median, quartiles, and values beyond the whiskers (often based on IQR fences); useful for comparing groups.
- **Histogram or density plot:** Helps reveal long tails, isolated peaks, and possible anomalies in a feature's distribution.
- **Scatter plot or pair plot:** Shows isolated points and unusual relationships between features that univariate checks may miss.
- **Q-Q plot:** Compares observed quantiles with a reference distribution, helping reveal tail departures and non-normality.

No method is best for every dataset. Combine an appropriate statistical check with visual inspection, and distinguish valid rare observations from errors before deciding whether to correct, cap, transform, or retain them.

## Ways to Remove or Treat Outliers

Remove an observation only when there is a defensible reason, such as a confirmed data-entry error or a value outside the population being studied. Otherwise, consider treatments that preserve the record:

- **Correct invalid values:** Verify the source and fix confirmed recording or unit-conversion errors; do not guess at replacements.
- **Filter rows:** Exclude records that violate documented domain limits or a chosen statistical rule, such as IQR or percentile thresholds. Review how many rows are removed and whether removal disproportionately affects a group.
- **Trim extremes:** Drop values below or above selected lower and upper bounds. Choose bounds based on domain knowledge or training data and document the loss of observations.
- **Cap (winsorize):** Replace values outside selected thresholds with the thresholds, limiting their influence without dropping rows.
- **Transform the feature:** For suitable skewed data, a log or other monotonic transformation can reduce the influence of a long tail while retaining observations.

Learn data-dependent thresholds or transformations from the training set only, then apply them unchanged to validation and test sets to avoid data leakage. Compare model results with and without treatment, and retain valid rare events when they contain useful signal.



# Categorical Data Encoding

Categorical encoding is the process of converting categorical values—such as colors, product types, or ratings—into numeric representations that machine-learning algorithms can use.

## Types of Categorical Data

Categorical variables usually fall into a few main groups:

- **Nominal data:** Categories with no meaningful order, such as colors, cities, or product types.
- **Ordinal data:** Categories with a meaningful rank or order, such as `low`, `medium`, and `high`, or satisfaction levels.
- **Binary data:** A special case of nominal data with exactly two categories, such as `yes/no`, `true/false`, or `pass/fail`.

Understanding the type of categorical data helps choose an appropriate encoding method. Nominal data usually needs one-hot or similar encoding, while ordinal data can sometimes use ordered numeric values when the order is meaningful.

We use it because many models and preprocessing operations require numerical input. The encoding method should match the data:

- **One-hot encoding:** Creates a separate binary (0/1) column for each category. For example, a `color` feature with `red`, `blue`, and `green` becomes three columns; a row with `red` is represented as `1, 0, 0`. This does not imply an order, so it is suitable for nominal data, but it can create many columns for high-cardinality features.
- **Ordinal encoding:** Replaces categories with numbers that reflect a meaningful order. For example, `low = 1`, `medium = 2`, and `high = 3`. Use it for ordinal data; the mapping should preserve the categories' actual order.
- **Label encoding:** Assigns an integer ID to each category, for example, `red = 0`, `blue = 1`, and `green = 2`. These IDs are arbitrary and do not express rank. For input features, a model may mistakenly interpret them as ordered or equally spaced, so one-hot encoding is often safer for nominal data unless the model handles categories natively. Label encoding is commonly used for classification target labels.

Fit encoders on the training data, then apply the same mapping to validation and test data. This prevents data leakage and ensures categories are represented consistently.

## Practical Example: Encoding with scikit-learn

Suppose a dataset contains a nominal `color` feature, an ordinal `size` feature, and a binary target. Encode `color` with one-hot encoding so its values do not imply an order. Encode `size` with an explicit order so the numeric values preserve its meaning. Keep the encoders inside a pipeline: they are fitted only on the training split and reused unchanged for test or future data.

```python
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

df = pd.DataFrame(
	{
		"color": ["red", "blue", "green", "red", "blue", "green",
				  "red", "blue", "green", "red", "blue", "green"],
		"size": ["small", "medium", "large", "medium", "small", "large",
				 "large", "medium", "small", "small", "large", "medium"],
		"purchased": [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
	}
)

X = df[["color", "size"]]
y = df["purchased"]
X_train, X_test, y_train, y_test = train_test_split(
	X, y, test_size=0.25, random_state=42
)

preprocessor = ColumnTransformer(
	transformers=[
		# Unknown colors at prediction time produce all-zero color columns.
		("color", OneHotEncoder(handle_unknown="ignore"), ["color"]),
		# Specify the true order; do not rely on alphabetical ordering.
		(
			"size",
			OrdinalEncoder(
				categories=[["small", "medium", "large"]],
				handle_unknown="use_encoded_value",
				unknown_value=-1,
			),
			["size"],
		),
	]
)

model = Pipeline(
	steps=[
		("encode", preprocessor),
		("classifier", LogisticRegression()),
	]
)
model.fit(X_train, y_train)

print("Test accuracy:", model.score(X_test, y_test))
new_items = pd.DataFrame({"color": ["purple"], "size": ["medium"]})
print("Prediction:", model.predict(new_items)[0])
```

`OneHotEncoder` learns the color categories from `X_train` and creates a separate indicator column for each. An unseen color such as `purple` is handled by `handle_unknown="ignore"` rather than causing an error. `OrdinalEncoder` maps `small`, `medium`, and `large` to `0`, `1`, and `2`; the explicit `categories` list defines the order, and an unseen size maps to `-1`. The `Pipeline` ensures that `fit` learns these mappings from training data only and that the same mappings are applied during scoring and prediction. For an ordinal feature without a meaningful order, use one-hot encoding instead.

# Data Transformation/Feature Transformation

Data transformation changes the scale, representation, or distribution of a feature so it is more suitable for analysis or modeling. Examples include scaling values with standardization or min-max scaling, applying `log` or square-root transforms, and encoding categories.

## Why transform a distribution?

Real-world features can be highly skewed, contain extreme values, or have very different scales. A suitable transformation can:

- Reduce skew and make relationships easier for a model to capture (for example, apply `log1p` to positive, right-skewed values).
- Stabilize variance when variability grows with the feature's magnitude.
- Limit the influence of extreme values and improve numerical behavior.
- Put features on comparable scales, which can help distance-based models and optimization methods.

Not every model requires normally distributed features. Linear-model assumptions generally concern the errors, not that every input feature must be normal; tree-based models often need little feature transformation. Choose transformations based on the feature's meaning and the model, and fit any learned transformation on training data only (for example, with a scikit-learn `Pipeline`) to avoid data leakage. A transform can also make results harder to interpret, so preserve or document the original scale when needed.

## Common methods to transform features

- **Standardization:** `StandardScaler` subtracts the training mean and divides by the training standard deviation. It centers features around zero but does not bound their range; it is often useful for linear models and distance-based methods.
- **Min-max scaling:** `MinMaxScaler` maps values to a chosen range, usually `[0, 1]`. It is sensitive to outliers, which can compress most values into a narrow range.
- **Robust scaling:** `RobustScaler` uses the median and interquartile range, making it less sensitive to outliers than standardization or min-max scaling.
- **Log and root transforms:** `np.log1p(x)` (for nonnegative values) or a square-root transform can reduce right skew. These change the scale and require valid input domains.
- **Power transforms:** `PowerTransformer` (Yeo-Johnson or Box-Cox) estimates a transformation to make data less skewed; Box-Cox requires strictly positive values.
- **Quantile transforms:** `QuantileTransformer` maps values to a uniform or normal-like distribution. It can reduce the effect of outliers, but may distort distances between values.
- **Clipping:** cap values at selected lower and upper bounds to limit extreme values. Choose bounds using training data and consider whether the extremes are meaningful.

Use the method that fits the feature and model; scaling is not automatically beneficial for every estimator. Put learned transformations in a scikit-learn `Pipeline` so they are fitted on training data and reused unchanged for validation, test, and new data.

# Feature Scaling

Feature scaling transforms numeric features so they are on comparable scales. For example, a dataset may contain age values in the tens and income values in the thousands. Scaling prevents differences in units or magnitude from disproportionately affecting a model's calculations.

## Why use feature scaling?

- It puts features on comparable scales so variables with larger units do not dominate distance-based methods such as k-nearest neighbors and k-means.
- It improves optimization for gradient-based models such as logistic regression, linear regression, and neural networks by making updates more stable and consistent.
- It helps regularization treat features more fairly, because coefficients are not penalized differently just because the raw feature values are larger in magnitude.
- It can reduce numerical instability and speed up convergence when features have very different ranges or units.
- It is usually unnecessary for tree-based models because their splits depend on thresholds, not feature magnitude.

Common techniques include:

- **Standardization:** subtract the training mean and divide by the training standard deviation. The result is centered around zero but is not limited to a fixed range.
- **Min-max scaling:** map values to a chosen range, commonly `[0, 1]`. It is sensitive to outliers.
- **Robust scaling:** use the median and interquartile range, making the result less sensitive to outliers.
- **Normalization:** scale each sample to unit norm, often useful for sparse data such as text features.

Fit the scaler on training data only, then use that same fitted scaler for validation, test, and new data. A scikit-learn `Pipeline` helps prevent data leakage by ensuring the scaler is fitted only during training. Scaling is not necessary for every estimator, and it does not guarantee that a feature becomes normally distributed.

# Feature Engineering

Feature engineering is the process of creating new input variables or transforming existing ones so that a machine learning model can learn patterns more effectively. It is often the difference between a model that performs only moderately well and one that captures the real structure of the problem. Feature engineering is not just about adding more columns; it is about selecting, combining, and representing data in a way that is meaningful for the learning algorithm.

## Why feature engineering matters

Real-world data is rarely perfectly ready for modeling. It may contain:

- Missing or inconsistent values
- Different units or scales across variables
- Categorical values that a model cannot interpret directly
- Temporal patterns that are buried in timestamps
- Redundant or noisy variables
- Nonlinear relationships that are not obvious in raw form

Feature engineering helps the model better understand these patterns by making the data more informative and more aligned with the task.

## Common types of feature engineering

### 1. Numerical transformations

These are used when raw numeric values are not in a useful form for the model.

- Log transformation for skewed distributions
- Square root or power transforms
- Binning continuous variables into intervals
- Creating ratios, differences, or proportions

Example:

- Instead of using only `house_price`, you may create `price_per_sqft = house_price / area_sqft`
- Instead of raw income, you may use `log(income + 1)` to reduce skewness

This often helps when the relationship is nonlinear or the variable has extreme values.

### 2. Categorical encoding

Most machine learning algorithms require numeric input. Categorical variables therefore need to be converted into a numerical representation.

Common methods:

- One-hot encoding
- Ordinal encoding
- Target encoding
- Frequency encoding

Example:

- `city = {"NYC", "Boston", "Chicago"}` can become:
  - NYC: [1, 0, 0]
  - Boston: [0, 1, 0]
  - Chicago: [0, 0, 1]

This allows a model to treat each category as a separate signal rather than a raw text label.

### 3. Date and time features

Timestamps often contain useful information that is hidden in the raw format.

Examples:

- Extract `day_of_week`
- Extract `month`
- Extract `hour`
- Compute `days_since_last_purchase`
- Create `is_weekend`

These features can capture seasonality and timing effects that are very important in retail, finance, and logistics.

### 4. Interaction features

Some patterns only emerge when two variables interact.

Example:

- `age` and `income` may together predict credit risk better than either one alone
- `temperature * humidity` may be more predictive of comfort or energy use than either alone

An interaction feature like `income_age_product = income * age` may help the model learn combined effects.

### 5. Domain-specific features

This is where business knowledge matters most. Transform features according to the problem's context.

Examples:

- In finance: debt-to-income ratio, credit utilization, monthly spending trends
- In healthcare: BMI, risk scores, age groups
- In marketing: customer lifetime value, recency-frequency-monetary (RFM) metrics
- In e-commerce: average order value, cart abandonment rate

These features can capture behavior that is not obvious from the raw dataset alone.

### 6. Missing value treatment

Missing values are not always just a nuisance; they may carry signal.

Examples:

- Replace missing `age` with median age
- Use a flag such as `missing_income = 1` when income is unknown
- Fill in missing dates with a default or estimate

This prevents the model from ignoring rows or failing on null values.

## Good vs. bad feature engineering

Good feature engineering:

- Uses domain knowledge
- Improves model performance and interpretability
- Reflects real patterns in the data
- Is learned or fitted only on training data when necessary
- Is tested and validated

Bad feature engineering:

- Adds random or noisy variables
- Leaks information from the test set into training
- Creates features that are hard to interpret or maintain
- Uses transformations without understanding the effect on the model

## Example: predicting house price

Suppose we want to predict the selling price of a house.

Raw columns:

- `square_feet`
- `bedrooms`
- `bathrooms`
- `neighborhood`
- `year_built`
- `sale_date`

A naive model might use only the raw numbers and strings, but feature engineering can create more useful inputs:

- `price_per_sqft = sale_price / square_feet`
- `age_of_house = 2025 - year_built`
- `bedrooms_per_sqft = bedrooms / square_feet`
- `is_new_home = 1 if age_of_house < 5 else 0`
- `month_sold = sale_date.month`
- `is_urban = 1 if neighborhood in ["Downtown", "Midtown"] else 0`
- `log_price = log(sale_price + 1)`

These features help the model understand the data better:

- `price_per_sqft` captures value density
- `age_of_house` reflects depreciation or renovation potential
- `month_sold` may capture seasonal demand
- `is_urban` encodes location effects
- `log_price` reduces skew in pricing distribution

This often improves a regression model compared with using only raw values.

## Feature engineering workflow

A typical workflow is:

1. Understand the problem and the business context
2. Explore the data and identify missing or noisy patterns
3. Decide which variables are relevant
4. Transform or combine features
5. Encode categorical variables
6. Validate the new features using cross-validation
7. Keep only features that improve the model
8. Repeat as needed

# Feature selection

Feature selection is the process of choosing a useful subset of the available input features for a model. Feature engineering creates or transforms features; feature selection decides which existing features to keep. The aim is to retain information useful for predicting the target while removing irrelevant, redundant, or misleading inputs.

Selecting features can reduce training time and make a model easier to interpret. Removing noisy inputs may also reduce overfitting, but fewer features do not automatically mean a better model. A feature that is weak on its own may be useful alongside another feature, and the best subset depends on the model and task. Evaluate choices using validation data or cross-validation.

### Main approaches

- **Filter methods** score features with statistics before model training. Examples include correlation, chi-square tests, and mutual information. They are generally fast, but may miss interactions and require methods appropriate to the data and target.
- **Wrapper methods** evaluate subsets by repeatedly fitting and validating a model. Recursive feature elimination (RFE), for example, removes less useful features iteratively. This can account for a particular model, but may be computationally expensive.
- **Embedded methods** select features during model fitting. L1-regularized models can shrink some coefficients to zero; tree models provide importance scores. These results depend on the model and do not establish that a feature causes the target.
- **Basic data checks** include dropping constant or duplicate columns and investigating highly correlated features. Correlated features may be redundant, but whether to remove one depends on the model and the analysis goal.

### Example: selecting features for customer churn

Suppose `churned` indicates whether a customer left (1) or stayed (0), and candidate inputs include `tenure_months`, `monthly_fee`, `total_charges`, `customer_id`, and `support_calls`. `customer_id` is an identifier, not a meaningful measurement, so exclude it rather than letting a model memorize IDs. `tenure_months` and `total_charges` may be correlated; test whether both improve validation performance. Retain `monthly_fee` or `support_calls` only if they add useful predictive signal.

Here, mutual information ranks features by their relationship with the binary target, and `SelectKBest` keeps two. The selector is inside a scikit-learn pipeline, so during cross-validation it is fitted only on each fold's training portion. This prevents information from that fold's validation portion influencing feature selection.

```python
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# df contains the churn label and candidate predictor columns.
X = df[["tenure_months", "monthly_fee", "total_charges", "support_calls"]]
y = df["churned"]

model = make_pipeline(
	StandardScaler(),
	SelectKBest(score_func=mutual_info_classif, k=2),
	LogisticRegression(max_iter=1000),
)
scores = cross_val_score(model, X, y, cv=5, scoring="roc_auc")
print(f"Mean cross-validation ROC AUC: {scores.mean():.3f}")

# Fit after choosing the approach, then inspect selected feature names.
model.fit(X_train, y_train)
selector = model.named_steps["selectkbest"]
print("Selected features:", X_train.columns[selector.get_support()].tolist())
```

Compare different values of `k` and selection methods using the same cross-validation strategy and a metric suited to the task. Keep a final test set untouched until choices are complete. For time-dependent or grouped data, use time-aware or group-aware splits instead of random folds. Fit every data-dependent preprocessing and selection step on training data only, preferably in a pipeline.

## Example in Python

Here is a simple example using pandas and scikit-learn:

```python
import pandas as pd
import numpy as np

# Example dataset

df = pd.DataFrame({
    'income': [30000, 45000, 70000, 120000, 90000],
    'age': [22, 30, 45, 60, 35],
    'city': ['NYC', 'Boston', 'Chicago', 'NYC', 'Boston'],
    'purchase_amount': [100, 200, 400, 700, 350]
})

# Create new features

df['log_income'] = np.log1p(df['income'])
df['income_per_age'] = df['income'] / df['age']

df = pd.get_dummies(df, columns=['city'], drop_first=True)

print(df)
```

This creates:

- `log_income`, which reduces skew in income
- `income_per_age`, which captures a combined signal
- one-hot encoded columns for city categories

These engineered features are often more useful than the raw values alone.

## Important caution: avoid data leakage

Feature engineering must be done carefully. If you create a transformation using the full dataset before splitting into train and test, you may leak information from the test set into the model.

For example:

- Do not compute the median of the full dataset to fill missing values before train/test split
- Do not fit an encoder on all data before separating data into training and validation
- Instead, fit transforms on the training set only and apply them to validation and test sets

This is why scikit-learn `Pipeline` is so useful: it ensures preprocessing and feature engineering steps are handled correctly during training and inference.

## Summary

Feature engineering is the art and science of turning raw data into better model inputs. It includes transformations, encoding, combinations, and domain-inspired features. The goal is not to add complexity for its own sake, but to provide the model with representations that reveal the underlying patterns in the data. When done well, feature engineering can significantly improve model accuracy, robustness, and interpretability.

