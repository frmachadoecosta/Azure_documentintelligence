
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure_secrets import key, endpoint

client = DocumentIntelligenceClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)
#MODEL_NAME = "prebuilt-layout"
MODEL_NAME = "prebuilt-idDocument"
with open(r"sample\sample#1.pdf", "rb") as f:
    pdf_bytes = f.read()

# Azure OCR call
poller = client.begin_analyze_document(
    model_id=MODEL_NAME,
    body=pdf_bytes
)

result = poller.result()
print(result)
# Show text
for page in result.pages:
    for line in page.lines:
        print(line.content)