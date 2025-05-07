from langchain.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
import shutil
import openai

# REFERENCE FOR THE CODE: https://github.com/pixegami/langchain-rag-tutorial

openai.api_key = os.environ["OPENAI_API_KEY"]

CHROMA_PATH = "chroma"
DATA_PATH = "data"
QUERY = "What happened recently on Reddit that could be of interest to me ?"

PROMPT_TEMPLATE = """
You are provided with a certain number of reddit posts, with some pieces of information about them.
Using the number of upvotes, the upvote ratio, the user's tastes (if you know any) and the gilded,
your task is the following:

1) Find the most interesting posts for the user.
2) Write a short, engaging summary for each (1 paragraph per post).
3) Include a direct URL for each post using the full reddit.com domain.

Prioritize posts with both high upvote counts and high (or very low) upvote ratios, unless gilded is greater than zero (gilded has the top priority).

You will ONLY use the data from the following context: {context}

Your restrictions:
- Do not assume anything about the responses in the post, as you only know what the author said.
- If the author didn't provide any text, then try to infer from the title only.
- The response should be quickly and easily readable for a human. So, don't make it excessively long.
- Don't use any markdown.
- Write with a friendly and slightly witty tone, but avoid exaggerated humor.

The user's request that you have to fulfill is the following: {question}
"""


def load_documents():
    loader = DirectoryLoader(DATA_PATH)
    documents = loader.load()
    return documents


def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=500, length_function=len, add_start_index=True
    )

    chunks = text_splitter.split_documents(documents)

    return chunks


def save_to_chroma(chunks):
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
    )
    db.persist()


def query_data(query=QUERY):
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    results = db.similarity_search_with_relevance_scores(query, k=3)

    if len(results) == 0 or results[0][1] < 0.7:
        print(f"Unable to find matching results.")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    # print(context_text)
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query)

    model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.6)

    response = model.invoke(prompt)
    os.system("cls" if os.name == "nt" else "clear")
    print(response.content)
