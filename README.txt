SCRAP2SOIL WEB PROTOTYPE

Project structure:
- app.py: application entry point and navigation
- data/materials.py: material categories and reference properties
- logic/compost_logic.py: C:N calculations and recommendations
- ui/: shared layout components and styling
- app_pages/: Home, Compost Planner, Compost Guide, Batch Tracking and About pages
- assets/: images used by the interface

To run the application:
1. Open this folder in VS Code.
2. Install packages: python -m pip install -r requirements.txt
3. Start the application: python -m streamlit run app.py

Calculation method:
The Compost Planner follows Cornell University's wet-weight C:N mixture equation. It uses each
material's wet mass, dry-basis carbon and nitrogen percentages, and wet-basis moisture content.
Carbon percentage is estimated as nitrogen percentage multiplied by the material C:N ratio.
The result is an estimate based on typical reference data, not a laboratory measurement.
Cornell describes approximately 30:1 as a usual starting guideline; the suitable ratio can vary
with the materials and the availability of their carbon and nitrogen.

Materials without a complete set of reference values are not silently included in the calculation.
