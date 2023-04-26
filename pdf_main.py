import PyPDF2


def learning_pdf():
    # Open the PDF file using a with statement
    with open("resources/files/Working_Business_Proposal.pdf", "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        print(len(pdf_reader.pages))
        page_one = pdf_reader.pages[0]
        page_one_text = page_one.extract_text()
        print(page_one_text)

    # adding page to pdf
    with open("resources/files/Working_Business_Proposal.pdf", "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        page_one = pdf_reader.pages[1]
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(page_one)
        print(type(pdf_writer))
        with open("resources/files/saving-working-business-proposal.pdf", "wb") as save_file:
            pdf_writer.write(save_file)


def divider(title: str):
    print(f"=========={title.upper()}==========")


if __name__ == '__main__':
    divider("learning pdf")
    learning_pdf()
