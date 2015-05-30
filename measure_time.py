__author__ = 'ubuntu'

import timeit

scripts = [multiply_my_way, multiply_with_numpy]

if __name__ == '__main__':
    for script in scripts:
        import_command = "from " + str(script.__name__) + " import main"
        t = timeit.Timer("main()", import_command)
        print("Multiply with " + str(script.__name__) + ":  " + str(round(t.timeit(1), 4)) + "s")