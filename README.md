<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=26&pause=1000&color=39FF14&center=true&vCenter=true&width=600&lines=%F0%9F%8D%BF+Top+10+Movies+Site;%F0%9F%8C%90+Flask+Web+App;%F0%9F%93%BD%EF%B8%8F+TMDB+API+Integration" alt="Animated Header" />
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
  <span style="color: #39FF14;">🚀 Project Overview</span><br>
  <img src="https://placehold.co/1000x2/39FF14/39FF14.png" width="100%" height="2" alt="Green Divider"/>
</h3>

A dynamic web application that serves as a personal cinema diary. It allows users to search for movies via the TMDB API, add them to a local SQLite database, and provide custom ratings and reviews. The application automatically handles the ranking logic, ensuring the highest-rated movie always holds the top position.

**Technical Logic (Verified):**
* **🎬 TMDB API Workflow:** Implements a two-step API process: searching for titles and then fetching specific movie details (poster, description, year) by ID for database entry.
* **📊 Automated Ranking System:** Features a backend logic that sorts the entire movie collection by rating and assigns a rank dynamically whenever a score is updated.
* **✍️ Full CRUD Capability:** Users can Create (add movie), Read (view list), Update (edit review/rating), and Delete entries, with immediate database synchronization.
* **🧬 Jinja2 Templating:** Uses server-side rendering to inject database content into HTML, maintaining a consistent UI across different movie entries.

<br>

<h3>
  <span style="color: #00E5FF;">📁 Project Structure</span><br>
  <img src="https://placehold.co/1000x2/00E5FF/00E5FF.png" width="100%" height="2" alt="Cyan Divider"/>
</h3>

```text
top-10-movies-site/
├── main.py                     # Flask routes, API logic & Database models
├── forms.py                    # WTForms definitions for secure input
├── movies.db                   # SQLite storage for movie records
├── templates/                  # Jinja2 HTML templates (index, edit, add)
└── static/                     # Custom CSS and UI styling
```
<h3>
  <span style="color: #BC13FE;">🧠 Code Review & Complexity</span><br>
  <img src="https://placehold.co/1000x2/BC13FE/BC13FE.png" width="100%" height="2" alt="Purple Divider"/>
</h3>

<div align="center">
  <img src="https://img.shields.io/badge/OVERALL_DIFFICULTY-INTERMEDIATE-FE428E?style=for-the-badge&logoColor=white" height="35">
</div>

<br>

> <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=18&pause=1000&color=39FF14&vCenter=true&width=400&lines=>_ANALYZING_SYSTEM_COMPLEXITY..." alt="Animated Loading" />
> 
> <table>
>   <tr>
>     <td width="260"><b><span style="color: #39FF14;">ORM Integration (SQLAlchemy)</span></b></td>
>     <td width="200"><img src="https://placehold.co/160x10/39FF14/39FF14.png"/><img src="https://placehold.co/40x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #39FF14;">80%</span></b></td>
>   </tr>
>   <tr>
>     <td width="260"><b><span style="color: #00E5FF;">API Search & Fetch Logic</span></b></td>
>     <td width="200"><img src="https://placehold.co/160x10/00E5FF/00E5FF.png"/><img src="https://placehold.co/40x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #00E5FF;">80%</span></b></td>
>   </tr>
>   <tr>
>     <td width="260"><b><span style="color: #BC13FE;">Dynamic Sorting Algorithm</span></b></td>
>     <td width="200"><img src="https://placehold.co/140x10/BC13FE/BC13FE.png"/><img src="https://placehold.co/60x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #BC13FE;">70%</span></b></td>
>   </tr>
>   <tr>
>     <td width="260"><b><span style="color: #39FF14;">Form Validation (WTForms)</span></b></td>
>     <td width="200"><img src="https://placehold.co/120x10/39FF14/39FF14.png"/><img src="https://placehold.co/80x10/2F2F2F/2F2F2F.png"/></td>
>     <td width="50"><b><span style="color: #39FF14;">60%</span></b></td>
>   </tr>
> </table>

<br>

**🟢 High-Impact Wins:**
* **Data Flow:** Smooth transition of data from an external API through a Flask form and into a persistent SQLite database.
* **SQLAlchemy Mastery:** Using ORM (Object-Relational Mapping) to keep database queries clean and Pythonic.

**🔧 Technical Debt:**
* **API Security:** The TMDB API Key is currently embedded in the code. (Pro-tip: Explain that you would move this to an `.env` file for a production environment).
* **Search Refinement:** The search results could be improved by adding "Pagination" if the API returns more than 10 results at once.

<br>

<div align="center">
  <img src="https://img.shields.io/badge/🤖_AI_Contribution-Project_HTML_%26_CSS-50FA7B?style=flat-square" alt="AI Note">
  <br>
  <samp style="font-size: 12px; color: #6272a4;">Any custom HTML/CSS used in this project's templates was co-authored with AI.</samp>
</div>

<br>

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=16&duration=3000&pause=1000&color=00E5FF&center=true&vCenter=true&width=500&lines=[SYSTEM_SCAN_COMPLETE]----------------------------" alt="Animated Scan Divider" />
</div>
