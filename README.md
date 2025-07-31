# Decision Tree Fraud Detection Program

Welcome to the Decision Tree Fraud Detection Program! This tool is designed to help detect fraudulent transactions using a decision tree classifier. Below you will find a comprehensive overview of the program, its features, usage instructions, and additional resources.

## Key Features
- **Dynamic Feature Selection:** Users can specify which features to include in the analysis.
- **Data Balancing:** Utilizes SMOTE (Synthetic Minority Oversampling Technique) to address class imbalance by generating synthetic samples of fraudulent transactions.
- **Model Training and Evaluation:** Splits the dataset into training and testing sets, trains a decision tree, and evaluates its performance.
- **Decision Explanation:** Provides insights into how the decision tree made its predictions.
- **Blockchain Integration:** Authenticates transactions on the Ethereum network using smart contracts.

## Dataset Columns
- **General Information:**
  - `Unnamed: 0`: Row index (not used as a feature)
  - `accountNumber`: Unique account identifier (not recommended as a feature)
  - `customerId`: Unique customer identifier (may be useful for customer-level analysis)
- **Financial Information:**
  - `creditLimit`: Credit limit of the account
  - `availableMoney`: Remaining credit
  - `currentBalance`: Current account balance
- **Transaction Details:**
  - `transactionDateTime`: Timestamp of the transaction
  - `transactionAmount`: Amount of the transaction
  - `transactionType`: Type of transaction (e.g., purchase, withdrawal)
- **Merchant Information:**
  - `merchantName`: Name of the merchant
  - `acqCountry`: Country of the acquiring bank
  - `merchantCountryCode`: Merchant's country code
  - `merchantCity`, `merchantState`, `merchantZip`: Merchant location details
- **POS Information:**
  - `posEntryMode`: Mode of transaction entry (e.g., chip, swipe)
  - `posConditionCode`: POS condition at the time of transaction
  - `cardPresent`: Indicates if the card was present
  - `posOnPremises`: POS on-premises indicator
- **Additional Features:**
  - `recurringAuthInd`: Recurring authorization indicator
  - `expirationDateKeyInMatch`: Match status of entered vs. stored expiration date
  - `cardCVV`, `enteredCVV`: CVV codes for mismatch detection
  - `cardLast4Digits`: Last four digits of the card
- **Target Variable:**
  - `isFraud`: Indicates whether the transaction is fraudulent (1 for fraud, 0 for not fraud)

## Explanation of Imports
- **numpy:** Numerical computations and array manipulations
- **pandas:** Data manipulation and analysis
- **scikit-learn:**
  - `SelectKBest`, `chi2`: Feature selection
  - `KBinsDiscretizer`: Discretizes continuous features
  - `DecisionTreeClassifier`, `plot_tree`: Model building and visualization
  - `train_test_split`: Data splitting
  - `accuracy_score`, `classification_report`, `confusion_matrix`: Model evaluation
  - `GridSearchCV`: Hyperparameter tuning
- **imbalanced-learn:**
  - `SMOTE`: Synthetic oversampling for class imbalance
- **matplotlib.pyplot:** Visualizations
- **seaborn:** Enhanced visualizations
- **joblib:** Model saving and loading
- **solcx:** Solidity compiler management for blockchain interaction
- **web3:** Ethereum blockchain interaction
- **hardhat:** Ethereum development environment (see below)

## Relational Model of the Dataset
This dataset, found on Kaggle, represents various credit card transactions. The focus is on predicting fraudulent transactions based on external factors.

- [Fraud Detection Dataset on Kaggle](https://www.kaggle.com/datasets/ranjeetshrivastav/fraud-detection-dataset?resource=download)

## How to Use
### Step 1: Install Dependencies
Ensure you have the required Python libraries installed:
- numpy
- pandas
- scikit-learn
- imbalanced-learn
- matplotlib
- seaborn
- web3

### Step 2: Prepare Your Dataset
Place your dataset (`transactions.csv`) in the same directory as the script. Ensure it contains the columns listed above.

### Step 3: Run the Jupyter Notebook / Python Script
1. Open the script or notebook in your Python IDE.
2. Modify the `selected_features` list to include the features you want to use.
3. Run the script to train the decision tree model and evaluate its performance.

### Step 4: Interpret the Results
- The script will print the model's accuracy, classification report, and confusion matrix.
- Visualize the decision tree structure and feature importances.
- Authenticate a transaction on the Ethereum network based on the decision tree's criteria.

## How to Enable Hardhat for ETH Transactions
Run the following commands in your terminal:
```sh
mkdir AIBlockchainProj
cd AIBlockchainProj
npm init -y
npm install --save-dev hardhat
npx hardhat
npx hardhat node
```

## Sample Results
**Data Preview:**
```
   Unnamed: 0  accountNumber  customerId  creditLimit  availableMoney  ...
0           0      737265056   737265056         5000          5000.0  ...
1           1      737265056   737265056         5000          5000.0  ...
2           2      737265056   737265056         5000          5000.0  ...
3           3      737265056   737265056         5000          5000.0  ...
4           4      830329091   830329091         5000          5000.0  ...
```

**Contract deployed at:** `0x5FbDB2315678afecb367f032d93F642f64180aa3`

**Funds released to payee.**

## More Information about Packages
- **Hardhat:** [GitHub - NomicFoundation/hardhat](https://github.com/NomicFoundation/hardhat) | [Hardhat Official Site](https://hardhat.org/)
- **Web3:** [web3.py Documentation](https://web3py.readthedocs.io/)
- **scikit-learn:** [SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html), [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html), [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
- **GeeksforGeeks:** [Decision Tree Classifier Guide](https://www.geeksforgeeks.org/decision-tree-classifier-in-python-using-scikit-learn/)
- **DataCamp:** [Decision Tree Classification Tutorial](https://www.datacamp.com/tutorial/decision-tree-classification-python)

## Overview of the Algorithm
The program uses a Decision Tree Classifier, a supervised learning algorithm for classification tasks. The tree splits the data into subsets based on feature values. Each node represents a decision, each branch an outcome, and each leaf a class label (fraudulent or not).

## Analysis of the Solution
**Strengths:**
- Easy to visualize and interpret
- Captures non-linear relationships
- Provides feature importance insights

**Weaknesses:**
- Prone to overfitting, especially with complex trees
- Sensitive to small changes in the data

## Relation to Class
This project applies supervised learning techniques, as covered in business analytics courses, to train agents on financial data for fraud detection.

## Results
The model achieved a good balance between precision and recall, as indicated by the F1 score. The confusion matrix visualization highlighted both strengths and areas for improvement.
