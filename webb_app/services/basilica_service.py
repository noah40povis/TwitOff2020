import basilica
from basilica import Connection
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BASILICA_API_KEY")

connection = Connection(API_KEY)
print("CONNECTION", type(connection))

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

embedding = connection.embed_sentence("Hellow World!!!", model="Twitter")
breakpoint()

# with basilica.Connection(API_KEY) as c:
#     embeddings = c.embed_sentences(["Hello world!", "How are you?"])
#     print(list(embeddings)) # [[0.8556405305862427, ...], ...]