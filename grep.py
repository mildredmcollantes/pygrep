import argparse
import re
import glob


def main(options):
    regex = options.regex
    file = options.filepattern
    filepath = options.dir

    for name in glob.glob('{}/{}'.format(filepath,file), recursive=True):
        with open(name) as infile:
            for line in infile:
                try:
                    if re.search(regex,line).group():
                        print(line)
                except Exception as ex:
                    continue


def _get_args():
    parser=None
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("regex", help="regex pattern")
        parser.add_argument("filepattern", help="file pattern")
        parser.add_argument("dir", help="path to search")
    except Exception as ex:
        print("[ERROR] Error getting arguments {}".format(ex))
    finally:
        return parser


if __name__ == "__main__":
    options = _get_args().parse_args()
    if options:
        main(options)