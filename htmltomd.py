from markdownify import markdownify as md
import re

with open('Description.html', 'r', encoding='utf-8') as html_file:
    html_content = html_file.read()

md_content = md(html_content)

# Replace multiple newlines with a single newline
md_content = re.sub(r'\n\s*\n+', '\n\n', md_content)

with open('output.md', 'w', encoding='utf-8') as md_file:
    md_file.write(md_content)
