# Short exercise: Rewrite the histogram function on page 105 while using the
# get method. It should allow us to remove the if/else statements.

def histogram(s):
    d = dict()
    for c in s:
        cache = d.get(c, 0) + 1
        d[c] = cache
    return d

if __name__=='__main__':
    print(histogram('brontosaurus'))