from typing import NewType

# Document class define kar rahe hain jo content aur review status ko handle karti hai
class Document:
    def __init__(self, content: str):
        self.content = content
        self.reviewed = False

    def mark_reviewed(self):
        # Yeh method document ko reviewed mark kar deta hai
        self.reviewed = True

    def is_reviewed(self) -> bool:
        # Yeh check karta hai ke document reviewed hai ya nahi
        return self.reviewed

# `ReadyToPublishDocument` aik naya type banate hain jo `Document` par base hai
ReadyToPublishDocument = NewType('ReadyToPublishDocument', Document)

# Yeh function sirf `ReadyToPublishDocument` ko accept karega
def publish_document(doc: ReadyToPublishDocument):
    # Document ko publish karta hai
    print(f"Publishing document: {doc.content}")

# Document ko review ke baad `ReadyToPublishDocument` mein convert karne ka function
def prepare_for_publishing(doc: Document) -> ReadyToPublishDocument:
    # Ensure karte hain ke document reviewed hai
    assert doc.is_reviewed(), "Document must be reviewed before publishing"
    return ReadyToPublishDocument(doc)

# Example workflow
if __name__ == "__main__":
    # Ek naya draft document banate hain
    draft_doc = Document("Yeh aik draft content hai.")
    print("Initial Document:", draft_doc.content)  # Output: Draft document ka content


    draft_doc.mark_reviewed()
    ready_doc = prepare_for_publishing(draft_doc)  # `ReadyToPublishDocument` mein convert

    publish_document(ready_doc)