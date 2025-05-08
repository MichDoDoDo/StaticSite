import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_htmlnode_props(self):
        testdict = {
        "href": "https://www.google.com",
        "target": "_blank",}
        
        node = HTMLNode(None,None,None,testdict)
        teststr = node.props_to_html()
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")
        
        self.assertNotEqual(node.props_to_html(), "href=\"https://www.google.com\" target=\"_blank\"")
        
    def test_repr(self):
        node = HTMLNode(None,None,None,None)
        self.assertEqual(repr(node),"HTMLNode(None,None,None,None)")
        
    def test_to_html(self):
        node = HTMLNode(None,None,None,None)
        with self.assertRaises(NotImplementedError):
            node.to_html()        

class TestLeafNode(unittest.TestCase):
    def test_to_html_no_props(self):
        node = LeafNode("p", "This is a paragraph of text.").to_html()
        self.assertEqual(node, "<p>This is a paragraph of text.</p>")
        
    def test_to_html_props(self):
        dicttest = {"href": "https://www.youtube.com"}
        node = LeafNode("a", "Click me!", dicttest).to_html()
        self.assertEqual(node,"<a href=\"https://www.youtube.com\">Click me!</a>")
        
class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],)
        result = node.to_html()
        self.assertEqual(result,"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")