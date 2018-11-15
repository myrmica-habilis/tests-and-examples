import os, PyPDF2

filenames = ["pdf/not_a_PDF_file.pdf", "pdf/non-existent-file.pdf", "pdf/Tire_size_chart_ENG.pdf", "pdf/tldr-book.pdf"]

# EXAMPLE 1
# two unsafe actions, nested in separate try statements:

for filename in filenames:
    print("-" * 40)
    try:
        print("Trying to read:", os.path.split(filename)[1])
        reader = PyPDF2.PdfFileReader(filename)          # potential exception #1
    except Exception as err:
        print(err)
    # or:
    # except:
    #     print(sys.exc_info()[1])
    else:
        try:
            print("Trying to get number of pages...")
            pages = reader.numPages                      # potential exception #2
        except Exception as err:
            print(err)
        else:
            print("This file has {} pages.".format(pages))

# EXAMPLE 2
# two unsafe actions, both in one try clause:

for filename in filenames:
    print("-" * 40)
    try:
        print("Trying to read:", os.path.split(filename)[1])
        reader = PyPDF2.PdfFileReader(filename)          # potential exception #1
        print("Trying to get number of pages...")
        pages = reader.numPages                          # potential exception #2
    except Exception as err:
        print(err)
    else:
        print("This file has {} pages.".format(pages))
