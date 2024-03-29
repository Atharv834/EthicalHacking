from reportlab.pdfgen import canvas
import json

def create_pdf_with_malicious_content(pdf_file_name, text_message, js_message):
    """Creates a PDF file with specified text content and JavaScript."""
    # Create PDF with text content
    c = canvas.Canvas(pdf_file_name)
    c.drawString(100, 750, text_message)
    c.save()
    print("Text content added to PDF.")

    # Create PDF content with JavaScript
    pdf_content = {
        "pdf_version": "1.7",
        "pages": [
            {
                "page_id": 1,
                "open_action": {
                    "action_type": "JavaScript",
                    "javascript": f"app.alert('{js_message}')",
                },
            },
        ],
    }

    # Write PDF content to file
    with open(pdf_file_name, "wb") as file:  # Use "wb" for binary mode
        file.write(json.dumps(pdf_content).encode("utf-8"))
    
    print("JavaScript added to PDF.")
    print("PDF creation completed successfully.")

if __name__ == "__main__":
    create_pdf_with_malicious_content(
        "test.pdf",
        "This is a regular PDF file.",
        "This PDF file is designed to steal your personal information."
    )
