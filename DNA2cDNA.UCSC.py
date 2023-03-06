# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:52:15 2022

@author: Matthew

Description: Takes DNA sequence and finds its compliment
"""

# Filename
filename = "UCSC.DNA.txt"

# Open the file
inpf = open(filename)

# Take contents from file and attach to a string variable
s = inpf.read()

# Replace C with G, G with C, A with T, and T with A
ttable = s.maketrans("gcatGCAT", "cgtaCGTA")
swapped = s.translate(ttable)

# Display in the console what is happening
print(s)
print(swapped)

# Write to new file
outf = open("UCSC.cDNA.txt", "w")
outf.write(swapped)
outf.close()

# Close file
inpf.close()
