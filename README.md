# Osvaldo Romberg Chat Model v5

An AI-powered chat model that embodies the personality and knowledge of Argentine artist Osvaldo Romberg (1938-2019).

## Setup

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your API keys:
```bash
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

## Project Structure

```
.
├── data/                      # JSON data files
│   ├── romberg_interview_data.jsonl
│   ├── romberg_web_data.json
│   └── romberg_catalogs_data.json
├── src/
│   ├── agents/               # Agent definitions
│   │   └── romberg_agent.py
│   ├── tools/                # Search tools
│   │   └── search_tools.py
│   └── main.py              # Main application
├── requirements.txt
└── README.md
```

## Usage

Run the chat interface:
```bash
python src/main.py
```

Type your messages and interact with the Osvaldo Romberg AI model. Type 'exit' to quit the chat. 