# Conversational Agentic AI for a Simulated Robot

This project is a simulation of the agentic AI system described in the `aicar.md` file, based on the JetRover robot from the Merlin AI video. This version uses the Gemini API to interpret natural language commands.

## Project Structure

- **`main.py`**: The main entry point for the conversational AI. It takes user commands and orchestrates the agent tools.
- **`agents/`**: A Python package containing the different agent tools, categorized by function:
    - `perception.py`: Tools for understanding the environment (object detection, scene description, etc.).
    - `mobility.py`: Tools for movement and navigation.
    - `manipulation.py`: Tools for interacting with objects (picking, placing, sorting).
    - `task_planning.py`: The core of the AI's intelligence. It uses the Gemini API to interpret user commands and translate them into structured JSON.
    - `interaction.py`: Tools for communicating with the user (listening for commands, generating speech).
- **`logs/`**: Contains the `agent.log` file, which logs all the actions taken by the agents.
- **`output/`**: A directory for any output files (currently unused in this simulation).
- **`doc/`**: Contains this README file.
- **`.env`**: A file to store your Gemini API key (not committed to Git).
- **`requirements.txt`**: A list of the Python dependencies for this project.

## How to Run

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Set up your API key:**
    - Open the `.env` file and replace `your_gemini_api_key_here` with your actual Gemini API key.
3.  **Run the main program:**
    ```bash
    python3 main.py
    ```
4.  The AI will greet you and prompt you for commands. You can now use natural language to give commands like:
    - "Can you detect the medicine box?"
    - "I want you to track the purple ball."
    - "Describe the scene for me."
    - "Go to the bedroom."
    - "Pick up the remote and put it on the table."
    - "Sort the red blocks."
    - "goodbye"

## How it Works

The `main.py` script now relies on the `task_planning.py` agent to interpret user commands. The `interpret_command` function in `task_planning.py` sends a request to the Gemini API with a carefully crafted prompt. The prompt instructs the model to act as the robot's brain and return a JSON object with the user's `intent` and any relevant `entities`.

The `main.py` script then parses this JSON object to determine which agent tool to call and what parameters to pass to it. This makes the AI much more flexible and capable of understanding a wider range of natural language commands.