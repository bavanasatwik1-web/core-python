# with open('Transction.txt','w') as t:
#     t.write('user_id,amount,category\n')
#     t.write('U1,100,food\n')
#     t.write('U2,-50,shopping\n')
#     t.write('U3,200,travel\n')
#     t.write('U4,abc,food\n')
#     t.write('U5,300,shopping\n')
#     t.write('U6,120,food\n')
#     t.write('U7,,travel\n')
#     t.write('U8,450,electronics\n')

with open("Transction.txt","r")as t,open("clean.txt","w")as c,open("error.txt","w")as err:
    t.readline()
    total_lines = 0
    clean_lines = 0
    error_lines = 0
    total_amount = 0
    cat_amount={}
    for line in t:
        total_lines+=1
        u,a,cat=line.split(",")
        try:    
            if cat=="" or a=="" or u=="":
                raise ValueError("cannot have empty values")
            a=int(a)
            if a<0:
                raise ValueError
            c.write(line)
            clean_lines+=1
            total_amount+=a
            cat_amount[cat]=cat_amount.get(cat,0)+a
        except ValueError as e:
            error_lines+=1
            err.write(f"{line}-->{e}\n")
            err.flush
with open("report.txt","w")as r:    
    r.write(f"{total_lines}lines has clean lines\n")    
    r.write(f"{clean_lines}lines has processed\n")
    r.write(f"{error_lines}lines error\n")
    r.write(f"total_amount={total_amount}\n")

