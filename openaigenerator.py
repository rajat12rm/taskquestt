from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="",
)


def gpt_reply(user_input):
  stream = client.chat.completions.create(
      model="gpt-4",
      messages=[{"role": "user", "content": user_input}],
      stream=True,
      temperature =0
  )
  string =" "
  for x in stream :
    string += (x.choices[0].delta.content or "")
  print(string)
  return string

