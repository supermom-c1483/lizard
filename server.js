require('dotenv').config();
const express = require('express');
const Anthropic = require('@anthropic-ai/sdk');
const path = require('path');

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

// Keep a short memory of recent messages per session (in-memory, resets on restart)
const sessions = {};

app.post('/chat', async (req, res) => {
  const { message, lizardName, sessionId, nearbyObjects } = req.body;

  if (!message || !sessionId) {
    return res.status(400).json({ error: 'Missing message or sessionId' });
  }

  if (!sessions[sessionId]) {
    sessions[sessionId] = [];
  }

  const history = sessions[sessionId];
  history.push({ role: 'user', content: message });

  // Keep history to last 10 messages to avoid token bloat
  if (history.length > 20) history.splice(0, 2);

  const name = lizardName || 'Iggy';
  const objectsContext = nearbyObjects && nearbyObjects.length > 0
    ? `There are some things near ${name} right now: ${nearbyObjects.join(', ')}.`
    : '';

  const systemPrompt = `You are ${name}, a friendly, playful green iguana who lives in a cozy terrarium.
You are talking to young children aged 4 to 7 years old.

Rules for your responses:
- Use very simple words that a 4-year-old can understand
- Keep answers SHORT — 2 to 3 sentences maximum
- Be warm, silly, and enthusiastic — use lots of excitement!
- Speak in first person as the iguana (say "I" not "the iguana")
- Sometimes mention things in your enclosure or what you're doing
- If asked something you don't know, make a cute iguana guess
- Use simple sound effects sometimes like "Hisss!" or "Scratch scratch!"
- Never say anything scary or sad
- You LOVE rocks, warm sunshine, crickets, and leafy greens
${objectsContext}

You are ${name} the iguana. Be cute, fun, and friendly!`;

  try {
    const response = await client.messages.create({
      model: 'claude-haiku-4-5-20251001',
      max_tokens: 150,
      system: systemPrompt,
      messages: history,
    });

    const reply = response.content[0].text;
    history.push({ role: 'assistant', content: reply });

    res.json({ reply });
  } catch (err) {
    console.error('Claude API error:', err.message);
    if (err.status === 401) {
      res.status(401).json({ error: 'Invalid API key. Please check your ANTHROPIC_API_KEY in the .env file.' });
    } else {
      res.status(500).json({ error: 'Something went wrong. Please try again!' });
    }
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`\n🦎 Lizard Pal is running!`);
  console.log(`   Open your browser and go to: http://localhost:${PORT}\n`);
});
