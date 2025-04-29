def save(filename,data):
    with open (filename,"a")  as file:
        output =  file.write(f"{data}\n")
        


