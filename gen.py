from random import randint

original = "Rick Sanchez"

def leeter(letter):
    a = ['a','A','4','@']
    b = ['b','B','6','8']
    c = ['c','C']
    d = ['d','D']
    e = ['e','E','3','€','eE']
    f = ['f','F']
    g = ['g','G','9']
    h = ['h','H','#','1-1']
    i = ['i','I','!','ii']
    j = ['j','J']
    k = ['k','K']
    l = ['l','L','%']
    m = ['m','M']
    n = ['n','N']
    o = ['o','O','0',"o0"]
    p = ['p','P','?']
    q = ['q','Q']
    r = ['r','R','rR','RR']
    s = ['s','S','$','5']
    t = ['t','T']
    u = ['u','U']
    v = ['v','V']
    w = ['w','W']
    x = ['x','X','*','+']
    y = ['y','Y']
    z = ['z','Z']
    SPACE = ['-','_']
    dico = {'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,'x':x,'y':y,'z':z}
    randchar = ['§','&']
    try:
        candidate = dico[letter]
        return candidate[randint(0,len(candidate)-1)] 
    except:
        return randchar[randint(0,len(randchar)-1)]

fname = "rick_and_morty"
f = open(fname,"r")
lines = f.read().splitlines() 

origin = lines[randint(0,len(lines)-1)]

mdp = ""
for c in origin:
    mdp += leeter(c.lower())

print(mdp)
f.close()
