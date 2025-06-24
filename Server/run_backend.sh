cat db.conf > .env
docker compose down
docker compose up -d
rm -fr venv/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 run.py