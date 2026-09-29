# Boston Housing Price Prediction

A machine learning project for analyzing the Boston Housing dataset and predicting house prices based on different housing and socioeconomic features.

## Project Overview

This project explores the Boston Housing dataset through data analysis, visualization, preprocessing, and machine learning.

The main goal is to understand the relationships between the available features and house prices, then build a machine learning model that can predict the target house price.

## Dataset

The project uses the Boston Housing dataset stored in:

```text
data/raw/housing.csv
```

The dataset contains housing-related and socioeconomic features that can be used to predict the median value of houses.

## Project Structure

```text
predicting-boston-housing-prices/
│
├── data/
│   ├── raw/
│   │   └── housing.csv
│   └── processed/
│
├── models/
│
├── notebooks/
│   └── boston_housing.ipynb
│
├── reports/
│
├── src/
│
├── visuals.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Workflow

The project follows these main steps:

1. Load the dataset
2. Explore the data
3. Check data types and missing values
4. Perform exploratory data analysis (EDA)
5. Visualize relationships between features and house prices
6. Prepare the data for machine learning
7. Train machine learning models
8. Evaluate model performance
9. Compare the obtained results

## Exploratory Data Analysis

The analysis includes:

* Dataset structure and summary statistics
* Distribution analysis
* Feature relationships
* Correlation analysis
* Outlier investigation
* Data visualization

The main analysis is available in:

```text
notebooks/boston_housing.ipynb
```

## Visualization

The project also includes reusable visualization functions in:

```text
visuals.py
```

These functions are used to make the exploratory analysis more organized and reusable.

## Machine Learning

The project uses supervised machine learning for a regression task.

The target variable represents the median house value, while the remaining relevant features are used as predictors.

Model performance is evaluated using appropriate regression metrics such as:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

## Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook

## Getting Started

Clone the repository:

```bash
git clone https://github.com/AAshrafR/predicting-boston-housing-prices.git
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run Jupyter Notebook:

```bash
jupyter notebook
```

Then open:

```text
notebooks/boston_housing.ipynb
```

## Project Status

The project is currently under development. The analysis and machine learning workflow will be extended as the project progresses.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
