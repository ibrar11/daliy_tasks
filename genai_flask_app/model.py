import os
from dotenv import load_dotenv as env
env()
url = os.getenv("URL")
api_key = os.getenv("API_KEY")

from ibm_watsonx_ai import Credentials
credentials = Credentials(
    url = url, 
    api_key = api_key
)

from ibm_watsonx_ai.metanames import GenTextParamsMetaNames
params = {
    GenTextParamsMetaNames.DECODING_METHOD: "greedy",
    GenTextParamsMetaNames.MAX_NEW_TOKENS: 100
}

from ibm_watsonx_ai.foundation_models import ModelInference
model = ModelInference(
    model_id="ibm/granite-3-8b-instruct",
    params=params,
    credentials=credentials,
    project_id="9a84ef08-3951-4195-bbc4-90d096773e14"
)

# text = """
# Only reply with the answer. What is the capital of Canada?
# """
# print(model.generate(text)['results'][0]['generated_text'])

from langchain_core.prompts import PromptTemplate
llama3_template = PromptTemplate(
    template='''<|begin_of_text|><|start_header_id|>system<|end_header_id|>
{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>
{user_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
''',
    input_variables=["system_prompt", "user_prompt"]
)

print("llama3_templatellama3_template",llama3_template)

from langchain_core.runnables.base import Runnable

class IBMWatsonxLLM(Runnable):
    def __init__(self, model):
        self.model = model

    def invoke(self, prompt, config=None) -> str:
        # Accept string or dict input
        if hasattr(prompt, "to_string"):
            text = prompt.to_string()
        elif isinstance(prompt, dict):
            # If prompt is dict with system/user prompts
            text = f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
{prompt.get('system_prompt', '')}<|eot_id|><|start_header_id|>user<|end_header_id|>
{prompt.get('user_prompt', '')}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""
        else:
            text = str(prompt)

        result = self.model.generate(text)
        return result['results'][0]['generated_text']

def get_ai_response(model, template, system_prompt, user_prompt):
    ibm_llm = IBMWatsonxLLM(model)
    chain = template | ibm_llm
    return chain.invoke({'system_prompt': system_prompt, 'user_prompt': user_prompt})

system_prompt = "You are an AI assistant helping with customer inquiries. Provide a concise response."
user_prompt = """
Only reply with the answer. What is the capital of Canada?
"""
print("\nAI response: ",get_ai_response(model,llama3_template,system_prompt,user_prompt))

text = """
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are an expert assistant who provides concise and accurate answers.<|eot_id|>
<|start_header_id|>user<|end_header_id|>
What is the capital of Canada?<|eot_id|>

<|start_header_id|>assistant<|end_header_id|>
"""

from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
class AIResponse(BaseModel):
    summary: str = Field(description="Summary of the user’s message")
    sentiment: int = Field(description="Sentiment score from 0 to 100")
    response: str = Field(description="Generated AI response")

json_parser = JsonOutputParser(pydantic_object=AIResponse)

def get_ai_response(model, template, system_prompt, user_prompt):
    chain = template | model | json_parser
    return chain.invoke({
        'system_prompt': system_prompt,
        'user_prompt': user_prompt,
        'format_prompt': json_parser.get_format_instructions()
    })

def get_model_response(model, template, system_prompt, user_prompt):

    # Combine template → model → parser
    chain = template | model | json_parser

    output = chain.invoke({
        "system_prompt": system_prompt,
        "user_prompt": user_prompt,
        "format_prompt": json_parser.get_format_instructions()
    })
    
    return output