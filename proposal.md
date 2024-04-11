# 911 Project

## Team Member

Liming Huang(Team Lead), Anqi Nie, Jiahong Liu

## Stakeholders

- [Teresa May, DO](https://www.mainehealth.org/providers/teresa-l-may-do) -- Internal Medicine, Critical Care, Pulmonary Disease, Neurocritical Care, Maine Health
- [Christine Lary, PhD](https://roux.northeastern.edu/people/christine-lary/) -- Research Associate Professor, The Roux Institute
- [Qingchu Jin, PhD](https://roux.northeastern.edu/people/qingchu-jin/) -- Research Scientist (Primary POC), The Roux Institute

## Project Background:

The National Emergency Medical Services Information System (NEMSIS) gathers, stores, and disseminates EMS data across the U.S., aiding organizations in assessing and improving EMS performance and planning. Our project focuses on the EMS data subset related to cardiac arrest incidents, particularly analyzing the disparities in rescue outcomes in Maine's rural versus urban settings. Initial findings indicate a significant underuse of epinephrine, prompting further investigation into geographical disparities and procedural effectiveness.

## Project Goal:

Our primary goal is to employ statistical analysis to understand and improve the effectiveness of first responder interventions during cardiac arrest incidents, with a focus on the administration of epinephrine. We aim to:

1. Predict the likelihood of epinephrine administration based on factors like patient demographics, incident location (rural vs urban), and time of response.
2. Classify the outcomes of rescue efforts (e.g., survival rates, recovery quality) using predictors derived from the EMS data.

## Methodology:
We propose using Lasso Regression for both prediction and classification tasks due to its efficiency in handling high-dimensional data and its ability to perform feature selection:

1. Data Preprocessing: Filter the NEMSIS dataset to focus on cardiac arrest incidents. Cleanse the data for missing values and outliers, particularly focusing on the rural and urban classification.
2. Feature Engineering: Develop features from raw data, such as time to intervention, type of intervention, demographic data, and geographic data (rural vs urban settings).
Lasso Regression Analysis:
3. Prediction Model: Develop a model to predict the probability of epinephrine use. Use Lasso regression to identify the most impactful predictors and reduce overfitting.
Classification Model: Build a classification model to categorize patient outcomes post-rescue. Evaluate model performance using accuracy, precision, and recall metrics.
4. Validation: Use cross-validation techniques to assess the robustness of the models. Ensure that the models perform well across different subsets of data, particularly when distinguishing between rural and urban scenarios.

Data Utilization:
Focus on a specific subset of the NEMSIS dataset pertaining to cardiac arrests, ensuring a more manageable and relevant analysis scope. This subset will be screened to ensure data integrity and relevance to the research questions posed.

Theoretical Framework:
Integrate theories related to emergency medical response, geographical influence on healthcare access, and statistical analysis in epidemiology. This comprehensive approach will allow us to explore complex interactions between variables and provide actionable insights.

Risk and Considerations:
Address potential biases in data collection and the challenge of applying findings across diverse geographic settings. Assess the validity of the dataset by comparing observed epinephrine administration rates with expected norms.
