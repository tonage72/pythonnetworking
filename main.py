import os


def main():
    user = os.environ.get('USERNAME', 'devuser')
    print(user)

if __name__ == '__main__':
    main()