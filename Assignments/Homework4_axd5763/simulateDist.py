import math
import sys
import random
random.seed(1343)
def geometric(instance,probability):
    i=0
    dist=[]
    instance=int(instance)
    probability=float(probability)
    how_many=0
    success=0
    while(i<instance):
        i+=1
        how_many=0
        dist=[]
        while(1):
            if(random.random()<=probability):
                how_many+=1
                success=1
                dist.extend([1])
                break
            else:
                how_many+=1
                dist.extend([0])

        if(success==1):
            print(how_many,"sample(s) were generated for getting a success")
            print(dist)
        else:
            print("No successful sampless were generated")

def binomial(instance,times,probability):
    i=0
    j=0
    dist=[]
    instance=int(instance)
    probability=float(probability)
    times=int(times)
    while(j<instance):
        j+=1
        ones=0
        i=0
        dist=[]
        while(i<times):
            i+=1
            if(random.random()<=probability):
                dist.extend([1])
                ones+=1
            else:
                dist.extend([0])
        print(dist,ones," is the number of successes\n")
    
def bernoulli(instance,probability):
    i=0
    dist=[]
    sum=0
    instance=int(instance)
    probability=float(probability)
    while(i<instance):
        i+=1
        if(random.random()<=probability):
            dist.extend([1])
        else:
            dist.extend([0])
    
    print("The bernoulli distribution is \n",dist)


def neg_binomial(instance,k,probability):
    i=0
    dist=[]
    instance=int(instance)
    probability=float(probability)
    k=int(k)
    temp=k
    while(i<instance):
        i+=1
        how_many=0
        success=0
        k=temp
        while(1):
            if(random.random()<=probability):
                    success+=1
            how_many+=1
            if(success == k):
                break

        if(success == k):
            print("{} sample(s) were generated before {} getting successes".format(how_many,success))
        else:
            print("No successful sampless were generated")

def poisson(instance,lamb):
    instance=int(instance)
    lamb=int(lamb)
    i=0
    pl=[]
    while(i<instance):
        i+=1
        F=math.exp(-lamb)
        j=0
        prob=random.random()
        while(prob>=F):
            F=F+math.exp(-lamb)*((lamb**j)/math.factorial(j))
            j+=1
        pl.extend([j-1])
    print(pl)
    


def arb_discrete(*args):
    instance=int(args[1])
    val=args[3:]
    mylist=[float(i) for i in val]
    i=1
    pl=[]
    while(i<len(mylist)):
        mylist[i]+=mylist[i-1]
        i+=1
    k=0
    if(mylist[len(mylist)-1]>1)or(mylist[len(mylist)-1]!=1.0):
        print("wrong probability values!!Exiting!")
        return
    while(k<instance):
        k+=1
        j=1
        prob=random.random()
        if(mylist[0]>=prob):
            pl.extend([0])
        while(j<len(mylist)):
            flag=0
            if(mylist[j]>=prob>=mylist[j-1]):
                place=j+1
                flag=1
                pl.extend([place-1])
                break
            else:
                j+=1
    print(pl)   

def uniform(instance,upper,lower):      
    instance=int(instance)
    upper=int(upper)
    lower=int(lower)
    i=0
    while(i<instance):
        print(lower+((lower-upper)*random.random()))
        i+=1

def exponential(instance,lamb):
    instance=int(instance)
    lamb=float(lamb)
    i=0
    while(i<instance):
        i+=1
        print((math.log(1-random.random())/lamb))

def gamma(instance,alpha,lamb):
    alpha=int(alpha)
    lamb=int(lamb)
    instance=int(instance)
    i=0
    while(i<instance):
        temp=0
        i+=1
        j=0
        while(j<alpha):
            j+=1
            temp+=(math.log(1-random.random())/lamb)
        print(-1*temp)

def normal(instance,nu,sigma):
    instance=int(instance)
    nu=int(nu)
    sigma=int(sigma)
    x=[]
    i=0
    while(i<instance/2):
        i+=1
        u1 = random.random()
        a = math.sqrt(-2*math.log(u1))
        u2 = random.random()
        b = 2*math.pi*u2
        Z0 = a*math.cos(b)
        Z1 = a*math.sin(b)
        x.append(Z0*sigma + nu)
        x.append(Z1*sigma + nu)    
    print(x[:instance])

def main():
    distrib = sys.argv[2]

    if distrib=='bernoulli':                    #done
        bernoulli(sys.argv[1],sys.argv[3])              
    elif distrib=='binomial':                   #done
        binomial(sys.argv[1],sys.argv[3],sys.argv[4])               
    elif distrib=='geometric':                  #done
        geometric(sys.argv[1],sys.argv[3])
    elif distrib=='neg_binomial':               #done
        neg_binomial(sys.argv[1],sys.argv[3],sys.argv[4])
    elif distrib=='poisson':                    
        poisson(sys.argv[1],sys.argv[3])
    elif distrib=='arb_discrete':               #done
        arb_discrete(*sys.argv[:])
    elif distrib=='uniform':
        uniform(sys.argv[1],sys.argv[3],sys.argv[4])    
    elif distrib=='exponential':                #done
        exponential(sys.argv[1],sys.argv[3])
    elif distrib=='gamma':
        gamma(sys.argv[1],sys.argv[3],sys.argv[4])
    elif distrib=='normal':
        normal(sys.argv[1],sys.argv[3],sys.argv[4])
    else:
        print('wrong distribution, EXITING!!!1')   

if __name__ == "__main__": main()
