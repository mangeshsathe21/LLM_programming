from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.globals import set_debug
import tiktoken

#set_debug(True)
def calculate_stats(prompt_template : ChatPromptTemplate,input_data : dict, est_output_token: int):
    prompt_data = prompt_template.invoke(input_data)
    prompt_string = prompt_data.to_string() #prompt to string conversion
    char_count = len(prompt_string) # Total prompt count
    
    tokenizer = tiktoken.get_encoding("cl100k_base")
    compiled_prompt = prompt_template.format(**input_data)
    token_count = len(tokenizer.encode(compiled_prompt))
    return {"prompt_length" : char_count, "prompt_token_count": token_count}
    
    
def llm_ollama_organization (text_content : list = ["the staff was very friendly", "service was slow"]):
    llm = ChatOllama(model="llama3.1:latest", format="json", temperature= 0.2)
    combined_comments = "\n".join(text_content)
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", """You are an expert organizational analyst. Evaluate the provided organization reviews and give rating and provide your analysis .

        Respond ONLY with a valid, raw JSON object following this exact schema:
        {{
        "rating": <integer from 1 to 5, where 1 is extremely negative and 5 is extremely positive>,
        "analysis_by_llm": "<must stick to the reviews and mention first employee as well>"
        }}

        if you dont gave analysis_by_llm then just pass rating as "0" and give some reason for no analysis_by_llm

        """),
                ("human","these are the reviews : {text_comment}")
            ])
    
    input_data = {"text_comment": combined_comments}

    prompt_stats = calculate_stats(
        prompt_template,
        input_data,
        est_output_token = 150
    )
    
    chain = prompt_template|llm|JsonOutputParser()
    response = chain.invoke(input_data)

    return {'llm_response' : response, 'prompt_stats' : prompt_stats}