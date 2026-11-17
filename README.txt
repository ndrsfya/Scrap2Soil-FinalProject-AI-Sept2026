SCRAP2SOIL WEB PROTOTYPE

Project structure:
- app.py: starts the application and controls navigation
- data/materials.py: compost material information and shared colours
- logic/compost_logic.py: compost recommendations and keyword-based assistant replies
- ui/styles.py: shared CSS theme and visual styling
- ui/components.py: reusable page heading component
- app_pages/home.py: Home dashboard
- app_pages/planner.py: Compost Planner screen
- app_pages/guide.py: Compost Guide and assistant screen
- app_pages/tracking.py: Batch Tracking screen
- app_pages/about.py: About page and material guide

Note: The screen folder is named app_pages (not pages) to prevent Streamlit from creating a second automatic navigation menu.
- assets/: illustration files used by the interface

To run:
1. Open this folder in VS Code.
2. Install dependencies: python -m pip install -r requirements.txt
3. Run: python -m streamlit run app.py

Keep all folders together with app.py.
