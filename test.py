# import cohere
# from rich import print
# from dotenv import dotenv_values
# import logging
# import re

# # Configure logging for debugging and monitoring
# logging.basicConfig(
#     filename="brai.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# # Load environment variables from .env file
# env_vars = dotenv_values(".env")

# # Use provided Cohere API key as fallback
# COHERE_API_KEY = env_vars.get("COHEREAPIKEY", "")

# # Initialize Cohere client
# try:
#     co = cohere.Client(api_key=COHERE_API_KEY)
# except Exception as e:
#     logging.error(f"Failed to initialize Cohere client: {str(e)}")
#     print(f"[ERROR] Failed to initialize Cohere client: {str(e)}")
#     exit(1)

# # Expanded list of recognized function keywords for task categorization
# funcs = [
#     "exit", "general", "realtime", "open", "close", "play", "pause", "stop",
#     "generate image", "system", "content", "google search", "youtube search",
#     "reminder", "calculate", "weather", "translate", "summarize", "analyze"
# ]

# # Updated preamble with modified exit command
# preamble = """
# You are an advanced Decision-Making Model designed to accurately categorize user queries. Your task is to identify the type of query without answering it. Return only the categorized query type(s) in the specified format. Use confidence scoring (0.0 to 1.0) internally to select the most likely category, but do not include scores in the output. Consider context from previous interactions provided in the prompt.

# *** Instructions for Categorization ***
# - Respond with 'general (query)' for queries answerable by an LLM without real-time data, e.g., 'who was akbar?' → 'general who was akbar?', 'how to study effectively?' → 'general how to study effectively?', 'what is python?' → 'general what is python?'. Also use for incomplete queries or those without proper nouns, e.g., 'who is he?' → 'general who is he?', 'what's the time?' → 'general what's the time?'.
# - Respond with 'realtime (query)' for queries requiring up-to-date information, e.g., 'who is the indian prime minister?' → 'realtime who is the indian prime minister', 'what is today's news?' → 'realtime what is today's news?', 'who is elon musk?' → 'realtime who is elon musk?'.
# - Respond with 'open (app or website)' for opening applications or websites, e.g., 'open facebook' → 'open facebook'. For multiple apps, e.g., 'open facebook and telegram' → 'open facebook, open telegram'.
# - Respond with 'close (app or website)' for closing applications or websites, e.g., 'close notepad' → 'close notepad'. For multiple, e.g., 'close facebook and telegram' → 'close facebook, close telegram'.
# - Respond with 'play (song name)' for playing songs, e.g., 'play let her go' → 'play let her go'. For multiple, e.g., 'play song1 and song2' → 'play song1, play song2'.
# - Respond with 'pause (media)' for pausing media, e.g., 'pause music' → 'pause music'.
# - Respond with 'stop (media)' for stopping media, e.g., 'stop video' → 'stop video'.
# - Respond with 'generate image (prompt)' for image generation, e.g., 'generate image of a lion' → 'generate image of a lion'. For multiple, e.g., 'generate images of a cat and dog' → 'generate image of a cat, generate image of a dog'.
# - Respond with 'reminder (datetime with message)' for reminders, e.g., 'set a reminder for 9:00pm on 25th June for meeting' → 'reminder 9:00pm 25th June meeting'.
# - Respond with 'system (task)' for system tasks like 'mute', 'volume up', e.g., 'mute system' → 'system mute'. For multiple, e.g., 'mute and volume down' → 'system mute, system volume down'.
# - Respond with 'content (topic)' for content creation, e.g., 'write a python script' → 'content python script', 'write an email about sales' → 'content email about sales'.
# - Respond with 'google search (topic)' for Google searches, e.g., 'search python tutorials on google' → 'google search python tutorials'.
# - Respond with 'youtube search (topic)' for YouTube searches, e.g., 'search cooking videos on youtube' → 'youtube search cooking videos'.
# - Respond with 'calculate (expression)' for calculations, e.g., 'calculate 5 + 3' → 'calculate 5 + 3'.
# - Respond with 'weather (location)' for weather queries, e.g., 'what's the weather in New York?' → 'weather New York'.
# - Respond with 'translate (text to language)' for translations, e.g., 'translate hello to Spanish' → 'translate hello to Spanish'.
# - Respond with 'summarize (text or topic)' for summarization, e.g., 'summarize this article' → 'summarize article'.
# - Respond with 'analyze (data or topic)' for analysis, e.g., 'analyze sales data' → 'analyze sales data'.
# - For multiple tasks, e.g., 'open facebook and set a reminder for tomorrow' → 'open facebook, reminder tomorrow'.
# - For goodbye or exit commands, e.g., 'bye Brainy' → 'exit'.
# - For unrecognized or ambiguous queries, respond with 'general (query)', e.g., 'what's up?' → 'general what's up?'.
# - Ensure responses are precise, lowercase, and comma-separated for multiple tasks.
# """

# # Chat history with lowercase roles for consistency
# ChatHistory = [
#     {"role": "user", "content": "how are you?"},
#     {"role": "assistant", "content": "general how are you"},
#     {"role": "user", "content": "do you like pizza?"},
#     {"role": "assistant", "content": "general do you like pizza"},
#     {"role": "user", "content": "open chrome and tell me about quaid-e-azam"},
#     {"role": "assistant", "content": "open chrome, general tell me about quaid-e-azam"},
#     {"role": "user", "content": "open groq and microsoft edge"},
#     {"role": "assistant", "content": "open groq, open microsoft edge"},
#     {"role": "user", "content": "what is today's date and remind me of a dancing performance on 5th June at 11am"},
#     {"role": "assistant", "content": "general what is today's date, reminder 11:00am 5th June dancing performance"},
#     {"role": "user", "content": "chat with me"},
#     {"role": "assistant", "content": "general chat with me"},
# ]

# def FirstLayerDMM(prompt: str = "test"):
#     """Categorize the user's query using Cohere API with enhanced processing."""
#     try:
#         # Log the incoming prompt
#         logging.info(f"Received prompt: {prompt}")

#         # Construct a single message by combining preamble, chat history, and prompt
#         history_text = "\n".join(
#             [f"{msg['role'].title()}: {msg['content']}" for msg in ChatHistory]
#         )
#         message = f"{preamble}\n\n--- Previous Interactions ---\n{history_text}\n\n--- Current Query ---\nUser: {prompt}"

#         # Stream response from Cohere API
#         stream = co.chat_stream(
#             model="command-r-plus",
#             message=message,  # Use 'message' instead of 'messages'
#             temperature=0.7,
#             prompt_truncation="OFF",
#             connectors=[],
#             max_tokens=512
#         )

#         response = ""
#         for event in stream:
#             if event.event_type == "text-generation":
#                 response += event.text

#         # Handle empty response
#         if not response.strip():
#             logging.warning("Empty response from API")
#             return ["general (empty response)"]

#         # Process response: normalize and split
#         response = re.sub(r'\s+', ' ', response.strip())
#         response = response.split(",")
#         response = [task.strip() for task in response if task.strip()]

#         # Filter valid tasks
#         valid_tasks = []
#         for task in response:
#             for func in funcs:
#                 if task.startswith(func):
#                     valid_tasks.append(task)
#                     break
#         response = valid_tasks if valid_tasks else response

#         # Recursive call if categorization fails
#         if any("(query)" in task for task in response):
#             logging.warning(f"Ambiguous response: {response}. Retrying...")
#             return FirstLayerDMM(prompt=prompt)

#         # Update chat history
#         if response != ["exit"]:
#             ChatHistory.append({"role": "user", "content": prompt})
#             ChatHistory.append({"role": "assistant", "content": ", ".join(response)})
#             # Keep history manageable (e.g., last 20 messages)
#             if len(ChatHistory) > 20:
#                 ChatHistory[:] = ChatHistory[-20:]

#         # Log the categorized response
#         logging.info(f"Categorized response: {response}")
#         return response

#     except Exception as e:
#         logging.error(f"API call failed: {str(e)}")
#         print(f"[ERROR] API call failed: {str(e)}")
#         return ["general (error occurred)"]

# # Main loop with exit condition
# if __name__ == "__main__":
#     try:
#         while True:
#             user_input = input(">>> ").strip()
#             result = FirstLayerDMM(user_input)
#             print(result)
#             if "exit" in result:
#                 logging.info("Exiting program due to 'exit' command")
#                 break
#     except KeyboardInterrupt:
#         logging.info("Program terminated by user")
#         print("\n[INFO] Program terminated by user")



# from rev_ai import apiclient as api
# from rev_ai.models.customer_url_data import CustomerUrlData

# # Create your client using your access token
# access_token = "your access token here"
# client = api.RevAiAPIClient(access_token)

# # Submit an audio file to Rev AI
# source_config = CustomerUrlData(url="https://www.rev.ai/FTC_Sample_1.mp3")
# job = client.submit_job_url(source_config=url)

# # Check your job's status
# details = client.get_job_details(job.id);

# # Retrieve your transcript
# # transcript = client.get_transcript_text(jort hf_api; api = hf_api.HfApi(token=""); print(api.model_info("stabilityai/stable-diffusion-3.5-large"))

# from diffusers import BitsAndBytesConfig, SD3Transformer2DModel
# from diffusers import StableDiffusion3Pipeline
# import torch

# model_id = "stabilityai/stable-diffusion-3.5-large"

# nf4_config = BitsAndBytesConfig(
#     load_in_4bit=True,
#     bnb_4bit_quant_type="nf4",
#     bnb_4bit_compute_dtype=torch.bfloat16
# )
# model_nf4 = SD3Transformer2DModel.from_pretrained(
#     model_id,
#     subfolder="transformer",
#     quantization_config=nf4_config,
#     torch_dtype=torch.bfloat16
# )

# pipeline = StableDiffusion3Pipeline.from_pretrained(
#     model_id, 
#     transformer=model_nf4,
#     torch_dtype=torch.bfloat16
# )
# pipeline.enable_model_cpu_offload()

# prompt = "A whimsical and creative image depicting a hybrid creature that is a mix of a waffle and a hippopotamus, basking in a river of melted butter amidst a breakfast-themed landscape. It features the distinctive, bulky body shape of a hippo. However, instead of the usual grey skin, the creature's body resembles a golden-brown, crispy waffle fresh off the griddle. The skin is textured with the familiar grid pattern of a waffle, each square filled with a glistening sheen of syrup. The environment combines the natural habitat of a hippo with elements of a breakfast table setting, a river of warm, melted butter, with oversized utensils or plates peeking out from the lush, pancake-like foliage in the background, a towering pepper mill standing in for a tree.  As the sun rises in this fantastical world, it casts a warm, buttery glow over the scene. The creature, content in its butter river, lets out a yawn. Nearby, a flock of birds take flight"

# image = pipeline(
#     prompt=prompt,
#     num_inference_steps=28,
#     guidance_scale=4.5,
#     max_sequence_length=512,
# ).images[0]
# image.save("whimsical.png")



#                   REALTIME - SEARCH ENGINE (TEST)
# import os
# from groq import Groq
# from json import dump, load
# import datetime
# from dotenv import dotenv_values
# import logging
# import re
# from googlesearch import search
# import requests
# from bs4 import BeautifulSoup

# # Configure logging
# logging.basicConfig(
#     filename="search_engine.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# # Define .env file path
# ENV_PATH = r"C:\Users\Naveed Asghar\Desktop\B.R.A.I.N.Y\.env"

# # Load environment variables
# try:
#     config = dotenv_values(ENV_PATH)
# except Exception as e:
#     logging.error(f"Failed to load .env file from {ENV_PATH}: {str(e)}")
#     print(f"[ERROR] Failed to load .env file: {str(e)}")
#     exit(1)

# # Retrieve environment variables with fallbacks
# Username = config.get("Username", "User")
# AssistantName = config.get("AssistantName", "Brainy")
# GroqAPIKey = config.get("GroqAPIKey")

# # Validate Groq API key
# if not GroqAPIKey:
#     logging.error("GroqAPIKey not found in .env file")
#     print("[ERROR] GroqAPIKey not found in .env file")
#     exit(1)

# # Initialize Groq client
# try:
#     client = Groq(api_key=GroqAPIKey)
# except Exception as e:
#     logging.error(f"Failed to initialize Groq client: {str(e)}")
#     print(f"[ERROR] Failed to initialize Groq client: {str(e)}")
#     exit(1)

# # Define chat log file path
# CHAT_LOG_PATH = os.path.join(os.path.dirname(ENV_PATH), "Data", "ChatLog.json")

# # Initialize chat history
# try:
#     with open(CHAT_LOG_PATH, "r") as f:
#         loaded_messages = load(f)
#     # Filter messages to ensure they have 'role' and 'content'
#     messages = [msg for msg in loaded_messages if "role" in msg and "content" in msg]
# except FileNotFoundError:
#     messages = []
#     try:
#         os.makedirs(os.path.dirname(CHAT_LOG_PATH), exist_ok=True)
#         with open(CHAT_LOG_PATH, "w") as f:
#             dump([], f)
#     except Exception as e:
#         logging.error(f"Failed to create chat log file: {str(e)}")
#         print(f"[ERROR] Failed to create chat log file: {str(e)}")
#         exit(1)

# # System message for chatbot
# System = f"""Hello, I am {Username}, You are {AssistantName}, a very accurate and advanced AI chatbot with real-time up-to-date information from the internet.
# *** Provide answers in a professional manner, using proper grammar, punctuation, and formatting. ***
# *** Answer the question based on provided search results or real-time data, keeping responses concise. ***
# *** Reply in English only, even if the input is in another language. ***
# *** Do not include notes or mention training data. ***
# *** If the user says 'bye Brainy', respond with 'Goodbye!' and exit. ***
# """

# # System instructions
# SystemChatBot = [{"role": "system", "content": System}]

# def RealtimeInformation():
#     """Generate real-time date and time information."""
#     current_date_time = datetime.datetime.now()
#     day = current_date_time.strftime("%A")
#     date = current_date_time.strftime("%d")
#     month = current_date_time.strftime("%B")
#     year = current_date_time.strftime("%Y")
#     hour = current_date_time.strftime("%H")
#     minute = current_date_time.strftime("%M")
#     second = current_date_time.strftime("%S")
#     data = (
#         f"Please use this real-time information if needed:\n"
#         f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}\n"
#         f"Time: {hour}:{minute}:{second}"
#     )
#     return data

# def AnswerModifier(Answer):
#     """Modify the response for better formatting."""
#     lines = Answer.split('\n')
#     non_empty_lines = [line for line in lines if line.strip()]
#     return '\n'.join(non_empty_lines)

# def GoogleSearch(query, num_results=5):
#     """Perform a Google search and return formatted results."""
#     try:
#         results = list(search(query, advanced=True, num_results=num_results))
#         answer = f"Search results for '{query}':\n\n"
#         for idx, result in enumerate(results, 1):
#             answer += f"{idx}. **{result.title}**\n   Description: {result.description or 'No description available.'}\n   URL: {result.url}\n\n"
#         return answer
#     except Exception as e:
#         logging.error(f"Google search failed for query '{query}': {str(e)}")
#         return f"Failed to retrieve search results for '{query}'. Please try again later."

# def WebScrape(url, max_chars=500):
#     """Scrape a webpage for a brief summary."""
#     try:
#         headers = {'User-Agent': 'Mozilla/5.0'}
#         response = requests.get(url, headers=headers, timeout=5)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.text, 'html.parser')
#         text = ' '.join(p.get_text() for p in soup.find_all('p'))
#         text = re.sub(r'\s+', ' ', text).strip()
#         return text[:max_chars] + '...' if len(text) > max_chars else text
#     except Exception as e:
#         logging.warning(f"Web scraping failed for {url}: {str(e)}")
#         return "Unable to scrape content from this page."

# def RealTimeSearchEngine(prompt: str, max_retries=3):
#     """Perform a real-time search and generate a response."""
#     try:
#         # Log the incoming query
#         logging.info(f"Received search query: {prompt}")

#         # Handle exit command
#         if prompt.lower() == "bye brainy":
#             return "Goodbye!"

#         # Load chat history with filtering
#         try:
#             with open(CHAT_LOG_PATH, "r") as f:
#                 loaded_messages = load(f)
#             # Filter messages to ensure they have 'role' and 'content'
#             messages_local = [msg for msg in loaded_messages if "role" in msg and "content" in msg]
#         except Exception as e:
#             logging.warning(f"Error loading chat history: {str(e)}. Starting with empty history.")
#             messages_local = []

#         # Append user query with correct format
#         messages_local.append({"role": "user", "content": prompt})

#         # Perform Google search
#         search_result = GoogleSearch(prompt)
#         # Scrape top result for additional context
#         try:
#             top_url = list(search(prompt, num_results=1))[0]
#             search_result += f"\nSummary from top result:\n{WebScrape(top_url)}\n"
#         except Exception as e:
#             logging.warning(f"Failed to scrape top result: {str(e)}")

#         # Prepare messages for Groq API
#         messages_to_send = SystemChatBot + [
#             {"role": "system", "content": RealtimeInformation()},
#             {"role": "system", "content": search_result}
#         ]
#         messages_to_send.extend(messages_local)

#         # Validate all messages have 'role' and 'content'
#         for msg in messages_to_send:
#             if "role" not in msg or "content" not in msg:
#                 logging.error(f"Malformed message detected: {msg}")
#                 raise ValueError("All messages must have 'role' and 'content' keys.")

#         # Call Groq API
#         completion = client.chat.completions.create(
#             model="llama3-70b-8192",
#             messages=messages_to_send,
#             temperature=0.7,
#             max_tokens=2048,
#             top_p=1,
#             stream=True,
#             stop=None
#         )

#         Answer = ""
#         for chunk in completion:
#             if chunk.choices[0].delta.content:
#                 Answer += chunk.choices[0].delta.content

#         Answer = Answer.strip().replace("</s>", "")
#         modified_answer = AnswerModifier(Answer)

#         # Update chat history with assistant's response
#         messages_local.append({"role": "assistant", "content": modified_answer})
#         if len(messages_local) > 20:
#             messages_local = messages_local[-20:]

#         # Save chat history
#         try:
#             with open(CHAT_LOG_PATH, "w") as f:
#                 dump(messages_local, f, indent=4)
#         except Exception as e:
#             logging.error(f"Failed to save chat log: {str(e)}")
#             print(f"[ERROR] Failed to save chat log: {str(e)}")

#         logging.info(f"Response: {modified_answer}")
#         return modified_answer

#     except Exception as e:
#         logging.error(f"Search engine error: {str(e)}")
#         print(f"[ERROR] Search engine error: {str(e)}")
#         if max_retries > 0:
#             logging.info(f"Retrying query '{prompt}' ({max_retries} retries left)")
#             return RealTimeSearchEngine(prompt, max_retries - 1)
#         return "An error occurred. Please try again later."

# # Main program
# if __name__ == "__main__":
#     try:
#         print(f"Welcome to {AssistantName}'s Real-Time Search Engine! Type 'bye Brainy' to exit.")
#         while True:
#             prompt = input(">>> ").strip()
#             if not prompt:
#                 continue
#             response = RealTimeSearchEngine(prompt)
#             print(response)
#             if response == "Goodbye!":
#                 logging.info("Exiting program due to 'exit' command")
#                 break
#     except KeyboardInterrupt:
#         logging.info("Program terminated by user")
#         print("\n[INFO] Program terminated by user")



#                   FINALLY AFFAN U CREATED IT CONGRATUALTIONS TO MYSELF AFTER THE PRACTICE OF PYTHON 1 YEAR AND STRUGGLE I HAVE REACHED TO THIS POINT AND CREATED MY DREAM BRAINY