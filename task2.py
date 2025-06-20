file = open("Python/Tutedude/Assignment_4/output.txt" , "w")
file.write(input("Enter text to the file: "))
print("Data successfull written to output.txt." )
file.close()

with open("Python/Tutedude/Assignment_4/output.txt","a") as file :
    file.write("\n"+input("Enter additional text to append: "))
    print("Data successfully appended." )

with open("Python/Tutedude/Assignment_4/output.txt","r") as file :
    print("Final content output.txt :")
    for l in file.readlines():
        print(l,end="")

