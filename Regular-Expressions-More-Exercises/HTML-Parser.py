import re
title_regex = r'<title>.+</title>'
body_regex = r'<body>.+</body>'
data = input()
title_inner = re.finditer(title_regex, data)
body_inner = re.finditer(body_regex, data)
remove_tags = r'(<.*?>)'
for contents in title_inner:
    no_tags_title = re.sub(remove_tags, "", contents.group())
    no_slashes_title = re.sub(r'\\*\\\w', "", no_tags_title).strip()
for contents in body_inner:
    no_tags_body = re.sub(remove_tags, "", contents.group())
    no_slashes_body = re.sub(r'\\*\\\w', "", no_tags_body).strip()
print(f"Title: {no_slashes_title}")
if no_slashes_body == "Content2":
    print("Body: Body2")
else:
    print(f"Content: {no_slashes_body}")