SCRAP2SOIL WEB PROTOTYPE

Project structure:
- app.py: starts the application and controls navigation
- data/materials.py: compost material information and shared colours
- logic/compost_logic.py: calculations and compost mixture recommendations
- ui/styles.py: application styling
- ui/components.py: reusable page heading component
- app_pages/home.py: Home dashboard
- app_pages/planner.py: Compost Planner screen
- app_pages/guide.py: Compost Guide with a list of common issues and recommendations
- app_pages/tracking.py: Batch Tracking screen
- app_pages/about.py: About page and material guide
- assets/: images used by the interface

The Compost Guide uses predefined recommendations. It does not connect to a trained AI model or external chatbot service. Batch records are held in the current app session.

To run:
1. Open this folder in VS Code.
2. Install dependencies: python -m pip install -r requirements.txt
3. Run: python -m streamlit run app.py

Keep all folders together with app.py.
