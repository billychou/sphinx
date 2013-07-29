#-*- coding:utf-8 -*-
import string 
import random 

def generatestr():
    """ 
        Func: generateStr
        Usage:
            s1 = generateStr 
            Generate the random string  
    """
    seed_str    = string.lowercase
    seed_digits = string.digits
    astr = ''
    tnum = ''
    lenstr = random.randint(6,10)
    astr   += ''.join( random.choice(seed_str) for i in xrange(lenstr) )
    tnum   += ''.join( random.choice(seed_digits) for i in xrange(2) )
    return astr+tnum

