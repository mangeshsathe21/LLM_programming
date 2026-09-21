from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from llm.organization_reviews import llm_ollama_organization
from time import perf_counter, time
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "http://localhost:5173"
    ],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/")
def start():
    return {"message" : "this is test"}

@app.get("/fetch_google_reviews/organization/{organization_name}")
def fetch_reviews(organization_name : str):
    
    fetch_reviews_from_google_place_api = {
            "cohezia_india": {
                "organization": "Cohezia India",
                "reviews": [
                    {
                        "id": 1,
                        "comment": "Nothing is good about this company, there is no growth level professionally also and personally also not so many departments and you can not learn full technology your knowledge will be limited to what you are doing."
                    },
                    {
                        "id": 2,
                        "comment": "no work ethic.They don't think about the employee at all."
                    },
                    {
                        "id": 3,
                        "comment": "Old culture, No clarity about hr decision and process is not defined.This will lead company downfall"
                    },
                    {
                        "id": 4,
                        "comment": "worst work culture"
                    }
                ]
            },
            "ntt_docomo": {
                "organization": "NTT Docomo",
                "reviews": [
                    {
                        "id": 1,
                        "comment": "Senior management make increment of self. No increments to juniors. Partiality between junior and seniors in policies, seating, laptop, everything."
                    },
                    {
                        "id": 2,
                        "comment": "3 months notice period is very long period. At least 1.5 months is best for my opinion."
                    },
                    {
                        "id": 3,
                        "comment": "The company is open to innovation and readily adopts latest technology. I love the fact that I am a part of a team that markets reliable, high quality products and has global client base. Its my pleasure to work with the company"
                    },
                    {
                        "id": 4,
                        "comment": "There was nothing much to dislike, other than pantry area I have seen cockroaches on the coffee machine and mosqitoes in the working NOC."
                    }
                ]
            }
        }
    
    
    return_data = fetch_reviews_from_google_place_api[organization_name] if organization_name in fetch_reviews_from_google_place_api else {}
    
    if not return_data:
        return {
                "status" : 200,
                "data" : return_data,
                "llm_response" : "No response from LLM",
                "prompt_stats" : {"prompt_length" : 0, "prompt_token_count": 0, 'execution_time': 0},
            }
    else:   
            text_content = return_data['reviews']
            text_content_combined = ["Employee " + str(items["id"]) +" says "+ items['comment'] for items in text_content]
            start = perf_counter()
            llm_response = llm_ollama_organization(text_content_combined)
            
            #llm_response = []
            llm_response['prompt_stats']['execution_time'] = perf_counter() - start

            return {
                "status" : 200,
                "llm_response" : llm_response['llm_response'],
                "prompt_stats" : llm_response['prompt_stats'],
                "data" : return_data
            }