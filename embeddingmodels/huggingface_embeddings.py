from langchain_huggingface import HuggingFaceEmbeddings
embeddings =  HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
texts =[
    "Hello this is Adnan Tariq Bhat",
    "Hello your name is youtube",
    "And you all are very beautiful people"
]

vector = embeddings.embed_query(texts)
print(vector)