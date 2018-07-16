from bs4 import *
import requests
class Parser:
    def __init__(self, filename):
        self.filename = filename
        print("GET " + self.filename)
        self.contents = requests.get(self.filename).text
    def refresh(self):
        print("refreshing content")
        print("GET " + self.filename)
        self.contents = requests.get(self.filename).text
    def extract(self):
        self.soup = BeautifulSoup(self.contents, 'html.parser')#We parse the contents by calling beautiful soup constructor
        # print(self.soup.)
    def search(self, tag_name, attr):
        for tag in self.soup.find_all(True):
            if tag.name == tag_name:
                # print(tag.name, tag.attrs)
                found = True
                for key in attr.keys():
                    if key not in tag.attrs.keys():
                        found = False
                        break
                    if type(tag[key]) is list:
                        tag[key].sort()
                        attr[key].sort()
                        # print(tag[key], attr[key], tag[key] == attr[key])
                    if tag[key] != attr[key]:
                        found = False
                        break
                if found is True:
                    # print("success")
                    # print(tag.attrs, attr)
                    print("for tag name : " + tag.name + " " + str(tag.contents))
                    return tag
    def searchChild(self, parent_tag, tag_name, attr):
        for child in parent_tag.children:
            # print(child.name)
            if child.name == tag_name:
                # print(child.name, child.attrs)
                found = True
                for key in attr.keys():
                    if key not in child.attrs.keys():
                        found = False
                        break
                    if type(child[key]) is list:
                        child[key].sort()
                        attr[key].sort()
                        # print(child[key], attr[key], child[key] == attr[key])
                    if child[key] != attr[key]:
                        found = False
                        break
                if found is True:
                    # print("success")
                    # print(child.attrs, attr)
                    print("for tag name : " + child.name + " " + str(child.contents))
                    return child
    def searchChildren(self, parent_tag, tag_name, attr):
        children = []
        for child in parent_tag.children:
            # print(child.name)

            if child.name == tag_name:
                # print(child.name, child.attrs)
                found = True
                for key in attr.keys():
                    if key not in child.attrs.keys():
                        found = False
                        break
                    if type(child[key]) is list:
                        child[key].sort()
                        attr[key].sort()
                        # print(child[key], attr[key], child[key] == attr[key])
                    if child[key] != attr[key]:
                        found = False
                        break
                if found is True:
                    # print("success")
                    # print(child.attrs, attr)
                    print("for tag name : " + child.name + " ")
                    print(child.contents)
                    children.append(child)
        return children


