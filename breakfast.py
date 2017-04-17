def make_breakfast(food):
    print('Get the ingredients')
    print('Mix')
    print('Pour into the heated pan')
    print('Flip it to the other side')
    breakfast = '---YUMMY TASTY {}---'.format(food)
    print(breakfast)


def main():
    make_breakfast('eggs')

if __name__ == '__main__':
    main()