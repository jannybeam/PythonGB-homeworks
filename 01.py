import sys

if len(sys.argv) < 5:
    print(f'Enter paramrters (output, rate, premium)')
else:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    result = a * b * c
    print(result)