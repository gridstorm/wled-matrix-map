# Python program to export list of serpentine led indicies to put into text output
# formatted for WLED matrix json files
# Upload the file ledmap.json to the /edit folder on your WLED device
# Version 1.0
# Author: gridstorm
# Updated: 2022-12-15
#

# input lines and columns
x = int(input("Length of Line: "))
y = int(input("Number of Columns: "))

count = 0  # current led position

line_length = x  # led line length
col_length = y   # led column length
pixels = line_length * col_length

out_string = "{\"map\":["  # Add header to output

while col_length > 0:

	for i in range(count, count+line_length):  #total number of leds
	    out_string = out_string + str(i) + ', '
	count += line_length
	col_length -= 1

	if col_length > 0:
	  for i in reversed(range(count, count+line_length)):  #total number of leds
	      out_string = out_string + str(i) + ', '
	  count += line_length
	col_length -= 1

#Finalize string and output result without trailing comma and space
out_string = out_string.removesuffix(', ') + "]}"

print("\n ======================= Copy This Output ==============================")
print("\n",out_string)
print("\n =======================================================================")

# print some statistics
print("\nLine Length:", x)
print("Column Number:", y)
print("Total Pixels:", pixels)
