<h1> Scraping NBA data from the Web (ESPN). <br>
Comparison between European and American Players, time to reach the Maximum PER </h1>


<h4> See the file main_reasearch.ipynb for the Jupyter notebook with results. </h4>



The goal: <br>
Compare between European and American NBA Players and check the hypothesis that European players reach their Career Peak later than American NBA players (Takes longer)

how: <br>
Choose KPI- ESPN Hollinger's PER - Read definition [here](https://en.wikipedia.org/wiki/Player_efficiency_rating)

Pulled biographic data for NBA Players from NBA API (get_data_from_nbaApi.py).  <br>
Scraped PER data from ESPN website. (Scrape_data_from_ESPN.py) - <br>


Results: <br>
After some data work, we saw that Europeans reach their peak later than the North Americans: <br>

Europe            6.322816 <br>
North America     5.404482 <br>

For the research, work done, and results, see the file main_reasearch.ipynb