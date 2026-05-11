import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader

"""inserir as variveis de ambiente e api keys"""

arnaLoader = WebBaseLoader(
    'https://asimov.academy/',
    requests_kwargs={
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        }
    }
)
arnaConhecimento = arnaLoader.load()

arnaListaConhecimento = ''
for i in arnaConhecimento:
    arnaListaConhecimento += i.page_content

# A lei completa excede o limite de tokens da Groq (free tier: 12k tokens/min).
# Truncamos para ~6000 caracteres (~1500 tokens), deixando margem para a conversa.
MAX_CHARS = 6000
arnaListaConhecimento = arnaListaConhecimento[:MAX_CHARS]

chat = ChatGroq(model='llama-3.3-70b-versatile')

def respbot(listamsg):
    template = ChatPromptTemplate.from_messages(
        [('system', 'você é um assistente amigavel chamado arnaBot especialista na Lei {lei}')] +
        listamsg
    )
    chain = template | chat
    return chain.invoke({'lei': arnaListaConhecimento})


arnaMensagem = []
while True:
    arnaPergunta = input('Usuario ..: ').lower()
    if arnaPergunta == 'x':
        break
    arnaMensagem.append(('human', arnaPergunta))
    arnaRes = respbot(arnaMensagem)
    arnaMensagem.append(('assistant', arnaRes.content))
    print(f'Bot:  {arnaRes.content}')
print('Obrigado por utilizar nosso Bot!')
