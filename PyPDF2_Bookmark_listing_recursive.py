import PyPDF2


def show(bookmark_list, indent=0):
    for item in bookmark_list:
        if isinstance(item, list):
            # recursive call with increased indentation
            show(item, indent + 4)
        else:
            print("{} {}{}".format(reader.getDestinationPageNumber(item),
                  " " * indent, item.title,))


reader = PyPDF2.PdfFileReader("pdf/a-whirlwind-tour-of-python.pdf")
show(reader.getOutlines())
