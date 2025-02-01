from openai import OpenAI
from config import LM_STUDIO_CONFIG

# Configuração do cliente OpenAI para LM Studio
client = OpenAI(
    base_url=LM_STUDIO_CONFIG["api_url"],
    api_key=LM_STUDIO_CONFIG["api_key"]  # Pode ser qualquer valor
)

def generate_response(prompt, temperature=0.7, max_tokens=150):
    
    #Gera uma resposta usando o LM Studio.
   
    try:
        response = client.chat.completions.create(
            model=LM_STUDIO_CONFIG["model"],
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Erro ao gerar resposta: {e}")
        return None

def stream_response(prompt, temperature=0.7, max_tokens=150):
    
    #Gera uma resposta em streaming para o prompt usando o LM Studio.
 
    try:
        response = client.chat.completions.create(
            model=LM_STUDIO_CONFIG["model"],
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True
        )
        for chunk in response:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
    except Exception as e:
        print(f"Erro ao gerar resposta em streaming: {e}")

if __name__ == "__main__":
    # Teste de resposta regular
    print("Testing regular response:")
    prompt = "Gere um poema curto sobre tecnologia."
    response = generate_response(prompt, temperature=0.9, max_tokens=500)
    print(f"Prompt: {prompt}")
    print(f"Response: {response}")

    # Teste de resposta em streaming
    print("\nTesting streaming response:")
    prompt = "Conte uma história curta sobre um robô."
    print(f"Prompt: {prompt}\n")
    stream_response(prompt)


    # Teste de tratamento de erros
    print("\nTesting error handling:")
    try:
        response = generate_response("", temperature=0.9, max_tokens=500)
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error caught successfully: {e}")