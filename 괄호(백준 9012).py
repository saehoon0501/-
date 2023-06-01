
n = int(input());
ps = [list(map(str, input())) for _ in range(n)];

def checkVps(ps):    
    for p in ps:
        count = 0;        
        for s in p:            
            if s == "(":
                count += 1;
            else:
                count -= 1;
            if count < 0:                
                break;

        if count == 0:
            print("YES");
        else:
            print("NO");

checkVps(ps);