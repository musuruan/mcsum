#!/usr/bin/python3

import os
import sys
import argparse

def main():
	parser = argparse.ArgumentParser(description='Print MC checksum data from a C64 basic file')
	parser.add_argument('filename', metavar='filename', nargs='?', help='C64 basic file')
	args = parser.parse_args()
	filename = args.filename

	if not filename:
		parser.print_help()
		sys.exit(1)

	if not os.path.isfile(filename):
		print("Cannot find file '{0}'".format(filename));
		sys.exit(1)

	with open(filename, "rb") as f:
		loadAddr = f.read(2)
		loadAddr = int.from_bytes(loadAddr, byteorder='little', signed=False)
		print("{0} === {1} ({2}) ===".format(filename, hex(loadAddr), loadAddr))

		currAddr=loadAddr

		ptrNextLine = f.read(2)
		ptrNextLine = int.from_bytes(ptrNextLine, byteorder='little', signed=False)

		while ptrNextLine !=0:
			lineNum = f.read(2)
			checksum = lineNum[0]+lineNum[1]
			lineNum = int.from_bytes(lineNum, byteorder='little', signed=False)

			for i in range(3, ptrNextLine - currAddr - 1):
				byte = f.read(1)
				checksum = checksum + byte[0]
			print("{0}: {1}".format(lineNum, checksum))

			currAddr=ptrNextLine
			ptrNextLine = f.read(2)
			ptrNextLine = int.from_bytes(ptrNextLine, byteorder='little', signed=False)


if __name__ == "__main__":
	main()

