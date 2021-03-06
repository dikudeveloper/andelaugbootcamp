import time


def generate_prime_numbers(n):
    """Function generates prime numbers from 0 to n Asymptotically"""
    if isinstance(n, int) and n > 1:
        not_prime = []
        prime = []
        for i in range(2, n + 1):
            if i not in not_prime:
                prime.append(i)
                for j in range(i * i, n + 1, i):
                    not_prime.append(j)
        return prime


def main():
    # Testing Function generate_prime_numbers(n)
    print(generate_prime_numbers(12))

    # Asymptotic Tests -- Please find output in file on my Github repo
    # https://github.com/dikudeveloper/andelaugbootcamp
    for primenumsize in range(1000, 100001, 10000):
        start = time.time()
        generate_prime_numbers(primenumsize)
        end = time.time()
        print('size: %d time: %f' % (primenumsize, end-start))

if __name__ == '__main__':
    main()