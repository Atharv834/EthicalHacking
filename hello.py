import json

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

    with open(pdf_file_name, "w") as file:  # Change "wb" to "w" for writing as text
        json.dump(pdf_content, file, indent=4)  # Encode dictionary to JSON

    return pdf_content

def malicious_pdf_creator(pdf_file_name, message):
    """Creates malicious PDF file for the specified PDF file name and message."""
    pdf_content = pdf_content_creator(pdf_file_name, message)
    print("PDF creation completed successfully.")

if __name__ == "__main__":
    malicious_pdf_creator("test.pdf", "This PDF file is designed to steal your personal information.")

