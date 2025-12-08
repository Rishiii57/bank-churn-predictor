# Bank Churn Prediction — Machine Learning Project

This project predicts whether a bank customer will churn (leave the bank) using machine learning model.  
The dataset used is the Bank Churn Kaggle dataset.

# Project Overview
This ML project includes:
- Loading and cleaning the data  
- Exploratory Data Analysis (EDA)  
- Removing unnecessary columns  
- Encoding categorical variables  
- Splitting the dataset
- Training and testing the model  
- Evaluating results

I have received an accuracy for 83.2% by this model.

# Project Structure
│── churn_predictor.py     # Main ML code
│── data.csv               # Kaggle dataset
│── README.md              # Documentation

# Technologies Used
Python
Pandas
NumPy
Matplotlib / Seaborn
Scikit-Learn
Jupyter / VS Code

# Model Details
The model pipeline includes:
Cleaning missing data
One-hot encoding (pd.get_dummies())
Train-test split
Training ML model (Logistic Regression / Random Forest)
Accuracy & performance evaluation

# Dataset
10,000 customers
Features including age, credit score, balance, tenure, geography, etc.

# Future Improvements
Hyperparameter tuning
XGBoost / LightGBM models
Deployment with Flask / FastAPI

#  Author
Rishi Kumar
Machine Learning & AI enthusiast
Github: Rishiii57