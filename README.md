# 2ECEB-VELONZA-PA-3

#PROBLEM 1
1. Import the pandas library and assign it as 'pd'.
2. Reads the 'Cars.csv' file into pandas Dataframe.
3. Returns the first 5 rows of the DataFrame Cars.
   - When no limit is specified within the parenthesis, it only returns the first 5.
4. Returns the last 5 rows of the DataFrame Cars.
   - When no limit is specified within the parenthesis, it only returns the last 5.
5. Join together the first and last 5 rows of Cars.csv using concat.

#PROBLEM 2
1. Import the pandas library and assign it as 'pd'.
2. Reads the 'Cars.csv' file into pandas Dataframe.
3. Use slicing to get first five rows with odd-numbered columns.
   - The ':5' inside the closed brackets are the first five rows.
   - '1::2' selects columns starting at index 1, stepping by 2 (i.e., columns 1, 3, 5, 7, ...).
4. Use positional slicing to get the row that contains the ‘Model’ of ‘Mazda RX4’.
   - Inside the closed brackets, put the range of the desired rows and add stop index.
5. Retrieve the 'Model' and 'cyl' (cylinders) values for the car at index 23 in the Cars DataFrame.
   - Use ".loc" to pick rows and columns from a pandas DataFrame.
   - Use the "['row number', 'column title']" format.
6. Locate the 'Model', 'cyl', and 'gear' data for the Cars at index positions 1, 28, and 18 in the DataFrame Cars,
   which correspond to 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'.
