def connect(host,port=3306,protocal='tcp'):
    print(f"host={host},port={port},protocal={protocal}")

connect("localhost")   
connect("localhost",8000)