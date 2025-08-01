import logging

logging.basicConfig(level=logging.INFO, filename='/home/arihant/car/logs/agent.log', format='%(asctime)s - %(levelname)s - %(message)s')

def pick_and_place(item):
    logging.info(f"Manipulation Tool: Picking and placing {item}")
    print(f"Manipulation Tool: Picking and placing {item}")

def sort_blocks(color):
    logging.info(f"Manipulation Tool: Sorting {color} blocks.")
    print(f"Manipulation Tool: Sorting {color} blocks.")
