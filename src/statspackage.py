def mean(t,n):                       #mean is used to find the average of given numbers
    return (t/n)                     #t is the sum of given numbers and n is the no. of inputs
def median(a,n):                    # median is used to find the middle value of the list
    if n%2==0:                      #this condition is used when the given inputs are even
        median1=a[n//2]
        median2=a[n//2-1]
        median=(median1+median2)/2
    else:                            #this condition is used when the given inputs are odd
        median=a[n//2]
    return median
def mode(a,n):                        #mode is used to find the most repeated value and return the number of times the value is present
    freq={}
    for n in a:
        freq.setdefault(n,0)
        freq[n]+=1
        mode=max(freq.values())

    return mode
