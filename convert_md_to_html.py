#!/usr/bin/env python3
"""
Script to convert Markdown to HTML using mistletoe
"""
from mistletoe import markdown

def md_to_html(md_file_path, html_file_path):
    """
    Converts a Markdown file to HTML and writes the output to an HTML file.
    
    Args:
        md_file_path (str): Path to the Markdown file
        html_file_path (str): Path to the HTML file to write output to
    """
    try:
        # Read the Markdown file
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()
        
        # Convert Markdown to HTML
        html_content = markdown(md_content)
        
        # Add basic HTML structure
        html_document = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Notes</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        code {{
            font-family: monospace;
        }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>"""
        
        # Write the HTML to a file
        with open(html_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_document)
        
        print(f"Successfully converted {md_file_path} to {html_file_path}")
        return True
    
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    md_to_html("notes.md", "index.html")
