#coding=utf-8
'''
Created on 2013-6-2

@author: SnowOnion
'''

class FileUtil(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    # @quite well
    @staticmethod    
    def tolog(str, filePath="log.txt"):
        f = file(filePath, 'w')
        f.write(str)
        f.close

        