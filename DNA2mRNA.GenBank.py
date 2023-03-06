# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 01:02:53 2022

@author: Matthew

Description: Takes DNA sequence and finds the mRNA sequence
"""

# Filename
filename = "GenBank.DNA.txt"

# Open the file
inpf = open(filename)

# Take contents from file and attach to a string variable
s = inpf.read()

# Replace T with U
ttable = s.maketrans("t", "u")
swapped = s.translate(ttable)

# Display in the console what is happening
print(s)
print(swapped)

# Write to new file
outf = open("GenBank.mRNA.txt", "w")
outf.write(swapped)
outf.close()

# Close file
inpf.close()