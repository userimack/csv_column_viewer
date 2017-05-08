#!/usr/bin/env python3

import csv
import os
import sys
import traceback
from optparse import OptionParser


def viewer(filename, columns, delimit):
    with open(filename) as robj:
        csvreader = csv.reader(robj, delimiter=delimit)
        for line in csvreader:
            try:
                columns_list = [int(x) for x in columns.split(" ")]  # list(map(int, columns.split(" ")))
                for column in columns_list:
                    print(line[column], end=',')
                print("\n", end='')
            except (BrokenPipeError, IOError):
                pass
            except Exception as e:
                print(traceback.format_exc())


if __name__ == "__main__":
    parser = OptionParser()
    parser.set_defaults(delimiter=',')
    parser.add_option("-f", "--file", help="Input CSV file", action="store", dest="input_file")
    parser.add_option("-c", "--columns", help="Column numbers to extract", action="store", dest="columns")
    parser.add_option("-d", "--delimiter", help="CSV file delimiter", action="store", dest="delimiter")
    (options, args) = parser.parse_args(sys.argv)
    if options.input_file is None or options.columns is None:
        parser.error("Incorrect number of argumens supplierd\nRun as \n$ python3 filename.py -f file.csv -c 1 2 3\nor\n$ pyhton3 filename.py --file file.csv --columns 1 2 3 \nNote: If you want you can give delimiter explicitly using the -d or --delimiter (default delimiter is  ',') ")
        sys.exit(1)
    else:
        if not os.path.isfile(options.input_file):
            print("Error: File {0} doesn't  exists!!".format(options.input_file))
            sys.exit(1)
        else:
            print("file: {}, Columns: {}, delimiter:{}".format(options.input_file, options.columns, options.delimiter))
            viewer(options.input_file, options.columns, options.delimiter)

            sys.stderr.close()
