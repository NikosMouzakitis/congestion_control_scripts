def process_stage1(input_f,output_f):
	with open(input_f,’r’) as infile, open(output_f, “w”) as outfile:
		lines = infile.readlines() #read all of lines.
		i = 0
		while(i < len(lines) - 1):
			line = lines[i] #fetch one line.
			
			if ‘tcp’ in line and (‘42024’ in line or ‘42026’ in line or ‘42028’ in line):
				concat_line=line.strip() + “ “ + lines[i+1].strip() + “\n”
				outfile.write(concat_line)
				i+=1 #increment because we fetch the next line.
			i+=1 #original incrementation in the loop manner.

process_stage1(“sender-ss.txt”,”stage1.txt”)

