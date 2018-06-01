# -*- coding: utf-8 -*-
import time

def fibs(num):
    result = [0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

def main():
    result = fibs(100000)
    fobj = open('D:\\python\\Daily Test\\test file\\result.txt','w+')
    for i,num in enumerate(result):
        print (u"第 %d 个数是： %d" % (i,num))
        fobj.write("%d" % num)
        time.sleep(0.0001)

if __name__ == '__main__':
    main()