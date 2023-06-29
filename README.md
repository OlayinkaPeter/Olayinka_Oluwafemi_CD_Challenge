# 1. Credit Risk Scoring Challenge | Logistic Regression | GermanCredit

The steps in the notebook are as follows: 
 

1.   Install & import necessary libraries.
2.   Cleaning our data
3.   One-hot Encoding for categorical data
4.   Splitting into Training Data and Testing Data
     * Split features from labels
5.   Normalization
6.   Building the model: Logistic Regression with Keras
7.   Train the model
8.   Evaluate the model  
9.   Run predictions on validation data  
10.   Deployment


<br>


# 2. Feature Engineering Challenge

The importance of extracting each of the following features from the
Credit Bureau dataset can vary depending on the specific context 
and use case. 

However, for our case, we have selected 54 features and here are some 
general reasons why the chosen features are considered important:

* **`no_of_other_accounts_bad`** and **`no_of_other_accounts_good`**: These features provide information about the number of other accounts the individual has, categorized as either bad or good. It helps evaluate the individual's credit behavior and history in relation to accounts other than the specific types mentioned in the other features. It provides insights into the overall credit risk associated with the individual.
* **`no_of_retail_accounts_bad`** and **`no_of_retail_accounts_good`**: These features indicate the number of retail accounts the individual has, categorized as either bad or good. Retail accounts are often associated with consumer credit, such as credit cards or store cards. They provide insights into the individual's credit utilization, payment history, and financial responsibility in the retail sector.
* **`no_of_telecom_accounts_bad`** and **`no_of_telecom_accounts_good`**: These features represent the number of telecom accounts the individual has, categorized as either bad or good. Telecom accounts include mobile phone contracts or utility bills. They provide insights into the individual's payment history and financial commitments in the telecom sector.
* **`no_of_autoloan_accounts_bad`** and **`no_of_autoloan_accounts_good`**: These features indicate the number of auto loan accounts the individual has, categorized as either bad or good. Auto loan accounts provide insights into the individual's ability to manage vehicle financing and their creditworthiness in the automotive lending sector.
* **`no_of_jointloan_accounts_bad`** and **`no_of_jointloan_accounts_good`**: These features represent the number of joint loan accounts the individual has, categorized as either bad or good. Joint loan accounts involve multiple borrowers sharing the responsibility for repayment. They provide insights into the individual's credit behavior and financial obligations in joint lending situations.
* **`no_of_studyloan_accounts_bad`** and **`no_of_studyloan_accounts_good`**: These features indicate the number of study loan accounts the individual has, categorized as either bad or good. Study loan accounts reflect the individual's educational borrowing and repayment history. They provide insights into their financial responsibility and repayment behavior in the education lending sector.
* **`no_of_homeloan_accounts_bad`** and **`no_of_homeloan_accounts_good`**: This feature provides information about the number of home loan accounts that have been labeled as bad or good, respectively.. Home loan accounts are significant financial obligations, and a higher number of good home loan accounts indicates the individual's ability to manage mortgage repayments and maintain a positive credit history. It reflects their financial stability and responsible behavior in managing home loan debt. While the number of bad home loan accounts can indicate the individual's financial distress or difficulties in managing mortgage repayments.
* **`no_of_creditcard_accounts_bad`** and **`no_of_creditcard_accounts_good`**: These features indicate the number of credit card accounts that have been labeled as bad or good, respectively. Credit card accounts are commonly used credit instruments, and their performance is crucial in credit assessments. A higher number of good credit card accounts suggests responsible credit card usage and repayment behavior, while a higher number of bad credit card accounts may indicate financial distress or difficulties in managing credit card debt.
* **`no_of_personalloan_accounts_bad`** and **`no_of_personalloan_accounts_good`**: These features represent the number of personal loan accounts that have been labeled as bad or good, respectively. Personal loan accounts provide insights into the individual's borrowing behavior and repayment history outside of specific sectors like home or auto loans. A higher number of good personal loan accounts indicates responsible borrowing and timely repayments, while a higher number of bad personal loan accounts may indicate financial difficulties or defaulting on loan obligations.
* **`enquiry_matching_rate`**: This feature indicates the rate of enquiry matching, which represents how closely the individual's credit inquiries align with the records in the CreditHistory dataset. Enquiry matching is important as it helps verify the accuracy and reliability of the credit information provided by the individual. Higher matching rates indicate a more accurate representation of the individual's credit behavior and history.
* **`no_of_guarantor_accounts`** and **`no_of_guarantors_secured`**: These features provide information about the number of guarantor accounts and the number of guarantors secured, respectively. Guarantor accounts involve a third party guaranteeing the repayment of a loan or credit facility. These features can be important in assessing the individual's level of financial responsibility, as well as the potential risk associated with the presence of guarantors.
* **`guarantor_date_of_birth`**: This feature represents the guarantor's date of birth. It can be useful in verifying the age and legal capacity of the guarantor and assessing their suitability for assuming financial responsibility.
* **`employment_type`**: This feature indicates the type of employment of the individual. Employment type is crucial in credit assessment as it provides insights into the stability of income, job security, and overall financial capacity. Different employment types may have varying levels of risk associated with them.
* **`no_of_past_enquiries`**: This feature indicates the number of previous credit inquiries made by the individual. It can provide insights into the applicant's credit-seeking behavior and their level of credit activity.
* **`rating`**: The credit rating represents the evaluation of an individual's creditworthiness. It is often used by lenders to assess the borrower's ability to repay loans. This feature is crucial in determining the risk associated with extending credit to a particular individual.
* **`amount_arrear`** and **`amount_arrear_extra`**: These features indicate the amount of outstanding payments or debts that are past their due dates. They provide information about the individual's payment history and their ability to meet financial obligations.
* **`total_accounts`** and **`total_accounts_extra`**: These features represent the total number of accounts or credit lines the individual holds. They provide an overview of the person's credit utilization and financial commitments.
* **`total_account_arrear`** and **`total_account_arrear_extra`**: These features indicate the total amount of arrears across all accounts held by the individual. They provide insights into the overall level of delinquency and financial distress.
* **`total_judgement_amount`** and **`total_judgement_amount_extra`**: These features represent the total amount of outstanding judgments against the individual. Judgments can be significant negative factors in credit assessment, as they indicate legal actions taken due to unpaid debts or financial disputes.
* **`total_outstanding_debt`** and **`total_outstanding_debt_extra`**: These features indicate the total amount of debt owed by the individual across all accounts. It provides an assessment of the individual's overall financial liability and debt burden.
* **`total_dishonoured_amount`** and **`total_dishonoured_amount_extra`**: These features represent the total amount of dishonored or bounced payments made by the individual. They provide insights into the individual's financial stability and ability to manage their finances responsibly.
* **`total_monthly_instalment`** and **`total_monthly_instalment_extra`**: These features indicate the total amount of monthly installment payments the individual is obligated to pay. It provides insights into their ongoing financial commitments and ability to manage debt repayment.
* **`total_number_of_judgement`** and **`total_number_of_judgement_extra`**: These features indicate the total number of judgments against the individual. It provides additional information about their financial history and legal disputes.
* **`total_number_of_dishonoured`** and **`total_number_of_dishonoured_extra`**: These features indicate the total number of dishonored payments made by the individual. They provide insights into their financial behavior and ability to fulfill payment obligations.
* **`total_account_in_good_condition`** and **`total_account_in_good_condition_extra`**: These features represent the total number of accounts in good standing or with a positive credit history. They indicate the individual's ability to manage credit responsibly and make timely payments.
* **`account_bank_name`**: This feature represents the name of the bank associated with the account. It can provide insights into the individual's banking relationships and potentially impact credit decisions.
* **`account_age_date`**: This feature indicates the age or duration of the account. It provides information about the length of the individual's credit history, which is an important factor in credit assessment.
* **`identification_provision`**: This feature indicates the type or provision of identification used by the individual. It can be relevant for verification and authentication purposes.
* **`total_credit_amount_overdue`**: This feature represents the total amount of credit that is currently overdue. It provides insights into the individual's current financial liabilities and their ability to manage debt repayment.
* **`gender`**: Gender can be relevant in credit assessment as it may influence factors such as employment stability, income levels, and overall financial behavior. Certain industries or financial products might have gender-specific risk profiles, making this feature useful for evaluating creditworthiness.
* **`birthdate`**: Birthdate or age is crucial for assessing creditworthiness. It helps determine the individual's credit history length, stability, and potential retirement timeline. Age can also be a factor in assessing income levels, employment stability, and overall financial responsibility.
* **`dependants`**: The number of dependents an individual has can provide insights into their financial obligations and responsibilities. It helps evaluate the individual's ability to manage their finances, especially when considering their ability to meet additional financial commitments.
* **`nationality`**: Nationality can impact credit assessment, especially in cases where it influences factors such as residency status, legal obligations, and potential access to certain financial products or services. It can also provide insights into the individual's exposure to political or economic risks.
* **`property_owned_type`**: This feature indicates the type of property owned by the individual. Property ownership can be an important factor in credit assessment, as it provides insights into the individual's assets, collateral options, and overall financial stability. Different property types may have varying levels of risk associated with them.


<br>


# 3. SQL Code Challenge

## — On which day of the week do we on average have the longest trip?

``` sql
SELECT
    DATE_FORMAT(start_time, '%W') AS day_of_week,
    AVG(duration_minutes) AS average_trip_duration
FROM
    bikerdatav2
GROUP BY
    day_of_week
ORDER BY
    average_trip_duration DESC
LIMIT 1;
```


## — What month/year has the most bike trips and what is the count of the trips?

``` sql
SELECT
    DATE_FORMAT(start_time, '%Y-%m') AS month_year,
    COUNT(*) AS trip_count
FROM
    bikerdatav2
GROUP BY
    month_year
ORDER BY
    trip_count DESC
LIMIT 1;
```

####  We can use `EXTRACT` for year specifically

``` sql
SELECT
    EXTRACT(YEAR FROM start_time) AS year,
    COUNT(*) AS trip_count
FROM
    bikerdatav2
GROUP BY
    year
ORDER BY
    trip_count DESC
LIMIT 1;
```


## — In the same table, return which particular trip has longest duration and the trip that has the shortest duration (return all the information(columns) on the table for this record)

``` sql
SELECT *
FROM bikerdatav2
WHERE start_station_id != end_station_id
  AND duration_minutes = (
    SELECT MAX(duration_minutes)
    FROM bikerdatav2
    WHERE start_station_id != end_station_id
  )
UNION ALL
SELECT *
FROM bikerdatav2
WHERE start_station_id != end_station_id
  AND duration_minutes = (
    SELECT MIN(duration_minutes)
    FROM bikerdatav2
    WHERE start_station_id != end_station_id
  );
```

