# tkinter_weather_app
this is a python desktop app made using tkinter for GUI and beautiful soup for web scraping. The data is collected from weather.com
<br><br>
<br>API documentation for Parser class (beautiful_soup_wrapper.py)<br>
<br>Parser(filename)
  <br>this is the constructor for the Parser class. It takes web address for eg. https://github.com, https://stackoverflow.com, and so on.For now an instance of this class can only handle content of one page.
<br><br>refresh()
  <br>this is the method that refreshes the content of the buffer of the html held by the object. If you have to reload a link due to data change(for eg. in real time data like weather, score, etc.) then you can make use of it. <b>It takes no parameters.</b>
<br><br>extract()
  <br>this method calls the BeautifulSoup Constructor on the data recieved by the requests.get() function.It takes no parameters
<br><br>search(tag_name, attr)
  <br>this method takes as parameters:
  <br>  1.tag_name: the tag name which you want to search
  <br>  2.attr: a dict object holding any attribute values of the tag. This is used for further filtering 
  <br>It returns a tag
<br><br>searchChild(parent, tag_name, attr)
  <br>this pretty much does the same thing as the method above. Except, this method looks for children tags of a tag <i>parent</>. It returns the first match as a tag
<br><br>searchChildren(parent, tag_name, attr)
  <br>The onlu difference between searchChild and searchChildren is searchChildren returns a list of tags matching tag_name and <br>attributes in <i>parent's</i> children whereas searchChild returns the first found match.
<br><br>  
<br>Example
  <br>p = Parser("https://stackoverflow.com")
  <br>p.extract()
  <br>tag = p.search("head", {}) #search for <head> tag in the HTML
  <br>print(tag.contents)#print contents of the <head> tag
  <br>
  <br>any feedback appreciated.
