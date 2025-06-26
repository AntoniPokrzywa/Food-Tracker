#cat db.conf > .env
docker compose down
docker compose up -d
rm -fr venv/
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python run.py