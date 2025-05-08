from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"
    
    
class TextNode():
   def __init__(self, text, text_type, url = None):
      self.text = text
      self.text_type = text_type
      self.url = url
       
    
   def __repr__(self):
      return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
   def __eq__(self, textnode):
      if(self.text ==  textnode.text and self.text_type == textnode.text_type and self.url == textnode.url):
         return True 
      
   def text_node_to_html_node(self):
      match self.text_type:
         case TextType.TEXT:
            return LeafNode(None,self.text)
         case TextType.BOLD_TEXT:
            return LeafNode("b",self.text )
         case TextType.ITALIC_TEXT:
            return LeafNode("i",self.text)
         case TextType.CODE_TEXT:
            return LeafNode("code",self.text)
         case TextType.LINK:
           return LeafNode("a", self.text, {"href": self.url})
         case TextType.IMAGE:
            return LeafNode("img", "", {"src":self.url, "alt":self.text})
         
        
      