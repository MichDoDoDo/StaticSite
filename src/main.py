from textnode import *

def main():
    node = TextNode("this is text",TextType.LINK,"https://www.boot.dev")   
    
    print(type(node.__repr__()))
    
    
main()