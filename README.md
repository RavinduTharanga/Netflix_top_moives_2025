## Netflix Top 10 Scraper 2025

### Overview
This Python script scrapes the Netflix Tudum website to extract the **Top 10 movies** along with their **view counts**. The data is then saved into a CSV file, making it easy to analyze or visualize Netflix's most-watched content.

### Features
- **Web Scraping:** Utilizes `BeautifulSoup` and `requests` to extract movie names and view counts.
- **Data Processing:** Cleans and formats the data for better readability.
- **CSV Export:** Saves the extracted data into a `netflix.csv` file.
- **Example Output:**
    ```
    Movie Name,Views
    La Dolce Villa,19800000
    Kinda Pregnant,13700000
    Aftermath,9900000
    Shrek,7000000
    Shrek 2,6100000
    Back in Action,5700000
    The Witcher: Sirens of the Deep,4800000
    Norbit,3900000
    Mission: Impossible - Dead Reckoning,3900000
    Shrek the Third,3600000
    ```

---

### Technologies Used
- **Python** - Core programming language.
- **BeautifulSoup** - For HTML parsing and web scraping.
- **Requests** - To fetch the webpage content.
- **Pandas** - Data manipulation and cleaning.
- **CSV** - Exporting data into CSV format.

---

### Prerequisites
Ensure you have the following libraries installed:
```sh
pip install beautifulsoup4 requests pandas
```

---

### How It Works
1. **Web Scraping:** 
    - Fetches the HTML content of [Netflix Tudum Top 10](https://www.netflix.com/tudum/top10).
    - Extracts movie names from `<button>` tags.
    - Extracts view counts from `<td>` tags with class `views`.

2. **Data Processing:** 
    - Cleans the extracted view counts (removing commas).
    - Combines movie names with corresponding view counts into a dictionary.

3. **Exporting Data:**
    - Saves the final data into a CSV file named `netflix.csv`.

---

### Installation and Usage
1. **Clone the Repository:**
    ```sh
    git clone https://github.com/your-username/netflix-top10-scraper.git
    cd netflix-top10-scraper
    ```

2. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the Script:**
    ```sh
    python main.py
    ```

4. **Output:**
    - The script will generate a `netflix.csv` file with the top 10 movies and their view counts.

---

### Example Output File
`netflix.csv`:
```
Movie Name,Views
La Dolce Villa,19800000
Kinda Pregnant,13700000
Aftermath,9900000
Shrek,7000000
Shrek 2,6100000
Back in Action,5700000
The Witcher: Sirens of the Deep,4800000
Norbit,3900000
Mission: Impossible - Dead Reckoning,3900000
Shrek the Third,3600000
```

---

### Potential Improvements
- Implement error handling for network requests.
- Schedule the scraper to run periodically to track view trends.
- Visualize the data using libraries like `Matplotlib` or `Seaborn`.


### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Acknowledgements
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://docs.python-requests.org/en/latest/)
- [Netflix Tudum](https://www.netflix.com/tudum/top10) for the movie data.


- Clean and maintainable code
- Documentation and communication

It’s designed to leave a positive impression on interviewers. If you want to make any edits or add more sections, let me know!
