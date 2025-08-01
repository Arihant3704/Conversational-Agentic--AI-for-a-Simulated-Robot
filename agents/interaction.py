import logging

logging.basicConfig(level=logging.INFO, filename='/home/arihant/car/logs/agent.log', format='%(asctime)s - %(levelname)s - %(message)s')

def listen_for_command():
    logging.info("Interaction Tool: Listening for command.")
    return input("Please enter your command: ")

def generate_speech(text):
    logging.info(f"Interaction Tool: Generating speech: {text}")
    print(f"Interaction Tool: {text}")
