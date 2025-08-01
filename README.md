Based on the transcript from the video **"[How LLMs (Large Language Models) Power JetRover Robot](https://www.youtube.com/watch?v=JqcXD34EuyY)" by Merlin AI**, the JetRover robot demonstrates a variety of tasks and behaviors powered by LLMs and agentic AI design. Here's a list of **agent tools** you could build or define within this agentic AI framework based on the video:

---

### 🧠 **Perception & Understanding Tools**

1. **Object Detection Tool**

   * Detect specific objects like: `medicine box`, `remote control`, `breakfast`, `bath supplies`, `blocks`, `purple ball`, `carrot`, `Jeep`.

2. **Object Tracking Tool**

   * Follow a moving or stationary object (e.g., ball, carrot, Jeep).

3. **Scene Description Tool**

   * Visually analyze the surroundings and describe the environment using LLM-generated language.

4. **Obstacle Detection Tool**

   * Identify obstacles and trigger a stop or rerouting.

---

### 🏃 **Mobility & Navigation Tools**

5. **Move To Location Tool**

   * Navigate from one room to another (e.g., living room → bedroom → bathroom → kitchen).

6. **Follow Line Tool**

   * Follow a black line on the ground and stop upon detecting an obstacle.

7. **Return to Start Tool**

   * Return to a starting point after completing a task.

8. **Precision Movement Tool**

   * Execute specific movement sequences (e.g., spin, move forward/back/left/right for specified durations, drift in place).

---

### 📦 **Manipulation Tools**

9. **Pick and Place Tool**

   * Pick up objects (e.g., medicine box, remote, breakfast, bath supplies) and place them in a designated location.

10. **Sorting Tool**

* Sort colored blocks (red, green, blue) into matching boxes.

---

### 🧾 **Task Planning & Execution Tools**

11. **Command Interpretation Tool**

* Convert spoken or written commands into structured tasks the robot can execute.

12. **Task Sequencer Tool**

* Chain subtasks (e.g., move, detect, pick up, drop off) in order to complete a complex instruction.

13. **Error Recovery Tool**

* Handle failure cases, such as object not found or path blocked.

---

### 📡 **Interaction Tools**

14. **Voice Assistant Tool**

* Respond to “Hello, High Wonder” and listen for follow-up instructions.

15. **Speech Generation Tool**

* Generate voice responses like “Medicine box on the way” or “Jeep detected and ready to track.”

---

These tools form the **modular capabilities** of an agentic AI robot system powered by LLMs and perception/motor control stacks. Each tool corresponds to a discrete skill or API-style callable action that can be invoked by a central planner or decision engine.

Would you like a visual diagram of how these tools might be structured in an agent system?



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
