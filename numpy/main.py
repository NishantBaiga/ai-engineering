import numpy as np

## array creation
# my_array = np.array([10,20,30,40,50])
# print("my first array", my_array)


# double_array = my_array * 2
# print("Doubled Array", double_array)

# print("Array Shape:", my_array.shape)
# print("Data Type:", my_array.dtype)



#### usefull constructors

# # create array of zeros,
# a = np.zeros(3)  
# print(a)

# # create array of ones
# b = np.ones(5) 
# print(b)

#  # create array of with desire element
# c = np.full((2,3),7)
# print(c)

# # Sequential numbers from 0 up to (but not including) 10, skipping by 2
# d= np.arange(0,10,2) 
# print(d)

# # 5 evenly spaced numbers between 0 and 1 (inclusive)
# e=np.linspace(0,1,5)
# print(e)

# # A 2x2 matrix of random floats between 0 and 1
# random_matrix = np.random.rand(2, 2)
# print

# # Roll a 6-sided die 10 times (random integers from 1 up to 6)
# dice_rolls = np.random.randint(1, 7, size=10)
# print(dice_rolls)


# # By default, functions like np.zeros and np.ones create arrays using 64-bit floating-point numbers (float64), which is why you see a decimal point in the output (0.). If you are working with whole numbers and want to save memory, explicitly pass the dtype parameter:

# # Memory efficient integer array
# int_zeros = np.zeros((3, 3), dtype=np.int32)
# print(int_zeros)


# # If you already have an existing array and want to create a matching mask or blank canvas with the exact same shape and data type, use the _like counterparts:

# existing_data = np.array([[1, 2], [3, 4]])

# # Creates a 2x2 matrix of zeros automatically matching the structure above
# blank_canvas = np.zeros_like(existing_data)





#### array properties

# # Create a 2D matrix with 2 rows and 3 columns
# matrix = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)

# print("--- Array Inspection ---")
# print("Dimensions (ndim):", matrix.ndim)      # Output: 2
# print("Shape (shape):     ", matrix.shape)     # Output: (2, 3) -> 2 rows, 3 columns
# print("Total Items (size):", matrix.size)      # Output: 6
# print("Data Type (dtype): ", matrix.dtype)     # Output: int32

# print("\n--- Memory Inspection ---")
# print("Item Size (bytes): ", matrix.itemsize)  # Output: 4 (because 32 bits = 4 bytes)
# print("Total Size (bytes):", matrix.nbytes)    # Output: 24 (6 elements x 4 bytes)





#### Indexing and slicing
# arr = np.array([10, 20, 30, 40, 50, 60])

# # Indexing: Get a single value (0-indexed)
# print(arr[0])       # Output: 10
# print(arr[-1])      # Output: 60 (Negative indexing starts from the end)

# # Slicing: Extract a chunk [start:stop]
# print(arr[1:4])     # Output: [20, 30, 40] (Indices 1, 2, and 3)

# # Slicing with Steps [start:stop:step]
# print(arr[0:6:2])   # Output: [10, 30, 50] (Every 2nd element)
# print(arr[::-1])    # Output: [60, 50, 40, 30, 20, 10] (Reverses the array)




#### math operations

# import numpy as np

# arr = np.array([1, 2, 3, 4])

# # Scalar Operations
# print(arr + 10)  # Output: [11 12 13 14]
# print(arr * 2)   # Output: [2 4 6 8]
# print(arr ** 2)  # Output: [1 4 9 16] (Squaring)

# # Array-to-Array Operations (Shapes must match)
# arr2 = np.array([10, 20, 30, 40])
# print(arr + arr2)  # Output: [11 22 33 44]
# print(arr * arr2)  # Output: [10 40 90 160]


# #  Mathematical Functions (Universal Functions / ufuncs)
# angles = np.array([0, np.pi/2, np.pi])

# print(np.sin(angles))   # Trigonometric sine
# print(np.sqrt([4, 9, 16]))  # Square root -> Output: [2. 3. 4.]
# print(np.exp([1, 2]))   # Exponential (e^x)
# print(np.log([1, np.e]))  # Natural logarithm -> Output: [0. 1.]

# # aggregation functions
# matrix = np.array([[1, 2], [3, 4]])

# print(np.sum(matrix))   # Total sum of all elements -> 10
# print(np.mean(matrix))  # Arithmetic mean (average) -> 2.5
# print(np.max(matrix))   # Highest value -> 4
# print(np.std(matrix))   # Standard deviation


####  Working across Axes (Rows vs. Columns)
# matrix = np.array([[1, 2], [3, 4]])
# # Sum of each column (downwards)
# print(matrix.sum(axis=0))  # Output: [4 6]  (1+3 and 2+4)

# # Sum of each row (across)
# print(matrix.sum(axis=1))  # Output: [3 7]  (1+2 and 3+4)



#### Matrix Multiplication (Linear Algebra)
# A = np.array([[1, 2], 
#               [3, 4]])

# B = np.array([[2, 0], 
#               [1, 2]])


# # Element-wise (Not matrix multiplication)
# print(A * B)
# # Output:
# # [[2 0]
# #  [3 8]]

# # True Matrix Multiplication (Dot Product)
# print(A @ B)
# # Output:
# # [[ 4  4]
# #  [[10  8]]


#### reshaping
# # Create a 1D array of 12 elements (Size = 12)
# arr = np.arange(1, 13) 
# print("Original:", arr)  # [ 1  2  3 ... 12]

# # Reshape into a 2D matrix (3 rows, 4 columns) -> 3 x 4 = 12
# matrix_3x4 = arr.reshape(3, 4)
# print("\n3x4 Matrix:\n", matrix_3x4)

# # Reshape into a 3D tensor (2 blocks, 3 rows, 2 columns) -> 2 x 3 x 2 = 12
# tensor_3d = arr.reshape(2, 3, 2)
# print(tensor_3d)


#### The Clever -1 Trick (Auto-Calculated Dimensions)
# data = np.arange(10)  # 10 elements

# # Force it to have exactly 2 rows; let NumPy calculate the columns
# auto_matrix = data.reshape(2, -1) 
# print(auto_matrix.shape)  # Output: (2, 5) -> NumPy figured out it needs 5 columns!
