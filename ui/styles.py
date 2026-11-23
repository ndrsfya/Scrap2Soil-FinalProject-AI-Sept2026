"""Shared visual theme for Scrap2Soil."""

from data.materials import GREEN, DARK_GREEN, PALE_GREEN, SOFT_GREEN, TEXT


def apply_styles(st):
    st.markdown(f"""
<style>
    @import url("https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&display=swap");
    :root {{
        --green: {GREEN};
        --dark-green: {DARK_GREEN};
        --pale-green: {PALE_GREEN};
        --soft-green: {SOFT_GREEN};
        --text: {TEXT};
    }}
    .stApp {{
        background: #FBF8F0;
        color: #1F3526 !important;
        font-family: "Nunito", "Trebuchet MS", "Segoe UI", sans-serif;
    }}
    html, body, [class*="css"], .stMarkdown, .stText, p, li, label,
    [data-testid="stMarkdownContainer"], [data-testid="stWidgetLabel"] {{
        color: #1F3526 !important;
        font-family: "Nunito", "Trebuchet MS", "Segoe UI", sans-serif !important;
    }}
    h1, h2, h3, h4, h5, h6 {{
        color: #294B34 !important;
        font-family: "Nunito", "Trebuchet MS", "Segoe UI", sans-serif !important;
        font-weight: 750 !important;
        letter-spacing: -0.35px;
    }}
    input, textarea, [data-baseweb="select"], [data-baseweb="input"] {{
        color: #1F3526 !important;
        font-family: "Nunito", "Trebuchet MS", "Segoe UI", sans-serif !important;
    }}
    input::placeholder, textarea::placeholder {{
        color: #657267 !important;
        opacity: 1 !important;
    }}
    [data-testid="stDataFrame"], [data-testid="stTable"] {{
        color: #1F3526 !important;
        max-width: 100%;
    }}
    [data-testid="stMarkdownContainer"], .stMarkdown, .stCaption {{
        overflow-wrap: anywhere;
        word-break: normal;
    }}
    [data-testid="stDataFrame"] [role="gridcell"],
    [data-testid="stDataFrame"] [role="columnheader"] {{
        white-space: normal !important;
    }}
    [data-testid="stMetricValue"] {{
        color: #294B34 !important;
        font-weight: 750 !important;
    }}
    [data-testid="stMetricLabel"] {{
        color: #35483A !important;
        font-weight: 600 !important;
    }}
    [data-testid="stSidebar"] * {{
        color: #F9F8EF;
    }}
    [data-testid="stSidebar"] [role="radiogroup"] label[data-checked="true"] {{
        background: #E7EFDC;
        border-radius: 14px;
    }}
    [data-testid="stSidebar"] [role="radiogroup"] label[data-checked="true"] * {{
        color: #294B34 !important;
        font-weight: 800 !important;
    }}
    [data-testid="stSidebar"] {{
        background: #66866D;
        border-right: 1px solid #54765D;
    }}
    [data-testid="stSidebar"] > div:first-child {{
        padding-top: 1.2rem;
    }}
    .brand {{
        color: {DARK_GREEN};
        font-size: 1.62rem;
        font-weight: 800;
        letter-spacing: -0.8px;
        margin-bottom: 0;
    }}
    .brand-sub {{
        color: #F1F5E9;
        font-size: 0.82rem;
        margin-top: 0.15rem;
        margin-bottom: 1.4rem;
    }}
    .page-kicker {{
        color: {GREEN};
        font-size: 0.78rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-bottom: 0.2rem;
    }}
    .page-title {{
        color: {DARK_GREEN};
        font-size: 2.15rem;
        font-weight: 800;
        letter-spacing: -1px;
        margin: 0 0 0.2rem 0;
    }}
    .page-desc {{
        color: #596B5C;
        margin-bottom: 1.2rem;
    }}
    .section-title {{
        color: {DARK_GREEN};
        font-size: 1.12rem;
        font-weight: 700;
        margin: 0.8rem 0 0.55rem 0;
    }}
    .small-muted {{
        color: #F1F5E9;
        font-size: 0.88rem;
    }}
    .simple-card {{
        background: #FFFEFB;
        border: 1px solid #DCE4D8;
        border-radius: 20px;
        padding: 1rem 1.1rem;
        height: 100%;
        transition: transform 160ms ease, box-shadow 160ms ease, border-color 160ms ease;
    }}
    .simple-card:hover {{
        transform: translateY(-3px);
        border-color: #A9BFA9;
        box-shadow: 0 8px 20px rgba(34, 76, 43, 0.08);
    }}
    .hero-panel {{
        background: linear-gradient(120deg, #E5EEE2 0%, #F7F4ED 72%);
        border: 1px solid #D3DFD0;
        border-radius: 24px;
        padding: 1.4rem 1.5rem;
        margin: 0.25rem 0 1.1rem 0;
    }}
    .hero-eyebrow {{
        color: #47734E;
        font-size: 0.76rem;
        font-weight: 800;
        letter-spacing: 1.1px;
        text-transform: uppercase;
        margin-bottom: 0.35rem;
    }}
    .hero-heading {{
        color: #294B34 !important;
        font-size: 1.85rem;
        line-height: 1.16;
        font-weight: 850;
        letter-spacing: -0.8px;
        margin-bottom: 0.45rem;
    }}
    .hero-copy {{
        color: #344C39 !important;
        font-size: 0.98rem;
        line-height: 1.55;
        max-width: 34rem;
    }}
    .tip-strip {{
        background: #F8E9E7;
        border: 1px dashed #C9B7AE;
        border-radius: 10px;
        padding: 0.7rem 0.9rem;
        color: #294B31;
        font-size: 0.9rem;
    }}
    .feature-title {{
        color: {DARK_GREEN};
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 0.25rem;
    }}
    .feature-copy {{
        color: #657267;
        font-size: 0.88rem;
    }}
    .green-note {{
        background: #E8F0E5;
        border-left: 4px solid #789B83;
        border-radius: 7px;
        padding: 0.8rem 1rem;
        color: #344C38;
        margin: 0.5rem 0 1rem 0;
    }}
    .tag-green {{
        display: inline-block;
        background: #E1EDE0;
        color: #28603A;
        border-radius: 20px;
        padding: 0.18rem 0.6rem;
        font-size: 0.78rem;
        font-weight: 650;
    }}
    .tag-brown {{
        display: inline-block;
        background: #F3E7DC;
        color: #76552D;
        border-radius: 20px;
        padding: 0.18rem 0.6rem;
        font-size: 0.78rem;
        font-weight: 650;
    }}
    div.stButton > button[kind="primary"],
    div.stFormSubmitButton > button[kind="primary"] {{
        background: {GREEN};
        border: 1px solid {GREEN};
        color: white;
        border-radius: 8px;
        font-weight: 650;
    }}
    div.stButton > button[kind="primary"]:hover,
    div.stFormSubmitButton > button[kind="primary"]:hover {{
        background: {DARK_GREEN};
        border-color: {DARK_GREEN};
        color: white;
    }}
    div.stButton > button,
    div.stFormSubmitButton > button {{
        border-radius: 8px;
    }}
    [data-testid="stMetric"] {{
        background: #FFFEFB;
        border: 1px solid #DCE4D8;
        padding: 0.85rem 1rem;
        border-radius: 11px;
    }}
    [data-testid="stMetricLabel"] {{
        color: #637267;
    }}
    [data-testid="stMetricValue"] {{
        color: {DARK_GREEN};
    }}
    div[data-testid="stExpander"] {{
        border: 1px solid #DCE4D8;
        border-radius: 10px;
        background: #FFFEFB;
    }}
    .footer {{
        color: #849087;
        font-size: 0.78rem;
        border-top: 1px solid #E0E7DC;
        padding-top: 0.8rem;
        margin-top: 2rem;
    }}
    .simple-card, .hero-panel, .green-note, .tip-strip {{
        border-radius: 18px;
    }}
    .simple-card {{
        box-shadow: 0 3px 12px rgba(48, 76, 59, 0.045);
    }}
    .simple-card:hover {{
        box-shadow: 0 10px 22px rgba(48, 76, 59, 0.10);
    }}
    .hero-panel {{
        background: linear-gradient(135deg, #E4EEE1 0%, #F7F3EA 78%);
        border: 1px solid #D4E0D1;
        position: relative;
    }}
    .hero-eyebrow {{
        color: #6E9279;
    }}
    .hero-heading {{
        color: #304C3B !important;
    }}
    .hero-copy {{
        color: #344C39 !important;
    }}
    .stButton > button, .stFormSubmitButton > button {{
        border-radius: 14px !important;
        transition: all 160ms ease;
        font-weight: 650 !important;
    }}
    .stButton > button[kind="secondary"] {{
        border: 1px solid #C9D8C8 !important;
        background: #FDFCF7 !important;
        color: #304C3B !important;
    }}
    .stButton > button[kind="secondary"]:hover {{
        border-color: #789B83 !important;
        background: #EEF4EB !important;
    }}
    [data-testid="stTextInput"] input, [data-testid="stNumberInput"] input {{
        border-radius: 10px !important;
    }}
    [data-testid="stSelectbox"] [data-baseweb="select"] > div,
    [data-testid="stMultiSelect"] [data-baseweb="select"] > div {{
        border-radius: 10px !important;
    }}
    [data-testid="stMetric"] {{
        background: #FFFEFB;
        border: 1px solid #DCE4D8;
        border-radius: 16px;
    }}
    [data-testid="stSidebar"] [role="radiogroup"] label {{
        border-radius: 12px;
        padding: 0.35rem 0.55rem;
    }}
    [data-testid="stSidebar"] [role="radiogroup"] label:hover {{
        background: #DDE9DA;
    }}
    .soft-pink-note {{
        background: #F7E4E5;
        border: 1px solid #EAD4D1;
        color: #5B3C3B;
        border-radius: 14px;
        padding: 0.75rem 0.9rem;
    }}

    .brand {{
        color: #FFFDF4 !important;
        font-size: 1.8rem;
        font-weight: 900;
        letter-spacing: -0.8px;
    }}
    .brand-sub {{
        color: #F3F5E9 !important;
        line-height: 1.35;
    }}
    .page-title, .section-title, .feature-title {{
        color: #294B34 !important;
        font-family: "Nunito", sans-serif !important;
        font-weight: 900 !important;
    }}
    .hero-panel {{
        background: linear-gradient(135deg, #E7F0E1 0%, #FDF8EE 78%);
        border: 1px solid #D2E0CC;
        box-shadow: 0 8px 22px rgba(45, 76, 51, 0.07);
    }}
    .hero-heading {{
        font-size: 2.45rem !important;
        font-weight: 900 !important;
        line-height: 1.05 !important;
        color: #294B34 !important;
    }}
    .simple-card {{
        border-radius: 22px !important;
        border: 1px solid #D7E4D2 !important;
        box-shadow: 0 6px 18px rgba(45, 76, 51, 0.07);
    }}
    .simple-card:hover {{
        transform: translateY(-4px);
        box-shadow: 0 12px 24px rgba(45, 76, 51, 0.13);
    }}
    .stButton > button, .stFormSubmitButton > button {{
        font-family: "Nunito", sans-serif !important;
        font-weight: 800 !important;
        border-radius: 15px !important;
        min-height: 2.65rem;
    }}
    [data-testid="stMetric"] {{
        border-radius: 18px !important;
        background: #F1F5E9 !important;
        border: 1px solid #DCE7D5 !important;
    }}
    [data-testid="stChatMessage"] {{
        background: #F0F5EB;
        border-radius: 18px;
        border: 1px solid #DFE9D8;
    }}
    [data-testid="stTabs"] button {{
        font-family: "Nunito", sans-serif !important;
        font-weight: 800 !important;
        color: #294B34 !important;
    }}
    .decor-mark {{
        color: #D98F98;
        font-size: 1.5rem;
        font-weight: 900;
        letter-spacing: 0.15rem;
    }}
    /* Framed botanical dashboard styling */
    .stApp {{
        background:
            radial-gradient(ellipse at 75% 4%, rgba(224, 237, 214, 0.78) 0, rgba(224, 237, 214, 0) 23%),
            radial-gradient(ellipse at 95% 92%, rgba(194, 218, 177, 0.55) 0, rgba(194, 218, 177, 0) 18%),
            #FBF8F0;
    }}
    .welcome-line {{
        color: #294B34;
        font-family: "Nunito", sans-serif;
        font-size: 2.6rem;
        font-weight: 900;
        line-height: 1.1;
    }}
    .welcome-copy {{
        color: #344C39;
        font-size: 1.08rem;
        line-height: 1.5;
    }}
    .home-panel {{
        background: #FFFEFA;
        border: 1.5px solid #D7E1D1;
        border-radius: 24px;
        padding: 1.1rem 1.2rem;
        box-shadow: 0 5px 18px rgba(44, 66, 45, 0.055);
    }}
    .pastel-green, .pastel-pink, .pastel-yellow {{
        border: 1.5px solid rgba(77, 112, 75, 0.18);
        border-radius: 22px;
        box-shadow: 0 4px 12px rgba(44, 66, 45, 0.055);
        transition: transform 160ms ease, box-shadow 160ms ease;
    }}
    .pastel-green:hover, .pastel-pink:hover, .pastel-yellow:hover {{
        transform: translateY(-3px);
        box-shadow: 0 9px 18px rgba(44, 66, 45, 0.10);
    }}
    [data-testid="stVerticalBlockBorderWrapper"] {{
        border: 1.5px solid #D7E1D1 !important;
        border-radius: 22px !important;
        background: #FFFEFA;
        box-shadow: 0 4px 14px rgba(44, 66, 45, 0.045);
    }}
    [data-testid="stImage"] img {{
        border-radius: 24px;
    }}
    .botanical-divider {{
        height: 10px;
        border-radius: 99px;
        background: linear-gradient(90deg, #9DBB91, #E4EEE1, #F3E4D9, #9DBB91);
        opacity: 0.8;
        margin: 0.5rem 0 1rem;
    }}
    .welcome-line {{
        color: #294B34;
        font-family: "Nunito", sans-serif;
        font-size: 2.6rem;
        font-weight: 900;
        line-height: 1.1;
    }}
    .welcome-copy {{
        color: #344C39;
        font-size: 1.08rem;
        line-height: 1.5;
    }}
    .home-panel {{
        background: #FFFEFA;
        border: 1px solid #E5E7DA;
        border-radius: 24px;
        padding: 1.1rem 1.2rem;
        box-shadow: 0 5px 18px rgba(44, 66, 45, 0.045);
    }}
    .pastel-green {{
        background: #E7F0E2;
        border-radius: 20px;
        padding: 1rem;
    }}
    .pastel-pink {{
        background: #F8E8E8;
        border-radius: 20px;
        padding: 1rem;
    }}
    .pastel-yellow {{
        background: #FBF0D2;
        border-radius: 20px;
        padding: 1rem;
    }}


    /* Readable light widgets across browsers and operating-system themes */
    [data-baseweb="select"] > div {{
        background-color: #F9FCF7 !important;
        border: 1.5px solid #AFC5AE !important;
        color: #24452F !important;
        box-shadow: none !important;
    }}
    [data-baseweb="select"] input,
    [data-baseweb="select"] [role="combobox"],
    [data-baseweb="select"] span,
    [data-baseweb="select"] div {{
        color: #24452F !important;
    }}
    [data-baseweb="popover"] [role="listbox"],
    [data-baseweb="menu"],
    [data-baseweb="popover"] ul {{
        background: #FFFFFF !important;
        color: #24452F !important;
    }}
    [data-baseweb="popover"] [role="option"] {{
        background: #FFFFFF !important;
        color: #24452F !important;
    }}
    [data-baseweb="popover"] [role="option"]:hover,
    [data-baseweb="popover"] [aria-selected="true"] {{
        background: #E5F0E2 !important;
        color: #24452F !important;
    }}
    input, textarea,
    [data-testid="stTextInput"] input,
    [data-testid="stNumberInput"] input,
    [data-testid="stDateInput"] input,
    [data-testid="stChatInput"] textarea {{
        background: #FFFFFF !important;
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
        border: 1.5px solid #B8CBB4 !important;
        border-radius: 12px !important;
        caret-color: #294B34 !important;
    }}
    input::placeholder, textarea::placeholder {{
        color: #687B6A !important;
        -webkit-text-fill-color: #687B6A !important;
        opacity: 1 !important;
    }}
    [data-testid="stChatInput"] {{
        background: #F4F8F1 !important;
        border: 1.5px solid #B8CBB4 !important;
        border-radius: 18px !important;
        padding: 0.3rem !important;
    }}
    [data-testid="stChatInput"] button {{
        background: #668E70 !important;
        color: #FFFFFF !important;
        border-radius: 12px !important;
    }}
    [data-testid="stDataFrame"],
    [data-testid="stTable"] {{
        background: #F8FCF6 !important;
        color: #203B29 !important;
        border: 1px solid #C8D9C4 !important;
        border-radius: 14px !important;
        overflow: hidden !important;
    }}
    [data-testid="stDataFrame"] *,
    [data-testid="stTable"] * {{
        color: #203B29 !important;
    }}
    [data-testid="stTable"] table {{
        background: #F8FCF6 !important;
        color: #203B29 !important;
        border-collapse: collapse !important;
    }}
    [data-testid="stTable"] th {{
        background: #DCEBDD !important;
        color: #24452F !important;
        font-weight: 800 !important;
    }}
    [data-testid="stTable"] td {{
        background: #F8FCF6 !important;
        color: #203B29 !important;
        border-color: #DCE8D8 !important;
    }}
    /* Sidebar navigation: replace dark radio dots with a clean pill menu */
    [data-testid="stSidebar"] [role="radiogroup"] label {{
        background: transparent !important;
        border-radius: 13px !important;
        padding: 0.45rem 0.65rem !important;
        margin: 0.15rem 0 !important;
        color: #F8FBF3 !important;
    }}
    [data-testid="stSidebar"] [role="radiogroup"] label > div:first-child {{
        display: none !important;
    }}
    [data-testid="stSidebar"] [role="radiogroup"] label p {{
        color: #F8FBF3 !important;
        font-weight: 650 !important;
    }}
    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {{
        background: #E5F0E2 !important;
    }}
    [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) p {{
        color: #24452F !important;
        font-weight: 900 !important;
    }}
    /* Green guide layout and illustrated topic tiles */
    .guide-banner {{
        display: block;
        background: linear-gradient(120deg, #E2EEDF, #F2F7ED);
        border: 1.5px solid #BFD3BA;
        border-radius: 22px;
        padding: 1.1rem 1.3rem;
        margin: 0.6rem 0 1.2rem;
    }}
    .guide-banner-title {{
        color: #244B30 !important;
        font-size: 1.15rem;
        font-weight: 900;
        margin-bottom: 0.2rem;
    }}
    .guide-banner-copy {{
        color: #385440 !important;
        font-size: 0.94rem;
        line-height: 1.45;
    }}

    .guide-answer {{
        background: #EAF2E6;
        border: 1.5px solid #C8D9C2;
        border-radius: 18px;
        padding: 1.15rem 1.25rem;
        margin-top: 1rem;
        color: #24452F !important;
        font-size: 1.02rem;
        line-height: 1.65;
    }}
    .guide-answer-title {{
        color: #24452F !important;
        font-size: 1.15rem;
        font-weight: 900;
        margin-bottom: 0.45rem;
    }}

    .plant-card {{
        background: #FFFEFC;
        border: 1.5px solid #D9E5D5;
        border-radius: 20px;
        padding: 0.95rem;
        min-height: 150px;
        box-shadow: 0 4px 13px rgba(41, 75, 52, 0.045);
    }}
    .plant-icon {{
        width: 54px;
        height: 54px;
        display: grid;
        place-items: center;
        border-radius: 16px;
        background: #E4EFE0;
        font-size: 1.9rem;
        margin-bottom: 0.55rem;
    }}
    .plant-name {{
        color: #294B34 !important;
        font-size: 1rem;
        font-weight: 900;
        margin-bottom: 0.12rem;
    }}
    .plant-caption {{
        color: #637766 !important;
        font-size: 0.82rem;
        line-height: 1.35;
    }}
    .stat-panel {{
        background: #FFFEFC;
        border: 1.5px solid #D9E5D5;
        border-radius: 22px;
        padding: 1.1rem 1.2rem;
        box-shadow: 0 5px 16px rgba(41, 75, 52, 0.05);
        height: 100%;
    }}
    .stat-number {{
        color: #294B34 !important;
        font-size: 1.8rem;
        font-weight: 900;
        line-height: 1.1;
    }}
    .stat-label {{
        color: #637766 !important;
        font-size: 0.82rem;
        font-weight: 700;
    }}
    .mix-track {{
        height: 13px;
        width: 100%;
        border-radius: 99px;
        overflow: hidden;
        background: #E9EEE4;
        display: flex;
        margin: 0.4rem 0 0.55rem;
    }}
    .mix-green {{
        height: 100%;
        background: #679A70;
    }}
    .mix-brown {{
        height: 100%;
        background: #C69A68;
    }}
    .mix-legend {{
        display: flex;
        justify-content: space-between;
        gap: 0.7rem;
        color: #405443;
        font-size: 0.84rem;
        font-weight: 750;
    }}
    .batch-progress-label {{
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        color: #294B34;
        font-weight: 850;
        gap: 0.5rem;
    }}
    .batch-progress-label span:last-child {{
        color: #62896B;
        font-size: 1.05rem;
        font-weight: 900;
    }}
    .percentage-note {{
        color: #687B6A !important;
        font-size: 0.76rem;
        line-height: 1.4;
    }}


    /* Success and warning messages: force light backgrounds and dark text */
    div[data-testid="stAlert"],
    div[data-testid="stAlert"] [data-baseweb="notification"],
    div[data-testid="stAlert"] [role="alert"] {{
        background: #E8F2E6 !important;
        background-color: #E8F2E6 !important;
        border: 1px solid #B8D0B4 !important;
        border-radius: 14px !important;
        color: #294B34 !important;
    }}

    /* Keep nested alert containers transparent so they do not cover the light background */
    div[data-testid="stAlert"] > div,
    div[data-testid="stAlert"] > div > div,
    div[data-testid="stAlert"] [data-testid="stMarkdownContainer"] {{
        background: transparent !important;
        background-color: transparent !important;
    }}

    /* Force all alert text to use a readable dark green */
    div[data-testid="stAlert"] *,
    div[data-testid="stAlert"] p,
    div[data-testid="stAlert"] span {{
        color: #294B34 !important;
        -webkit-text-fill-color: #294B34 !important;
    }}

    /* Alert icons */
    div[data-testid="stAlert"] svg {{
        color: #527D59 !important;
        fill: #527D59 !important;
    }}

    [data-testid="stException"] {{
        background: #FFF1EF !important;
        border: 1px solid #E5B9B4 !important;
        border-radius: 12px !important;
    }}
    [data-testid="stException"] * {{
        color: #702F2F !important;
    }}


    /* Consistent light green controls and readable tables. */
    [data-testid="stSelectbox"] [data-baseweb="select"] > div,
    [data-testid="stMultiSelect"] [data-baseweb="select"] > div {{
        background: #F4F8F1 !important;
        border: 1.5px solid #AFC5AE !important;
        color: #24452F !important;
    }}
    [data-testid="stSelectbox"] [data-baseweb="select"] input,
    [data-testid="stSelectbox"] [data-baseweb="select"] span,
    [data-testid="stSelectbox"] [data-baseweb="select"] div {{
        color: #24452F !important;
        -webkit-text-fill-color: #24452F !important;
    }}
    [data-baseweb="popover"] [role="listbox"],
    [data-baseweb="popover"] [role="option"],
    [data-baseweb="menu"] {{
        background: #F7FBF5 !important;
        color: #24452F !important;
    }}
    [data-baseweb="popover"] [role="option"] * {{
        color: #24452F !important;
        -webkit-text-fill-color: #24452F !important;
    }}
    [data-baseweb="popover"] [role="option"]:hover,
    [data-baseweb="popover"] [aria-selected="true"] {{
        background: #DDEBDD !important;
        color: #24452F !important;
    }}
    .green-table-wrap {{
        width: 100%; overflow-x: auto; border: 1px solid #BFD2BC;
        border-radius: 13px; margin: 0.5rem 0 1rem; background: #F6FAF3;
    }}
    .green-table {{
        width: 100%; border-collapse: collapse; background: #F6FAF3;
        color: #203B29; font-size: 0.94rem; line-height: 1.45;
    }}
    .green-table th {{
        background: #D8E8D5; color: #203B29; font-weight: 800;
        text-align: left; padding: 0.8rem 0.75rem; border: 1px solid #C6D9C2;
        white-space: normal;
    }}
    .green-table td {{
        background: #F6FAF3; color: #203B29; padding: 0.75rem;
        border: 1px solid #D8E5D4; vertical-align: top; white-space: normal;
        overflow-wrap: anywhere; min-width: 90px;
    }}
    .green-table tbody tr:nth-child(even) td {{ background: #EAF2E7; }}
    [data-testid="stChatMessage"] p {{
        color: #203B29 !important; font-size: 1rem !important; line-height: 1.55 !important;
    }}
    [data-testid="stChatInput"] textarea {{
        background: #FFFFFF !important; color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
    }}


    /* Make all form controls readable and consistent with the light theme */
    [data-testid="stTextInput"] input,
    [data-testid="stNumberInput"] input,
    [data-testid="stDateInput"] input,
    [data-testid="stTimeInput"] input,
    [data-testid="stTextArea"] textarea,
    [data-baseweb="input"] input,
    [data-baseweb="textarea"] textarea,
    [data-baseweb="datepicker"] input {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
        caret-color: #203B29 !important;
        border-color: #AFC5AE !important;
    }}

    /* Light backgrounds for the outer input containers */
    [data-testid="stTextInput"] [data-baseweb="input"],
    [data-testid="stNumberInput"] [data-baseweb="input"],
    [data-testid="stDateInput"] [data-baseweb="input"],
    [data-testid="stTimeInput"] [data-baseweb="input"],
    [data-testid="stTextArea"] [data-baseweb="textarea"],
    [data-baseweb="datepicker"] {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        border: 1px solid #AFC5AE !important;
        border-radius: 10px !important;
    }}

    /* Text inside selected dropdown values */
    [data-testid="stSelectbox"] [data-baseweb="select"] *,
    [data-testid="stMultiSelect"] [data-baseweb="select"] *,
    [data-testid="stSelectbox"] [data-baseweb="select"] input,
    [data-testid="stMultiSelect"] [data-baseweb="select"] input {{
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
    }}

    /* Multiselect selected tags */
    [data-testid="stMultiSelect"] [data-baseweb="tag"] {{
        background: #DDEBDD !important;
        border: 1px solid #AFC5AE !important;
        color: #203B29 !important;
    }}
    [data-testid="stMultiSelect"] [data-baseweb="tag"] *,
    [data-testid="stMultiSelect"] [data-baseweb="tag"] span {{
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
    }}

    /* Number input increment and decrement controls */
    [data-testid="stNumberInput"] button {{
        background: #E8F2E6 !important;
        color: #294B34 !important;
        border-color: #AFC5AE !important;
    }}
    [data-testid="stNumberInput"] button svg {{
        fill: #294B34 !important;
        color: #294B34 !important;
    }}

    /* Input labels, help text and placeholders */
    [data-testid="stWidgetLabel"],
    [data-testid="stWidgetLabel"] *,
    [data-testid="stHelp"],
    [data-testid="stMarkdownContainer"] label {{
        color: #203B29 !important;
    }}
    input::placeholder,
    textarea::placeholder {{
        color: #718071 !important;
        -webkit-text-fill-color: #718071 !important;
        opacity: 1 !important;
    }}

    /* Dropdown menus and date picker calendar */
    [data-baseweb="popover"],
    [data-baseweb="popover"] *,
    [data-baseweb="calendar"],
    [data-baseweb="calendar"] * {{
        color: #203B29 !important;
    }}
    [data-baseweb="popover"] [role="listbox"],
    [data-baseweb="popover"] [role="option"],
    [data-baseweb="calendar"] {{
        background: #F7FBF5 !important;
    }}

    /* Keep success and warning alerts light and readable */
    div[data-testid="stAlert"],
    div[data-testid="stAlert"] [role="alert"] {{
        background: #E8F2E6 !important;
        background-color: #E8F2E6 !important;
        border: 1px solid #B8D0B4 !important;
        border-radius: 14px !important;
        color: #294B34 !important;
    }}
    div[data-testid="stAlert"] > div,
    div[data-testid="stAlert"] > div > div,
    div[data-testid="stAlert"] [data-testid="stMarkdownContainer"] {{
        background: transparent !important;
        background-color: transparent !important;
    }}
    div[data-testid="stAlert"] *,
    div[data-testid="stAlert"] p,
    div[data-testid="stAlert"] span {{
        color: #294B34 !important;
        -webkit-text-fill-color: #294B34 !important;
    }}
    div[data-testid="stAlert"] svg {{
        color: #527D59 !important;
        fill: #527D59 !important;
    }}


    /* Final Compost Planner overrides: preserve the original cream, green and red design */
    .stApp {{
        background: #FBF8F0 !important;
        color: #1F3526 !important;
    }}

    /* Keep text fields and date inputs white with dark readable text */
    [data-testid="stTextInput"] input,
    [data-testid="stNumberInput"] input,
    [data-testid="stDateInput"] input,
    [data-testid="stTimeInput"] input,
    [data-testid="stTextArea"] textarea,
    [data-baseweb="input"] input,
    [data-baseweb="textarea"] textarea,
    [data-baseweb="datepicker"] input {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
        caret-color: #203B29 !important;
        border-color: #C9D8C8 !important;
    }}

    [data-testid="stTextInput"] [data-baseweb="input"],
    [data-testid="stNumberInput"] [data-baseweb="input"],
    [data-testid="stDateInput"] [data-baseweb="input"],
    [data-testid="stTimeInput"] [data-baseweb="input"],
    [data-testid="stTextArea"] [data-baseweb="textarea"],
    [data-baseweb="datepicker"] {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        border: 1px solid #C9D8C8 !important;
        border-radius: 10px !important;
    }}

    /* Restore the red selected-material chips from the original design */
    [data-testid="stMultiSelect"] [data-baseweb="tag"] {{
        background: #C83B50 !important;
        border: 1px solid #C83B50 !important;
        color: #FFFFFF !important;
    }}
    [data-testid="stMultiSelect"] [data-baseweb="tag"] *,
    [data-testid="stMultiSelect"] [data-baseweb="tag"] span,
    [data-testid="stMultiSelect"] [data-baseweb="tag"] svg {{
        color: #FFFFFF !important;
        fill: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }}

    /* Keep the multiselect field itself light */
    [data-testid="stMultiSelect"] [data-baseweb="select"] > div {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        border: 1px solid #C9D8C8 !important;
    }}
    [data-testid="stMultiSelect"] [data-baseweb="select"] input {{
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
    }}

    /* Restore the red primary action button */
    div.stButton > button[kind="primary"],
    div.stFormSubmitButton > button[kind="primary"] {{
        background: #C83B50 !important;
        background-color: #C83B50 !important;
        border: 1px solid #C83B50 !important;
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        border-radius: 10px !important;
    }}
    div.stButton > button[kind="primary"]:hover,
    div.stFormSubmitButton > button[kind="primary"]:hover {{
        background: #AD3044 !important;
        background-color: #AD3044 !important;
        border-color: #AD3044 !important;
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }}

    /* Keep number stepper controls light green */
    [data-testid="stNumberInput"] button {{
        background: #E8F2E6 !important;
        color: #294B34 !important;
        border-color: #C9D8C8 !important;
    }}
    [data-testid="stNumberInput"] button svg {{
        color: #294B34 !important;
        fill: #294B34 !important;
    }}

    /* Keep success and warning messages readable without changing the page theme */
    div[data-testid="stAlert"] {{
        background: #E8F2E6 !important;
        background-color: #E8F2E6 !important;
        border: 1px solid #B8D0B4 !important;
        border-radius: 14px !important;
        color: #294B34 !important;
    }}
    div[data-testid="stAlert"] > div,
    div[data-testid="stAlert"] > div > div,
    div[data-testid="stAlert"] [data-testid="stMarkdownContainer"] {{
        background: transparent !important;
        background-color: transparent !important;
    }}
    div[data-testid="stAlert"] *,
    div[data-testid="stAlert"] p,
    div[data-testid="stAlert"] span {{
        color: #294B34 !important;
        -webkit-text-fill-color: #294B34 !important;
    }}
    div[data-testid="stAlert"] svg {{
        color: #527D59 !important;
        fill: #527D59 !important;
    }}



    /* Final Scrap2Soil palette: sage sidebar, green actions, cream canvas */
    [data-testid="stSidebar"],
    [data-testid="stSidebar"] > div:first-child {{
        background-color: #66866D !important;
    }}

    /* Primary buttons use the same sage-green family as the sidebar */
    div.stButton > button[kind="primary"],
    div.stFormSubmitButton > button[kind="primary"],
    [data-testid="stForm"] button[kind="primary"] {{
        background: #71977A !important;
        background-color: #71977A !important;
        border: 1px solid #71977A !important;
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        border-radius: 12px !important;
    }}
    div.stButton > button[kind="primary"]:hover,
    div.stFormSubmitButton > button[kind="primary"]:hover,
    [data-testid="stForm"] button[kind="primary"]:hover {{
        background: #587C61 !important;
        background-color: #587C61 !important;
        border-color: #587C61 !important;
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }}

    /* Date input: white field with dark readable text */
    [data-testid="stDateInput"],
    [data-testid="stDateInput"] > div,
    [data-testid="stDateInput"] [data-baseweb="datepicker"],
    [data-testid="stDateInput"] [data-baseweb="input"],
    [data-testid="stDateInput"] [data-baseweb="input"] > div {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        border-color: #C9D8C8 !important;
        color: #203B29 !important;
        border-radius: 10px !important;
        box-shadow: none !important;
    }}
    [data-testid="stDateInput"] input,
    [data-testid="stDateInput"] input[type="text"] {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
        caret-color: #203B29 !important;
        border: 0 !important;
    }}
    [data-testid="stDateInput"] button {{
        background: #FFFFFF !important;
        color: #587C61 !important;
        border: 0 !important;
    }}
    [data-testid="stDateInput"] svg {{
        color: #587C61 !important;
        fill: #587C61 !important;
    }}

    /* Material multiselect: white input area, readable selected values */
    [data-testid="stMultiSelect"] [data-baseweb="select"],
    [data-testid="stMultiSelect"] [data-baseweb="select"] > div,
    [data-testid="stMultiSelect"] [data-baseweb="select"] > div > div {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        border-color: #C9D8C8 !important;
        color: #203B29 !important;
        box-shadow: none !important;
    }}
    [data-testid="stMultiSelect"] input,
    [data-testid="stMultiSelect"] [role="combobox"],
    [data-testid="stMultiSelect"] [data-baseweb="select"] span {{
        background: transparent !important;
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
    }}
    [data-testid="stMultiSelect"] [data-baseweb="tag"] {{
        background: #DDEBDD !important;
        border: 1px solid #B7CDB5 !important;
        color: #294B34 !important;
    }}
    [data-testid="stMultiSelect"] [data-baseweb="tag"] *,
    [data-testid="stMultiSelect"] [data-baseweb="tag"] span,
    [data-testid="stMultiSelect"] [data-baseweb="tag"] svg {{
        color: #294B34 !important;
        fill: #294B34 !important;
        -webkit-text-fill-color: #294B34 !important;
    }}

    /* Keep all other text and number inputs white as well */
    [data-testid="stTextInput"] input,
    [data-testid="stNumberInput"] input,
    [data-testid="stTextArea"] textarea,
    [data-testid="stTimeInput"] input {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
        border-color: #C9D8C8 !important;
    }}

    /* White calendar popup with dark text */
    [data-baseweb="calendar"],
    [data-baseweb="calendar"] *,
    [data-baseweb="datepicker"] [role="dialog"] {{
        background-color: #FFFFFF !important;
        color: #203B29 !important;
    }}
    [data-baseweb="calendar"] button:hover {{
        background: #E8F2E6 !important;
    }}


    /* FINAL FIX: date picker and material chooser must stay white */
    [data-testid="stDateInput"] [data-baseweb="datepicker"],
    [data-testid="stDateInput"] [data-baseweb="datepicker"] > div,
    [data-testid="stDateInput"] [data-baseweb="input"],
    [data-testid="stDateInput"] [data-baseweb="input"] > div,
    [data-testid="stDateInput"] [data-baseweb="input"] > div > div {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: #203B29 !important;
        border-color: #C9D8C8 !important;
        box-shadow: none !important;
    }}
    [data-testid="stDateInput"] input {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
    }}
    [data-testid="stDateInput"] button,
    [data-testid="stDateInput"] button:hover {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: #587C61 !important;
    }}
    [data-testid="stDateInput"] svg {{
        color: #587C61 !important;
        fill: #587C61 !important;
    }}

    [data-testid="stMultiSelect"] [data-baseweb="select"],
    [data-testid="stMultiSelect"] [data-baseweb="select"] > div,
    [data-testid="stMultiSelect"] [data-baseweb="select"] > div > div,
    [data-testid="stMultiSelect"] [data-baseweb="select"] > div > div > div {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: #203B29 !important;
        border-color: #C9D8C8 !important;
        box-shadow: none !important;
    }}
    [data-testid="stMultiSelect"] input,
    [data-testid="stMultiSelect"] [role="combobox"] {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
    }}
    /* Keep selected material chips sage green */
    [data-testid="stMultiSelect"] [data-baseweb="tag"] {{
        background: #DDEBDD !important;
        background-color: #DDEBDD !important;
        border: 1px solid #B7CDB5 !important;
        color: #294B34 !important;
    }}
    [data-testid="stMultiSelect"] [data-baseweb="tag"] *,
    [data-testid="stMultiSelect"] [data-baseweb="tag"] svg {{
        color: #294B34 !important;
        fill: #294B34 !important;
        -webkit-text-fill-color: #294B34 !important;
    }}


    /* Final form-control correction to match the light Compost Planner design */

    /* Date input: white field and dark text */
    [data-testid="stDateInput"] [data-baseweb="datepicker"],
    [data-testid="stDateInput"] [data-baseweb="input"],
    [data-testid="stDateInput"] [data-baseweb="input"] > div,
    [data-testid="stDateInput"] [data-baseweb="input"] > div > div {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        border-color: #C9D8C8 !important;
        color: #203B29 !important;
        box-shadow: none !important;
    }}
    [data-testid="stDateInput"] input,
    [data-testid="stDateInput"] input[type="text"] {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
        caret-color: #203B29 !important;
    }}
    [data-testid="stDateInput"] button,
    [data-testid="stDateInput"] button:hover {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: #66866D !important;
    }}
    [data-testid="stDateInput"] button svg {{
        color: #66866D !important;
        fill: #66866D !important;
    }}

    /* Material chooser: white control with dark text */
    [data-testid="stMultiSelect"] [data-baseweb="select"] {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        border: 1px solid #C9D8C8 !important;
        box-shadow: none !important;
    }}
    [data-testid="stMultiSelect"] [data-baseweb="select"] > div,
    [data-testid="stMultiSelect"] [data-baseweb="select"] > div > div,
    [data-testid="stMultiSelect"] [data-baseweb="select"] > div > div > div {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: #203B29 !important;
        box-shadow: none !important;
    }}
    [data-testid="stMultiSelect"] input,
    [data-testid="stMultiSelect"] [role="combobox"] {{
        background: transparent !important;
        background-color: transparent !important;
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
    }}

    /* Keep selected material chips red with white text, as in the reference design */
    [data-testid="stMultiSelect"] [data-baseweb="tag"] {{
        background: #C83B50 !important;
        background-color: #C83B50 !important;
        border: 1px solid #C83B50 !important;
        color: #FFFFFF !important;
    }}
    [data-testid="stMultiSelect"] [data-baseweb="tag"] *,
    [data-testid="stMultiSelect"] [data-baseweb="tag"] span,
    [data-testid="stMultiSelect"] [data-baseweb="tag"] svg {{
        background: transparent !important;
        color: #FFFFFF !important;
        fill: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }}

    /* Light dropdown and calendar popovers */
    [data-baseweb="popover"],
    [data-baseweb="popover"] > div,
    [data-baseweb="popover"] [role="dialog"],
    [data-baseweb="calendar"],
    [data-baseweb="calendar"] > div {{
        background: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: #203B29 !important;
    }}
    [data-baseweb="calendar"] *,
    [data-baseweb="popover"] [role="option"],
    [data-baseweb="popover"] [role="listbox"] {{
        color: #203B29 !important;
    }}
    [data-baseweb="calendar"] button:hover,
    [data-baseweb="popover"] [role="option"]:hover {{
        background: #E8F2E6 !important;
        color: #203B29 !important;
    }}


    /* Starting date field matches the cream page background */
    div[data-testid="stDateInput"] [data-baseweb="datepicker"],
    div[data-testid="stDateInput"] [data-baseweb="input"],
    div[data-testid="stDateInput"] [data-baseweb="input"] > div,
    div[data-testid="stDateInput"] [data-baseweb="input"] > div > div,
    div[data-testid="stDateInput"] input,
    div[data-testid="stDateInput"] button {{
        color-scheme: light !important;
        background-color: #FBF8F0 !important;
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
        border-color: #DCE4D8 !important;
    }}

    div[data-testid="stDateInput"] svg,
    div[data-testid="stDateInput"] button svg {{
        background-color: transparent !important;
        color: #66866D !important;
        fill: #66866D !important;
        -webkit-text-fill-color: #66866D !important;
    }}

    /* The calendar is rendered in a popover outside the date-input wrapper */
    div[data-baseweb="popover"]:has([data-baseweb="calendar"]),
    div[data-baseweb="popover"]:has([data-baseweb="calendar"]) *,
    [data-baseweb="calendar"],
    [data-baseweb="calendar"] * {{
        color-scheme: light !important;
        background-color: #FFFFFF !important;
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
    }}

    [data-baseweb="calendar"] button:hover {{
        background-color: #E8F2E6 !important;
        color: #203B29 !important;
    }}

    [data-baseweb="calendar"] button[aria-selected="true"],
    [data-baseweb="calendar"] button[aria-pressed="true"] {{
        background-color: #71977A !important;
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }}

    /* White material-selection field; preserve the red selected chips */
    div[data-testid="stMultiSelect"] [data-baseweb="select"],
    div[data-testid="stMultiSelect"] [data-baseweb="select"] > div,
    div[data-testid="stMultiSelect"] [data-baseweb="select"] > div > div,
    div[data-testid="stMultiSelect"] [data-baseweb="select"] > div > div > div {{
        color-scheme: light !important;
        background-color: #FFFFFF !important;
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
        border-color: #C9D8C8 !important;
    }}

    div[data-testid="stMultiSelect"] input,
    div[data-testid="stMultiSelect"] [role="combobox"] {{
        background-color: transparent !important;
        color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
    }}

    div[data-testid="stMultiSelect"] [data-baseweb="tag"] {{
        background-color: #C83B50 !important;
        color: #FFFFFF !important;
    }}

    div[data-testid="stMultiSelect"] [data-baseweb="tag"] *,
    div[data-testid="stMultiSelect"] [data-baseweb="tag"] svg {{
        background-color: transparent !important;
        color: #FFFFFF !important;
        fill: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }}

    </style>
    """, unsafe_allow_html=True)

        margin-bottom: 0.55rem;
    }}
    .plant-name {{
        color: #294B34 !important;
        font-size: 1rem;
        font-weight: 900;
        margin-bottom: 0.12rem;
    }}
    .plant-caption {{
        color: #637766 !important;
        font-size: 0.82rem;
        line-height: 1.35;
    }}
    .stat-panel {{
        background: #FFFEFC;
        border: 1.5px solid #D9E5D5;
        border-radius: 22px;
        padding: 1.1rem 1.2rem;
        box-shadow: 0 5px 16px rgba(41, 75, 52, 0.05);
        height: 100%;
    }}
    .stat-number {{
        color: #294B34 !important;
        font-size: 1.8rem;
        font-weight: 900;
        line-height: 1.1;
    }}
    .stat-label {{
        color: #637766 !important;
        font-size: 0.82rem;
        font-weight: 700;
    }}
    .mix-track {{
        height: 13px;
        width: 100%;
        border-radius: 99px;
        overflow: hidden;
        background: #E9EEE4;
        display: flex;
        margin: 0.4rem 0 0.55rem;
    }}
    .mix-green {{
        height: 100%;
        background: #679A70;
    }}
    .mix-brown {{
        height: 100%;
        background: #C69A68;
    }}
    .mix-legend {{
        display: flex;
        justify-content: space-between;
        gap: 0.7rem;
        color: #405443;
        font-size: 0.84rem;
        font-weight: 750;
    }}
    .batch-progress-label {{
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        color: #294B34;
        font-weight: 850;
        gap: 0.5rem;
    }}
    .batch-progress-label span:last-child {{
        color: #62896B;
        font-size: 1.05rem;
        font-weight: 900;
    }}
    .percentage-note {{
        color: #687B6A !important;
        font-size: 0.76rem;
        line-height: 1.4;
    }}

    [data-testid="stAlert"] {{
        background: #1F2A3D !important;
        background-color: #1F2A3D !important;
        border: 1px solid #34445F !important;
        border-radius: 14px !important;
    }}
    [data-testid="stAlert"] p,
    [data-testid="stAlert"] span,
    [data-testid="stAlert"] div,
    [data-testid="stAlert"] [data-testid="stMarkdownContainer"],
    [data-testid="stAlert"] [data-testid="stMarkdownContainer"] * {{
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }}
    [data-testid="stAlert"] svg {{
        color: #FFFFFF !important;
        fill: #FFFFFF !important;
    }}
    [data-testid="stException"] {{
        background: #FFF1EF !important;
        border: 1px solid #E5B9B4 !important;
        border-radius: 12px !important;
    }}
    [data-testid="stException"] * {{
        color: #702F2F !important;
    }}


    /* Consistent light green controls and readable tables. */
    [data-testid="stSelectbox"] [data-baseweb="select"] > div,
    [data-testid="stMultiSelect"] [data-baseweb="select"] > div {{
        background: #F4F8F1 !important;
        border: 1.5px solid #AFC5AE !important;
        color: #24452F !important;
    }}
    [data-testid="stSelectbox"] [data-baseweb="select"] input,
    [data-testid="stSelectbox"] [data-baseweb="select"] span,
    [data-testid="stSelectbox"] [data-baseweb="select"] div {{
        color: #24452F !important;
        -webkit-text-fill-color: #24452F !important;
    }}
    [data-baseweb="popover"] [role="listbox"],
    [data-baseweb="popover"] [role="option"],
    [data-baseweb="menu"] {{
        background: #F7FBF5 !important;
        color: #24452F !important;
    }}
    [data-baseweb="popover"] [role="option"] * {{
        color: #24452F !important;
        -webkit-text-fill-color: #24452F !important;
    }}
    [data-baseweb="popover"] [role="option"]:hover,
    [data-baseweb="popover"] [aria-selected="true"] {{
        background: #DDEBDD !important;
        color: #24452F !important;
    }}
    .green-table-wrap {{
        width: 100%; overflow-x: auto; border: 1px solid #BFD2BC;
        border-radius: 13px; margin: 0.5rem 0 1rem; background: #F6FAF3;
    }}
    .green-table {{
        width: 100%; border-collapse: collapse; background: #F6FAF3;
        color: #203B29; font-size: 0.94rem; line-height: 1.45;
    }}
    .green-table th {{
        background: #D8E8D5; color: #203B29; font-weight: 800;
        text-align: left; padding: 0.8rem 0.75rem; border: 1px solid #C6D9C2;
        white-space: normal;
    }}
    .green-table td {{
        background: #F6FAF3; color: #203B29; padding: 0.75rem;
        border: 1px solid #D8E5D4; vertical-align: top; white-space: normal;
        overflow-wrap: anywhere; min-width: 90px;
    }}
    .green-table tbody tr:nth-child(even) td {{ background: #EAF2E7; }}
    [data-testid="stChatMessage"] p {{
        color: #203B29 !important; font-size: 1rem !important; line-height: 1.55 !important;
    }}
    [data-testid="stChatInput"] textarea {{
        background: #FFFFFF !important; color: #203B29 !important;
        -webkit-text-fill-color: #203B29 !important;
    }}

</style>
    """, unsafe_allow_html=True)
