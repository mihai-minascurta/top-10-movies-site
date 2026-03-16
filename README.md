<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=26&pause=1000&color=FE428E&center=true&vCenter=true&width=600&lines=%F0%9F%8D%BF+Top+10+Movies+Site;%F0%9F%8C%90+Flask+Web+App;%F0%9F%93%BD%EF%B8%8F+TMDB+API+Integration" alt="Animated Header" />
</div>

<br>

<div align="center">
  <img src="https://img.shields.io/badge/Python-FE428E?style=for-the-badge&logo=python&logoColor=white" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Flask-A9FEF7?style=for-the-badge&logo=flask&logoColor=black" height="35">
  &nbsp;&nbsp;
  <img src="https://img.shields.io/badge/SQLite-C3B550?style=for-the-badge&logo=sqlite&logoColor=black" height="35">
</div>

<br>

<h3>
  🚀 Project Overview<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

A fully functional web application that allows users to curate and rank their favorite movies. The app connects to the TMDB API to fetch movie data, stores user ratings and reviews in a local database, and dynamically sorts the list based on the user's score.

**Key Features:**
* **🔍 Movie Search:** Real-time search functionality using the TMDB API to find and add movies.
* **✍️ CRUD Operations:** Full ability to Add, Edit (rating/review), and Delete entries from the database.
* **📊 Automatic Ranking:** Movies are automatically ranked and reordered based on the numerical rating provided.
* **🎨 Modern UI:** Clean interface built with Bootstrap and Jinja2 templates.

<br>

<h3>
  📁 Project Structure<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

```text
top-10-movies-site/
├── main.py                     # Flask application logic & Routes
├── forms.py                    # WTForms for Rating & Add functionality
├── movies.db                   # SQLite Database storage
├── templates/                  # HTML Templates (Jinja2)
│   ├── index.html
│   ├── add.html
│   └── edit.html
└── static/                     # CSS & Styling assets"center">
  <img src="https://placehold.co/1000x3/FE428E/FE428E.png" width="100%" height="3" alt="Pink Divider"/>
</div>
```
<h3>
  🧠 Code Review & Complexity<br>
  <img src="https://placehold.co/1000x2/C3B550/C3B550.png" width="100%" height="2" alt="Yellow Divider"/>
</h3>

<div align="center">
  <img src="https://img.shields.io/badge/OVERALL_DIFFICULTY-INTERMEDIATE-FE428E?style=for-the-badge&logoColor=white" height="35">
</div>

<br>

> **📊 SYSTEM COMPLEXITY RADAR**
>
> 🟩🟩🟩🟩🟩🟩🟩🟩⬛⬛ **80%** | **Database Management (SQLAlchemy)**<br>
> 🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛ **80%** | **API Integration (TMDB)**<br>
> 🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛ **70%** | **Frontend Logic (Jinja2/Flask)**<br>
> 🟪🟪🟪🟪🟪🟪⬛⬛⬛⬛ **60%** | **Form Validation (WTForms)**

<br>

**🟢 High-Impact Wins:**
* **API Integration:** Excellent handling of external requests and parsing JSON data into the app.
* **Database Logic:** Implementation of SQLAlchemy for clean, Pythonic database interactions.

**🔧 Key Recommendations:**
* **Security:** Move the TMDB API Key into an environment variable (`.env`) for safety.
* **UI/UX:** Add a loading spinner during API calls to improve user experience.

<br>

<div align="center">
  <img src="https://img.shields.io/badge/🤖_AI_Contribution-Project_HTML_%26_CSS-50FA7B?style=flat-square" alt="AI Note">
  <br>
  <samp style="font-size: 12px; color: #6272a4;">The HTML and CSS templates within this project were co-authored with AI.</samp>
</div>

<br>

<div align="center">
  <img src="https://placehold.co/1000x3/FE428E/FE428E.png" width="100%" height="3" alt="Pink Divider"/>
</div>
