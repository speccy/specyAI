p_data= input(">> ")

#lines = [line.split() for line in f]
while p_data != 'exit':

    with open("./data/db", "r+") as f:
        #flag is false by default
        is_matched = False
         
        for line in f:
            if p_data.lower() == line.split()[0].lower():
                print(line.split()[1])
                #set flag to true so input not recognised wont print
                is_matched = True
        
        if is_matched != True:
                #in any case that is not matched, flag will be false
                print("Input not recognised")
        
        p_data = input(">> ")
