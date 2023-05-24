import pinecone
import os

# get api key from app.pinecone.io
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY') or 'PINECONE_API_KEY'
# find your environment next to the api key in pinecone console
PINECONE_ENV = os.environ.get('PINECONE_ENVIRONMENT') or 'PINECONE_ENVIRONMENT'

pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENV
)

class CohereModel:
    def __init__(self):
        import cohere
        self.co = cohere.Client(api_key=os.environ.get('COHERE_API_KEY'))
        self.model_name = "embed-multilingual-v2.0"
    
    def encode_slice(self, slice):
        return self.co.embed(
            slice,
            model=self.model_name,
            truncate='END'
        ).embeddings
    
    def encode(self, query):
        return self.co.embed(
            [query],
            model=self.model_name,
            truncate='END'
        ).embeddings
    
    def get_dimension(self):
        # https://docs.cohere.com/reference/embed
        return 768
    
    def batch_size(self):
        return 96
    
    def index_name(self):
        return 'cohere-multingual'
    

class PineconeSearch:
    def __init__(self):
        self.model = CohereModel()
        self.model_index = pinecone.Index(self.model.index_name())

    def search(self,query):
        # create the query vector
        xq = self.model.encode(query)
        xc = self.model_index.query(xq, top_k=5, include_metadata=True)
        return xc.matches