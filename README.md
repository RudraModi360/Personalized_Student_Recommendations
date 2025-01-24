<div align="center">
  <h3 align="center">Student Performance Analysis and Recommendations</h3>

  <p align="center">
    A Streamlit app for visualizing student performance and providing personalized recommendations.
    <br />
    <a href="https://drive.google.com/file/d/1QlA72cfUAUsV8plKaY2uaXlpn4TqQ5c6/view?usp=sharing">View Demo</a>
    &middot;
    &middot;
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Average Time Taken by user](img_vid\Time.png)](img_vid\Time.png)
Average Time Taken By User

[![Average Initial Mistake Done by user](img_vid\Mistake.png)](img_vid\Mistake.png)
Average Mistakes Done By User

[![Average Score of user](img_vid\Avg_Score.png)](img_vid\Avg_Score.png)
Average Score of User

[![Average Accuracy of user](img_vid\Avg_Acc.png)](img_vid\Avg_Acc.png)
Average Accuracy for problem solving of User

- This project is a Streamlit web application designed to visualize and analyze student performance across various metrics such as score, accuracy, mistake count, and time. It also provides personalized recommendations based on the student's quiz performance.

### Key Features:

- **Student Performance Visualization**: Visualizations for quiz scores, accuracy, mistakes, and time.
- **Personalized Recommendations**: Fetch tailored recommendations based on the student’s performance.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [Streamlit](https://streamlit.io/)
- [Matplotlib](https://matplotlib.org/)
- [Sklearn](https://scikit-learn.org/)
- [Pandas](https://pandas.pydata.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To get a local copy of this project up and running, follow these simple steps.

### Prerequisites

This project requires Python and Streamlit to be installed. Make sure you have the following:

- Python 3.x
- Streamlit
- Requests
- Matplotlib

You can install the required dependencies by running the following command:

```bash
pip install streamlit requests matplotlib
```

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/RudraModi360/Personalized_Student_Recommendations.git
   ```
2. Navigate to the project directory
   ```bash
   cd Personalized_Student_Recommendations
   ```
3. Run the Streamlit app
   ```bash
   streamlit run app.py
   ```
4. Run the Server
   ```bash
   uvicorn Server:app
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Once the app is running, you can:

- Input the quiz title and score in the sidebar.
- Click on **"Fetch Recommendations"** to get personalized recommendations based on the score.
- View the student performance analysis plots (Score, Accuracy, Mistakes, and Time) on the left side of the page.
- View the recommendations on the right side of the page.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
