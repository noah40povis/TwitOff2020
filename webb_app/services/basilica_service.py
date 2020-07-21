import basilica
from basilica import Connection
from dotenv import load_dotenv
import os 

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")

connection = Connection(API_KEY)
print("CONNECTION", type(connection))

#could use a function here to return 


if __name__ == "__main__":


    sentences = [
        "This is a sentence!",
        "This is a similar sentence!",
        "I don't think this sentence is very similar at all..."

    ]

    connection = Connection(API_KEY)
    print("CONNECTION", type(connection))

    embeddings = list(connection.embed_sentences(sentences))
    print(embeddings)

    embedding = connection.embed_sentence("Hello World!!!", model="Twitter")
    print(type(embedding))
    print(type(embedding[0]))
    print(len(embedding))