import re

def is_html_tags_balanced_with_attributes(html):
    tag_pattern = re.compile(r'<(/?)([a-zA-Z0-9]+)([^>]*)>')
    stack = []

    for match in tag_pattern.finditer(html):
        slash, tag_name, attr = match.groups()

        
        is_self_closing = attr.strip().endswith('/')

        if slash == '':  
            if not is_self_closing:
                stack.append(tag_name)
        else:  
            if not stack or stack[-1] != tag_name:
                return False
            stack.pop()

    return len(stack) == 0


html1 = '<div class="container"><p style="color:red;">Hello</p></div>'
html2 = '<div><img src="pic.jpg" /></div>'
html3 = '<div><p>Text</div></p>'

print(is_html_tags_balanced_with_attributes(html1))  
print(is_html_tags_balanced_with_attributes(html2))  
print(is_html_tags_balanced_with_attributes(html3))  