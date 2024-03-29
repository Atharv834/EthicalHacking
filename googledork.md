### Sensitive Dorks

- [DorkGPT](https://dorkgpt.com/): Use to generate Google dorks for finding sensitive information using AI.

Reference: [OSINT Techniques for Sensitive Documents That Have Escaped into the Clear Web](https://christina-lekati.medium.com/osint-techniques-for-sensitive-documents-that-have-escaped-into-the-clear-web-6659f29e6010)

- `"company name" AND internal (filetype:docx OR filetype:pdf)`
- `Site:companyname.com AND "keywords" AND inurl:fileadmin`
- `Site:companyname.com (filetype:pdf OR filetype:ppt OR filetype:xls)`
- `"company name" AND confidential (filetype:ppt OR filetype:pdf)`
- `Site:companyname.com AND (contract OR "internal use only") filetype:pdf`
- `"company name" AND ("service agreement" OR "memorandum") -public`

#### Context-Based Search

- `"Context"`: Shows only those pages that contain the exact word or statement.
- `site:website "Context"`: Retrieves information only from the specified website with the exact context.
- `filetype:pdf intitle:"Context"`: Searches only for PDF files with the exact title content provided.
- `filetype:pdf OR filetype:docx OR filetype:ppt "Context"`: Searches for PDF, DOCX, PPT files with the exact context provided.
- `site:SocialNetwork | site:SocialNetowrk2 | site:SocialNetwork3… "Context"`: Searches in the given Social Media platforms with the exact context provided.
- `"Context" after:YYYY-MM-DD AND before:YYYY-MM-DD`: Searches for the given context after and before the specified dates.
- `site:Blog | site:Blog2 | site:Blog3 after:YYYY-MM-DD AND before:YYYY-MM-DD "Context"`: Searches the given websites for the specified context after and before the specified dates.
