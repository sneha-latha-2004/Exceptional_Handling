try:
    f = open("sample.txt", "r")
    print(f.read())
except:
    print("File not found")
finally:
    print("This will always execute")