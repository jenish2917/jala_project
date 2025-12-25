import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

print("=" * 60)
print("PANDAS AND DATA SCIENCE ASSIGNMENTS")
print("=" * 60)
print()

# Create sample datasets for demonstrations
print("Creating sample datasets...")

# Sample employees dataset
employees_data = {
    'EmployeeID': range(1, 21),
    'Name': ['John', 'Sarah', 'Mike', 'Emma', 'David', 'Lisa', 'Tom', 'Anna', 
             'Chris', 'Mary', 'James', 'Linda', 'Robert', 'Patricia', 'Michael',
             'Jennifer', 'William', 'Elizabeth', 'David', 'Susan'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'IT',
                   'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR',
                   'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'Salary': [75000, 65000, 80000, np.nan, 62000, 85000, 70000, 78000,
               67000, np.nan, 82000, 64000, 73000, 79000, 66000,
               71000, 84000, 68000, 72000, 81000],
    'Age': [28, 35, 42, 29, 38, 45, 32, 27, 36, 41, 33, 39, 44, 30, 37,
            43, 31, 34, 38, 40]
}
df_employees = pd.DataFrame(employees_data)

# Sample sales dataset
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=100, freq='D')
sales_data = {
    'Date': dates,
    'Product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Monitor'], 100),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'SalesAmount': np.random.randint(1000, 10000, 100),
    'Quantity': np.random.randint(1, 20, 100)
}
df_sales = pd.DataFrame(sales_data)

# Sample customers dataset
customers_data = {
    'CustomerID': range(1, 11),
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Henry', 'Iris', 'Jack'],
    'Email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', 'diana@email.com',
              'eve@email.com', 'frank@email.com', 'grace@email.com', 'henry@email.com',
              'iris@email.com', 'jack@email.com'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix',
             'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
}
df_customers = pd.DataFrame(customers_data)

print("Sample datasets created successfully!")
print()

print("=" * 60)
print("1. DATA IMPORT AND CLEANING")
print("=" * 60)
print()

# Q1: Import CSV and drop rows with missing values
print("Q1. Identifying and dropping rows with missing values:")
print("\nOriginal DataFrame:")
print(df_employees.head(10))
print(f"\nMissing values per column:")
print(df_employees.isnull().sum())

df_cleaned = df_employees.dropna()
print(f"\nAfter dropping rows with missing values:")
print(f"Original rows: {len(df_employees)}, Cleaned rows: {len(df_cleaned)}")
print()

# Q2: Replace missing numerical values with mean
print("Q2. Replacing missing numerical values with column mean:")
df_employees_filled = df_employees.copy()
mean_salary = df_employees_filled['Salary'].mean()
df_employees_filled['Salary'].fillna(mean_salary, inplace=True)
print(f"Mean salary: ${mean_salary:.2f}")
print("\nDataFrame after filling missing salaries:")
print(df_employees_filled[['Name', 'Salary']].head(10))
print()

# Q3: Replace missing categorical values with mode
print("Q3. Replacing missing categorical values with mode:")
# Add some missing departments
df_test = df_employees.copy()
df_test.loc[2, 'Department'] = np.nan
df_test.loc[5, 'Department'] = np.nan
mode_dept = df_test['Department'].mode()[0]
df_test['Department'].fillna(mode_dept, inplace=True)
print(f"Mode department: {mode_dept}")
print("DataFrame after filling missing departments:")
print(df_test[['Name', 'Department']].head(10))
print()

print("=" * 60)
print("2. DATA TRANSFORMATION")
print("=" * 60)
print()

# Q1: Create new column using NumPy vectorized operations
print("Q1. Creating new column as sum of two existing columns:")
df_sales_copy = df_sales.copy()
df_sales_copy['TotalValue'] = np.add(df_sales_copy['SalesAmount'], df_sales_copy['Quantity'] * 100)
print(df_sales_copy[['Product', 'SalesAmount', 'Quantity', 'TotalValue']].head(10))
print()

# Q2: Apply mathematical function to column
print("Q2. Applying square root to numerical column:")
df_sales_copy['SqrtSales'] = np.sqrt(df_sales_copy['SalesAmount'])
print(df_sales_copy[['Product', 'SalesAmount', 'SqrtSales']].head(10))
print()

# Q3: Normalize using MinMaxScaler
print("Q3. Normalizing numerical column using MinMaxScaler:")
scaler = MinMaxScaler()
df_employees_norm = df_employees_filled.copy()
df_employees_norm['Salary_Normalized'] = scaler.fit_transform(df_employees_norm[['Salary']])
print("Explanation: MinMaxScaler transforms data to range [0, 1] using formula: (X - X_min) / (X_max - X_min)")
print(df_employees_norm[['Name', 'Salary', 'Salary_Normalized']].head(10))
print()

print("=" * 60)
print("3. MERGING AND JOINING DATASETS")
print("=" * 60)
print()

# Create related datasets for merging
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [85, 90, 78, 92]
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4, 5],
    'City': ['NYC', 'LA', 'Chicago', 'Houston'],
    'Age': [25, 30, 28, 35]
})

# Q1: Merge and fill missing values
print("Q1. Merging two DataFrames and filling missing values:")
print("\nDataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

merged_df = pd.merge(df1, df2, on='ID', how='outer')
print("\nMerged DataFrame (outer join):")
print(merged_df)
merged_df.fillna({'Score': 0, 'City': 'Unknown', 'Age': 0}, inplace=True)
print("\nAfter filling missing values:")
print(merged_df)
print()

# Q2: Left join
print("Q2. Performing left join:")
left_join = pd.merge(df1, df2, on='ID', how='left')
print(left_join)
print()

# Q3: Concatenate DataFrames
print("Q3. Concatenating DataFrames along columns:")
df_concat = pd.concat([df1, df2[['City', 'Age']]], axis=1)
print(df_concat)
print()

print("=" * 60)
print("4. GROUPING AND AGGREGATION")
print("=" * 60)
print()

# Q1: GroupBy with mean and std
print("Q1. Grouping by Department and calculating mean and std of Salary:")
grouped = df_employees_filled.groupby('Department')['Salary'].agg(['mean', 'std'])
print(grouped)
print()

# Q2: GroupBy with NumPy function
print("Q2. Using groupby with NumPy function:")
grouped_sum = df_employees_filled.groupby('Department')['Salary'].sum()
print("Sum of salaries by department:")
print(grouped_sum)
print("\nApplying NumPy sqrt to grouped results:")
print(np.sqrt(grouped_sum))
print()

# Q3: Pivot table
print("Q3. Creating pivot table:")
pivot = df_sales.pivot_table(
    values='SalesAmount',
    index='Product',
    columns='Region',
    aggfunc=np.sum,
    fill_value=0
)
print(pivot)
print()

print("=" * 60)
print("5. ARRAY OPERATIONS AND MANIPULATION")
print("=" * 60)
print()

# Q1: Create NumPy array from DataFrame column
print("Q1. Creating NumPy array from DataFrame column and performing operations:")
salary_array = df_employees_filled['Salary'].to_numpy()
print(f"Salary array (first 10): {salary_array[:10]}")
doubled_salary = salary_array * 2
print(f"Doubled salaries (first 10): {doubled_salary[:10]}")
print()

# Q2: Reshape array and assign to DataFrame
print("Q2. Reshaping NumPy array and assigning to new column:")
ages_array = df_employees_filled['Age'].to_numpy()
reshaped = ages_array.reshape(-1, 1)
df_employees_filled['Age_Reshaped'] = reshaped
print(df_employees_filled[['Name', 'Age', 'Age_Reshaped']].head(10))
print()

# Q3: Filter DataFrame using NumPy
print("Q3. Filtering DataFrame using NumPy threshold:")
threshold = 75000
mask = np.array(df_employees_filled['Salary'] > threshold)
high_earners = df_employees_filled[mask]
print(f"Employees with salary > ${threshold}:")
print(high_earners[['Name', 'Department', 'Salary']])
print()

print("=" * 60)
print("6. BROADCASTING AND VECTORIZED OPERATIONS")
print("=" * 60)
print()

# Q1: Broadcast NumPy array across DataFrame column
print("Q1. Broadcasting NumPy array across DataFrame column:")
bonus_array = np.array([5000])
df_employees_filled['Salary_With_Bonus'] = df_employees_filled['Salary'] + bonus_array
print(df_employees_filled[['Name', 'Salary', 'Salary_With_Bonus']].head(10))
print()

# Q2: Vectorized operation on multiple columns
print("Q2. Creating new column from vectorized operation on multiple columns:")
df_sales['Revenue'] = np.multiply(df_sales['SalesAmount'], df_sales['Quantity'])
print(df_sales[['Product', 'SalesAmount', 'Quantity', 'Revenue']].head(10))
print()

# Q3: Subtract mean from each row
print("Q3. Subtracting mean of each row from row elements:")
df_numeric = df_employees_filled[['Salary', 'Age']].copy()
row_means = df_numeric.mean(axis=1).to_numpy().reshape(-1, 1)
df_centered = df_numeric - row_means
print("Original DataFrame:")
print(df_numeric.head(10))
print("\nAfter subtracting row means:")
print(df_centered.head(10))
print()

print("=" * 60)
print("7. LINEAR ALGEBRA WITH NUMPY")
print("=" * 60)
print()

# Q1: Solve linear equations and store in DataFrame
print("Q1. Solving linear equations and storing in DataFrame:")
# System: 2x + 3y = 13, 4x + y = 11
A = np.array([[2, 3], [4, 1]])
b = np.array([13, 11])
solution = np.linalg.solve(A, b)
solution_df = pd.DataFrame({'Variable': ['x', 'y'], 'Value': solution})
print(solution_df)
print()

# Q2: Dot product of two DataFrame columns
print("Q2. Computing dot product of two DataFrame columns:")
dot_product = np.dot(df_sales['SalesAmount'][:10], df_sales['Quantity'][:10])
print(f"Dot product of SalesAmount and Quantity (first 10 rows): {dot_product}")
print()

# Q3: Matrix multiplication on DataFrames
print("Q3. Performing matrix multiplication on DataFrames:")
df_mat1 = pd.DataFrame(np.random.randint(1, 10, (3, 3)), columns=['A', 'B', 'C'])
df_mat2 = pd.DataFrame(np.random.randint(1, 10, (3, 3)), columns=['X', 'Y', 'Z'])
print("Matrix 1:")
print(df_mat1)
print("\nMatrix 2:")
print(df_mat2)
result_mat = pd.DataFrame(np.matmul(df_mat1.values, df_mat2.values))
print("\nResult of matrix multiplication:")
print(result_mat)
print()

print("=" * 60)
print("8. HANDLING MISSING DATA")
print("=" * 60)
print()

# Q1: Interpolate missing values
print("Q1. Interpolating missing values using linear method:")
df_interp = pd.DataFrame({
    'Value': [1, 2, np.nan, np.nan, 5, 6, np.nan, 8]
})
print("Original DataFrame:")
print(df_interp)
df_interp['Value_Interpolated'] = df_interp['Value'].interpolate(method='linear')
print("\nAfter interpolation:")
print(df_interp)
print()

# Q2: Fill missing values using NumPy mask
print("Q2. Filling missing values using NumPy mask:")
df_mask = df_employees.copy()
mask = np.isnan(df_mask['Salary'])
df_mask.loc[mask, 'Salary'] = 70000
print("After filling missing salaries with 70000:")
print(df_mask[['Name', 'Salary']].head(10))
print()

# Q3: Replace outliers with median
print("Q3. Replacing outliers with median using NumPy mask:")
df_outlier = df_sales.copy()
median_sales = np.median(df_outlier['SalesAmount'])
q1 = np.percentile(df_outlier['SalesAmount'], 25)
q3 = np.percentile(df_outlier['SalesAmount'], 75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outlier_mask = (df_outlier['SalesAmount'] < lower_bound) | (df_outlier['SalesAmount'] > upper_bound)
df_outlier.loc[outlier_mask, 'SalesAmount'] = median_sales
print(f"Median: {median_sales}, Lower bound: {lower_bound:.2f}, Upper bound: {upper_bound:.2f}")
print(f"Number of outliers replaced: {outlier_mask.sum()}")
print()

print("=" * 60)
print("9. ADVANCED DATA ANALYSIS")
print("=" * 60)
print()

# Q1: GroupBy with NumPy operations on multi-level data
print("Q1. Analyzing trends in multi-level categorical dataset:")
multi_grouped = df_sales.groupby(['Product', 'Region'])['SalesAmount'].agg([np.mean, np.std, np.sum])
print(multi_grouped.head(15))
print()

# Q2: Correlation matrix
print("Q2. Creating correlation matrix:")
corr_matrix = df_employees_filled[['Salary', 'Age']].corr()
print("Correlation matrix:")
print(corr_matrix)
print("\nUsing NumPy to compute correlation:")
np_corr = np.corrcoef(df_employees_filled['Salary'], df_employees_filled['Age'])
print(np_corr)
print()

# Q3: Rolling mean calculation
print("Q3. Performing rolling mean calculation on time series:")
df_sales_sorted = df_sales.sort_values('Date')
df_sales_sorted['Rolling_Mean_7'] = df_sales_sorted['SalesAmount'].rolling(window=7).mean()
print(df_sales_sorted[['Date', 'SalesAmount', 'Rolling_Mean_7']].head(15))
print()

print("=" * 60)
print("10. DATAFRAME AND ARRAY MANIPULATION")
print("=" * 60)
print()

# Q1: Convert DataFrame to array and back
print("Q1. Converting DataFrame to NumPy array, performing operation, and converting back:")
df_temp = df_employees_filled[['Salary', 'Age']].head(5)
print("Original DataFrame:")
print(df_temp)
array_temp = df_temp.to_numpy()
array_temp = array_temp * 1.1  # 10% increase
df_result = pd.DataFrame(array_temp, columns=['Salary_Increased', 'Age_Increased'])
print("\nAfter 10% increase:")
print(df_result)
print()

# Q2: Generate DataFrame with random values and filter
print("Q2. Generating DataFrame with random values and filtering:")
random_df = pd.DataFrame(
    np.random.randint(1, 100, (10, 3)),
    columns=['A', 'B', 'C']
)
print("Random DataFrame:")
print(random_df)
filtered = random_df[(random_df['A'] > 30) & (random_df['B'] < 70)]
print("\nFiltered (A > 30 AND B < 70):")
print(filtered)
print()

# Q3: Apply custom NumPy function
print("Q3. Applying custom NumPy function to create DataFrame:")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])
custom_func = lambda x, y: np.power(x, 2) + np.sqrt(y)
result_arr = custom_func(arr1, arr2)
result_df = pd.DataFrame({'Array1': arr1, 'Array2': arr2, 'Result': result_arr})
print(result_df)
print()

print("=" * 60)
print("11. DATA RESHAPING AND ANALYSIS")
print("=" * 60)
print()

# Q1: Reshape array from DataFrame and analyze
print("Q1. Reshaping array extracted from DataFrame:")
sales_array = df_sales['SalesAmount'].head(12).to_numpy()
reshaped_sales = sales_array.reshape(3, 4)
print("Reshaped to 3x4:")
print(reshaped_sales)
print(f"Mean of reshaped array: {np.mean(reshaped_sales):.2f}")
print()

# Q2: Stack DataFrames vertically
print("Q2. Stacking DataFrames vertically and analyzing:")
df_part1 = df_employees_filled.head(5)
df_part2 = df_employees_filled.tail(5)
stacked = pd.concat([df_part1, df_part2], ignore_index=True)
print("Stacked DataFrame:")
print(stacked)
print(f"\nMean salary: ${np.mean(stacked['Salary']):.2f}")
print()

# Q3: Create 3D array and convert to MultiIndex DataFrame
print("Q3. Creating 3D array and converting to MultiIndex DataFrame:")
array_3d = np.random.randint(1, 100, (2, 3, 4))
print("3D Array shape:", array_3d.shape)
# Flatten and create MultiIndex
reshaped_2d = array_3d.reshape(2*3, 4)
index = pd.MultiIndex.from_product([range(2), range(3)], names=['Level1', 'Level2'])
df_multi = pd.DataFrame(reshaped_2d, index=index, columns=['A', 'B', 'C', 'D'])
print("\nMultiIndex DataFrame:")
print(df_multi)
print("\nGrouped by Level1:")
print(df_multi.groupby(level=0).mean())
print()

print("=" * 60)
print("12. TIME SERIES ANALYSIS")
print("=" * 60)
print()

# Q1: Convert to time series and perform NumPy operation
print("Q1. Converting column to time series and performing NumPy operation:")
df_ts = df_sales.copy()
df_ts['Date'] = pd.to_datetime(df_ts['Date'])
df_ts.set_index('Date', inplace=True)
df_ts['Log_Sales'] = np.log(df_ts['SalesAmount'])
print(df_ts[['SalesAmount', 'Log_Sales']].head(10))
print()

# Q2: Moving average
print("Q2. Calculating moving average using Pandas and NumPy:")
window_size = 7
df_ts['MA_7'] = df_ts['SalesAmount'].rolling(window=window_size).mean()
print(df_ts[['SalesAmount', 'MA_7']].head(15))
print()

# Q3: Time difference calculation
print("Q3. Computing time difference between rows:")
df_time = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-05', '2023-01-10', '2023-01-20']
})
df_time['Date'] = pd.to_datetime(df_time['Date'])
df_time['Days_Diff'] = np.diff(df_time['Date'].values.astype('datetime64[D]'), prepend=df_time['Date'].values[0].astype('datetime64[D]'))
print(df_time)
print()

print("=" * 60)
print("ADDITIONAL PANDAS QUESTIONS (Q11-30)")
print("=" * 60)
print()

# Q11: Load CSV and display first 10 rows
print("Q11. Loading CSV and displaying first 10 rows:")
print("(Using in-memory DataFrame as demonstration)")
print(df_employees.head(10))
print()

# Q12: GroupBy operations
print("Q12. GroupBy operations to find mean and sum:")
grouped_stats = df_employees_filled.groupby('Department').agg({
    'Salary': ['mean', 'sum'],
    'Age': 'mean'
})
print(grouped_stats)
print()

# Q13: Handle missing data
print("Q13. Handling missing data by replacing NaN with column mean:")
df_handle = df_employees.copy()
df_handle['Salary'].fillna(df_handle['Salary'].mean(), inplace=True)
print(df_handle[['Name', 'Salary']].head(10))
print()

# Q14: Merge DataFrames with different join types
print("Q14. Merging DataFrames with different join types:")
df_a = pd.DataFrame({'ID': [1, 2, 3], 'Value': [10, 20, 30]})
df_b = pd.DataFrame({'ID': [2, 3, 4], 'Score': [100, 200, 300]})

print("Inner join:")
print(pd.merge(df_a, df_b, on='ID', how='inner'))
print("\nOuter join:")
print(pd.merge(df_a, df_b, on='ID', how='outer'))
print("\nLeft join:")
print(pd.merge(df_a, df_b, on='ID', how='left'))
print("\nRight join:")
print(pd.merge(df_a, df_b, on='ID', how='right'))
print()

# Q15: Type conversion
print("Q15. Converting column from object to float:")
df_convert = pd.DataFrame({'Value': ['1.5', '2.3', '3.7', 'invalid', '5.1']})
print("Original DataFrame:")
print(df_convert)
df_convert['Value_Float'] = pd.to_numeric(df_convert['Value'], errors='coerce')
print("\nAfter conversion (errors='coerce'):")
print(df_convert)
print()

# Q16: Filter by range
print("Q16. Filtering DataFrame by value range:")
filtered_salary = df_employees_filled[(df_employees_filled['Salary'] >= 70000) & 
                                       (df_employees_filled['Salary'] <= 80000)]
print("Employees with salary between $70,000 and $80,000:")
print(filtered_salary[['Name', 'Department', 'Salary']])
print()

# Q17: Pivot table with multiple aggregations
print("Q17. Creating pivot table with multiple aggregations:")
pivot_multi = df_sales.pivot_table(
    values='SalesAmount',
    index='Product',
    columns='Region',
    aggfunc=[np.mean, np.sum, np.std],
    fill_value=0
)
print(pivot_multi)
print()

# Q18: Apply custom function
print("Q18. Using apply() to apply custom function:")
def categorize_salary(salary):
    if salary < 70000:
        return 'Low'
    elif salary < 80000:
        return 'Medium'
    else:
        return 'High'

df_employees_filled['Salary_Category'] = df_employees_filled['Salary'].apply(categorize_salary)
print(df_employees_filled[['Name', 'Salary', 'Salary_Category']].head(10))
print()

# Q19: Binning numerical column
print("Q19. Categorizing numerical column into bins:")
bins = [0, 30, 40, 100]
labels = ['Young', 'Middle', 'Senior']
df_employees_filled['Age_Group'] = pd.cut(df_employees_filled['Age'], bins=bins, labels=labels)
print(df_employees_filled[['Name', 'Age', 'Age_Group']].head(10))
print()

# Q20: Replace values
print("Q20. Replacing specific values in DataFrame column:")
df_replace = df_employees_filled.copy()
df_replace['Department'] = df_replace['Department'].replace('IT', 'Technology')
print(df_replace[['Name', 'Department']].head(10))
print()

print("=" * 60)
print("DATA CLEANING & PREPROCESSING (Q21-25)")
print("=" * 60)
print()

# Q21: Clean mixed data types
print("Q21. Cleaning dataset with mixed data types:")
df_mixed = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Value': ['100', '200', 'invalid', '400', '500']
})
print("Original DataFrame:")
print(df_mixed)
df_mixed['Value_Clean'] = pd.to_numeric(df_mixed['Value'], errors='coerce')
df_mixed.dropna(subset=['Value_Clean'], inplace=True)
print("\nAfter cleaning:")
print(df_mixed)
print()

# Q22: Remove duplicates
print("Q22. Identifying and removing duplicate rows:")
df_dup = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'Age': [25, 30, 25, 35, 30]
})
print("Original DataFrame:")
print(df_dup)
print(f"\nDuplicate rows: {df_dup.duplicated().sum()}")
df_no_dup = df_dup.drop_duplicates()
print("\nAfter removing duplicates:")
print(df_no_dup)
print()

# Q23: StandardScaler normalization
print("Q23. Normalizing using StandardScaler:")
print("Explanation:")
print("- MinMaxScaler: Scales data to range [0, 1] using (X - X_min) / (X_max - X_min)")
print("- StandardScaler: Standardizes data to mean=0, std=1 using (X - mean) / std")
print()

scaler_standard = StandardScaler()
df_standard = df_employees_filled.copy()
df_standard['Salary_Standardized'] = scaler_standard.fit_transform(df_standard[['Salary']])
print(df_standard[['Name', 'Salary', 'Salary_Standardized']].head(10))
print(f"\nMean of standardized values: {df_standard['Salary_Standardized'].mean():.10f}")
print(f"Std of standardized values: {df_standard['Salary_Standardized'].std():.2f}")
print()

# Q24: Label encoding
print("Q24. Converting categorical column using label encoding:")
encoder = LabelEncoder()
df_encoded = df_employees_filled.copy()
df_encoded['Department_Encoded'] = encoder.fit_transform(df_encoded['Department'])
print("Explanation: Label encoding converts categories to integers (0, 1, 2, ...)")
print("Impact: Creates ordinal relationship where none may exist")
print(df_encoded[['Name', 'Department', 'Department_Encoded']].head(10))
print(f"\nEncoding mapping: {dict(zip(encoder.classes_, encoder.transform(encoder.classes_)))}")
print()

# Q25: Train-test split
print("Q25. Splitting dataset into training and testing sets (80-20):")
X = df_employees_filled[['Age', 'Salary']]
y = df_employees_filled['Department']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)
print(f"Total samples: {len(X)}")
print(f"Training samples: {len(X_train)} ({len(X_train)/len(X)*100:.0f}%)")
print(f"Testing samples: {len(X_test)} ({len(X_test)/len(X)*100:.0f}%)")
print("\nTraining set (first 5 rows):")
print(X_train.head())
print()

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS (Q26-30)")
print("=" * 60)
print()

# Q26: Summary statistics
print("Q26. Calculating summary statistics:")
summary_stats = df_employees_filled[['Salary', 'Age']].agg(['mean', 'median', 'std'])
print(summary_stats)
print(f"\nMode of Age: {df_employees_filled['Age'].mode()[0]}")
print()

# Q27: Histogram and box plot
print("Q27. Visualizing distribution with histogram and box plot:")
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].hist(df_employees_filled['Salary'], bins=10, edgecolor='black')
axes[0].set_title('Salary Distribution (Histogram)')
axes[0].set_xlabel('Salary')
axes[0].set_ylabel('Frequency')

axes[1].boxplot(df_employees_filled['Salary'])
axes[1].set_title('Salary Distribution (Box Plot)')
axes[1].set_ylabel('Salary')

plt.tight_layout()
plt.savefig('salary_distribution.png')
print("Histogram and box plot saved as 'salary_distribution.png'")
print("Outliers: Values beyond 1.5 * IQR from Q1/Q3 quartiles")
plt.close()
print()

# Q28: Correlation matrix heatmap
print("Q28. Creating correlation matrix and heatmap:")
corr_data = df_employees_filled[['Salary', 'Age']].corr()
print("Correlation Matrix:")
print(corr_data)

plt.figure(figsize=(8, 6))
plt.imshow(corr_data, cmap='coolwarm', aspect='auto')
plt.colorbar()
plt.xticks(range(len(corr_data.columns)), corr_data.columns)
plt.yticks(range(len(corr_data.columns)), corr_data.columns)
plt.title('Correlation Heatmap')
for i in range(len(corr_data.columns)):
    for j in range(len(corr_data.columns)):
        plt.text(j, i, f'{corr_data.iloc[i, j]:.2f}', ha='center', va='center')
plt.savefig('correlation_heatmap.png')
print("\nHeatmap saved as 'correlation_heatmap.png'")
print("Interpretation: Values close to 1/-1 indicate strong positive/negative correlation")
plt.close()
print()

# Q29: Scatter plot matrix
print("Q29. Creating scatter plot matrix:")
from pandas.plotting import scatter_matrix
scatter_data = df_employees_filled[['Salary', 'Age']]
scatter_matrix(scatter_data, figsize=(10, 10), diagonal='hist')
plt.savefig('scatter_matrix.png')
print("Scatter plot matrix saved as 'scatter_matrix.png'")
print("Analysis: Shows pairwise relationships between variables")
plt.close()
print()

# Q30: Feature engineering
print("Q30. Feature engineering and importance visualization:")
df_features = df_employees_filled.copy()
df_features['Salary_Per_Age'] = df_features['Salary'] / df_features['Age']
df_features['Experience_Estimate'] = df_features['Age'] - 22  # Assuming graduation at 22

feature_importance = {
    'Salary': df_features['Salary'].std(),
    'Age': df_features['Age'].std(),
    'Salary_Per_Age': df_features['Salary_Per_Age'].std(),
    'Experience_Estimate': df_features['Experience_Estimate'].std()
}

plt.figure(figsize=(10, 6))
plt.bar(feature_importance.keys(), feature_importance.values())
plt.title('Feature Importance (Based on Standard Deviation)')
plt.xlabel('Features')
plt.ylabel('Standard Deviation')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('feature_importance.png')
print("Feature importance chart saved as 'feature_importance.png'")
print("\nNew features created:")
print(df_features[['Name', 'Salary', 'Age', 'Salary_Per_Age', 'Experience_Estimate']].head(10))
plt.close()
print()

print("=" * 60)
print("ALL PANDAS ASSIGNMENTS COMPLETED SUCCESSFULLY!")
print("=" * 60)
