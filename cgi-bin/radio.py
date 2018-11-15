#!/usr/bin/python
import cgi,cgitb

form = cgi.FieldStorage()

if(form.getvalue("gender")):
	gen = form.getvalue("gender")


print("Content-type:text/html \n")
print("<html>")
print("<body>")
print("<h2>Gender selected : "+gen+"</h2>")
print("</body></html>")
# print("</html>")