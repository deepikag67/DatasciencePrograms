# Writing files
# a - Append - will append to the end of the file
# W - write - Will overwrite any existing content



# Opening the file and appending the contents to the file
#f = open("C://Technology//DevOps//Steps//aditya.txt", "a")
#f.write("Writing contents to file")
#f.close()

# Appending some more contents to the file - the contents will be appended to the end of the file.
#f = open("C://Technology//DevOps//Steps//aditya.txt", "a")
#f.write(" Contents")
#f.close()

# Writing to the file - Make sure there is some string written already inside the file.
# After running the below lines entire string will be overwritten

f = open("C://Technology//DevOps//Steps//aditya.txt", "w")
f.write(" Contents")
f.close()

