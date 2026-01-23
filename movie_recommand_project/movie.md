# 🎬 Movie Recommendation System

This is a content-based Movie Recommendation System built using **TF-IDF vectorization** and **Cosine Similarity** with Python.  
The system suggests movies similar to a given movie based on textual features such as plot overview and metadata.

---

## 🧠 Features

- 🔍 **Content-based Filtering**
- 📊 **TF-IDF Vectorization**
- 📏 **Cosine Similarity for movie similarity**
- 🐍 Built with **Python** and **Scikit-Learn**
- 📓 Developed and tested in **Jupyter Notebook**

---

## 🛠️ Technologies

- Python  
- Jupyter Notebook  
- pandas, NumPy  
- scikit-learn (TF-IDF & cosine similarity)

---

## 🚀 How It Works

1. **Preprocess movie text data** (e.g., overview or description).  
2. **Convert text to TF-IDF vectors** using scikit-learn.  
3. **Compute cosine similarity** between movie vectors.  
4. **Generate recommendations** by ranking movies by similarity.

This content-based recommendation approach finds movies with similar features (text representations) to a given input movie.

---

## 📦 Project Structure

movie_recommand_project/
├── movie_recommend.ipynb
└── README.md


---

## 🧪 Usage

To run and explore the recommendation notebook:
Download movie_recommend.ipynb

```bash
Install dependencies:

pip install -r requirements.txt
Open the notebook:

jupyter notebook movie_recommend.ipynb
```
