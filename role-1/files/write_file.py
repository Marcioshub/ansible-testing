import sys

# Access command line arguments
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]

f = open("/home/pi/new_file.txt", "a")
f.write("Now the file has more content!\n")
f.write(arg1 + "\n")
f.write(arg2 + "\n")
f.write(arg3 + "\n")
f.close()
