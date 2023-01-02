import numpy as np

data = np.loadtxt(fname="data\inflammation-01.csv", delimiter=",")
print(data)

print('This data is a ', type(data))
print('The elements are ', data.dtype)
print('The shape, or dimensions, of this data is (row, columns)',data.shape)

print('The first value in data:', data[0,0])
print('The middle value in data:', data[30,20])

print("\n Slicing Data")
print(" \n Select the first ten days (columns) of values for the first four patients (rows) \n")

print(data[0:4, 0:10])

print(" \n don’t have to start slices at 0 \n" )
print(data[5:10, 0:10])

print("\nDon’t have to include the upper and lower bound on the slice.")
print("If not included, the lower bound uses 0 by default.")
print("If not included, the upper bound slice runs to the end of the axis.")
print("If neither are included (i.e., if we use ‘:’ on its own), the slice includes everything \n" )


print("This example selects rows 0 through 2 and columns 36 through to the end of the array.")
small = data[:3, 36:]
print('small is:')
print(small)

print("\nAnalyzing Data")
print("\nFind the average inflammation for all patients on all days ask NumPy to compute data’s mean value:")
print(np.mean(data))

maxval, minval, stdval = np.max(data), np.min(data), np.std(data)
print("max inflammation:", maxval)
print("min inflammation:", minval)
print("standard deviation:", stdval)
print("")
print("When analyzing data, though, we often want to look at variations in statistical values, such as the maximum inflammation per patient or the average inflammation per day.")
print("One way to do this is to create a new temporary array of the data we want, then ask it to do the calculation.")


# patient zero
# 0 on the first axis (rows), everything on the second (columns)
patient_0 = data[0,:]
print('Max inflammation for patient 0:', np.max(patient_0))

print('Max inflammation for patient 2:', np.max(data[2, :]))

print("If the maximum inflammation for each patient over all days or the average for each day, we want to perform the operation across an axis")
print("For a 2-D array, rows are axis=1, columns axis=0")

# over days, average inflammation per day for all patients
print(np.mean(data, axis=0))
print(np.mean(data, axis=0).shape)

# per patient, average inflammation per patient across all days
print(np.mean(data, axis=1))
print(np.mean(data, axis=1).shape)

print("\n Slicing Strings")

element = 'oxygen'
print('first three characters:', element[0:3])
print('last three characters:', element[3:6])

print('element[:4]:', element[:4])
print('element[4:]:', element[4:])
print('element[:]:', element[:])

print('element[-1]:', element[-1])
print('element[-2]:', element[-2])

# removes the first and last letters from ‘oxygen’
print('element[1:-1]:', element[1:-1])

# rewrite the slice to get the last three characters of element, so that it works even if we assign a different string to element.
# Test your solution with the following strings: carpentry, clone, hi.

element = 'oxygen'
print('last three characters:', element[-3:])
element = 'carpentry'
print('last three characters:', element[-3:])
element = 'clone'
print('last three characters:', element[-3:])
element = 'hi'
print('last three characters:', element[-3:])

print("\n Thin Slices")

print('data[3:3, 4:4]:', type(data[3:3, 4:4]), data[3:3, 4:4].shape, data[3:3, 4:4].dtype)
print('data[3:3, :]:', type(data[3:3, :]), data[3:3, :].shape, data[3:3, :].dtype)

print("\nStacking Arrays")

# build array
A = np.array([[1,2,3], [4,5,6], [7, 8, 9]])
print('A = ')
print(A)

# horizontal stack of two arrays of A
B = np.hstack([A, A])
print('B = ')
print(B)

# vertical stack of two arrays of A
C = np.vstack([A, A])
print('C = ')
print(C)

 # Write some additional code that slices the first and last columns of A, and stacks them into a 3x2 array.

# A[:, :1] returns a two dimensional array with one singleton dimension (i.e. a column vector).
D = np.hstack((A[:, :1], A[:, -1:]))
print('D = ')
print(D)

#  alternative way to achieve the same result is to use Numpy’s delete function to remove the second column of A.
E = np.delete(A, 1, 1)
print('E = ')
print(E)

# The patient data is longitudinal, each row represents a series of observations relating to one individual.
# This means that the change in inflammation over time is a meaningful concept.
# Using NumPy calculate changes in the data contained in an array.
# The numpy.diff() function takes an array and returns the differences between two successive values.
# Examine the changes each day across the first week for patient 3 from our inflammation dataset.

patient3_week1 = data[3, :7]
print(patient3_week1)
print(np.diff(patient3_week1))

# Note that the array of differences is shorter by one element (length 6).

# When calling numpy.diff with a multi-dimensional array, an axis argument can be passed to the function to specify which axis to process.
# When applying numpy.diff to the 2D inflammation array data, the axis specified would be the column axis (1) which is in days,
# so the difference is the change in inflammation.

print(np.diff(data, axis = 1))

# The shape of the data file is (60, 40) (60 rows and 40 columns).
# After you run the diff() function the shape is  (60, 39) because there is one fewer difference between columns than there are columns in the data.
print(np.diff(data, axis = 1).shape)

# Find the largest change in inflammation for each patient.
# Using the numpy.max() function after the numpy.diff() function, to get the largest difference between days.
print(np.max(np.diff(data, axis=1), axis=1))

# If inflammation values decrease along an axis, then the difference from one element to the next will be negative.
# If you are interested in the magnitude of the change and not the direction, use the numpy.absolute() function

print(np.max(np.absolute(np.diff(data, axis=1)), axis=1))

