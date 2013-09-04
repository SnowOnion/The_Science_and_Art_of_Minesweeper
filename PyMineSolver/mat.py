# coding=utf-8
#!/usr/bin/python2

'''
Created on 2013-5-29

@author: SnowOnion
'''

from matUtil import MatUtil
from fileUtil import FileUtil

# @well
def addPre(lst, alphabet):
    newlst = []
    for alpha in alphabet:
        for ele in lst:
            alst = [alpha]
            alst.extend(ele)
            newlst.append(alst)
    return newlst

# @well
def dicOrder(length=1, alphabet=[0, 1]):
    lst = [[]]
    for i in range(length):
        lst = addPre(lst, alphabet)
    return lst
    


# @quite well
def examSolu(mat, solu): 
    for equ in mat:
        multi = 0        
        for i in range(len(solu)):
            multi += equ[i] * solu[i]
        
        if multi == equ[-1]:
            pass  # 通过了这个方程的检验
        else:
            return False
    return True  # 渡尽劫波, 通过所有方程检验
    

def record(solu):
    print solu
    

# @quite well
def calcProb(soluPool):
    '''返回是雷概率list。长度等于len(soluPool[0])
    '''
    lenlen = len(soluPool[0])
    plst = [0] * lenlen
    for solu in soluPool:
        for gi in  range(lenlen):
            plst[gi] += solu[gi]
    for pi in range(lenlen):
        plst[pi] /= float(len(soluPool))
        
    return plst
    
  

    
def doOpen(pmat):
    # 手工去做...
    # open
    # change game.txt
    pass

# @well
def readGame(filepath="game.txt"):
    '''return mines,row, col, rawGameMat
    '''
    f = file(filepath, 'r')
    mines = int(f.readline())
    lines = f.readlines()
    rawGameMat = [[int(ele, 16) for ele in line.split(' ')] for line in lines]
    f.close()
    return (mines, len(rawGameMat), len(rawGameMat[0]), rawGameMat)

# quite well!
def generateGame(rawGameMat, row, col, mine):
   
    zengguang = []
    zengguang.append([0] * row * col + [mine])
   
    gameList = MatUtil.mat2list(rawGameMat)    
    
    for ri in range(len(gameList)):  # 丑陋
        
        # 每个非0num有一方程。这个num值，应该改成减完flag的。。。
        if 1 <= gameList[ri] <= 8:
            
            equ = [0] * len(gameList)  # 初始化
            mines = gameList[ri]
            
            ind8 = MatUtil.circumIjIndexList(MatUtil.ijIndex(col, ri)[0], MatUtil.ijIndex(col, ri)[1], row, col)
            for ind in ind8:
                if gameList[MatUtil.realIndex(col, ind[0], ind[1])] == 12:  # c
                    equ[MatUtil.realIndex(col, ind[0], ind[1])] = 1
                    
                if gameList[MatUtil.realIndex(col, ind[0], ind[1])] == 15:  # f
                    mines -= 1
            equ.append(mines)  # 增广阵的b值
            zengguang.append(equ)
        elif gameList[ri] == 12:  # c
            zengguang[0][ri] = 1

    return zengguang
    

    
# 注意点。。0，[1,8]，12,15
def filt(rawGameMat, soluPool):
    '''简直不能更重要了。返回sage筛选后的soluPool
    '''
    gamelist = MatUtil.mat2list(rawGameMat)
    for i in range(len(gamelist)):
#         print 'i=',i,'solupool len=',len(soluPool)
        if not  gamelist[i] == 12:  # 非sage留0
            soluPool = filter(lambda x:x[i] == 0, soluPool)
#             print 'filt',i,'after, solupool len=',len(soluPool)
    return soluPool

   
# 蓝图
# 更新mat
def doit(mat, row, col, soluPool):
    for solu in soluPool:
        if examSolu(mat, solu):
            record(solu)
    plst = calcProb(solu)
#     displayProb(plst)
    doOpen(plst)
#     filt(readGame(), mat)



def cmd(rawcmd):
    sp=rawcmd.split(' ')
    
    if len(sp)!=3:
        print 'command var1 var2 not fit!'
        return
    
    
    
    

    
# 0~8 for num, C(12) for sage, F(15) for flag, 为了: 都用1个空格分隔，而且至少原始文件排版整齐
if __name__ == '__main__':
    
    mines, row, col, rawGameMat = readGame()
    MatUtil.printMatrix(rawGameMat, 'rawGameMat')
    print 'mines = ', mines

    gameMat = generateGame(rawGameMat, row, col, mines)
    MatUtil.printMatrix(gameMat, 'gameMat')
    
        
    # 这个全产生再筛选太蠢。。。可以砍掉好多大树杈
    soluPool = dicOrder(row * col, [0, 1]) 
    
    # num与flag者，尽筛成0 ###################flag不应0...而且flag表现在()上还是在本身=1上？？
    soluPool = filt(rawGameMat, soluPool)
    
    # 正确性
    right = 0
    newSoluPool = []
    for solu in soluPool:
        if examSolu(gameMat, solu):
            right += 1
            newSoluPool.append(solu)
    soluPool = newSoluPool  ###########为了循环daze
    print 'right = ', right

    # calcProb，为每一个c
    
    probMat = MatUtil.list2mat(calcProb(soluPool), col)
    MatUtil.printMatrix(probMat, 'probMat', 6, 3) 
    
    
    
# #     while(True):
# #         inin=raw_input('Just enter, 主人樣')
# #         doit(gameMat,row,col,soluPool)
# #     
#     pass
#   
#     

    

