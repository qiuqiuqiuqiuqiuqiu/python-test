#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.sax
from xml.dom.minidom import parse
import xml.dom.minidom


# parse xml by sax
class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print "****Movie****"
            title = attributes["title"]
            print "Title:", title

    def endElement(self, tag):
        if self.CurrentData == "type":
            print "Type:", self.type
        elif self.CurrentData == "format":
            print "Format:",self.format
        elif self.CurrentData == "year":
            print "Year:", self.year
        elif self.CurrentData == "rating":
            print "Rating:", self.rating
        elif self.CurrentData == "stars":
            print "Stars:", self.stars
        elif self.CurrentData == "description":
            print "Description:", self.description
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


if __name__ == "__main__":
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("../../resources/movies.xml")


# parse xml by dom
DOMTree = xml.dom.minidom.parse("../../resources/movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print "Root element: %s" % collection.getAttribute("shelf")

movies = collection.getElementsByTagName("movie")

for movie in movies:
    print "****Movie****"
    if movie.hasAttribute("title"):
        print "Title: %s" % movie.getAttribute("title")
    type = movie.getElementsByTagName('type')[0]
    print "Type: %s" % type.childNodes[0].data
