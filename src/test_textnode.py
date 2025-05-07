import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        L_node = TextNode("this is text",TextType.ITALIC_TEXT) 
        R_node = TextNode("this is text",TextType.ITALIC_TEXT) 
        self.assertEqual(L_node, R_node)
        
        node_url_none = TextNode("this is text",TextType.ITALIC_TEXT) 
        self.assertEqual(node_url_none.url,None)
    
    def test_text_type_input(self):
        for type in TextType:
            if type == TextType.LINK:
                pass
            elif type == TextType.IMAGE:
                pass
            else :
                L_node = TextNode("this is some text", type)
                R_node = TextNode("this is some text", type)
                self.assertEqual(L_node.text_type, R_node.text_type)

    def test_text_input(self):
        L_node = TextNode("this is some text", TextType.BOLD_TEXT)
        R_node = TextNode("this is not some text", TextType.BOLD_TEXT)
        
        self.assertNotEqual(L_node.text, R_node.text)
        
        M_node = TextNode("this is some text", TextType.BOLD_TEXT)
        
        self.assertEqual(M_node.text, L_node.text)
        
    def test_URL(self):
        L_node = TextNode("this is some text", TextType.BOLD_TEXT,"https://www.youtube.com")
        R_node = TextNode("this is", TextType.BOLD_TEXT,"https://www.youtube.com")
        
        self.assertEqual(L_node.url, R_node.url)
        
        M_node = TextNode("this is some text", TextType.BOLD_TEXT,"https://www.youtube")
        
        self.assertNotEqual(M_node.url, L_node.url)
        
    def test_repr(self):
        node = TextNode("this is text",TextType.LINK,"https://www.boot.dev") 
        text = node.__repr__()
        self.assertEqual(text,"TextNode(this is text, link, https://www.boot.dev)")
    

if __name__ == "__main__":
    unittest.main()
    