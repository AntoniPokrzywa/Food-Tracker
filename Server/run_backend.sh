#cat db.conf > .env
docker compose down
docker compose up -d
rm -fr venv/
python -m venv venv
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
    source venv/bin/activate
elif [[ "$OSTYPE" == "msys"* || "$OSTYPE" == "cygwin"* || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    echo "Unsupported OS: $OSTYPE"
    exit 1
fi
pip install -r requirements.txt
python run.py