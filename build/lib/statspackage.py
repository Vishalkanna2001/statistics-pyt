def sum(a):
    return a[0]+a[1]+a[2]+a[3]+a[4]
def mean(t,n):
    return (t/n)
def median(a,n):
    if n%2==0:
        median1=a[n//2]
        median2=a[n//2-1]
        median=(median1+median2)/2
    else:
        median=a[n//2]
    return median
def mode(a,n):
    freq={}
    for n in a:
        freq.setdefault(n,0)
        freq[n]+=1
        mode=max(freq.values())

    return mode
