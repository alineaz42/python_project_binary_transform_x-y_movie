'''
Name: Ali Neaz
B.Sc(Hon's) in statistics at Islamic University,Kushtia,Bangladesh
'''
def transform(p):
    for i in range(len(p)-1):
        if p[i]== '1':
            p[i]="0"
            if p[i+1]=="0":
                p[i+1]="1"
            else:
                p[i+1]="0"
    return p

if __name__ == "__main__":
    a = list("111010111000101")
    print(a)
    while a!= transform(a.copy()):
        a = transform(a.copy())
    print(a)

