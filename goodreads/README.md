# Automated Data Analysis Report

## Dataset Overview
**Shape:** (10000, 23)

**Columns:**
- book_id: int64
- goodreads_book_id: int64
- best_book_id: int64
- work_id: int64
- books_count: int64
- isbn: object
- isbn13: float64
- authors: object
- original_publication_year: float64
- original_title: object
- title: object
- language_code: object
- average_rating: float64
- ratings_count: int64
- work_ratings_count: int64
- work_text_reviews_count: int64
- ratings_1: int64
- ratings_2: int64
- ratings_3: int64
- ratings_4: int64
- ratings_5: int64
- image_url: object
- small_image_url: object

**Missing Values:**
- book_id: 0
- goodreads_book_id: 0
- best_book_id: 0
- work_id: 0
- books_count: 0
- isbn: 700
- isbn13: 585
- authors: 0
- original_publication_year: 21
- original_title: 585
- title: 0
- language_code: 1084
- average_rating: 0
- ratings_count: 0
- work_ratings_count: 0
- work_text_reviews_count: 0
- ratings_1: 0
- ratings_2: 0
- ratings_3: 0
- ratings_4: 0
- ratings_5: 0
- image_url: 0
- small_image_url: 0

## Summary Statistics
|       |   book_id |   goodreads_book_id |     best_book_id |         work_id |   books_count |         isbn13 |   original_publication_year |   average_rating |    ratings_count |   work_ratings_count |   work_text_reviews_count |   ratings_1 |   ratings_2 |   ratings_3 |      ratings_4 |       ratings_5 |
|:------|----------:|--------------------:|-----------------:|----------------:|--------------:|---------------:|----------------------------:|-----------------:|-----------------:|---------------------:|--------------------------:|------------:|------------:|------------:|---------------:|----------------:|
| count |  10000    |     10000           |  10000           | 10000           |    10000      | 9415           |                    9979     |     10000        |  10000           |      10000           |                  10000    |    10000    |    10000    |     10000   | 10000          | 10000           |
| mean  |   5000.5  |         5.2647e+06  |      5.47121e+06 |     8.64618e+06 |       75.7127 |    9.75504e+12 |                    1981.99  |         4.00219  |  54001.2         |      59687.3         |                   2919.96 |     1345.04 |     3110.89 |     11475.9 | 19965.7        | 23789.8         |
| std   |   2886.9  |         7.57546e+06 |      7.82733e+06 |     1.17511e+07 |      170.471  |    4.42862e+11 |                     152.577 |         0.254427 | 157370           |     167804           |                   6124.38 |     6635.63 |     9717.12 |     28546.4 | 51447.4        | 79768.9         |
| min   |      1    |         1           |      1           |    87           |        1      |    1.9517e+08  |                   -1750     |         2.47     |   2716           |       5510           |                      3    |       11    |       30    |       323   |   750          |   754           |
| 25%   |   2500.75 |     46275.8         |  47911.8         |     1.00884e+06 |       23      |    9.78032e+12 |                    1990     |         3.85     |  13568.8         |      15438.8         |                    694    |      196    |      656    |      3112   |  5405.75       |  5334           |
| 50%   |   5000.5  |    394966           | 425124           |     2.71952e+06 |       40      |    9.78045e+12 |                    2004     |         4.02     |  21155.5         |      23832.5         |                   1402    |      391    |     1163    |      4894   |  8269.5        |  8836           |
| 75%   |   7500.25 |         9.38223e+06 |      9.63611e+06 |     1.45177e+07 |       67      |    9.78083e+12 |                    2011     |         4.18     |  41053.5         |      45915           |                   2744.25 |      885    |     2353.25 |      9287   | 16023.5        | 17304.5         |
| max   |  10000    |         3.32886e+07 |      3.55342e+07 |     5.63996e+07 |     3455      |    9.79001e+12 |                    2017     |         4.82     |      4.78065e+06 |          4.94236e+06 |                 155254    |   456191    |   436802    |    793319   |     1.4813e+06 |     3.01154e+06 |

## Insights
### Narrative Summary of the Dataset

The dataset consists of 10,000 records related to books, include 23 attributes. Key attributes include identifiers for the books (such as `book_id`, `goodreads_book_id`, `best_book_id`, `work_id`), information about the books (including `authors`, `title`, `original_title`, `language_code`, `isbn`, and `isbn13`), and various metrics regarding the books' popularity and reception (including `average_rating`, `ratings_count`, `work_ratings_count`, `work_text_reviews_count`, among others).

### Insights from the Analysis

1. **Missing Values**:
   - There are significant missing values for certain columns: `isbn` (700 missing), `isbn13` (585 missing), and `original_title` (585 missing) are the most prevalent. The `language_code` also has a substantial number of missing entries (1,084).
   - Understanding and addressing these missing values could enhance data integrity, especially if these fields are critical for analysis.

2. **Descriptive Statistics**:
   - The average rating of books is 4.00, with a relatively low standard deviation (0.25), indicating that most books have favorable reviews. The range of average ratings suggests some outliers at both low and high ends.
   - The `ratings_count` and `work_ratings_count` metrics have high means (54,001 and 59,687, respectively), suggesting a large volume of feedback being collected on a subset of books, likely indicating popularity or visibility.

3. **Author Popularity**:
   - A clear pattern of prolific authors is evident, with Stephen King leading with 60 books in the dataset, followed by Nora Roberts (59), Dean Koontz (47), Terry Pratchett (42), and Agatha Christie (39). This skew suggests that a few authors dominate the dataset significantly.

4. **Language Distribution**:
   - The majority of books are in English (`eng`), with over 6,341 records. This dominance reflects a focus on English literature, though it may limit insights into global literature trends.

5. **Publication Trends**:
   - The `original_publication_year` shows that the average publication year is around 1981. Despite this, recent books (up to 2017) are also represented, suggesting a mixture of classic and contemporary literature.

6. **Correlation Insights**:
   - There are notable negative correlations between `ratings_count`, `work_ratings_count`, and `average_rating` with `work_text_reviews_count`, suggesting that books with more ratings might receive slightly lower average ratings despite being favorites among readers, perhaps indicating a larger audience with diverse opinions.

### Suggestions for Further Investigation

1. **Address Missing Data**:
   - Investigate the reasons behind the high incidence of missing values, especially in columns related to `isbn` and `language_code`. Consider possible imputation methods or analyzing the impact of these missing values on overall analysis.

2. **Author Studies**:
   - Conduct a comparative study on the works of the top authors to understand styles, themes, and what drives their popularity. This could also lead to insights into genre-specific trends.

3. **Sentiment Analysis**:
   - Perform sentiment analysis on reviews associated with `work_text_reviews_count` to understand what readers appreciate or criticize. This could refine understanding of ratings beyond mere numbers.

4. **Language and Region Analysis**:
   - Deepen the analysis in relation to language. Explore the potential impact of language distribution on ratings and popularity metrics and consider including translations or works from non-English authors.

5. **Time Series Analysis**:
   - Conduct a time series analysis using `original_publication_year` to explore trends in genres or types of books published over the years and how their ratings and counts have evolved.

6. **Rating Distribution**:
   - Analyze the distribution of ratings (1-5 stars) more closely to understand reader sentiment in greater detail, considering potential biases in how books are rated across different genres.

Through these insights and further investigation, a more nuanced understanding of the dataset and its implications for book popularity and readership trends can be achieved.

## Visualizations
![correlation_heatmap.png](goodreads\correlation_heatmap.png)
![book_id_distribution.png](goodreads\book_id_distribution.png)
![goodreads_book_id_distribution.png](goodreads\goodreads_book_id_distribution.png)
![best_book_id_distribution.png](goodreads\best_book_id_distribution.png)
![work_id_distribution.png](goodreads\work_id_distribution.png)
![books_count_distribution.png](goodreads\books_count_distribution.png)
![isbn13_distribution.png](goodreads\isbn13_distribution.png)
![original_publication_year_distribution.png](goodreads\original_publication_year_distribution.png)
![average_rating_distribution.png](goodreads\average_rating_distribution.png)
![ratings_count_distribution.png](goodreads\ratings_count_distribution.png)
![work_ratings_count_distribution.png](goodreads\work_ratings_count_distribution.png)
![work_text_reviews_count_distribution.png](goodreads\work_text_reviews_count_distribution.png)
![ratings_1_distribution.png](goodreads\ratings_1_distribution.png)
![ratings_2_distribution.png](goodreads\ratings_2_distribution.png)
![ratings_3_distribution.png](goodreads\ratings_3_distribution.png)
![ratings_4_distribution.png](goodreads\ratings_4_distribution.png)
![ratings_5_distribution.png](goodreads\ratings_5_distribution.png)
