data = "Welcome to my website"
file = open("hello.txt",'w')
file.write(data)
file.close()

data = "\nwelcome to my website. This data is being amended to the hello.txt file"
file = open("hello.txt", 'a')
file.write(data)
file.close()