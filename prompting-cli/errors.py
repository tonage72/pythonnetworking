
def main():
    try:
        f = open('./some-text.txt')
        lines = f.readlines()
        print(lines)
    except FileNotFoundError as e:
        print('Hey, that file is not there')
    except Exception as e:
        print("Error encountered: {}".format(e))
    finally:
        print('finally is running')
        f.close()

if __name__ == "__main__":
    main()