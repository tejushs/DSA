import re

def is_html_tags_balanced(html):
    # Regex to find all tags
    tag_pattern = re.compile(r'</?([a-zA-Z0-9]+)[^>]*?>')
    tags = tag_pattern.findall(html)

    stack = []

    for match in re.finditer(r'</?([a-zA-Z0-9]+)[^>]*?>', html):
        tag = match.group()
        tag_name = match.group(1)

        if tag.startswith('</'):  # Closing tag
            if not stack or stack[-1] != tag_name:
                return False
            stack.pop()
        elif not tag.endswith('/>'):  # Ignore self-closing tags
            stack.append(tag_name)

    return len(stack) == 0

html1 = "<html><body><h1>Hello</h1></body></html>"
html2 = "<div><p>Hi</div></p>"
html3 = "<div><img src='pic.jpg' /></div>"

print(is_html_tags_balanced(html1))  
print(is_html_tags_balanced(html2))  
print(is_html_tags_balanced(html3))  
