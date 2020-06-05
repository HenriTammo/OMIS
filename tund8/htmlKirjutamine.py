file = open("tund8/näide.html", "w")

ülemine = """<html>
<head></head>
<body><p>"""
sisestus = input("ütle midagi")
alumine = """</p></body>
</html>"""

file.write(ülemine)
file.write(sisestus)
file.write(alumine)
file.close()