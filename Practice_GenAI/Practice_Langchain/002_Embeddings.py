# from langchain_openai import OpenAIEmbeddings
# from langchain_community.vectorstores import FAISS
# import faiss
# import numpy as np

# # Step 1: Generate Embeddings
# embeddings = OpenAIEmbeddings()
# texts = ["Hello, how are you?", "What is LangChain?", "Tell me about vector databases."]
# vector_store = []

# # print(embeddings)
# # print(texts)

# for text in texts:
#     vector = embeddings.embed_query(text)
#     # print(vector)
#     vector_store.append(vector)

# print(len(vector_store))
# print(type(vector_store))
# print(
#     "************************************************************************************************************************************************"
# )
# vector_store = np.array(vector_store, dtype=np.float32)
# print(type(vector_store))
# print(len(vector_store))
# print(vector_store.ndim)


# # Step 2: Build Faiss Index
# index = faiss.IndexFlatL2(vector_store.shape[1])
# index.add(vector_store)

# # # Step 3: Perform Search
# # query = "Tell me about LangChain"
# # query_vector = embeddings.embed_text(query)

# # _, indices = index.search(np.array([query_vector], dtype=np.float32), k=2)
# # print("Most similar texts:" [texts[i] for i in indices[0]])


# #
# Here are the tasks in question form:

# 1. Generate Embeddings for a Single Sentence
# How can you generate embeddings for the sentence "What is machine learning?" using OpenAIEmbeddings and print the vector representation?
# 2. Compare Embeddings for Similar Sentences
# How do the embeddings of two similar sentences, such as "What is artificial intelligence?" and "Define artificial intelligence.", compare? What do their vectors look like?
# 3. Use FAISS to Search for the Most Similar Sentence
# How can you store a few sentences in a FAISS index and perform a similarity search to find the most similar sentence to a query?
# 4. Save and Load FAISS Index Locally
# How can you save a FAISS index to a local file and then load it back from the file for performing a similarity search?
# 5. Visualize Embeddings
# How can you visualize the embeddings of sentences in 2D using a dimensionality reduction technique like PCA or t-SNE?
# 6. Check Similarity Between Two Embeddings Directly
# How can you calculate the cosine similarity between the embeddings of two sentences?


# from langchain_openai import OpenAIEmbeddings
# from langchain_community.vectorstores import FAISS
# import numpy as np

# #  used for creating the embeddings..
# embedding_ins = OpenAIEmbeddings()

# text = "What is machine learning?"

# # vec_store = FAISS.from_texts(text, embedding=embedding_ins)
# vec_store = embedding_ins.embed_query(text)

# print(type(vec_store))

# print(np.array(vec_store))

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


tushar_info = [
    "Tushar Kumar is a final-year B.Tech student at Dr. Kedar Nath Modi Institute of Engineering and Technology, graduating in 2025.",
    "Tushar is actively involved in organizing events as a technical team member.",
    "Tushar has completed an internship and training at Unified Mentor.",
    "Tushar has hobbies including cricket, solving Rubik's Cube, and playing badminton.",
    "Tushar is interested in spirituality.",
    "Tushar is applying for a frontend developer position at BharatPe.",
    "Tushar plans to create an automation tool to automatically apply for matching job positions on Internshala.",
    "Tushar wants to master Data Structures and Algorithms (DSA) and has 18 hours a day to dedicate to it.",
    "Tushar is working on a production-level project with the help of a business analyst and is seeking guidance on whether to contact an organization or hire a freelancer for assistance due to his limited experience.",
    "Tushar is considering a tech-related startup and seeks advice on how to build a project from SRS to delivery.",
    "Tushar is working on code to ensure that the value entered by the user is preserved and correctly outputted after performing operations.",
    "Tushar manages community inquiries and resolves doubts as a Google Arcade Volunteer.",
    "Tushar prefers using his own code for solving problems even when provided with corrections or alternative solutions.",
    "Tushar’s resume includes the following skill categories: Languages & Frameworks, Programming Languages, Frontend Development Tools, and Course Work.",
    "Tushar has created an e-commerce website clone that includes functionality such as add-to-cart, remove items, and real-time local storage data saving.",
    "Tushar includes a classic Tic Tac Toe game in his resume, showcasing its reimagined design and functionality using HTML, CSS, and JavaScript.",
    "Tushar has developed a Generative AI app using the Google Gemini API with React JS for his major project.",
    "Tushar developed a Netflix clone website using React, TMDB API, and Firebase for his major project.",
    "Tushar has completed a certificate course in C++ with a focus on pointers.",
    "Tushar is interested in the topic 'Machine Learning for Predictive Maintenance in Manufacturing' for research purposes.",
    "Tushar understands that while .js files can contain JSX code, .jsx files are used for better clarity and organization.",
    "Tushar has an interview for a personality test tomorrow.",
    "Tushar’s areas of knowledge and skills include: HTML, CSS, JavaScript, Data structures (Array, maps).",
    "Tushar had his online assessment for the frontend developer role yesterday.",
    "Tushar prefers concise emails and concise answers without lengthy explanations.",
    "Tushar is inquiring about the meaning and work involved in the branch of Information & Communication Technology System Maintenance.",
    "Tushar prefers exact answers according to test assessments.",
    "Tushar is working on finding the predecessor and successor of a key in a BST using vector-based methods and testing the logic with specific test cases.",
    "Tushar prefers his solution, which uses in-order traversal and new node creation, as it works better on another platform.",
    "Tushar has only mobile data and no Wi-Fi.",
    "Tushar is applying for the 2025 Engineering Campus Hiring Program.",
    "Tushar uses Coding Ninjas platform for testing his code.",
    "Tushar understands the importance of initializing `k` to `start` in the merge function to ensure elements are correctly placed back into the original array during merging.",
]


embeddings_openai = OpenAIEmbeddings()

#  creating the embedded vector for this list.
# vector_embe = [embeddings_openai.embed_query(text) for text in tushar_info]
# print(vector_embe)

# for text in tushar_info:
#     embeddings_openai.embed_query(text)


#  create the local faiss index that we need to store into the local device.
faiss_in_vect = FAISS.from_texts(tushar_info, embedding=embeddings_openai)

#  now we need to store into the vector database..
faiss_in_vect.save_local("faiss_indexings")


#  load the faiss index for performing the similarity search.
load_faiss_ind = FAISS.load_local(
    "faiss_indexings", embeddings_openai, allow_dangerous_deserialization=True
)

query = "Is Tushar read DSA if yes then tell me the time"

results = load_faiss_ind.similarity_search(query, k=2)

for result in results:
    print(result.page_content)
