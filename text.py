import gmpy2
print("4亿位圆周率！！！")
import time
time1=time.time()
gmpy2.get_context().precision =15
pi=gmpy2.acos(gmpy2.mpfr(-1))
time2=time.time()
o=time2 - time1
print(pi)
print ("总共耗时：%s秒"%(o))
data=open("E:三角函数计算圆周率2.txt",'w+')
print('%s'%pi,file=data)
data.close()

time.sleep(3600) 
