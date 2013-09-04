#coding=utf-8
'''
Created on 2013-5-29

@author: SnowOnion
'''

from os import linesep
import mat

def matrixForm(mat):
    rst=''
    for line in mat:
        for ele in line:
            rst=rst+str(ele)+' '
        rst+=linesep
    return rst

def printMatrixForm(mat):
    for line in mat:
        for ele in line:
            print ele,
        print ''    #肿么用iterator的方式防止最后那个换行捏?

if __name__ == '__main__':
    mat=[[(i,j) for i in range(4)] for j in range(3)]
    printMatrixForm(mat)
    print matrixForm(mat)

    matty=[[ele[0]+ele[1] for ele in line] for line in mat]    
    printMatrixForm(matty)
    print matrixForm(matty)