#!/usr/bin/env python
# coding: utf-8

import cgi
from datetime import datetime

html_body = """
<html><head>
    <meta http-equiv="content-type"
          content="text/html;charset=utf-8">
  </head>
  <body>
  {:s}
  </body>
</html>"""

content = ''

form = cgi.FieldStorage()
year_str = form.getvalue('year', '')
if not year_str.isdigit():
    content = "西暦を入力してください"
else:
    year = int(year_str)
    friday13 = 0
    for month in range(1, 13):
        date = datetime(year, month, 13)
        if date.weekday() == 4:
            friday13 += 1
            content += "{:d}年{:d}月13日は金曜日です".format(year, date.month)
            content += "<br />"

    if friday13:
        content += "{:d}年には合計{:d}個の13日の金曜日があります".format(year, friday13)
    else:
        content += "{:d}年には13日の金曜日がありません"

print("Content-type: text/html;charset=utf-8\n")
print(html_body.format(content).encode('utf-8'))
