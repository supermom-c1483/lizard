#!/bin/bash
# Double-click this file on a Mac to start Lizard Pal!
cd "$(dirname "$0")"

echo ""
echo "🦎 Starting Lizard Pal..."
echo ""

# Check for Python 3
if ! command -v python3 &> /dev/null; then
  echo "❌ Python 3 is not installed."
  echo "   Please install it from: https://www.python.org/downloads/"
  read -p "Press Enter to close..."
  exit 1
fi

# Check for .env file
if [ ! -f ".env" ]; then
  echo "❌ Missing .env file!"
  echo ""
  echo "   1. Find the file called '.env.example' in this folder"
  echo "   2. Make a copy of it and rename the copy to '.env'"
  echo "   3. Open .env and replace 'your-api-key-here' with your real API key"
  echo "   4. Save and double-click this file again"
  echo ""
  read -p "Press Enter to close..."
  exit 1
fi

# Open browser after a short delay
(sleep 2 && open "http://localhost:3000") &

python3 server.py
