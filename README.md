# Stallion-Statistics - Racing Insights

![Screenshot](Stallion_Statistics.png)

**Our Team:**

- Ayman Sulaiman https://www.linkedin.com/in/s-ayman-sulaiman/
- Andrew Wright https://www.linkedin.com/in/aesdub/
- Aldo Garcia https://www.linkedin.com/in/aldo-garcia-02/
- Hakob Harutyunyan https://www.linkedin.com/in/hakob-harutyunyan-4a7360199/

**Objective:**

Our goal as a team is the provide racing insights on both previous and upcoming races for the Churchill Downs racetrack. Even more in depth, using different programming languages and machine learning, we have created multiple ML models. These models can predict whether a horse is going to win or lose. 

**Methods:**

Retrieved the data from a reputable betting betting brand via SQL.  We cleaned the data with Pandas and stored the clean data into an S3 Bucket.  The cleaned data was then placed into a tableau workspace to preform analytics to gain insights into the data.  The clean data was also put through Machine Learning Algorithms to see what model would be the most reliable giving us true results.  The results of the machine learning models were analysed for accuracy and precision. To further develope insights into our models, an ROI analysis was conducted.

**ROI Analysis**

We found the Naive-Bayes model returned the highest ROI for the $2 bet simulation. While the XGBoost model returned the highest win rate, it's selected horses were lower on the odds spectrum, producing lower winnings as a result. The Naive-Bayes 23.1% win rate and ROI of -21.9% was the most successful of the three.

<img src="ROI_analysis.png" alt="drawing" height="600px"/>

**Next Steps**
- Running a probabilty model for a horse to get into 3 places in a race
- Applying a Neural Network/ AI with TensorFlow
- More Experimentation with more features with larger datasets

**Link to our [website](https://stallion-stats.herokuapp.com/)**


**Programming Languages/Technology Used:**

- Python
- Machine Learning Classification
- Javascript
- Tableau
- Dash
- Matplotlib
- HTML
- SQL 
- AWS S3







