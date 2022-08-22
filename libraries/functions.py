import math
import numpy as np
from statistics import variance
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy import stats
# chapter2 // Descrictive Statistics-------------
def k(n):
    k= 1+(3.322*math.log(n,10))
    print("k=", k)
    return k
def R(sample, n):
    R= sample[n-1]-sample[0]
    print("R= ", R)
    return R
def d(R,k):
    d= R/k
    if (d>1):
        d = int(R/k) + 1
    print("d= ", d)
    return  d
def freqOfValues(array, n):
    freq=1
    xi=[]
    fi=[]
    freqs=[]
    relFreq=[]
    cumFreq=0
    cumFreqs=[]
    relCumFreq=[]
    for i in range(n-1):
        if (array[i+1] == array[i]):
            freq+=1            
        else:
            xi.append(array[i])
            fi.append(freq) 
            freqs.append([array[i],freq])
            relFreq.append((array[i],freq/n))
            cumFreq+=freq
            cumFreqs.append((array[i], cumFreq))
            relCumFreq.append((array[i],cumFreq/n))
            freq=1# Init freq to 1 for the next repetition to start counting
        if (i==n-2 and array[i]==array[i+1]):    
            xi.append(array[i])
            fi.append(freq) 
            freqs.append([array[i],freq])
            relFreq.append((array[i],freq/n))
            cumFreq+=freq
            cumFreqs.append((array[i], cumFreq))
            relCumFreq.append((array[i],cumFreq/n))
            freq=1# Init freq to 1 for the next repetition to start counting
        elif (i==n-2 and array[i]!=array[i+1]): 
            xi.append(array[i+1])
            fi.append(1) 
            freqs.append([array[i+1],freq])
            relFreq.append((array[i+1],freq/n))
            cumFreq+=1
            cumFreqs.append((array[i+1], cumFreq))
            relCumFreq.append((array[i+1],cumFreq/n))        
    sumM=0
    for i in range(len(fi)):
        sumM = sumM + ( xi[i] * fi[i] )# Sum for -> mean
    mean = sumM/n
    # variance, standard deviation
    sumV=0
    sumV211=0
    sumStd=0
    Ex=0
    Ex2=0
    for i in range(len(fi)):
        sumV= sumV + ( xi[i] * xi[i] * fi[i] )# Σ(Xi^2*fi) -- (2.12)
        sumStd= sumStd + ( (xi[i]-mean)*(xi[i]-mean) )# Σ(Xi - Xmean)^2  
        sumV211= sumV211 + ( (xi[i]-mean)*(xi[i]-mean) )* fi[i]# Σ(Xi - Xmean)^2 -- (2.11)  
        Ex= Ex +  ( xi[i] * relFreq[i][1] ) # Ex= Σ(Xi*pi)
        Ex2= Ex2 +  ( xi[i] * xi[i] * relFreq[i][1] ) # Ex^2= Σ(Xi^2*pi)
    variance= 1/(n-1) * ( sumV- (n*mean*mean) ) # (2.12)
    v211= 1/(n-1) * (sumV211 ) # (2.11)
    std= math.sqrt( sumStd/(n-1) )
    varEx = Ex2- (Ex* Ex) # (4.9)
    CV= ( math.sqrt(variance)/mean ) *100
    # print
    print("\nValues: ")
    print("---------------------------------------")
    print("---------------------------------------")
    print("\nfreqOfValues=",freqs)
    print("\nrelFreqOfValues= ",relFreq)
    print("\ncumFreqOfValues= ",cumFreqs)
    print("\nrelCumFreqOfValues= ",relCumFreq)
    print("\nmeanOfValues= ", mean)
    print("\nvariancesOfValues=",variance)
    print("V (211) = ", v211)
    print("VarEx= ", varEx) 
    print("\nstdOfValues", std)
    print("\nC.V= ", CV,"% \n")
    return freqs, relFreq, cumFreqs, relCumFreq, mean, variance, std, CV
def freqOfBins(sample, n, bins, range):
    mul2Arrayes = lambda arr1,arr2 : [value1*value2 for value1,value2 in zip(arr1,arr2)]
    mul3Arrayes = lambda arr1,arr2,arr3 : [value1*value2*value3 for value1,value2,value3 in zip(arr1,arr2,arr3)]

    fi,edges =np.histogram(sample,bins=bins, range= range)
    xi= midpoints=0.5*(edges[1:]+edges[:-1]) #edges[1:]-> second edges to end, edges[:-1] -> first edges to prefinal 
    mulxifi = mul2Arrayes(xi,fi)
    meanxifi = sum(mulxifi)/n
    xi2fi = mul3Arrayes(xi,xi,fi)
    variance =( 1/(n-1) ) *( np.sum(xi2fi) - (n*meanxifi*meanxifi) ) #2.10
    # v2
    v2 =( 1/(n-1) ) *( np.sum(mul2Arrayes(mul2Arrayes((xi - meanxifi),(xi - meanxifi)), fi)))   #2.9

    print("\nBins: ")
    print("---------------------------------------")
    print("---------------------------------------")
    print("\nfreqOfBins=",fi)
    print("\nedges= ",edges)
    print("\nxi= ", xi)
    print("\nmeanxifi= ", meanxifi)
    print("\nvariance", variance)
    print("\nv2", v2)

    return fi, edges, xi, variance
def relCumFreq(sample,cumFreq):
    relCumFreq = [(cumFreq/len(sample))]
    print("\nrelCumFreq: ")
    print("---------------------------------------")
    print("---------------------------------------")
    print("\nrelCumFreq=",relCumFreq)
    
    return relCumFreq
def meanSimple(sample,n):
    sum = 0
    for value in sample:
        sum= sum + value
    meanSimple= sum/n
    # print("\nMeanSimple: ")
    # print("---------------------------------------")
    # print("---------------------------------------")
    # print("\nmeanSimple=",meanSimple)
    return meanSimple
def medianBins(sample,n, d, bins, srange):
    cumFreq, lowLimit, binSize, extraPoints = stats.cumfreq(sample, numbins = bins, defaultreallimits= srange)

    fi,edges =np.histogram(sample,bins=bins, range= srange)
    for i in range(len(cumFreq)):
        if (cumFreq[i] > n/4):
    # Li =edges[i]
            F25 = edges[i] + d* ( (n/4) - cumFreq[i-1] ) / fi[i] 
            break
    for i in range(len(cumFreq)):
        if (cumFreq[i] > n/2):
    # Li =edges[i]
            median = edges[i] + d* ( (n/2) - cumFreq[i-1] ) / fi[i] 
            break
    for i in range(len(cumFreq)):
        if (cumFreq[i] > 3*n/4):
    # Li =edges[i]
            F75 = edges[i] + d* ( (3*n/4) - cumFreq[i-1] ) / fi[i] 
            break
    print("\nmedianBins: ")
    print("---------------------------------------")
    print("---------------------------------------")
    print("fi",fi)
    print("edges",edges)
    print("cumFreq",cumFreq)
    
    print("\nF25%= ", F25)
    print("\nmedianBins= ",median)
    print("\nF75%= ", F75)
    return median
def relFreqOfRange(array,start,end):
    f = 0
    for value in array:
        if value >= start and value <= end:
            f += 1
    relFreqOfRange = f/len(array)
    print("\nrelFreqOfRange: ")
    print("---------------------------------------")
    print("---------------------------------------")
    print("\nrelFreqOfRange=",relFreqOfRange)
   
    return relFreqOfRange
def lessThan(sample, value):
    count=0
    for i in range(len(sample)):
        if (sample[i] < value):
            count+=1
        else: 
            break    
    p = count/len(sample)
    print("\nLess Than :")
    print("---------------------------------------")
    print("---------------------------------------")
    print("Less than: ",value, "is ", count,"OR ", p  )
def moreThan(sample, value):
    count=0
    for i in range(len(sample)):
        if (sample[i] > value):
            count+=1    
    p = count/len(sample)
    print("\nMore Than :")
    print("---------------------------------------")
    print("---------------------------------------")
    print("More than: ",value, "is ", count,"OR ", p)
def printValues( cumFreqStats, lowLimit, binSize, extraPoints,
                 meanNp, varStats, medianNp, modeStats, stdNp, CV):
    print("\nprintValues:")
    print("---------------------------------------")
    print("---------------------------------------")
    print ("\ncumulative frequency (statistcs) : ", cumFreqStats)
    print ("Lower Limit : ", lowLimit)
    print ("bin size : ", binSize)
    print ("extra-points : ", extraPoints)
    # print ("res.binsize : ", res.binsize)
    # print ("res cumcount : ", res.cumcount)
    # print ("res cumcount.size : ", res.cumcount.size)
    # # print ("np.lispace : ", np.linspace(0, res.binsize*res.cumcount.size, res.cumcount.size))

    notation="meanNp= "
    print(notation,meanNp)
    
    notation="statistics.variance= "
    print(notation,varStats)

    notation="medianNp= "
    print(notation, medianNp)
    
    notation="modeStats= "
    print(notation,modeStats)
    
    notation="stdNp= "
    print(notation,stdNp)

    print("CV: ", CV)
def printStatsInfo(sample, n, k, R, d,):
    # stats info
    print("----stats info----")

    print("\nn=", n)
    notation="sample= "
    print(notation,sample)

    notation="k= "
    print(notation,k)

    notation="R= "
    print(notation,R)

    notation="d= "
    print(notation,d)
def figureFreqs(sample, bins, range, base):
    #res -> is for plotting cumulative histogram
    res = stats.cumfreq(sample, numbins=bins, defaultreallimits=range)
    x = res.lowerlimit + np.linspace(0, res.binsize*res.cumcount.size, res.cumcount.size)

    cumFreq, lowLimit, binSize, extraPoints = stats.cumfreq(sample, numbins = bins, defaultreallimits=range)
    
    #plot
    fig = plt.figure(figsize=(10, 10))
    histFreq = fig.add_subplot(2, 2, 1)
    histCumFreq = fig.add_subplot(2, 2, 2)
    histRelFreq = fig.add_subplot(2, 2, 3)
    histRelCumFreq = fig.add_subplot(2, 2, 4)
    # histFreq
    freqOfBins,edges, patches= histFreq.hist(sample,bins=bins, range= range, orientation='vertical',histtype='step', align='mid', edgecolor='k')
    histFreq.set_title('Frequency Histogram')
    midpoints=0.5*(edges[1:]+edges[:-1]) #edges[1:]-> second edges to end, edges[:-1] -> first edges to prefinal 
    histFreq.plot(midpoints,freqOfBins)# polygon
    loc = ticker.MultipleLocator(base=base) # this locator puts ticks at regular intervals
    histFreq.xaxis.set_major_locator(loc)
    # histCumFreq
    # histCumFreq.bar(x, res.cumcount, width=res.binsize, color='red')
    cumFreqOfBins, edges1, patches1 = histCumFreq.hist(sample,bins=bins, range= range, cumulative=True, orientation='vertical',histtype='step', align='mid', edgecolor='k')
    histCumFreq.set_title('Cumulative Histogram')
    histCumFreq.set_xlim([x.min(), x.max()])
    polPoints=(edges[1:]) #edges[1:]-> second edges to end, edges[:-1] -> first edges to prefinal 
    histCumFreq.plot(polPoints, cumFreq)#polygon
    loc = ticker.MultipleLocator(base=base) # this locator puts ticks at regular intervals
    histCumFreq.xaxis.set_major_locator(loc)
    # histRelFreq
    relFreqOfBins, edges1, patches1 = histRelFreq.hist(sample,bins=bins, range= range, density=True, orientation='vertical',histtype='step', align='mid', edgecolor='k')
    histRelFreq.set_title('Relative Frequency Histogram')
    histRelFreq.plot(midpoints, relFreqOfBins)# polygon
    # histRelCumFreq
    # histRelCumFreq.bar(x, res.cumcount/20, width=res.binsize, color='red', alpha=0.2)
    relCumFreqOfBins, edges1, patches1 = histRelCumFreq.hist(sample,bins=bins, range= range,density=True, cumulative=True, orientation='vertical',histtype='step', align='mid', edgecolor='k')
    histRelCumFreq.set_title(' Relative Cumulative Histogram')
    histRelCumFreq.set_xlim([x.min(), x.max()])
    histRelCumFreq.plot(polPoints, cumFreq/len(sample))# polygon
    plt.show()
# chapter3 // Elementary Probability Theory----------
def P(value, n): # Probability Simple
    p = value/n
    return p
def Pinter(p1,p2):  # Probability Intersection
    pinter = p1/p2
    return pinter
def Pun(p1, p2, p1inter2): # Probablity Union
    pun= p1 + p2 - p1inter2
    return pun
def Pcond(p1,p2): # Probability Conditional 
    pcond = p1/p2
    return pcond
def Pind(p1,p2): # Probablity of 2 independent sets
    pind=p1*p2
    return pind
def isIndependent(p1, p2,p1inter2):
    return p1inter2 == p1 * p2
# chapter4 // Random Variables - Probability Distributions----------
def fact(n):  # factorial
    return 1 if (n==1 or n==0) else n * fact(n - 1); 
def Pcomb(n,r): # Combinatorial Probablity - (3.7), page 67
    return fact(n)/( fact(r) * fact(n-r) )
def Pbinomial(n, x, p, q):
    return Pcomb(n,x) * pow(p,x) * pow(q,n-x) 
def Ppoisson (x, l):
    return ( math.exp(-l) * pow(l,x) )/ fact(x)
# chapter5 // Sampling Distibutions--------------------------
def std_m(std, n): # Standard deviation of mean value
    std_m = std/math.sqrt(n)
    # print("std_m= ",std_m)
    return std_m
# chapter6 // Statistical conclusion validity--------------------------
def print_stat_values(mean,variance,std,n,sem):
    print("\nstatistical values :")
    print("meax = ",mean) 
    print("var= ", variance)
    print("std= ",std)
    print("n= ", n)  
    print("sem = ", sem)
    print("var_m= ", sem * sem )
def confidenceInterval(q, df, mean, std):
    std_mean = std_m(std, df+1)
    t_a2_df = stats.t.ppf(q=(1-q)/2+q,df=df)
    # print("t_a2_df= ", t_a2_df) 
    l = mean - t_a2_df * std_mean
    u = mean + t_a2_df * std_mean
    confidenceLevel = np.array([l,u])
    np.set_printoptions(precision=3)
    print("Confidence Interval (t) of ", q," = ", confidenceLevel)
def confidenceIntervalNorm(q, df, mean, std):
    std_mean = std_m(std,df+1)
    z_a2_df = stats.norm.ppf(q=(1-q)/2+q)
    print("z_a2_df=%.3f " % z_a2_df) 
    l = mean - z_a2_df * std_mean
    u = mean + z_a2_df * std_mean
    confidenceLevel = np.array([l,u])
    np.set_printoptions(precision=3)
    print("Confidence Interval (normal) of ",q," = ", confidenceLevel)
def t(mean, m0, std, n):
    t = ( mean-m0 ) / ( std / math.sqrt(n) )
    print("t=%.3f" % t)
    return ( mean-m0 ) / ( std / math.sqrt(n) )
def hypothesis( a, mean, m0, std,  n):
    t_value = t(mean, m0, std, n)

    if ( mean-m0 > 0 ):
        t_crit = stats.t.ppf( (1-a), n-1 ) 
        print("t_crit=%.3f" % t_crit)

        if t_value < t_crit :
            print("H0 is approved")
        else:
            print("Ha is approved")
    else:
        t_crit = stats.t.ppf( (a), n-1 ) 
        print("t_crit=%.3f" % t_crit)

        if t_value > t_crit :
            print("H0 is approved")
        else:
            print("Ha is approved")
def hypothesis_norm( a, mean, m0, std,  n):
    z_value = t(mean, m0, std, n)

    if ( mean-m0 > 0 ):
        z_crit = stats.norm.ppf( (1-a) ) 
        print("z_crit=%.3f" % (z_crit))

        if z_value < z_crit :
            print("H0 is approved")
        else:
            print("Ha is approved")
    else:
        z_crit = stats.t.ppf( (a), n-1 ) 
        print("z_crit=%.3f" % (z_crit))

        if z_value > z_crit :
            print("H0 is approved")
        else:
            print("Ha is approved")

def Sp(S1 , n1, S2, n2 ):
    S_var_p = ( (n1-1)* pow(S1,2) + (n2-1)* pow(S2,2) ) / (n1+n2-2)
    print("S^2p = ", S_var_p)
    Sp = math.sqrt(S_var_p)
    print("Sp =", Sp)
    return Sp
# functions---------------------------------------------------------
# fi function
def frequency(data, bins):
    # work with local sorted copy of bins for performance
    bins = bins[:]
    bins.sort()
    freqs = [0] * (len(bins)+1)
    for item in data:
        for i, bin_val in enumerate(bins):
            if item <= bin_val:
                freqs[i] += 1
                break
        else:
            freqs[len(bins)] += 1
    return freqs

# Python program to count the frequency of
# elements in a list using a dictionary 
def CountFrequency(my_list):
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print ("% d : % d"%(key, value)) 
# Driver function
if __name__ == "__main__":
    my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
 
    CountFrequency(my_list)

#freq of specified range. From stackOF answers. I don'to use it
def freq(arr, min_n, max_n):
    return (
        len(arr) -
        next((j for j in range(len(arr)) if arr[j] >= min_n), len(arr)) - #next returns the next item in an iterator #len(arr) is default of next()
        next((j for j in range(len(arr)) if arr[len(arr) - j - 1] <= max_n), len(arr)) 
    ) / len(arr)