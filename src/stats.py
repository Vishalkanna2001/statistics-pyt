def sum(a):
    return a[0]+a[1]+a[2]+a[3]+a[4]
def mean(t,n):
    return (t/n)
def meadian(a,n):
    if n%2==0:
        meadian1=a[n//2]
        meadian2=a[n//2-1]
        meadian=(meadian1+meadian2)/2
    else:
        meadian=a[n//2]
    return meadian
def mode(a,n):
    freq={}
    for n in a:
        freq.setdefault(n,0)
        freq[n]+=1
        mode=max(freq.values())

    return mode
