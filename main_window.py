from tkinter import *
from beautiful_soup_wrapper import Parser

root = Tk()

p = Parser("https://weather.com/weather/today/l/INXX0012:1:IN")
p.extract()
tag = p.search("div", {'class' : ['today_nowcard-sidecar', 'component', 'panel']})
tag = p.searchChild(tag, "table", {})
tag = p.searchChild(tag, "tbody", {})
tags = p.searchChildren(tag, "tr", {})
data = {}
for tag in tags:
    th = p.searchChild(tag, "th", {})
    td = p.searchChild(tag, "td", {})
    span = p.searchChild(td, "span", {})
    if th.contents[0] == 'Humidity':
        span = p.searchChild(span, "span", {})
    data[th.contents[0]] = span.contents[0]

print(data)
for key in data.keys():
    value = data[key]
    Label(root, text = key + ' : ' + value).pack(side=LEFT)


root.mainloop()