from PyPDF2 import PdfReader

pdf_path = "../data/health_ipd.pdf"
output_path = "../data/health_ipd.txt"

if __name__ == "__main__":
    reader = PdfReader(pdf_path)

    with open(output_path, "w") as f:
        for page in reader.pages:
            text = page.extract_text().replace("\t", " ")
            f.write(text)
