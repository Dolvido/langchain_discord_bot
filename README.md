# Dungeon's Fortress Discord Bot with Langchain Integration

Welcome to Dungeon's Fortress, a powerful Discord bot that brings the capabilities of the Langchain service right into your Discord server. Dive into a world of adventure, strategy, and linguistic intelligence.

## Features

- Dungeon Adventures: Engage with your community in thrilling dungeon adventures.
- Langchain Integration: Harness the power of linguistic analysis for user interactions, making each response dynamic and unique.
- Interactive Games: Beyond dungeons, there are games that members of your server can participate in.
- Moderation Tools: Ensure that your server remains a safe space for all users with built-in moderation tools.

## Getting Started

### Prerequisites

- Python 3.x
- discordpy library

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   
Install the required packages:
```
pip install -r requirements.txt
```
Follow the instructions mentioned here to set up your bot account and obtain your bot token.

Add your bot token:

Open the "Secrets (Environment variables)" panel and add a new secret with the key of TOKEN and paste your bot token as its value.

Run the bot 
```
python main.py
```

| Command         | Description                                      |
| --------------- | ------------------------------------------------ |
| `!startDungeon` | Initiates a new dungeon adventure                |
| `!langchain`    | Runs a linguistic analysis                       |
| `!game`          | Starts a new interactive game                    |
| `!ban [user]`    | Bans a user (admin only)                        |
| `!unban [user]`  | Unbans a user (admin only)                      |

