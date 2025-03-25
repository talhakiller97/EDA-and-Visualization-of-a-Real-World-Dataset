# Titanic Dataset Analysis

## Description
This project explores and analyzes the Titanic dataset to understand passenger demographics, survival rates, and key correlations among features.

## Steps
### 1. Data Loading
- The dataset is loaded from a publicly available GitHub repository.
- Initial exploration includes displaying the first few rows and dataset information.

### 2. Data Cleaning
- Identified and handled missing values:
  - 'Age' was imputed with its median value.
  - 'Embarked' and 'Cabin' rows with missing values were removed.
- Removed duplicate entries.
- Detected and managed outliers in 'Fare' using the IQR method.

### 3. Data Visualization
- Bar charts were created for categorical variables such as 'Survived', 'Pclass', and 'Sex'.
- Histograms were plotted for 'Age' and 'Fare'.
- A correlation heatmap was generated to identify relationships between numerical features.

### 4. Insights
- **Survival Rate**: Around 38% of passengers survived, with a higher survival rate among women.
- **Age Distribution**: Most passengers were between 20 and 40 years old.
- **Fare Analysis**: Most fares were relatively low, but some passengers paid significantly higher fares.
- **Correlations**: Negative correlation between 'Fare' and 'Pclass' (higher class tickets had higher fares), and a small positive correlation between 'SibSp' and 'Parch'.

## Requirements
- Python 3.x
- NumPy
- Pandas
- Matplotlib
- Seaborn

## How to Run
1. Install dependencies:
   ```sh
   pip install numpy pandas matplotlib seaborn
   ```
2. Run the script:
   ```sh
   python titanic_analysis.py
   ```

## Author
Talha Saeed

