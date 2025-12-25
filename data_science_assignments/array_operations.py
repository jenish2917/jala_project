import numpy as np

print("Data Science Assignments - NumPy Practice")
print("========================================")

# Basic Array Operations

# 1. Create a 3x3 array filled with random integers between 0 and 10.
# Calculate the sum, mean, and standard deviation of the array.
print("1. Creating a 3x3 array with random integers between 0 and 10:")
array_3x3 = np.random.randint(0, 11, size=(3, 3))
print("Array:")
print(array_3x3)

# Calculate statistics
array_sum = np.sum(array_3x3)
array_mean = np.mean(array_3x3)
array_std = np.std(array_3x3)

print(f"Sum: {array_sum}")
print(f"Mean: {array_mean:.2f}")
print(f"Standard Deviation: {array_std:.2f}")
print()

# 2. Create a 1D array of 10 elements and compute the cumulative sum of the elements.
print("2. Creating a 1D array with 10 elements and computing cumulative sum:")
array_1d = np.random.randint(1, 11, size=10)
print(f"Array: {array_1d}")

# Calculate cumulative sum
cumulative_sum = np.cumsum(array_1d)
print(f"Cumulative Sum: {cumulative_sum}")
print()

# 3. Generate two 2x3 arrays with random integers and perform element-wise operations.
print("3. Creating two 2x3 arrays and performing element-wise operations:")
array1 = np.random.randint(1, 11, size=(2, 3))
array2 = np.random.randint(1, 11, size=(2, 3))

print("First Array:")
print(array1)
print("\nSecond Array:")
print(array2)

# Element-wise operations
addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2
division = array1 / array2

print("\nAddition:")
print(addition)
print("\nSubtraction:")
print(subtraction)
print("\nMultiplication:")
print(multiplication)
print("\nDivision:")
print(division)
print()

# 4. Create a 4x4 identity matrix.
print("4. Creating a 4x4 identity matrix:")
identity_matrix = np.eye(4)
print("Identity Matrix:")
print(identity_matrix)
print()

# 5. Given an array a = np.array([5, 10, 15, 20, 25]), divide each element by 5 using broadcasting.
print("5. Dividing each element by 5 using broadcasting:")
a = np.array([5, 10, 15, 20, 25])
print(f"Original Array: {a}")

# Divide each element by 5
result = a / 5
print(f"After dividing by 5: {result}")
print()

print("Array Manipulation:")
print("-" * 18)

# 6. Reshape a 1D array of 12 elements into a 3x4 matrix.
print("6. Reshaping a 1D array of 12 elements into a 3x4 matrix:")
array_12 = np.arange(1, 13)
print(f"Original 1D Array: {array_12}")

reshaped = array_12.reshape(3, 4)
print("Reshaped to 3x4:")
print(reshaped)
print()

# 7. Flatten a 3x3 matrix into a 1D array.
print("7. Flattening a 3x3 matrix into a 1D array:")
matrix_3x3 = np.random.randint(1, 11, size=(3, 3))
print("3x3 Matrix:")
print(matrix_3x3)

flattened = matrix_3x3.flatten()
print(f"Flattened to 1D: {flattened}")
print()

# 8. Stack two 3x3 matrices horizontally and vertically.
print("8. Stacking two 3x3 matrices horizontally and vertically:")
mat1 = np.random.randint(1, 6, size=(3, 3))
mat2 = np.random.randint(6, 11, size=(3, 3))

print("First Matrix:")
print(mat1)
print("\nSecond Matrix:")
print(mat2)

# Horizontal stacking
h_stacked = np.hstack((mat1, mat2))
print("\nHorizontally stacked:")
print(h_stacked)

# Vertical stacking
v_stacked = np.vstack((mat1, mat2))
print("\nVertically stacked:")
print(v_stacked)
print()

# 9. Concatenate two arrays along a new axis.
print("9. Concatenating two arrays along a new axis:")
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

print(f"First array shape: {arr1.shape}")
print(f"Second array shape: {arr2.shape}")

# Stack arrays along a new axis
stacked = np.stack((arr1, arr2), axis=0)
print("\nStacked along new axis:")
print(stacked)
print(f"New shape: {stacked.shape}")
print()

# 10. Transpose a 3x2 matrix.
print("10. Transposing a 3x2 matrix:")
matrix_3x2 = np.random.randint(1, 11, size=(3, 2))
print("Original 3x2 Matrix:")
print(matrix_3x2)

# Transpose the matrix
transposed = matrix_3x2.T
print("\nTransposed (2x3):")
print(transposed)
print()

print("Indexing and Slicing:")
print("-" * 20)

# 11. Given a 1D array of 15 elements, extract elements at positions 2 to 10 with a step of 2.
print("11. Extracting elements from a 1D array with specific step:")
arr_15 = np.arange(1, 16)
print(f"Array: {arr_15}")

# Extract elements from index 2 to 10 with step of 2
extracted = arr_15[2:11:2]
print(f"Extracted elements: {extracted}")
print()

# 12. Create a 5x5 matrix and extract the sub-matrix containing elements from rows 1 to 3 and columns 2 to 4.
print("12. Creating a 5x5 matrix and extracting a sub-matrix:")
matrix_5x5 = np.random.randint(1, 26, size=(5, 5))
print("5x5 Matrix:")
print(matrix_5x5)

# Extract sub-matrix from rows 1-3 and columns 2-4
sub_matrix = matrix_5x5[1:4, 2:5]
print("\nSub-matrix (rows 1-3, cols 2-4):")
print(sub_matrix)
print()

# 13. Replace all elements in a 1D array greater than 10 with the value 10.
print("13. Replacing elements greater than 10 with 10:")
arr_replace = np.random.randint(5, 20, size=10)
print(f"Original array: {arr_replace}")

# Replace elements greater than 10 with 10
arr_replace[arr_replace > 10] = 10
print(f"After replacement: {arr_replace}")
print()

# 14. Use fancy indexing to select elements from a 1D array at positions [0, 2, 4, 6].
print("14. Using fancy indexing to select specific elements:")
arr_fancy = np.random.randint(1, 21, size=10)
print(f"Original array: {arr_fancy}")

# Select elements at specific positions
positions = [0, 2, 4, 6]
selected = arr_fancy[positions]
print(f"Selected elements at positions {positions}: {selected}")
print()

# 15. Create a 1D array of 10 elements and reverse it using slicing.
print("15. Reversing a 1D array using slicing:")
arr_reverse = np.random.randint(1, 11, size=10)
print(f"Original array: {arr_reverse}")

# Reverse the array using slicing
reversed_arr = arr_reverse[::-1]
print(f"Reversed array: {reversed_arr}")
print()

print("Broadcasting:")
print("-" * 12)

# 16. Create a 3x3 matrix and add a 1x3 array to each row using broadcasting.
print("16. Adding a 1D array to each row of a 3x3 matrix using broadcasting:")
matrix_3x3 = np.random.randint(1, 6, size=(3, 3))
array_1x3 = np.random.randint(1, 4, size=3)

print("3x3 Matrix:")
print(matrix_3x3)
print(f"\n1D Array: {array_1x3}")

# Broadcasting addition
result = matrix_3x3 + array_1x3
print("\nResult after adding 1D array to each row:")
print(result)
print()

# 17. Multiply a 1D array of 5 elements by a scalar value using broadcasting.
print("17. Multiplying a 1D array by a scalar using broadcasting:")
arr_1d_5 = np.random.randint(1, 6, size=5)
scalar = 3

print(f"Original array: {arr_1d_5}")
print(f"Scalar value: {scalar}")

# Scalar multiplication
result = arr_1d_5 * scalar
print(f"Result: {result}")
print()

# 18. Subtract a 3x1 column vector from a 3x3 matrix using broadcasting.
print("18. Subtracting a column vector from a 3x3 matrix using broadcasting:")
matrix_3x3_new = np.random.randint(5, 11, size=(3, 3))
col_vector = np.random.randint(1, 4, size=(3, 1))

print("3x3 Matrix:")
print(matrix_3x3_new)
print("\nColumn Vector:")
print(col_vector)

# Broadcasting subtraction
result = matrix_3x3_new - col_vector
print("\nResult after subtracting column vector:")
print(result)
print()

# 19. Add a scalar to a 3D array and demonstrate how broadcasting works across all dimensions.
print("19. Adding a scalar to a 3D array using broadcasting:")
array_3d = np.random.randint(1, 6, size=(2, 3, 4))
scalar_3d = 10

print(f"3D Array shape: {array_3d.shape}")
print("\nFirst 2D slice:")
print(array_3d[0])
print(f"\nScalar value: {scalar_3d}")

# Broadcasting scalar addition
result_3d = array_3d + scalar_3d
print("\nResult after adding scalar (first 2D slice):")
print(result_3d[0])
print()

# 20. Create two arrays of shapes (4, 1) and (1, 5) and add them using broadcasting.
print("20. Adding two arrays with different shapes using broadcasting:")
arr_4x1 = np.random.randint(1, 6, size=(4, 1))
arr_1x5 = np.random.randint(1, 6, size=(1, 5))

print("Array (4, 1):")
print(arr_4x1)
print("\nArray (1, 5):")
print(arr_1x5)

# Broadcasting addition
result = arr_4x1 + arr_1x5
print(f"\nResult shape: {result.shape}")
print("Result:")
print(result)
print()

print("Vectorized Operations:")
print("-" * 22)

# 21. Compute the square root of each element
print("21. Computing the square root of each element in a 2D array:")
arr_2d_sqrt = np.random.randint(1, 26, size=(3, 4))
print("Original 2D array:")
print(arr_2d_sqrt)

# Calculate square root of each element
sqrt_result_2d = np.sqrt(arr_2d_sqrt)
print("Square roots:")
print(np.round(sqrt_result_2d, 2))
print()

# 22. Calculate the dot product of two 1D arrays of size 5
print("22. Calculating the dot product of two 1D arrays:")
arr1_dot = np.random.randint(1, 6, size=5)
arr2_dot = np.random.randint(1, 6, size=5)
print(f"First array: {arr1_dot}")
print(f"Second array: {arr2_dot}")

dot_product = np.dot(arr1_dot, arr2_dot)
print(f"Dot product: {dot_product}")
print()

# 23. Element-wise comparison returning boolean array
print("23. Element-wise comparison of two 1D arrays:")
arr1_comp = np.random.randint(1, 11, size=8)
arr2_comp = np.random.randint(1, 11, size=8)
print(f"First array: {arr1_comp}")
print(f"Second array: {arr2_comp}")

comparison_result = arr1_comp > arr2_comp
print(f"First array > Second array: {comparison_result}")
print()

# 24. Double the value of each element in a 2D array
print("24. Doubling each element in a 2D array using vectorized operation:")
arr_2d_double = np.random.randint(1, 11, size=(3, 3))
print("Original array:")
print(arr_2d_double)

doubled = arr_2d_double * 2
print("After doubling:")
print(doubled)
print()

# 25. Sum of all even numbers using vectorized operations
print("25. Computing sum of all even numbers in an array:")
arr_100 = np.random.randint(1, 101, size=100)
print(f"Array of 100 random integers (showing first 20): {arr_100[:20]}...")

# Filter even numbers and compute sum
even_mask = arr_100 % 2 == 0
even_numbers = arr_100[even_mask]
even_sum = np.sum(even_numbers)
print(f"Number of even values: {len(even_numbers)}")
print(f"Sum of all even numbers: {even_sum}")
print()

print("Linear Algebra:")
print("-" * 15)

# 26. Find determinant of a 3x3 matrix
print("26. Finding the determinant of a 3x3 matrix:")
matrix_det = np.random.randint(1, 6, size=(3, 3))
print("Matrix:")
print(matrix_det)

determinant = np.linalg.det(matrix_det)
print(f"Determinant: {determinant:.2f}")
print()

# 27. Matrix inverse and verification
print("27. Computing matrix inverse and verifying:")
matrix_inv = np.array([[4, 7], [2, 6]], dtype=float)
print("Original 2x2 Matrix:")
print(matrix_inv)

inverse = np.linalg.inv(matrix_inv)
print("\nInverse Matrix:")
print(np.round(inverse, 2))

# Verify by multiplication
identity_check = np.dot(matrix_inv, inverse)
print("\nVerification (Original × Inverse = Identity):")
print(np.round(identity_check, 2))
print()

# 28. Eigenvalues and eigenvectors
print("28. Calculating eigenvalues and eigenvectors of a 2x2 matrix:")
matrix_eigen = np.array([[3, 1], [1, 3]], dtype=float)
print("Matrix:")
print(matrix_eigen)

eigenvalues, eigenvectors = np.linalg.eig(matrix_eigen)
print(f"\nEigenvalues: {eigenvalues}")
print("Eigenvectors:")
print(eigenvectors)
print()

# 29. Solve system of linear equations
print("29. Solving system of linear equations: 2x + 3y = 5 and 4x + 6y = 10:")
# Coefficient matrix
A = np.array([[2, 3], [4, 6]], dtype=float)
# Constants vector
b = np.array([5, 10], dtype=float)

print("Coefficient matrix A:")
print(A)
print(f"Constants vector b: {b}")

try:
    solution = np.linalg.solve(A, b)
    print(f"Solution: x = {solution[0]:.2f}, y = {solution[1]:.2f}")
except np.linalg.LinAlgError:
    print("System has no unique solution (equations are dependent/inconsistent)")
    # Use least squares for dependent system
    solution, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
    print(f"Least squares solution: x = {solution[0]:.2f}, y = {solution[1]:.2f}")
print()

# 30. SVD and matrix reconstruction
print("30. Performing SVD and reconstructing the matrix:")
matrix_svd = np.random.randint(1, 6, size=(3, 3)).astype(float)
print("Original Matrix:")
print(matrix_svd)

# Perform SVD
U, S, Vt = np.linalg.svd(matrix_svd)
print("\nU matrix:")
print(np.round(U, 2))
print(f"\nSingular values: {np.round(S, 2)}")
print("\nVt matrix:")
print(np.round(Vt, 2))

# Reconstruct matrix
S_matrix = np.diag(S)
reconstructed = np.dot(U, np.dot(S_matrix, Vt))
print("\nReconstructed Matrix:")
print(np.round(reconstructed, 2))
print("\nVerification (difference from original):")
print(np.round(matrix_svd - reconstructed, 10))
print()

print("=" * 50)
print("Additional NumPy Questions:")
print("=" * 50)
print()

# Additional Q1: Min-max scaling normalization
print("Additional Q1. Normalizing array using min-max scaling:")
arr_normalize = np.random.randint(10, 100, size=10)
print(f"Original array: {arr_normalize}")

min_val = np.min(arr_normalize)
max_val = np.max(arr_normalize)
normalized = (arr_normalize - min_val) / (max_val - min_val)
print(f"Normalized array (0-1 range): {np.round(normalized, 3)}")
print()

# Additional Q2: Replace specific values
print("Additional Q2. Replacing all occurrences of a specific value:")
matrix_replace = np.random.randint(1, 6, size=(5, 5))
print("Original 5x5 matrix:")
print(matrix_replace)

value_to_replace = 3
new_value = 99
matrix_replace[matrix_replace == value_to_replace] = new_value
print(f"\nAfter replacing all {value_to_replace}s with {new_value}:")
print(matrix_replace)
print()

# Additional Q3: Element-wise operations (already covered in Q3, showing again)
print("Additional Q3. Element-wise operations on two arrays:")
arr_a = np.array([10, 20, 30, 40])
arr_b = np.array([2, 4, 6, 8])
print(f"Array A: {arr_a}")
print(f"Array B: {arr_b}")
print(f"Addition: {arr_a + arr_b}")
print(f"Subtraction: {arr_a - arr_b}")
print(f"Multiplication: {arr_a * arr_b}")
print(f"Division: {arr_a / arr_b}")
print()

# Additional Q4: Solve linear equations 3x + 4y = 7 and 5x + 2y = 8
print("Additional Q4. Solving: 3x + 4y = 7 and 5x + 2y = 8:")
A_eq = np.array([[3, 4], [5, 2]], dtype=float)
b_eq = np.array([7, 8], dtype=float)
solution_eq = np.linalg.solve(A_eq, b_eq)
print(f"Solution: x = {solution_eq[0]:.2f}, y = {solution_eq[1]:.2f}")
# Verify
print(f"Verification: 3({solution_eq[0]:.2f}) + 4({solution_eq[1]:.2f}) = {3*solution_eq[0] + 4*solution_eq[1]:.2f}")
print(f"Verification: 5({solution_eq[0]:.2f}) + 2({solution_eq[1]:.2f}) = {5*solution_eq[0] + 2*solution_eq[1]:.2f}")
print()

# Additional Q5: Broadcasting implementation
print("Additional Q5. Broadcasting a 1D array across a 3x3 matrix:")
mat_broadcast = np.random.randint(1, 6, size=(3, 3))
arr_broadcast = np.array([10, 20, 30])
print("3x3 Matrix:")
print(mat_broadcast)
print(f"1D Array: {arr_broadcast}")
result_broadcast = mat_broadcast + arr_broadcast
print("Result (matrix + array broadcasted to each row):")
print(result_broadcast)
print()

# Additional Q6: Identity matrix (already covered in Q4)
print("Additional Q6. Creating a 3x3 identity matrix:")
identity_3x3 = np.eye(3)
print(identity_3x3)
print()

# Additional Q7: Matrix multiplication
print("Additional Q7. Matrix multiplication of two 2D arrays:")
mat_mult_a = np.random.randint(1, 6, size=(2, 3))
mat_mult_b = np.random.randint(1, 6, size=(3, 2))
print("Matrix A (2x3):")
print(mat_mult_a)
print("\nMatrix B (3x2):")
print(mat_mult_b)
result_mult = np.matmul(mat_mult_a, mat_mult_b)
print("\nResult of A × B (2x2):")
print(result_mult)
print()

# Additional Q8: Dot and cross product
print("Additional Q8. Dot product and cross product of two vectors:")
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
print(f"Vector 1: {vec1}")
print(f"Vector 2: {vec2}")

dot_prod = np.dot(vec1, vec2)
cross_prod = np.cross(vec1, vec2)
print(f"Dot product: {dot_prod}")
print(f"Cross product: {cross_prod}")
print()

# Additional Q9: Find unique elements
print("Additional Q9. Finding unique elements in an array:")
arr_unique = np.random.randint(1, 11, size=20)
print(f"Array of 20 random integers: {arr_unique}")
unique_elements = np.unique(arr_unique)
print(f"Unique elements: {unique_elements}")
print(f"Number of unique elements: {len(unique_elements)}")
print()

# Additional Q10: Matrix inverse function
print("Additional Q10. Function to return the inverse of a matrix:")
def matrix_inverse(matrix):
    """Returns the inverse of a given matrix"""
    try:
        return np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        return "Matrix is singular and cannot be inverted"

test_matrix = np.array([[1, 2], [3, 4]], dtype=float)
print("Test matrix:")
print(test_matrix)
inv_result = matrix_inverse(test_matrix)
print("Inverse:")
print(np.round(inv_result, 2))
print()

print("=" * 50)
print("All NumPy assignments completed successfully!")
print("=" * 50)
