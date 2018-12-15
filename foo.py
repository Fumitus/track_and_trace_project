import argparse

def main(passed_args=None):
    parser = argparse.ArgumentParser(description='test')
    parser.add_argument('--all', '-a', action='store_true', help='all')
    args = parser.parse_args(passed_args)

    if args.all:
        pass

if __name__ == '__main__':
    main()
  