# 🦎 Lizard Pal

An interactive iguana pet for kids! Kids can name their lizard, talk to it, and drag toys into its enclosure.

---

## How to set up (no technical skills needed!)

### Step 1 — Get your free API key
1. Go to **https://console.anthropic.com** and sign up for a free account
2. Click **API Keys** on the left, then click **Create Key**
3. Copy the key — it starts with `sk-ant-...`

---

### Step 2 — Add your API key to the app

1. Find the file called **`.env.example`** in the lizard folder
2. Make a copy of it and rename the copy to **`.env`** (no ".example" at the end)
3. Open the **`.env`** file with Notepad (Windows) or TextEdit (Mac)
4. Replace `your-api-key-here` with your actual key
5. Save the file — it should look like this:
   ```
   ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxx
   PORT=3000
   ```

> **Tip for Mac users:** Files starting with `.` may be hidden. Press **Cmd + Shift + .** in Finder to show hidden files.

---

### Step 3 — Start the app

**On a Mac:**
- Double-click **`START-Mac.command`**
- If you get a security warning, right-click it → Open → Open

**On Windows:**
- Double-click **`START-Windows.bat`**

Your browser will open automatically to the Lizard Pal page!

> If Python is not installed:
> - Mac: install from https://www.python.org/downloads/
> - Windows: install from https://www.python.org/downloads/ — make sure to check **"Add Python to PATH"** during install!

---

## How to use Lizard Pal

- **Name your lizard** — type a name in the box at the top
- **Talk to it** — type in the chat box or press the big buttons (Say hi!, Favorite food?, etc.)
- **Click the iguana** — it will say something!
- **Drag items** — drag rocks, plants, the water dish, food bowl, and toys around the enclosure
- **Toy shelf** — drag items from the shelf into the enclosure and the iguana reacts!

---

## Troubleshooting

| Problem | Fix |
|---|---|
| "Invalid API key" | Make sure your `.env` file has the right key and you restarted the app |
| Browser doesn't open | Manually go to **http://localhost:3000** |
| "Python not found" | Install Python from https://www.python.org/downloads/ |
| App won't start on Mac | Right-click START-Mac.command → Open → Open |
