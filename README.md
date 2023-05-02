## Telecome Industry Offer Recommender

### Introduction

Offer recommendation in the telecom industry refers to the process of suggesting personalized offers to customers based on their usage patterns, demographics, and other relevant factors. Offering recommendations in the telecom industry is crucial for improving customer satisfaction and increasing revenue. By using advanced algorithms and big data techniques, telecom companies can provide customers with relevant and valuable offers, leading to higher customer loyalty and long-term growth.

### Business Impact of Offer Recommendation

- Increase customer satisfaction: Offer recommendation allows telecom companies to understand their customers better and provide them with relevant and valuable offers, leading to higher customer satisfaction.

- Increase revenue: By providing customers with relevant and valuable offers, telecom companies can increase their revenue through increased customer spending and reduced churn.

- Improve customer loyalty: By providing personalized offers to customers, telecom companies can create a better customer experience and build stronger relationships with their customers, leading to higher customer loyalty.

## Possible Solutions:-

### Methods for Offer Recommendation
1. Rule-based systems:
In this approach, offers are recommended based on predefined rules. Rule-based systems are easy to implement and interpret, but they may not be very accurate or adaptive. It makes sense to use them when you have a specific business mandate (example - we want to use product A to promote product B because of a Marketing Strategy so we will recommend product B to everyone who bot A).

2. Collaborative filtering:
Collaborative filtering is a type of recommendation that recommends offers based on the preferences of similar customers. In this approach, we find what customers are similar among themselves and similar offers to similar customers.

3. Content-based filtering:
In this approach, the system builds a model of the customer's preferences based on the features of the offers they have interacted with and then recommends offers that are similar in terms of those features. Content-based filtering is useful when the system has access to rich feature data, but it can struggle with the cold start problem (i.e., recommending new offers to customers who have not interacted with any offers yet). This is the type of thing that powers retailers' recommendations - they get similar products to what you bought and recommend it to you.

4. Hybrid systems:
Hybrid systems combine different approaches to leverage their strengths and mitigate their weaknesses. For example, a system might use a collaborative filtering approach to recommend offers to customers who have already interacted with offers, and a content-based approach to recommend offers to new customers.

### Assumptions
- We assume that there are multiple offers available
- We also assume that, at this point, a customer can only have 1 offer activated
- The column offer indicates what was offered to the customer, while the churn status indicates if the customer churned or not
- If the customer has an offer and no churn status, we will assume that they are currently using that offer

### Approach
We are treating this problem as an unsupervised learning problem. This means that, in practice, we don't have a way in this dataset to validate if what we did is 'right' or 'wrong'.

In real life, the approach here would be to test this algorithm with real customers to see if this improves churn.

Given our assumptions about the offers, we will build a collaborative-filtering system based on the user. Simplifying, here's the logic of what we'll build:

- We'll build an algorithm to identify who identifies, for customer A, who are the n-most similar customers;
- We'll use a churn-rate approach to identify, among the similar customers, what is the most successful offer;
- We will then choose the most successful offer to provide to our customer A.
- We'll be training this algorithm on part of the dataset of customers who have received the offer (have A,B,C,D,E,F,G,H,I or J) in their 'offer' field. The idea is to apply that to the 'No Offer' group.

### Unsupervised Machine Learning:

In unsupervised machine learning, the algorithm is trained on an unlabeled dataset without any predefined target variable. The goal is to identify patterns, relationships, and structures within the data, such as clustering, dimensionality reduction, or anomaly detection, without any prior knowledge of the data distribution or outcome variable.

## Execution Instructions
#### Package Requirements

`!pip install numpy==1.22.4 --quiet`
`!pip install pandas==1.3.5 --quiet`
`!pip install scikit-learn==1.2.1  --quiet`

### 1) Data Reading from Different Sources
**AWS S3 - CSV**
- Use the S3 public link to read the CSV file directly into a pandas DataFrame
`s3_link = 'https://s3.amazonaws.com/projex.dezyre.com/recommender-system-for-telecom-products/materials/Telecom_data.csv'`
`df = pd.read_csv(s3_link)`

### 2) Exploratory Data Analysis
**Data Exploration**

## **Data Dictionary**



| Column name	 | Description|
| ----- | ----- |
| Customer ID	 | Unique identifier for each customer |
| Month | Calendar Month- 1:12 | 
| Month of Joining |	Calender Month -1:14, Month for which the data is captured|
| zip_code |	Zip Code|
|Gender |	Gender|
| Age |	Age(Years)|
| Married |	Marital Status |
|Dependents | Dependents - Binary |
| Number of Dependents |	Number of Dependents|
|Location ID |	Location ID|
|Service ID	 |Service ID|
|state|	State|
|county	|County|
|timezone	|Timezone|
|area_codes|	Area Code|
|country	|Country|
|latitude|	Latitude|
|longitude	|Longitude|
|arpu|	Average revenue per user|
|roam_ic	|Roaming incoming calls in minutes|
|roam_og	|Roaming outgoing calls in minutes|
|loc_og_t2t|	Local outgoing calls within same network in minutes|
|loc_og_t2m	|Local outgoing calls outside network in minutes(outside same + partner network)|
|loc_og_t2f|	Local outgoing calls with Partner network in minutes|
|loc_og_t2c	|Local outgoing calls with Call Center in minutes|
|std_og_t2t|	STD outgoing calls within same network in minutes|
|std_og_t2m|	STD outgoing calls outside network in minutes(outside same + partner network)|
|std_og_t2f|	STD outgoing calls with Partner network in minutes|
|std_og_t2c	|STD outgoing calls with Call Center in minutes|
|isd_og|	ISD Outgoing calls|
|spl_og	|Special Outgoing calls|
|og_others|	Other Outgoing Calls|
|loc_ic_t2t|	Local incoming calls within same network in minutes|
|loc_ic_t2m|	Local incoming calls outside network in minutes(outside same + partner network)|
|loc_ic_t2f	|Local incoming calls with Partner network in minutes|
|std_ic_t2t	|STD incoming calls within same network in minutes|
|std_ic_t2m	|STD incoming calls outside network in minutes(outside same + partner network)|
|std_ic_t2f|	STD incoming calls with Partner network in minutes|
|std_ic_t2o|	STD incoming calls operators other networks in minutes|
|spl_ic|	Special Incoming calls in minutes|
|isd_ic|	ISD Incoming calls in minutes|
|ic_others|	Other Incoming Calls|
|total_rech_amt|	Total Recharge Amount in Local Currency|
|total_rech_data|	Total Recharge Amount for Data in Local Currency
|vol_4g|	4G Internet Used in GB|
|vol_5g|	5G Internet used in GB|
|arpu_5g|	Average revenue per user over 5G network|
|arpu_4g|	Average revenue per user over 4G network|
|night_pck_user|	Is Night Pack User(Specific Scheme)|
|fb_user|	Social Networking scheme|
|aug_vbc_5g|	Volume Based cost for 5G network (outside the scheme paid based on extra usage)|
|offer|	Offer Given to User|
|Referred a Friend|	Referred a Friend : Binary|
|Number of Referrals|	Number of Referrals|
|Phone Service|	Phone Service: Binary|
|Multiple Lines|	Multiple Lines for phone service: Binary|
|Internet Service|	Internet Service: Binary|
|Internet Type|	Internet Type|
|Streaming Data Consumption|	Streaming Data Consumption|
|Online Security|	Online Security|
|Online Backup|	Online Backup|
|Device Protection Plan|	Device Protection Plan|
|Premium Tech Support|	Premium Tech Support|
|Streaming TV|	Streaming TV|
|Streaming Movies|	Streaming Movies|
|Streaming Music|	Streaming Music|
|Unlimited Data|	Unlimited Data|
|Payment Method|	Payment Method|
|Status ID|	Status ID|
|Satisfaction Score|	Satisfaction Score|
|Churn Category|	Churn Category|
|Churn Reason|	Churn Reason|
|Customer Status|	Customer Status|
|Churn Value|	Binary Churn Value


## 3)Data Processing
 - **Missing Value Detection and Imputation**
 - **Outlier Detection and Imputation**

## 4)Data Preprocessing and Leakage

# Feature engineering
**1. Splitting the dataset into a training and production dataset**
**2. Converting the Month of Joining into a customer tenure**
**3.Transforming Categorical Variables**

# Model Building and Testing
## Collaborative filtering

## **Mathematical explanation for distance measure**

Manhattan, cosine, and Euclidean distance are different distance metrics used in machine learning and data science.

### **Manhattan distance:**
Manhattan distance, also known as taxicab distance or L1 distance, is a measure of the distance between two points in a n-dimensional space. It is called Manhattan distance because it is analogous to the distance a taxi would travel on the streets of Manhattan, where you can only move in straight lines along the grid.
The formula for Manhattan distance between two points P and Q in n-dimensional space is:

\begin{equation}
d(P,Q) = |x_1-y_1| + |x_2-y_2| + ... + |x_n-y_n|
\end{equation}

where $x_1, x_2, ..., x_n$ are the coordinates of point $P$ and $y_1, y_2, ..., y_n$ are the coordinates of point $Q$.

### **Cosine similarity:**
Cosine similarity is a measure of the similarity between two non-zero vectors of an inner product space. It is the cosine of the angle between the two vectors and ranges from -1 to 1. A value of 1 indicates that the two vectors are identical, while a value of -1 indicates that they are completely dissimilar.
The formula for cosine similarity between two vectors A and B is:

\begin{equation}
\text{cosine   similarity}(A, B) = \frac{A * B }{ ||A|| * ||B||}
\end{equation}



where $A * B$ is the dot product of vectors A and B, and $||A||$ and $||B||$ are the magnitudes of vectors A and B, respectively.

###**Euclidean distance:**
Euclidean distance is a measure of the distance between two points in a n-dimensional space. It is called Euclidean distance because it is the distance between two points in a straight line, as defined by Euclidean geometry.
The formula for Euclidean distance between two points P and Q in n-dimensional space is:
\begin{equation}
d(P,Q) = \sqrt{(x_1-y_1)^2 + (x_2-y_2)^2 + ... + (x_n-y_n)^2}
\end{equation}
where $x_1$, $x_2$, ..., $x_n$ are the coordinates of point P and $y_1, y_2, ..., y_n$ are the coordinates of point Q.

## **The minimal threshold parameter**

Whenever we are building any framework, and especially unsupervised ones, it is important that we establish parameters that can help us have confidence in what we are doing.

In this particular case, we are assigning a minimal threshold of 10% for an offer to be potentially chosen to customers.

This comes from the fact that we have 10 offers (A-> J). If we were to randomly assign an offer to a customer, we would likely give each offer an equal probability of being assigned, so 100%/10%. So given that, if we are going to recommend something, it needs to be better than the random assignment.

## **Which distance to choose?**

In Summary
*  Manhattan distance: This metric measures the distance between two points by summing the absolute differences between their coordinates. It is also called the "taxicab" or "city block" distance because it measures the distance a taxicab would have to travel to get from one point to another on a city grid. 

*  Cosine similarity: This metric measures the cosine of the angle between two vectors in a high-dimensional space. It is commonly used in text analysis and information retrieval to measure the similarity between documents. Cosine similarity is often preferred over Euclidean distance when the magnitude of the vectors is not important, and only the direction matters.

*  Euclidean distance: This metric measures the distance between two points in a straight line. It is the most common distance metric used in machine learning and data science. Euclidean distance is useful when the data is dense, and the features have similar scales.

In general, if you have high-dimensional data or sparse data, Manhattan or cosine distance may be more appropriate. If you have dense data with similar scales, Euclidean distance is a good choice.

For this problem in particular, we recommend Manhattan or Cosine

## **Bootstrapping the framework**


Especially in unsupervised learning problems, it is always a good idea to run several approaches ('bootstrap') and chose the most common answer amongst the different models. This mechanism is similar to what algorithms like random forest do, for example: they fit several trees and each tree votes the final classification of a sample.

We are going to play with the 3 distances we have in our function + the number of customers we pull the data from in order to get a voted answer

## **Conclusion**

In this project we used a simple yet effective unsupervised model to provide offers to customers.

A collaborative offer recommendation system can be a valuable tool for telecom companies to increase customer satisfaction and revenue. By using data on customer behavior and preferences, the system can provide personalized offers that are more likely to be accepted by customers.

To implement such a system, several steps need to be taken, including collecting and cleaning data, creating customer profiles, selecting appropriate distance functions, and validating the system's performance. It is also essential to consider ethical considerations related to data privacy and security.

Overall, a collaborative offer recommendation system can be a powerful tool for telecom companies to enhance their marketing strategies and provide better services to their customers. However, it is important to continuously evaluate and update the system to ensure its effectiveness and address any potential issues.


In conclusion, a successful data science project requires a clear understanding of the business problem and the data available, as well as the ability to select and apply appropriate data preprocessing techniques, feature engineering methods, and machine learning algorithms. It is also important to assess and optimize the performance of the model and communicate the results effectively to stakeholders. 

