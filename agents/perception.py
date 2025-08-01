import logging

logging.basicConfig(level=logging.INFO, filename='/home/arihant/car/logs/agent.log', format='%(asctime)s - %(levelname)s - %(message)s')

def detect_object(object_name):
    logging.info(f"Perception Tool: Detecting object: {object_name}")
    print(f"Perception Tool: Detecting object: {object_name}")

def track_object(object_name):
    logging.info(f"Perception Tool: Tracking object: {object_name}")
    print(f"Perception Tool: Tracking object: {object_name}")

def describe_scene():
    logging.info("Perception Tool: Describing the scene.")
    print("Perception Tool: The room is well-lit. There is a table and a chair.")

def detect_obstacle():
    logging.info("Perception Tool: Detecting obstacle.")
    print("Perception Tool: Obstacle detected!")
