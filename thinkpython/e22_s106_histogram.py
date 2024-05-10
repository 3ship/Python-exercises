# Short exercise: Rewrite the histogram function on page 105 while using the
# get method. It should allow us to remove the if/else statements.

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

if __name__=='__main__':
    print(histogram('brontosaurus'))