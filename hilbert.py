import sys, math

def hilbert(x0, y0, xi, xj, yi, yj, n):
    if n <= 0:
        X = x0 + (xi + yi)/2
        Y = y0 + (xj + yj)/2

        #Outputs the coordinates of the cv
        print("%s %s 0" % (X, Y))

    else:
        hilbert(x0,                 y0,                   yi/2, yj/2, xi/2, yj/2, n - 1)
        hilbert(x0 + xi/2,          y0 + xj/2,            xi/2, xj/2, yi/2, yj/2, n - 1)
        hilbert(x0 + xi/2 + yi/2,   y0 + xj/2 + yj/2,     xi/2, xj/2, yi/2, yj/2, n - 1)
        hilbert(x0 + xi/2 + yi,     y0 + xj/2 + yj,      -yi/2,-yj/2,-xi/2,-xj/2, n - 1)

def main():
    args = sys.stdin.readline()

    #Remain in the loop until the renderer releases the helper function
    while args:
        arg = args.split()

        #Gets the inputs
        pixels = float(arg[0])
        ctype = arg[1]
        reps = int(arg[2])
        width = float(arg[3])

        #Calculating the number of curve cv's
        cvs = int(math.pow(4, reps))

        #Begin the curve statement
        print("Basis 'b-spline' 1 'b-spline' 1")
        print("Curves %s [%s] 'nonperiodic' 'P' [" % (ctype, cvs))

        #Calculate the curve
        hilbert(0.0, 0.0, 1.0, 0.0, 0.0, 1.0, reps)

        #End curve statement
        print("] 'constant width' %s" % width)

        #Tell the renderer we have finished
        sys.stdout.write('\377')
        sys.stdout.flush()

        #read the next set of inputs
        arg = sys.stdin.readline()

if __name__ == "__main__":
    main()
