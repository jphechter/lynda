def main():
    s = 'this is a string'
    for c in s:
        if c == 's': continue
        print(c, end='')

if __name__ == "__main__": main()