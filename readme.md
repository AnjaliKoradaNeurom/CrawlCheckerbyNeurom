# === Backend ===
cd backend
python -m venv venv
venv\Scripts\activate   # (Windows)
pip install -r requirements.txt
pip install openai==0.28
python -m uvicorn main:app --reload



npm install
npm install --legacy-peer-deps
pip install -r requirements-debug.txt
python scripts/install_dependencies.py
python scripts/debug_environment_differences.py
python scripts/fix_environment_consistency.py
npm run dev



- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

