import os
import PyPDF2

def remove_password(input_path, output_path, password=''):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)

        # Check if the PDF is encrypted
        if pdf_reader.isEncrypted:
            # Attempt to decrypt with the provided password
            if pdf_reader.decrypt(password) != 1:
                print("Incorrect password or encryption method. Trying without password.")
                if pdf_reader.decrypt(password) != 1:
                    raise Exception("Failed to decrypt PDF. Incorrect password or encryption method.")

        # Create a new PDF writer
        pdf_writer = PyPDF2.PdfFileWriter()

        # Add all pages to the new PDF writer
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

        # Write the modified PDF to the output file
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

        print("I am done, removing password from your file")

if __name__ == "__main__":
    input_pdf_file = input("PDF input file: ")
    pdf_pass = input("PDF password: ")
    output_pdf_file = input("PDF output file: ")
    current_directory = os.getcwd()  # Get the current working directory
    input_pdf_path = os.path.join(current_directory, input_pdf_file)
    output_pdf_path = os.path.join(current_directory, output_pdf_file)
    password_to_remove = pdf_pass

    remove_password(input_pdf_path, output_pdf_path, password_to_remove)
