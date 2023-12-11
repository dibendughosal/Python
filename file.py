file = open("even_odd.txt","rt") 
for i in file: 
    if i.strip: 
        num = int(i) 
        if (num % 2 == 0): 
            even = open("even.txt","a") 
            even.write(str(num)) 
            even.write("\n") 
        else: 
            odd = open("odd.txt","a") 
            odd.write(str(num)) 
            odd.write("\n") 