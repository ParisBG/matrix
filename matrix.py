#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 09:49:10 2022
@author: parisbg

Sean invented a game involving a 2n × 2n matrix where each cell of the matrix 
contains an integer. He can reverse any of its rows or columns any number of 
times. The goal of the game is to maximize the sum of the elements in the 
n × n submatrix located in the upper-left quadrant of the matrix.
Given the initial configurations for q matrices, help Sean reverse the 
rows and columns of each matrix in the best possible way so that the sum of 
the elements in the matrix's upper-left quadrant is maximal.
Example:
matrix = [[1, 2], [3, 4]]
"""
import numpy as np
#move max matrix value to matrix[0][0] only by reversing rows and cols
#Matrix is only 2x2 | 

#matrix[0][0] matrix[0][1] 
#matrix[1][0] matrix[1][1]

#Create empty dict
#Traverse matrix, put matrix_num as key, index as value
#and find highest value

matrix = [[1, 2, 3, 4],[5, 5, 6, 7],[1, 2, 3, 9],[8, 4, 5, 6]]
result = np.array(matrix).flatten()
print(result)
result.sort()
print(result)
print(result[len(result)-1])