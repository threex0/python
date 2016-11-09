# Create nice neatly little formatted HTML documents so I can stop creating them myself.

# Santa's Wishlist.
import sys

# Define a quick prompt function.
def prompt_yn(string):
	yesno = input(string + "(Y, N):\t")
	if (yesno == 'y' or yesno == 'Y'):
		return 1
	elif (yesno == 'n' or yesno == 'N'):
		return 0
	else:
		prompt_yn(string)

def newline(string):
	return "\n"
	
def tab(string,int):
	return ("\t" * int) + string
		
# Default directory this file works in
dir = "output/"
strings_dir = "strings/"

# Allow an argument to create a filename.
# Otherwise creates an index.html file.
if len(sys.argv) == 1:
	file_path = dir + "index.html"
else:
	file_path = dir + sys.argv[1]
	
# File ops
text_file = open(file_path, "w")
html_header=open(strings_dir + "html5header.txt", "r")

# Keep Count of tabs
tabcount = 0

# Header block
# Todo:  Make into an off-script string.
text_file.write(html_header.read())
html_header.close()

# Include Bootstrap?
# Todo:  Make an argument
# Todo:  Make into an off-script string.
boots_string = open(strings_dir + "bootstrap.txt","r")
if(prompt_yn("Include Bootstrap? ")):
	text_file.write(boots_string.read())
boots_string.close()
	
# Close Head.
text_file.write("\n\t</head>\n"

# Write the body
"\t<body>\n"
"\t</body>\n"

# Write the HTML
"</html>")
text_file.close()
