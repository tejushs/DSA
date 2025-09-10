class BrowserHistory:
    def __init__(self, homepage):
        self.current = homepage
        self.back_stack = []
        self.forward_stack = []

    def visit(self, url):
        self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()
        print(f"Visited: {self.current}")

    def back(self):
        if not self.back_stack:
            print("No pages in back history.")
            return self.current
        self.forward_stack.append(self.current)
        self.current = self.back_stack.pop()
        print(f"Back to: {self.current}")
        return self.current

    def forward(self):
        if not self.forward_stack:
            print("No pages in forward history.")
            return self.current
        self.back_stack.append(self.current)
        self.current = self.forward_stack.pop()
        print(f"Forward to: {self.current}")
        return self.current


browser = BrowserHistory("homepage.com")

browser.visit("page1.com")
browser.visit("page2.com")
browser.back()       
browser.back()        
browser.forward()     
browser.visit("page3.com") 
browser.forward()     