# 💰 Loan Eligibility Prediction App

This is a **Machine Learning-powered Loan Eligibility Predictor** built using **Streamlit**.  
It analyzes applicant financial details and predicts whether the loan is likely to be **Approved** or **Not Approved**.

## 🚀 Features

- User-friendly **Web Interface** (built with Streamlit)
- **Random Forest Classifier** Model for accurate predictions
- Automatic data preprocessing (Label Encoding + Scaling + Missing Value Handling)
- Smooth UI animations using **Lottie**
- Real-time prediction result with visual feedback

## 📊 Dataset

The dataset used is `loan_data.csv`, containing applicant demographic & financial features along with loan outcome status.

## 🧠 Model Used

- **Algorithm:** Random Forest Classifier  
- **Preprocessing:**
  - Label encoding categorical fields
  - Standard scaling numerical features
  - Replacing missing values with median

## 📂 Project Structure

```
Loan-prediction/
│
├── loan_app.py        # Main application script
├── loan_data.csv      # Dataset
└── README.md          # Project documentation
```

## ⚙️ Installation & Usage

### 1. Install Required Libraries
```
pip install streamlit pandas scikit-learn streamlit-lottie requests
```

### 2. Run the Streamlit App
```
streamlit run loan_app.py
```

Once running, open the browser link shown (usually `http://localhost:8501`).

## 📥 Input Fields

| Field | Options / Type |
|------|----------------|
| Gender | Male / Female |
| Married | Yes / No |
| Dependents | 0 / 1 / 2 / 3 |
| Education | Graduate / Not Graduate |
| Self Employed | Yes / No |
| Applicant Income | Numeric |
| Coapplicant Income | Numeric |
| Loan Amount | Numeric |
| Loan Amount Term | Numeric (months) |
| Credit History | 0 / 1 |
| Property Area | Rural / Semiurban / Urban |

## ✅ Output

| Result | Meaning |
|--------|----------|
| **Approved** | The loan is likely to be sanctioned |
| **Not Approved** | The loan may not meet eligibility criteria |

The app also displays animation and summary of the applicant details.

## 🎨 UI Enhancements

This app uses **Lottie animations** for a more interactive and engaging user experience.

## 🤝 Contributing

Contributions are welcome.  
Feel free to **fork this repository** and submit a pull request.

## 📜 License

This project is open-source and available under the **MIT License**.

### Developed by **Pallavi Bollojula**
