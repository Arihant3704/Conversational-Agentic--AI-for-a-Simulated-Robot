import logging

logging.basicConfig(level=logging.INFO, filename='/home/arihant/car/logs/agent.log', format='%(asctime)s - %(levelname)s - %(message)s')

def move_to_location(location):
    logging.info(f"Mobility Tool: Moving to location: {location}")
    print(f"Mobility Tool: Moving to location: {location}")

def follow_line():
    logging.info("Mobility Tool: Following the line.")
    print("Mobility Tool: Following the line.")

def return_to_start():
    logging.info("Mobility Tool: Returning to start.")
    print("Mobility Tool: Returning to start.")

def precision_movement(movement):
    logging.info(f"Mobility Tool: Executing precision movement: {movement}")
    print(f"Mobility Tool: Executing precision movement: {movement}")
