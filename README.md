# tkinter_weather_app
this is a python desktop app made using tkinter for GUI and beautiful soup for web scraping. The data is collected from weather.com

API documentation for Parser class (beautiful_soup_wrapper.py)
Parser(filename)
  this is the constructor for the Parser class. It takes web address for eg. https://github.com, https://stackoverflow.com, and so on.For now an instance of this class can only handle content of one page.
refresh()
  this is the method that refreshes the content of the buffer of the html held by the object. If you have to reload a link due to data change(for eg. in real time data like weather, score, etc.) then you can make use of it. <b>It takes no parameters.</b>
extract()
  this method calls the BeautifulSoup Constructor on the data recieved by the requests.get() function.It takes no parameters
search(tag_name, attr)
  this method takes as parameters:
  1.tag_name: the tag name which you want to search
  2.attr: a dict object holding any attribute values of the tag. This is used for further filtering 
  It returns a tag
searchChild(parent, tag_name, attr)
  this pretty much does the same thing as the method above. Except, this method looks for children tags of a tag <i>parent</>. It returns the first match as a tag
searchChildren(parent, tag_name, attr)
  The onlu difference between searchChild and searchChildren is searchChildren returns a list of tags matching tag_name and attributes in <i>parent's</i> children whereas searchChild returns the first found match.
  
Example
  p = Parser("https://stackoverflow.com")
  p.extract()
  tag = p.search("head", {}) #search for <head> tag in the HTML
  print(tag.contents)#print contents of the <head> tag
  
  any feedback appreciated.
