
def bigger_Is_greater(w):
    result = ''
    n = len(w)
    w = list(w)
    i=n-2
    

    while i >= 0 and w[i] >= w[i+1]:
        i-=1

    if i == -1:
        result = "no answer"
    else:   
        d = n-1
        while d >= i and w[d] <= w[i]:
            d-=1

        w[i], w[d] = w[d], w[i]
        w="".join(w)
        result = w[:i + 1] + w[i + 1:][::-1]
