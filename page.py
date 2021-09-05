a='a'
while a!='':
    a=input('> ')
    if a!='':
        try:
            d=open(f'docs/pages/{a}.html','x')
        except FileExistsError:
            print('File already exists!')
        else:
            d=open(f'docs/pages/{a}.html','a')
            d.write(f'''<!doctype html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8" http-equiv="refresh" content="0; URL={a}.html">
    <link rel="icon" href="../images/celebi.png">
    <title>{a} | Celebi</title>
    <style>@import url("../styles/index.css");</style>
  </head>
  <body>
    <h1>{a}</h1>
    <img src="https://gpvc.arturio.dev/{a}">
  </body>
</html>''')
            d.close()
            d=open('docs/index.html','a')
            d.write(f'''<!--
<li><img src="https://gpvc.arturio.dev/{a}" height="16px"> - <a href="pages/{a}.html" target="_blank" rel="noopener noreferrer">{a}</a></li>
-->\n''')
            print(f'Created {a}.html')
        print('')
