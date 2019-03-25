from json_to_html import converter

if __name__ == "__main__":
    json2html = converter.Converter()
    html_string = json2html.convert()
    print(html_string)
