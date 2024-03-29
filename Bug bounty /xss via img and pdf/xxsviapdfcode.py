
import sys

def pdf_content_creator(pdf_file_name, message):
    """Creates PDF content with JavaScript for the specified PDF file name and message."""
    pdf_content = {
        "pdf_version": "1.7",
        "pages": [
            {
                "page_id": 1,
                "open_action": {
                    "page_id": 2,
                },
            },
            {
                "page_id": 2,
                "javascript": f"app.alert('{message}')",
            },
        ],
    }

    with open(pdf_file_name, "wb") as file:
        file.write(pdf_content.encode("utf-8"))

    return pdf_content

def malicious_pdf_creator(pdf_file_name, message):
    """Creates malicious PDF file for the specified PDF file name and message."""
    pdf_content = pdf_content_creator(pdf_file_name, message)
    print("PDF creation completed successfully.")

if __name__ == "__main__":
    malicious_pdf_creator("test.pdf", "This PDF file is designed to steal your personal information.")
