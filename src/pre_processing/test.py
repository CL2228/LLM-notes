

if __name__ == '__main__':
    print("this is a preprocessing directory")

    a = [i for i in range(20)]
    for i in range(0, len(a) - 4, 1):
        print(i)
        # i=15
        print(a[i: i + 4])
        print(a[i + 1: i + 1 + 4])
