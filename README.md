# 🦎 Lizard Pal

An interactive iguana pet for kids! Kids can name their lizard, talk to it, and drag toys into its enclosure.

## Setup (5 minutes)

### Step 1 — Get your free API key
1. Go to https://console.anthropic.com
2. Sign up for a free account
3. Click **API Keys** → **Create Key**
4. Copy the key (it starts with `sk-ant-...`)

### Step 2 — Set up the project
Open a terminal in this folder and run:

```
npm install
```

### Step 3 — Add your API key
1. Find the file called `.env.example`
2. Make a copy of it and rename the copy to `.env`
3. Open `.env` and replace `your-api-key-here` with your actual key

The `.env` file should look like:
```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxx
PORT=3000
```

### Step 4 — Start the app
```
npm start
```

Then open your browser and go to: **http://localhost:3000**

---

## How to use

- **Name your lizard** — type in the name box at the top
- **Talk to it** — type in the chat box or click the quick question buttons
- **Click the iguana** — it will say something!
- **Drag items** — drag rocks, plants, water dishes, and more around the enclosure
- **Add toys** — drag items from the Toy Shelf into the enclosure; the iguana will react!

---

## Troubleshooting

**"Invalid API key" error** — Make sure your `.env` file has the correct key and you restarted the server.

**Blank page** — Make sure you ran `npm install` and the server is running (`npm start`).

**The iguana doesn't move** — It wanders on its own every few seconds. Click it to make it talk!
