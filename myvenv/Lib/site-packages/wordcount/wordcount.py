
import argparse
import os



parser = argparse.ArgumentParser(description='Get Word Count from file')
parser.add_argument('--infile',help="Enter the Name of Input File")
parser.add_argument('--outfile',help="Enter the Name of Output File")
args = parser.parse_args()
infile,outfile = None, None


class WordCount:
	'''
	Use the class WordCount passing arguments input filename and output filename
	'''
	def __init__(self, in_filename, out_filename):
		self.in_filename = in_filename
		self.out_filename = out_filename

	def get_count(self):
		data = {}
		with open(self.in_filename) as f:
			for line in f.readlines():
				for item in line.split():
					data[item] = data.get(item,0) + 1
		return data

	def write_text(self, data):
		with open(self.out_filename,"w") as f:
			f.write("Key \t \t \t Count\n")
			f.write("====================\n")
			for key, value in data.items():
					f.write("%s \t\t\t %s \n" %(key, value))

def main():	
	if args.infile:
		in_file = args.infile
	else:
		raise "Input File is Required"
	if args.outfile:
		out_file = args.outfile
	else:
		out_file = "output.txt"
	word = WordCount(in_file, out_file)
	datas = word.get_count()
	word.write_text(datas)

if __name__ == "__main__":
	main()

