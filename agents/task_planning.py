import logging
import os
import google.generativeai as genai
from dotenv import load_dotenv
import json

load_dotenv()

# Configure Gemini API
gemini_api_key = os.environ.get("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")
genai.configure(api_key=gemini_api_key)

logging.basicConfig(level=logging.INFO, filename='/home/arihant/car/logs/agent.log', format='%(asctime)s - %(levelname)s - %(message)s')

def interpret_command(command):
    logging.info(f"Task Planning Tool: Interpreting command with Gemini: {command}")
    print(f"Task Planning Tool: Interpreting command with Gemini: {command}")

    model = genai.GenerativeModel('gemini-1.5-flash-latest')

    prompt = f"""
    You are the brain of a robot. Your job is to interpret a user's command and translate it into a structured JSON object.
    The JSON object should have two keys: 'intent' and 'entities'.
    The 'intent' should be one of the following: 'detect_object', 'track_object', 'describe_scene', 'detect_obstacle', 'move_to_location', 'follow_line', 'return_to_start', 'precision_movement', 'pick_and_place', 'sort_blocks', 'exit'.
    The 'entities' should be a dictionary of any relevant information, such as 'object_name', 'location', 'movement', or 'color'.

    Here are some examples:
    - Command: "detect the medicine box"
      JSON: {{"intent": "detect_object", "entities": {{"object_name": "medicine box"}}}}
    - Command: "move to the bedroom"
      JSON: {{"intent": "move_to_location", "entities": {{"location": "bedroom"}}}}
    - Command: "sort the red blocks"
      JSON: {{"intent": "sort_blocks", "entities": {{"color": "red"}}}}
    - Command: "goodbye"
      JSON: {{"intent": "exit", "entities": {{}}}}

    Now, interpret the following command:
    Command: "{command}"
    JSON:
    """

    try:
        response = model.generate_content(prompt)
        # The response from the model might be in a markdown code block, so we need to clean it up
        cleaned_response = response.text.strip().replace('```json', '').replace('```', '')
        return json.loads(cleaned_response)
    except Exception as e:
        logging.error(f"Error interpreting command with Gemini: {e}")
        print(f"Error interpreting command with Gemini: {e}")
        return None

def sequence_tasks(tasks):
    logging.info(f"Task Planning Tool: Sequencing tasks: {tasks}")
    print(f"Task Planning Tool: Sequencing tasks: {tasks}")

def recover_from_error(error):
    logging.info(f"Task Planning Tool: Recovering from error: {error}")
    print(f"Task Planning Tool: Recovering from error: {error}")