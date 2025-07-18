# === Backend ===
<<<<<<< HEAD

cd backend
python -m venv venv
venv\Scripts\activate # (Windows)
pip install -r requirements.txt
pip install openai==0.28
uvicorn main:app --reload
python -m uvicorn main:app --reload

# === Frontend ===

cd ../frontend
npm install
=======
cd backend
python -m venv venv
venv\Scripts\activate   # (Windows)
pip install -r requirements.txt
python -m uvicorn main:app --reload



npm install
npm install --legacy-peer-deps
>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
pip install -r requirements-debug.txt
python scripts/install_dependencies.py
python scripts/debug_environment_differences.py
python scripts/fix_environment_consistency.py
<<<<<<< HEAD

npm start

cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

npm install
npm install --legacy-peer-deps
npm run dev

schema.org
=======
npm run dev



- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

>>>>>>> 7064d9fe2673553a70d9f990ad4b7a1ae5e6e69b
