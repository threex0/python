import sys
if len(sys.argv) == 1:
	filename = "index.html"
else:
	filename = sys.argv[1]
text_file = open(filename, "w")
text_file.write("<DOCTYPE html>\n"
"\t<!--File made by HTML writer by Robert Marin http://designeragents.com-->"
"\t<head>"
"\t</head>"
"\t<body>"
"<b>Hello, World.</b>"
"\t</body>"
"</html>")
text_file.close()
