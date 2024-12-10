# Automated Data Analysis Report

## Dataset Overview
**Shape:** (2363, 11)

**Columns:**
- Country name: object
- year: int64
- Life Ladder: float64
- Log GDP per capita: float64
- Social support: float64
- Healthy life expectancy at birth: float64
- Freedom to make life choices: float64
- Generosity: float64
- Perceptions of corruption: float64
- Positive affect: float64
- Negative affect: float64

**Missing Values:**
- Country name: 0
- year: 0
- Life Ladder: 0
- Log GDP per capita: 28
- Social support: 13
- Healthy life expectancy at birth: 63
- Freedom to make life choices: 36
- Generosity: 81
- Perceptions of corruption: 125
- Positive affect: 24
- Negative affect: 16

## Summary Statistics
|       |       year |   Life Ladder |   Log GDP per capita |   Social support |   Healthy life expectancy at birth |   Freedom to make life choices |     Generosity |   Perceptions of corruption |   Positive affect |   Negative affect |
|:------|-----------:|--------------:|---------------------:|-----------------:|-----------------------------------:|-------------------------------:|---------------:|----------------------------:|------------------:|------------------:|
| count | 2363       |    2363       |           2335       |      2350        |                         2300       |                    2327        | 2282           |                 2238        |       2339        |      2347         |
| mean  | 2014.76    |       5.48357 |              9.39967 |         0.809369 |                           63.4018  |                       0.750282 |    9.77213e-05 |                    0.743971 |          0.651882 |         0.273151  |
| std   |    5.05944 |       1.12552 |              1.15207 |         0.121212 |                            6.84264 |                       0.139357 |    0.161388    |                    0.184865 |          0.10624  |         0.0871311 |
| min   | 2005       |       1.281   |              5.527   |         0.228    |                            6.72    |                       0.228    |   -0.34        |                    0.035    |          0.179    |         0.083     |
| 25%   | 2011       |       4.647   |              8.5065  |         0.744    |                           59.195   |                       0.661    |   -0.112       |                    0.687    |          0.572    |         0.209     |
| 50%   | 2015       |       5.449   |              9.503   |         0.8345   |                           65.1     |                       0.771    |   -0.022       |                    0.7985   |          0.663    |         0.262     |
| 75%   | 2019       |       6.3235  |             10.3925  |         0.904    |                           68.5525  |                       0.862    |    0.09375     |                    0.86775  |          0.737    |         0.326     |
| max   | 2023       |       8.019   |             11.676   |         0.987    |                           74.6     |                       0.985    |    0.7         |                    0.983    |          0.884    |         0.705     |

## Insights
### Narrative Summary of the Dataset

The dataset encompasses global data related to subjective well-being and various socio-economic indicators across 2363 entries and 11 columns. The main objective appears to focus on measuring the perceived quality of life, conventionally represented by the "Life Ladder" score, across different countries and years from 2005 to 2023. The dataset includes data points for multiple individual factors such as Gross Domestic Product (GDP) per capita, social support, healthy life expectancy, personal freedoms, generosity, and perceptions of corruption, among others.

### Insights from the Analysis

1. **Missing Values**: 
   - The dataset has varying levels of missing values across columns. Notably, 'Generosity' has the highest missing value count (81), followed by 'Perceptions of corruption' (125). This may affect analyses relying heavily on these variables.
   
2. **Trends Over Time**:
   - The average year in the dataset is approximately 2014.76, indicating the data is relatively contemporary. The consistency of entries from 2005 to 2023 provides a robust timeframe to examine trends.
   
3. **Life Ladder**:
   - The mean score for the "Life Ladder" is approximately 5.48, reflecting a moderate level of reported personal well-being across countries. The range of life ladder scores (1.281 to 8.019) suggests significant variation in perceptions of life quality, indicating potential disparities among different countries.
   
4. **Strong Correlations**:
   - Multiple variables exhibit notable correlations with the "Life Ladder":
     - Strong positive correlation with 'Log GDP per capita' (0.78) suggests higher income aligns with perceived life satisfaction.
     - Similarly, 'Social support' and 'Healthy life expectancy' also present strong positive correlations (0.72 and 0.71, respectively) with "Life Ladder".
     - A negative correlation with 'Perceptions of corruption' (-0.43) indicates that higher perceived corruption is associated with lower life satisfaction.
   
5. **Freedom to Make Life Choices**:
   - This variable has a positive correlation (0.54) with the "Life Ladder". Countries that allow greater freedom tend to report higher satisfaction.
   
6. **Emotional Well-being**:
   - There are evident contrasts in the emotional metrics, with "Positive affect" averaging 0.65 while "Negative affect" averages 0.27, indicating a general tendency towards positive feelings among respondents.

7. **Top Countries**:
   - The dataset reveals that countries like Lebanon, Jordan, Nicaragua, Nepal, and Moldova each have 18 different entries, possibly indicating focused studies or surveys conducted in these nations.

### Suggestions for Further Investigation

1. **Handling Missing Values**: 
   - Analyze the patterns of missing data. Implementing appropriate imputation techniques could enhance the dataset’s integrity and reliability.

2. **Temporal Analysis**:
   - Conduct time-series analysis to observe how the sentiments reflected in "Life Ladder" and other socio-economic indicators have evolved over the years.

3. **Disparity Exploration**:
   - Examine disparities among countries with similar economic profiles but differing "Life Ladder" scores. This could unveil cultural, social, or political factors influencing life satisfaction.

4. **Cluster Analysis**:
   - Perform cluster analysis on countries based on socio-economic indicators and life satisfaction metrics to categorize them into distinct groups. This could provide insights into socio-economic performance and citizen well-being.

5. **Study Specific Regions**:
   - Focus on geographic disparities by segmenting the data by continent or region to identify localized patterns and trends.

6. **Examine Causality**:
   - Employ regression analysis or structural equation modeling to explore potential causal relationships between well-being indicators and life satisfaction.

7. **Deep Dive into Emotional Metrics**:
   - Analyze the emotional metrics further, contrasting countries with high "Positive affect" against those with low "Negative affect" to differentiate the socio-cultural factors at play.

By pursuing these directions, researchers can deepen insights gleaned from the dataset and potentially offer actionable recommendations for improving life satisfaction across different demographics and regions.

## Visualizations
![correlation_heatmap.png](happiness\correlation_heatmap.png)
![year_distribution.png](happiness\year_distribution.png)
![Life Ladder_distribution.png](happiness\Life Ladder_distribution.png)
![Log GDP per capita_distribution.png](happiness\Log GDP per capita_distribution.png)
![Social support_distribution.png](happiness\Social support_distribution.png)
![Healthy life expectancy at birth_distribution.png](happiness\Healthy life expectancy at birth_distribution.png)
![Freedom to make life choices_distribution.png](happiness\Freedom to make life choices_distribution.png)
![Generosity_distribution.png](happiness\Generosity_distribution.png)
![Perceptions of corruption_distribution.png](happiness\Perceptions of corruption_distribution.png)
![Positive affect_distribution.png](happiness\Positive affect_distribution.png)
![Negative affect_distribution.png](happiness\Negative affect_distribution.png)
