import os
import replicate
# export REPLICATE_API_TOKEN=r8_YbKYwwfBVYiVzox1z3SYPE9R4b5Fi0R1IBT2T
# Prompts
pre_prompt = ''''.'''

def generate_response(prompt_input):
# Generate LLM response
  output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', input={"prompt": f" list  top 2-3 based on the user query by understaing movie summary , just list their names ...User Question asked is  - {prompt_input} Assistant: ","temperature":0.3, "top_p":0.9, "max_length":128000
    , "repetition_penalty":1})
  full_response = ""

  for item in output:
    full_response += item

  print(full_response)
  return full_response

generate_response('hi recommend a good movie')