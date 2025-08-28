python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt


----
.env

GROQ_API_KEY=***
GROQ_API_URL=https://api.groq.com/v1/llm/generate
INPUT_DIR=./input
OUTPUT_DIR=./output
CHROMA_DIR=./output/chroma_db
LOG_FILE=./logs/pipeline.log
