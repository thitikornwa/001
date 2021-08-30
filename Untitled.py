#!/usr/bin/env python
# coding: utf-8

# In[3]:


# fibonacci for one interval
# input bl, bu, fh = Fn, fl = Fn-1,
bl = 1.64873
bu =  1.65124
fh = 2
fl = 1
print("reaching 1.6500\n")

k= fl/fh
print("k= ", k)
i= bu-bl
xu = bl+(k)*i
xl = bu-(k)*i

print("interval: ",i)
print("\nlow:  ",bl) 
print("f(l)",3*pow(bl,5)-7*pow(bl,3)-54*bl+21)
print("xl:  ",xl)
print("f(xl):",3*pow(xl,5)-7*pow(xl,3)-54*xl+21)
print("xu:  ",xu)
print("f(xu):",3*pow(xu,5)-7*pow(xu,3)-54*xu+21)
print("high:  ",bu)
print("f(h):",3*pow(bu,5)-7*pow(bu,3)-54*bu+21)


# In[5]:


#Golden methode one interval
#input bl,bu for each interval 
bl = 1.6497
bu =  1.6506
i= bu-bl
xu = bl+(0.618)*i
xl = bu-(0.618)*i

print("interval ",i)
print("lower bound ",bl) 
print(3*pow(bl,5)-7*pow(bl,3)-54*bl+21)
print("xl ",xl)
print(3*pow(xl,5)-7*pow(xl,3)-54*xl+21)
print("xu ",xu)
print(3*pow(xu,5)-7*pow(xu,3)-54*xu+21)
print("upper bound ",bu)
print(3*pow(bu,5)-7*pow(bu,3)-54*bu+21)


# In[93]:


#Powell
# input a, b, c

a = 1.66167
fa = 3*pow(a,5)-7*pow(a,3)-54*a+21

b = 1.64978
fb = 3*pow(b,5)-7*pow(b,3)-54*b+21

c= 1.64586
fc = 3*pow(c,5)-7*pow(c,3)-54*c+21



lam = 0.5*( fa*((b*b)-(c*c)) + (pow(c,2)-pow(a,2))*fb + fc*(pow(a,2)-pow(b,2)))  /  (fa*(b-c) + fb*(c-a) + fc*(a-b))

min_con = ( (b-c)*fa + (c-a)*fb -(a-b)*fc ) / ( (a-b)*(b-c)*(c-a) )

f_lam = 3*pow(lam,5)-7*pow(lam,3)-54*lam+21

print("f(a) ",fa)
print("f(b) ",fb)
print("f(c) ",fc)

print("lam ",lam)
print("F(lam) ",f_lam)


print(min_con)


# In[8]:


#Arithematics one interval
#inpu a[0]=a, a[1]=b, a[2]=c

a= [1.5827 ,1.6325 ,1.7370, 0]
tag=["a","b","c","s"]

a[3] = (a[0]+a[2]+a[1])/3
fr = [0,0,0,0]

for j in range(4):
    
    fr[j]= 3*pow(a[j],5)-7*pow(a[j],3)-54*a[j]+21
    
    print(tag[j],"=",a[j]," ",fr[j])
    
tole = abs(fr[1]-fr[3])/abs(fr[3])
print("tolerance=",tole)


# In[ ]:




