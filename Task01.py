#import webbrowser
f = open('table.html','w')
n = 10
table = [[(str(i) + " * " + str(j) + " = " + str(i * j)) for j in range (1, n + 1)] for i in range (1, n + 1)]
begin = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="windows-1251">
    <title>Таблица умножения</title>
    <h1>Таблица умножения</h1>
</head>
<body>
"""
middle = ""
for row in table:
    for elem in row:
          middle += "\t" + "<p>" + elem + "</p>" + "\n"
end = """</body>
</html>
"""
f.write(begin + middle + end)
f.close()
#webbrowser.open_new_tab('table.html')
