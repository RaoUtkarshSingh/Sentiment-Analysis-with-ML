# 😊 Sentiment Analysis Project using Machine Learning

![Sentiment Analysis](sentiment%20pic.jpg)

---

## 📖 About the Project

This project is an end-to-end **Natural Language Processing (NLP)** and **Machine Learning** application that predicts whether a text review expresses a **Positive 😊** or **Negative 😞** sentiment.

Built using the **IMDb 50K Movie Reviews Dataset**, it covers the complete workflow of a real-world ML project:

- 📦 Data Collection & Cleaning
- 🧹 Text Preprocessing & EDA
- ⚙️ Feature Engineering
- 🤖 Model Building & Evaluation
- 💾 Database Integration
- 🌐 Streamlit Web App Deployment

---

## 📌 Project Highlights

| 🏷️ Property | 📋 Detail |
|-------------|-----------|
| 📂 Dataset | IMDb 50,000 Movie Reviews |
| ⚖️ Classification | Binary (Positive / Negative) |
| 🥇 Best Model | Logistic Regression |
| 🎯 Best Accuracy | **89.8%** |
| 🌐 Web Framework | Streamlit |
| 💾 Database | MySQL |
| ⚡ Prediction | Real-time |

---

## 🎯 Why This Project?

Online platforms generate thousands of reviews daily. Reading and analyzing each review manually is time-consuming and inefficient.

This project solves that by automatically classifying reviews into ✅ **Positive** or ❌ **Negative** sentiment — helping businesses:

- 📈 Understand customer satisfaction
- 🔍 Monitor public sentiment
- ⚡ Analyze product feedback faster
- 🚨 Identify negative reviews quickly
- 💡 Improve decision making using data-driven insights

---

## 📂 Project Workflow

### 1️⃣ Data Collection
Collected the **IMDb 50K Movie Reviews Dataset** for training and testing.

### 2️⃣ Data Cleaning 🧹
- Lowercasing
- Removing HTML tags and punctuation
- Removing stopwords (preserving negation words: `not`, `no`, `never`)
- Tokenization

### 3️⃣ Exploratory Data Analysis (EDA) 📊
- Positive vs Negative review distribution
- Word frequency analysis
- Word clouds ☁️
- Review length distribution

### 4️⃣ Feature Engineering ⚙️
Converted text into numerical format using **TF-IDF Vectorization**.

### 5️⃣ Model Building & Comparison 🤖

| 🤖 Model | 🎯 Accuracy | 📊 F1 Score |
|----------|-------------|-------------|
| Logistic Regression | **89.8%** ✅ | **90.0%** ✅ |
| SVM | 89.5% | 89.6% |
| Naive Bayes | 86.8% | 86.8% |

### 6️⃣ Deployment 🚀
Built an interactive **Streamlit** web app for real-time sentiment prediction.

---

## 🛠️ Tools & Libraries

| 🔧 Tool | 📋 Purpose |
|---------|-----------|
| 🐍 Python | Programming |
| 🐼 Pandas | Data analysis |
| 🔢 NumPy | Numerical operations |
| 📊 Matplotlib / Seaborn | Visualization |
| 📝 NLTK | NLP preprocessing |
| 🤖 Scikit-learn | Machine Learning |
| 💾 Pickle | Model serialization |
| 🌐 Streamlit | Web application |
| 🗄️ MySQL | Database |
| 📓 Jupyter Notebook | Model development |

---

## ✨ Web App Features

✅ Enter any custom review text  
🧹 Automatic text preprocessing  
⚡ Instant Positive / Negative prediction  
📊 Confidence score with progress bar  
☁️ Word Cloud generation  
💾 Prediction history saved to MySQL database  
⬇️ Downloadable prediction history as CSV  
🌗 Light / Dark theme toggle  

---

## 📁 Project Structure

```bash
Sentiment Analysis ML project/
│
├── 🐍 app.py                        # Streamlit web application
│
├── 📁 ML/
│   ├── 🤖 model.pkl                 # Trained ML model
│   └── ⚙️  vectorizer.pkl           # TF-IDF Vectorizer
│
├── 📁 Database/
│   └── 🗄️  db.py                    # MySQL connection & insert logic
│
├── 📁 Notebook/
│   └── 📓 Sentiment_Analysis.ipynb  # Model training notebook
│
├── 📄 requirements.txt
└── 📄 README.md
```

---

## ▶️ Run Locally

### 1️⃣ Clone Repository
```bash
git clone https://github.com/RaoUtkarshSingh/sentiment-analysis-project.git
cd sentiment-analysis-project
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Setup MySQL Database 🗄️
```sql
CREATE DATABASE sentiment_db;

USE sentiment_db;

CREATE TABLE predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    review TEXT,
    cleaned TEXT,
    prediction VARCHAR(20),
    confidence FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Then update `Database/db.py` with your MySQL credentials:
```python
host="localhost",
user="your_username",
password="your_password",
database="sentiment_db"
```

### 4️⃣ Generate Model Files (if not present) 🤖
Run `Notebook/Sentiment_Analysis.ipynb` to generate `model.pkl` and `vectorizer.pkl`, then place them inside the `ML/` folder.

### 5️⃣ Run the App 🚀
```bash
streamlit run app.py
```

---

## 💡 Real-World Use Cases

| 🏢 Industry | 📋 Use Case |
|------------|------------|
| 🛒 E-commerce | Product Review Analysis |
| 🏨 Hospitality | Hotel & Restaurant Reviews |
| 📱 Social Media | Comment Sentiment Tracking |
| 🎬 Entertainment | Movie Review Classification |
| 🏷️ Brand Management | Reputation Monitoring |
| 📋 Research | Survey Feedback Analysis |

---

## 🚀 Capabilities Demonstrated

🐍 Python Programming  
📊 Data Analysis with Pandas & NumPy  
🧹 Data Cleaning & Text Preprocessing  
🔍 Natural Language Processing (NLP)  
🤖 Machine Learning Model Training  
📈 Data Visualization  
💾 MySQL Database Integration  
🌐 Streamlit Web App Development  
📑 End-to-End ML Project Deployment  

---

## 📬 Contact

Feel free to connect for collaboration, feedback, or opportunities!

📧 **Email:** utrajpatna1@email.com  
💼 **LinkedIn:** [linkedin.com/in/utkarsh-raj01](https://www.linkedin.com/in/utkarsh-raj01)  
🐙 **GitHub:** [github.com/RaoUtkarshSingh](https://github.com/RaoUtkarshSingh)  

---

> ⭐ If you found this project useful, consider giving it a star on GitHub!
