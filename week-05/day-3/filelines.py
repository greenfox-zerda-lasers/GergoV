# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def filelines(filename):
    try:
        f = open(filename, 'r')
        ln = 0
        for line in f:
            ln += 1
        print("No. of lines:", ln)
    except FileNotFoundError:
        # print(0)
        return 0
