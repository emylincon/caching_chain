def page(no):
    page_no = f"""<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>Page {no}</title>
                    </head>
                    <body>
                    <h1> This is page number {no}</h1>
                    </body>
                    </html>"""
    return page_no


for i in range(1,21):
    file = open(f'templates/{i}.html', 'w', encoding='utf-8')
    file.write(page(i))
    file.close()
