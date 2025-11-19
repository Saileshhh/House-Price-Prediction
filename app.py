import pandas as pd
import streamlit as st
import joblib

model = joblib.load("xgb_model.jb")

st.title("House Price Prediction")
st.write("Enter The Details Below To Predict The House Price")

OverallQual = st.slider(
    "Overall Quality (1 = Poor, 10 = Excellent)",
    1, 10, 5,
    help="Overall material and finish rating"
)

GrLivArea = st.slider(
    "Above Ground Living Area (sq ft)",
    300, 4000, 1500,
    help="Typical homes are 800–2500 sq ft"
)

GarageArea = st.slider(
    "Garage Area (sq ft)",
    0, 1200, 400,
    help="Size of the garage"
)

FirstFlrSF = st.slider(
    "1st Floor Area (sq ft)",
    300, 3000, 800,
    help="Area of the first floor"
)

FullBath = st.slider(
    "Full Bathrooms",
    0, 4, 2,
    help="Full bath = sink + toilet + shower"
)

YearBuilt = st.slider(
    "Year Built",
    1900, 2020, 1995
)

YearRemodAdd = st.slider(
    "Year Remodeled",
    1900, 2020, 2005,
    help="If not remodeled, keep same as Year Built"
)

MasVnrArea = st.slider(
    "Masonry Veneer Area (sq ft)",
    0, 1600, 0,
    help="Exterior brick/stone area"
)

Fireplaces = st.slider(
    "Number of Fireplaces",
    0, 3, 1
)

BsmtFinSF1 = st.slider(
    "Finished Basement Area (sq ft)",
    0, 2000, 500
)

LotFrontage = st.slider(
    "Lot Frontage (feet)",
    20, 200, 70
)

WoodDeckSF = st.slider(
    "Wood Deck Area (sq ft)",
    0, 800, 100
)

OpenPorchSF = st.slider(
    "Open Porch Area (sq ft)",
    0, 400, 50
)

LotArea = st.slider(
    "Lot Area (sq ft)",
    1000, 90000, 8000,
    help="Total land area of the property"
)

CentralAir = st.selectbox("Central Air Conditioning", ["Yes", "No"])

if st.button("Predict Price"):
    CentralAir_val = 1 if CentralAir == "Yes" else 0
    input_df = pd.DataFrame([{
        'OverallQual': OverallQual,
        'GrLivArea': GrLivArea,
        'GarageArea': GarageArea,
        '1stFlrSF': FirstFlrSF,
        'FullBath': FullBath,
        'YearBuilt': YearBuilt,
        'YearRemodAdd': YearRemodAdd,
        'MasVnrArea': MasVnrArea,
        'Fireplaces': Fireplaces,
        'BsmtFinSF1': BsmtFinSF1,
        'LotFrontage': LotFrontage,
        'WoodDeckSF': WoodDeckSF,
        'OpenPorchSF': OpenPorchSF,
        'LotArea': LotArea,
        'CentralAir': CentralAir_val
    }])

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted House Price: ${prediction:,.2f}")
