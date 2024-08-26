# Llama Chat Bot

## Description

The Llama Chat Bot is an interactive conversational agent powered by the Llama model. This bot is designed to provide a seamless and engaging chat experience leveraging advanced language processing capabilities.

## Getting Started

To get started with the Llama Chat Bot, follow these steps:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/llama-chat-bot.git
cd llama-chat-bot
chmod +x dev.sh
./dev.sh
```
### 2. Run the Development Script
Ensure you have Git Bash or a compatible shell environment. Execute the dev.sh script to set up and start the chat bot. This script will handle the installation of dependencies, pull the necessary model, and start the bot:

```bash

./dev.sh
```

### 3. Dependencies
The dev.sh script will automatically install the required Python packages listed in requirements.txt, pull the Llama model using ollama, and start the chat bot. Ensure you have Python and Git installed on your system.

### 4. Accessing the Chat Bot
Once the dev.sh script has completed, the chat bot should be up and running. You can access it through the interface provided by the bot or any other means as configured in your app.py.

### Prerequisites

* Git Bash or a compatible shell environment.
* Python (ensure pip is available and configured).
* Streamlit and Ollama should be installed (these will be handled by the script).

### Troubleshooting
If you encounter any issues, check the following:

* Script Permissions: Ensure the dev.sh file has execute permissions. If not, make it executable with:
```bash
chmod +x dev.sh
```

* Command Errors: Verify that all commands in the dev.sh script are correct and executable in your environment. Check error.log if you encounter any errors.

* Dependencies: Ensure all necessary dependencies are correctly installed. You can manually install them by running:

```bash
pip install -r requirements.txt
```


### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact
For any questions or support, please contact rk5970869@gmail.com.

