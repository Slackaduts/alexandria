import pdfplumber as plumber
import re

def main():
    path = r"C:\Users\Gabe\Downloads\Craig Zacker - CompTIA Network+ Practice Tests_ Exam N10-008 (2021, Sybex) - libgen.li.pdf"
    pdf = plumber.open(path)

    offset = input("How many preceeding non-numbered pages?")
    page_num = input("Enter a page number to start on:")

    pdf_text = ""
    for i, page in enumerate(pdf.pages):
        if i + 1 < int(offset) + int(page_num):
            continue

        print(f"Processing page {i}...")
        pdf_text += page.extract_text()

    regex = r"\d+\. "
    q_nums = re.findall(regex, pdf_text)
    q_text = re.split(regex, pdf_text)

    questions = [n + c for n, c in zip(q_nums, q_text[1:])]

    for question in questions:
        print("---------------------------------------------")
        print(question)
        input("Press Enter to continue...")


if __name__ == "__main__":
    main()