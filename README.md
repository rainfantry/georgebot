# GEORGEBOT - FIELD MANUAL FOR DUMB CUNTS
## Multi-Brain Aussie Voice Assistant
**Author:** George Wu
**Platform:** Windows
**Status:** Operational

---

## WHAT THE FUCK IS THIS

Georgebot is a voice assistant with swappable AI brains. Talk to it, it talks back. It remembers shit without you telling it to. It swears like an Aussie.

**Brains available:**
- `ollama` - Local models, free, no internet needed
- `grok` - xAI API, paid, needs internet

**Voice:**
- ElevenLabs TTS (sounds good)
- Windows SAPI fallback (sounds like shit but works offline)

---

## INSTALLATION (DO THIS FIRST YA DRONGO)

### Step 1: Clone the repo
```powershell
git clone https://github.com/rainfantry/georgebot.git
cd georgebot
```

### Step 2: Install Python dependencies
```powershell
pip install -e .
```

### Step 3: Install Ollama (for local brain)
1. Download from https://ollama.ai
2. Run installer
3. Restart PowerShell
4. Pull a model:
```powershell
ollama pull mistral:7b
```

### Step 4: Set up API keys
Create `.env` file:
```
ELEVENLABS_API_KEY=sk_your_key_here
GROK_API_KEY=xai-your_key_here
ELEVENLABS_VOICE_ID=your_voice_id
```

---

## QUICK START

```powershell
# Run with local Ollama
python georgebot.py --brain ollama

# Run with Grok API
python georgebot.py --brain grok

# Run silent (no voice)
python georgebot.py --brain ollama --no-voice
```

---

## THE THREE BRAINS (CUSTOM MODELS)

Georgebot has 3 specialized local brains. Build them:

### Build Commands
```powershell
cd C:\Users\gwu07\Desktop\georgebot
ollama create georgebot-chat -f models\georgebot-chat.Modelfile
ollama create georgebot-plan -f models\georgebot-plan.Modelfile
ollama create georgebot-build -f models\georgebot-build.Modelfile
```

### What Each Brain Does

| Brain | Base Model | Speed | Use For |
|-------|------------|-------|---------|
| `georgebot-chat` | mistral:7b (4.4GB) | Fast | Casual chat, quick answers, banter |
| `georgebot-plan` | deepseek-coder:33b (18GB) | Slow | Architecture, planning, complex reasoning |
| `georgebot-build` | deepseek-coder:6.7b (3.8GB) | Fast | Code generation, fixes, snippets |

### Switching Brains Mid-Session
```
You> model georgebot-chat
[Switched: mistral -> georgebot-chat]

You> model georgebot-plan
[Switched: georgebot-chat -> georgebot-plan]

You> model georgebot-build
[Switched: georgebot-plan -> georgebot-build]
```

---

## IN-SESSION COMMANDS

| Command | What It Does |
|---------|--------------|
| `exit` | Fuck off, end session |
| `clear` | Wipe conversation memory |
| `brain ollama` | Switch to local Ollama |
| `brain grok` | Switch to Grok API |
| `model <name>` | Switch Ollama model |
| `models` | List installed Ollama models |
| `pull <name>` | Download new Ollama model |
| `create` | Build default georgebot model |
| `load <topic>` | Search knowledge base |
| `remember <note>` | Save note to memory |
| `files` | List knowledge files |
| `help` | Show all commands |

---

## NATURAL LANGUAGE MEMORY

Just talk normally. It auto-remembers facts.

### Auto-Store (just say it)
```
You> my name is george
[Remembered: name: george]

You> i live in sydney
[Remembered: location: sydney]

You> i work at TAFE
[Remembered: work: tafe]
```

### Auto-Recall (just ask)
```
You> what's my name?
Georgebot: Your name's George, ya drongo.

You> where do i live?
Georgebot: Sydney, mate.
```

### Patterns It Detects
- "my name is X"
- "i am X"
- "call me X"
- "i live in X"
- "i work at/for X"
- "i like X"
- "i hate X"

---

## TROUBLESHOOTING (WHEN SHIT BREAKS)

### "Ollama not found"
```powershell
# Check if installed
where ollama

# If not found, reinstall from ollama.ai
# Restart PowerShell after install
```

### "Model not found"
```powershell
# Pull it first
ollama pull mistral:7b

# Check what you have
ollama list
```

### "No module named elevenlabs"
```powershell
# You're using wrong Python. Use:
python -m pip install elevenlabs

# NOT python3 (that's Windows Store Python)
```

### "Voice not working"
- Check ELEVENLABS_API_KEY in .env
- Check ELEVENLABS_VOICE_ID in .env
- Will fallback to Windows SAPI if ElevenLabs fails

### "Slow as fuck"
- Use smaller model: `model mistral:7b`
- Use georgebot-chat instead of georgebot-plan
- The 33b model is slow but smart

### "Out of memory"
```powershell
# Use quantized or smaller model
ollama pull mistral:7b-q4_0
ollama pull tinyllama
```

---

## FILE STRUCTURE

```
georgebot/
├── georgebot.py          # Main CLI
├── config.py             # Settings, brain loader, TTS
├── rag.py                # Knowledge base search
├── session.py            # Conversation memory
├── pyproject.toml        # pip install config
├── .env                  # API keys (gitignored)
├── clients/
│   ├── base.py           # Brain interface
│   ├── ollama.py         # Local Ollama client
│   └── grok.py           # Grok API client
├── models/
│   ├── georgebot-chat.Modelfile
│   ├── georgebot-plan.Modelfile
│   └── georgebot-build.Modelfile
├── knowledge/            # RAG markdown files
└── memory/               # Session files (gitignored)
```

---

## POWERSHELL ALIASES

Add to your PowerShell profile (`notepad $PROFILE`):
```powershell
function gb { python C:\Users\gwu07\Desktop\georgebot\georgebot.py --brain ollama $args }
function gb-chat { python C:\Users\gwu07\Desktop\georgebot\georgebot.py --brain ollama; model georgebot-chat }
function gb-plan { python C:\Users\gwu07\Desktop\georgebot\georgebot.py --brain ollama; model georgebot-plan }
function gb-build { python C:\Users\gwu07\Desktop\georgebot\georgebot.py --brain ollama; model georgebot-build }
function say { python C:\Users\gwu07\Desktop\talkytalk\talkytalk.py $args }
```

---

## RECOMMENDED MODELS

### For Chat
| Model | Size | Speed | Quality |
|-------|------|-------|---------|
| mistral:7b | 4.4GB | Fast | Good |
| llama3:8b | 4.7GB | Medium | Great |

### For Code
| Model | Size | Speed | Quality |
|-------|------|-------|---------|
| deepseek-coder:6.7b | 3.8GB | Fast | Great |
| deepseek-coder:33b | 18GB | Slow | Excellent |

### For Speed (Low RAM)
| Model | Size | Speed | Quality |
|-------|------|-------|---------|
| phi:2.7b | 1.6GB | Very Fast | OK |
| tinyllama:1b | 637MB | Instant | Basic |

---

## DEPENDENCIES

```
requests>=2.28.0
elevenlabs>=1.0.0
ollama (external, install from ollama.ai)
```

---

## LICENSE

MIT - Do whatever the fuck you want.

---

**VIDIMUS OMNIA**

*George Wu - 2026*
