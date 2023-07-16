import os
import openai


openai.api_key = os.getenv("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")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an Email to Boss on 4 Days Leave",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)