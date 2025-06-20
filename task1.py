try:
    with open('Python/Tutedude/Assignment_4/sample.txt', 'r') as file1 :
       
        for l in file1.readlines():
            print(l, end='')

    
    
except FileNotFoundError :
    print(f"The file 'sample.txt' was not found")

    