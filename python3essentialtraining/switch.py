def main():
    choices = dict(
        one = 'first',
        two = 'second',
        three = 'third'
    )
    v = 'one'
    print(choices.get(v, 'other'))

if __name__ == "__main__": main()