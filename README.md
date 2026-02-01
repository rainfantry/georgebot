# GEORGEBOT

Multi-brain Aussie voice assistant. Swappable AI backends. Natural language memory.

## Features

- **Swappable brains:** ollama (local, free), grok (xAI API)
- **Voice output:** ElevenLabs TTS via talkytalk, Windows SAPI fallback
- **Natural language memory:** auto-stores facts, auto-recalls on questions
- **RAG knowledge base:** markdown files, searchable

## Usage

```powershell
# With Grok (xAI)
python georgebot.py --brain grok

# With Ollama (local)
python georgebot.py --brain ollama

# No voice
python georgebot.py --brain grok --no-voice
```

## Commands

| Command | Description |
|---------|-------------|
| `exit` | End session |
| `clear` | Clear conversation + memory context |
| `brain <name>` | Switch brain (ollama, grok) |
| `load <topic>` | Manually load knowledge |
| `remember <note>` | Manually save note |
| `files` | List knowledge files |
| `help` | Show commands |

## Natural Language Memory

Just talk. It remembers.

```
You> my name is george
[Remembered: name: george]

You> what's my name?
Georgebot: Your name's George, ya drongo.
```

Auto-detects:
- "my name is X"
- "i am X"
- "call me X"
- "i live in X"
- "i work at X"
- "i like X"

## Setup

1. Clone repo
2. Copy `.env.example` to `.env`
3. Add API keys
4. `python georgebot.py --brain grok`

## Dependencies

- Python 3.x
- talkytalk (for voice)
- elevenlabs (pip install elevenlabs)
- requests (pip install requests)
- ollama (for local brain)

## Keys

Store in `.env` (gitignored):
```
ELEVENLABS_API_KEY=sk_...
GROK_API_KEY=xai-...
```

## License

MIT
