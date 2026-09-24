import pandas as pd



# A Series is a one-dimensional labeled array in pandas.
# products = pd.Series(['Laptop', 'Smartphone', 'Tablet'])
# print(products)


# Read the customer data from a CSV file into a pandas DataFrame.
df = pd.read_csv("dataset/customers-1000/customers-1000.csv")

# # Save the DataFrame to a new CSV file without writing the index column.
# df.to_csv("dataset/output.csv", index=False)
# print(df.head())





# # Inspect the data by viewing rows, dimensions, column names, and statistics.

# print(df.head()) # Display the first five rows.
# print(df.tail()) # Display the last five rows.
# print(df.sample(5)) # Display five randomly selected rows.

# print(df.shape) # Show the number of rows and columns.
# print(df.info()) # Show column names, data types, and non-null counts.
# print(df.describe()) # Show summary statistics for numeric columns.

# print(df.columns) # Display all column names.
# print(df.dtypes) # Display the data type of each column.






# .loc selects data using row labels and column names.
# .iloc selects data using zero-based row and column positions.

# x = df.head() # Store the first five rows in a separate DataFrame.
# print(x)

# a = df.loc[3] # Select the row whose index label is 3.
# print(a)

# b = df.loc[3, "Email"] # Select the Email value from the row with index label 3.
# print(b)

# # Select rows with labels 1 through 4 and the requested columns.
# df.loc[1:4, "Email","Webiste"]




# ## iloc
# a = df.iloc[1] # Select the second row using its integer position.
# print(a)

# df.iloc[0:4, 1:7] # Select rows 0–3 and columns 1–6 by position.


# ## Select a single column by its name.
# a = df["Email"]
# print(a)



# ### filtering
# x=df.head()
# print(x)

# a=df[df["Index"]<4]
# print(a)

# # we can use here operators like and ,or , not , equal , isin, .str.contains etc. search filtering on web 


#### crud columns 