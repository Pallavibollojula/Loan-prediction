import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from streamlit_lottie import st_lottie
import requests
data = pd.read_csv("loan_data.csv")
label_cols = ['Gender','Married','Education','Self_Employed','Property_Area','Loan_Status']
le = LabelEncoder()
for col in label_cols:
    data[col] = le.fit_transform(data[col])

data.fillna(data.median(numeric_only=True), inplace=True)

X = data.drop(['Loan_ID','Loan_Status'], axis=1)
y = data['Loan_Status']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_scaled, y)
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

loan_anim = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_x62chJ.json")  
success_anim = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_jbrw3hcz.json")  
fail_anim = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_touohxv0.json")  
st.set_page_config(page_title="💰 Loan Eligibility Predictor", page_icon="💸", layout="wide")

st.markdown("<h1 style='text-align: center; color: #4B0082;'>💰 Loan Eligibility Prediction</h1>", unsafe_allow_html=True)
st_lottie(loan_anim, speed=1, height=200, key="loan")
st.markdown("---")
st.sidebar.header("Applicant Details 📝")
with st.sidebar.form("applicant_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["Yes", "No"])
    dependents = st.selectbox("Dependents", [0,1,2,3])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])
    app_income = st.number_input("Applicant Income", min_value=0)
    coapp_income = st.number_input("Coapplicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)
    loan_term = st.number_input("Loan Amount Term (months)", min_value=0)
    credit_history = st.selectbox("Credit History", [0,1])
    property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])
    
    submit_button = st.form_submit_button(label='Predict Loan Eligibility 💡')
def gender_to_num(val): return 1 if val=="Male" else 0
def yes_no_to_num(val): return 1 if val=="Yes" else 0
def education_to_num(val): return 1 if val=="Graduate" else 0
def property_area_to_num(val):
    mapping = {'Rural':0,'Semiurban':1,'Urban':2}
    return mapping[val]
user_input = [[
    gender_to_num(gender),
    yes_no_to_num(married),
    dependents,
    education_to_num(education),
    yes_no_to_num(self_employed),
    app_income,
    coapp_income,
    loan_amount,
    loan_term,
    credit_history,
    property_area_to_num(property_area)
]]

user_input_scaled = scaler.transform(user_input)
result_placeholder = st.empty()
if submit_button:
    prediction = model.predict(user_input_scaled)
    result_text = "✅ Approved" if prediction[0]==1 else "❌ Not Approved"
    st.markdown('<a id="result"></a>', unsafe_allow_html=True)
    if prediction[0]==1:
        result_placeholder.success("🎉 Congratulations! Your loan is likely to be approved.")
        st_lottie(success_anim, speed=1, height=200, key="success")
        st.balloons()
    else:
        result_placeholder.error("⚠️ Sorry! Your loan is likely to be not approved.")
        st_lottie(fail_anim, speed=1, height=200, key="fail")

    st.markdown("### Applicant Details")
    st.info(f"""
    **Gender:** {gender}  
    **Married:** {married}  
    **Dependents:** {dependents}  
    **Education:** {education}  
    **Self Employed:** {self_employed}  
    **Applicant Income:** {app_income}  
    **Coapplicant Income:** {coapp_income}  
    **Loan Amount:** {loan_amount}  
    **Loan Term:** {loan_term} months  
    **Credit History:** {credit_history}  
    **Property Area:** {property_area}
    """)

    st.markdown(
        """
        <script>
        const element = document.getElementById("result");
        element.scrollIntoView({behavior: "smooth"});
        </script>
        """, unsafe_allow_html=True
    )

