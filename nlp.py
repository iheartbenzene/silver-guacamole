def read(fname):
	With open(fname, 'r') as f:
		contents = f.readlines()
	return contents
