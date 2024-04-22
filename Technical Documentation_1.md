# Technical Documentation

#### Setting Up Conda and Initializing the Environment with environment.yml

This project utilizes Conda to manage the Python environment and its dependencies. Use the following command to set up and activate the environment:

```
conda env create -f environment.yml && conda activate project
```

#### Data Importation

Request data access from the project stakeholder. Decompress and relocate the `processeddataCA` folder into the local data directory. Execute the command below to populate a SQLite3 database file (`nemsis.db`). This process involves cleaning the data (e.g., removing extra spaces) and deleting missing values such as "not applicable," "not recorded," or "unknown." It also includes the imputation of features essential for model development.

```
make preprocess.db
```

#### Handling Missing Data by Deletion

According to the [NEMSIS data user manual](https://nemsis.org/wp-content/uploads/2021/05/2020-NEMSIS-RDS-340-User-Manual_v3-FINAL.pdf), missing data varies widely across the elements in the National EMS Database. It is crucial to address these gaps appropriately to avoid analysis bias. Typically, software defaults to omitting data points with missing values during statistical analysis, which can lead to misleading outcomes. Alternatively, while supplying plausible substitute values through single or multiple imputation strategies can mitigate this issue, our approach varies depending on the data type:

1. For time-related data: We implement mean imputation to fill in missing entries.
2. For all other data types: We remove entries with missing values altogether.

This decision was based on the following considerations:

Mean Imputation for Time Data:
- Using the mean value to impute missing time data helps maintain the integrity of temporal relationships and ensures that analyses involving time variables are based on complete data sets. This method is chosen due to its simplicity and effectiveness in dealing with time series data where the continuity of time is crucial.

Deletion for Other Data Types:

- For categorical and numerical data that are not time-dependent, we opt to remove rows with missing data entirely. This is because imputation could introduce biases or distort the true characteristics of the data set, especially when the missing data is not missing at random.

**Implications of Our Approaches**

Data Integrity:
- By selectively imputing or removing missing data based on their types, we ensure that our analyses utilize the most appropriate and accurate information available. This maintains the reliability of our statistical conclusions without compromising the natural variance and relationships within the data.

Impact on Data Set Size:
- Although these methods might reduce the overall size of the data set, the remaining data are fully usable and more representative of the true phenomena being studied. For time data, mean imputation preserves essential temporal information which might be crucial for trend analysis and forecasting.

Simplified Data Handling:
- Our approach eliminates the need for managing multiple imputation methodologies across different types of data, simplifying the data preparation process. It also enhances the clarity and quality of our exploratory data analysis (EDA) and modeling stages by maintaining consistency in how missing values are handled across data types.

In conclusion, these tailored strategies for different data types help in optimizing the integrity and usability of the dataset. Entries that are imputed are carefully considered to prevent any potential misinterpretations, while the deletion of non-time data ensures that our analyses are robust and representative. This approach effectively balances the benefits of imputation for continuous data and the purity of the dataset by removing incomplete entries where appropriate.

#### Data Translation and Mapping

We anonymized the NEMSIS dataset and implemented translation functions in `src/map_feature_values.py` to convert data element codes into interpretable values. This was crucial for effective querying and exploratory analysis. The mappings for feature constants and values are stored in `src/feature-names.py` and `src/feature-values.py`.

#### Utility Scripts for Data Handling

To facilitate model preparation, we developed utility scripts housed in `src/data_helpers.py`. These scripts assist in querying feature data and setting up datasets for the xgBoost model. 

We filtered the dataset based on excessively long response times, older ages, and the presence of logical errors. The logical errors refer to clear contradictions in the dataset's records. For example, inconsistencies between cardiac arrest and electrocardiography (ECG) recordings:

- eVitals.04 - Showing any Cardiac Rhythm / Electrocardiography (ECG) pattern
- eVitals.10 - Heart Rate A logical contradiction occurs if the ECG record shows 'asystole' (no cardiac activity), but the heart rate is not zero.

Another example involves records of confirmed death and the destination being ICU:

- eDisposition.12 - Incident/Patient Disposition
- eDisposition.21 - Type of Destination. It is illogical for the records to state that a patient chose not to be transferred or have deceased yet the destination type is not null.

#### Model Development Tools

We enriched our toolkit with cross-validation utilities in `cross_val_helpers.py`, which manage input features and target values for various models. These tools prepare grid search parameters and pipelines tailored to the model type, execute train-test splits, perform grid searches, and identify the optimal estimator. The evaluation of this estimator on a "holdout" set helps gauge model performance and is supported by visualization tools for ROC curves and confusion matrices.