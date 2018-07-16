from tkinter import *
from beautiful_soup_wrapper import Parser
#this is the custom frame class
class CustomFrame(Frame):
    def __init__(self, title, row, column, parent=None):
        Frame.__init__(self, parent)
        self.grid(row = row, column = column)
        self.title = title
        #set frame state variables
        self.state = 42

        self.p = Parser("https://weather.com/weather/today/l/INXX0012:1:IN")
        self.p.extract()

        self.widgets = []
        self.make_widgets()

    def refresh_data(self):
        self.p.refresh()
        self.make_widgets()

    def make_widgets(self):
        for widget in self.widgets:
            widget.pack_forget()
        tag = self.p.search("div", {'class' : ['today_nowcard-sidecar', 'component', 'panel']})
        tag = self.p.searchChild(tag, "table", {})
        tag = self.p.searchChild(tag, "tbody", {})
        tags = self.p.searchChildren(tag, "tr", {})
        data = {}
        for tag in tags:
            th = self.p.searchChild(tag, "th", {})
            td = self.p.searchChild(tag, "td", {})
            span = self.p.searchChild(td, "span", {})
            if th.contents[0] == 'Humidity':
                span = self.p.searchChild(span, "span", {})
            data[th.contents[0]] = span.contents[0]

        print(data)
        for key in data.keys():
            value = data[key]
            self.widgets.append(Label(self, text = key + ' : ' + value))
            self.widgets[-1].pack(side=LEFT)
        refresh = Button(self, text = "refresh", command = self.refresh_data)
        refresh.pack()
        self.widgets.append(refresh)
