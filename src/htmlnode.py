
class HTMLNode ():
    
    def __init__(self, tag = None, value = None, child = None, props = None):
        self.tag = tag
        self.value = value
        self.child = child
        self.props = props
    
    def __repr__(self):
        return(f"HTMLNode({self.tag},{self.value},{self.child},{self.props})")
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        htmlStr = ""
        for key, value in self.props.items():
            propString = " " + key + "=\""+value+"\""
            htmlStr += propString
                 
        return htmlStr
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value,None, props)   
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
    def to_html(self):
        if self.value is None or not self.value:
            raise ValueError
        
        if(self.tag is None):
            return self.value
        else:
            if self.props:
                return "<"+ self.tag + self.props_to_html()+">"+self.value  + "</"+self.tag+">"
            else:
                return "<"+self.tag+">"+self.value+"</"+self.tag+">"

class ParentNode(HTMLNode):
    def __init__(self, tag, child, props=None):
        super().__init__(tag, None, child, props)     
    
    def to_html(self):
        htmlstr = ""
        if not self.tag:
            raise ValueError("Missing HTML tag")
        if not self.child:
            raise ValueError("Missing child")
        for child in self.child:
            htmlstr += child.to_html()
            
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{htmlstr}</{self.tag}>" 
        else :
            return f"<{self.tag}>{htmlstr}</{self.tag}>" 

            
            
        
    