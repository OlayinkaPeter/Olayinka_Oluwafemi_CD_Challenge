import csv
import json
import logging
from re import sub
from decimal import Decimal


class FeatureExtraction:
    """
        FeatureExtraction class to extract and transform features
    """
    extracted_features: list = []
    feature: dict = {}
    csv_file: str = "extracted_features.csv"

    def __init__(self, file_path):
        self.json_file_path = file_path

    def extract_features_from_json(self):
        """Extracts and transforms features from the given JSON data.
                Args:
                    self.json_file_path: File path for a JSON object containing credit data.
                :return:
                    A dictionary containing the extracted features.

                Important credit bureau features to be extracted for ML decision making:
                    : no_of_other_accounts_bad : Number of other accounts that have been labelled to be bad
                    : no_of_other_accounts_good : Number of other accounts that have been labelled to be good
                    : no_of_retail_accounts_bad : Number of retail accounts that have been labelled to be bad
                    : no_of_retail_accounts_good : Number of retail accounts that have been labelled to be good
                    : no_of_telecom_accounts_bad : Number of telecom accounts that have been labelled to be bad
                    : no_of_telecom_accounts_good : Number of telecom accounts that have been labelled to be good
                    : no_of_autoloan_accounts_bad : Number of auto loan accounts that have been labelled to be bad
                    : no_of_autoloan_accounts_good : Number of auto loan accounts that have been labelled to be good
                    : no_of_jointloan_accounts_bad : Number of joint loan accounts that have been labelled to be bad
                    : no_of_jointloan_accounts_good : Number of joint loan accounts that have been labelled to be good
                    : no_of_studyloan_accounts_bad : Number of study loan accounts that have been labelled to be bad
                    : no_of_studyloan_accounts_good : Number of study loan accounts that have been labelled to be good
                    : no_of_homeloan_accounts_bad : Number of home loan accounts that have been labelled to be bad
                    : no_of_homeloan_accounts_good : Number of home loan accounts that have been labelled to be good
                    : no_of_creditcard_accounts_bad : Number of credit card accounts that have been labelled to be bad
                    : no_of_creditcard_accounts_good : Number of credit card accounts that have been labelled to be good
                    : no_of_personalloan_accounts_bad : Number of personal loan accounts that have been labelled to be bad
                    : no_of_personalloan_accounts_good : Number of personal loan accounts that have been labelled to be good
                    : enquiry_matching_rate : Rate of enquiry matching
                    : no_of_guarantor_accounts : Number of guarantor accounts
                    : no_of_guarantors_secured : Number of guarantors secured
                    : guarantor_date_of_birth : Guarantor data of birth
                    : employment_type : Employment type
                    : no_of_past_enquiries :
                    : rating :
                    : amount_arrear :
                    : amount_arrear_extra :
                    : total_accounts :
                    : total_accounts_extra :
                    : total_account_arrear :
                    : total_account_arrear_extra :
                    : total_judgement_amount :
                    : total_judgement_amount_extra :
                    : total_outstanding_debt :
                    : total_outstanding_debt_extra :
                    : total_dishonoured_amount :
                    : total_dishonoured_amount_extra :
                    : total_monthly_instalment :
                    : total_monthly_instalment_extra :
                    : total_number_of_judgement :
                    : total_number_of_judgement_extra :
                    : total_number_of_dishonoured :
                    : total_number_of_dishonoured_extra :
                    : total_account_in_good_condition :
                    : total_account_in_good_condition_extra :
                    : account_bank_name :
                    : account_age_date :
                    : identification_provision :
                    : total_credit_amount_overdue :
                    : gender :
                    : birthdate :
                    : dependants :
                    : nationality :
                    : property_owned_type :
        """
        try:
            with open(self.json_file_path, 'r') as file:
                data = json.load(file)
                self.extracted_features = []

                for item in data:
                    feature = {}

                    feature['no_of_other_accounts_bad'] = item['data']['consumerfullcredit']['accountrating'][
                        'noofotheraccountsbad']
                    feature['no_of_other_accounts_good'] = item['data']['consumerfullcredit']['accountrating'][
                        'noofotheraccountsgood']
                    feature['no_of_retail_accounts_bad'] = item['data']['consumerfullcredit']['accountrating'][
                        'noofretailaccountsbad']
                    feature['no_of_retail_accounts_good'] = item['data']['consumerfullcredit']['accountrating'][
                        'noofretailaccountsgood']
                    feature['no_of_telecom_accounts_bad'] = item['data']['consumerfullcredit']['accountrating'][
                        'nooftelecomaccountsbad']
                    feature['no_of_autoloan_accounts_bad'] = item['data']['consumerfullcredit']['accountrating'][
                        'noofautoloanaccountsbad']
                    feature['no_of_autoloan_accounts_good'] = item['data']['consumerfullcredit']['accountrating'][
                        'noofautoloanccountsgood']
                    feature['no_of_homeloan_accounts_bad'] = item['data']['consumerfullcredit']['accountrating'][
                        'noofhomeloanaccountsbad']
                    feature['no_of_telecom_accounts_good'] = item['data']['consumerfullcredit']['accountrating'][
                        'nooftelecomaccountsgood']
                    feature['no_of_homeloan_accounts_good'] = item['data']['consumerfullcredit']['accountrating'][
                        'noofhomeloanaccountsgood']
                    feature['no_of_jointloan_accounts_bad'] = item['data']['consumerfullcredit']['accountrating'][
                        'noofjointloanaccountsbad']
                    feature['no_of_studyloan_accounts_bad'] = item['data']['consumerfullcredit']['accountrating'][
                        'noofstudyloanaccountsbad']
                    feature['no_of_creditcard_accounts_bad'] = item['data']['consumerfullcredit']['accountrating'][
                        'noofcreditcardaccountsbad']
                    feature['no_of_jointloan_accounts_good'] = item['data']['consumerfullcredit']['accountrating'][
                        'noofjointloanaccountsgood']
                    feature['no_of_studyloan_accounts_good'] = item['data']['consumerfullcredit']['accountrating'][
                        'noofstudyloanaccountsgood']
                    feature['no_of_creditcard_accounts_good'] = item['data']['consumerfullcredit']['accountrating'][
                        'noofcreditcardaccountsgood']
                    feature['no_of_personalloan_accounts_bad'] = item['data']['consumerfullcredit']['accountrating'][
                        'noofpersonalloanaccountsbad']
                    feature['no_of_personalloan_accounts_good'] = item['data']['consumerfullcredit']['accountrating'][
                        'noofpersonalloanaccountsgood']

                    feature['enquiry_matching_rate'] = item['data']['consumerfullcredit']['enquirydetails'][
                        'matchingrate']
                    feature['no_of_guarantor_accounts'] = item['data']['consumerfullcredit']['guarantorcount'][
                        'accounts']
                    feature['no_of_guarantors_secured'] = item['data']['consumerfullcredit']['guarantorcount'][
                        'guarantorssecured']
                    feature['guarantor_date_of_birth'] = item['data']['consumerfullcredit']['guarantordetails'][
                        'guarantordateofbirth']

                    feature['employment_type'] = item['data']['consumerfullcredit']['employmenthistory'][4][
                        'occupation']
                    feature['no_of_past_enquiries'] = len(item['data']['consumerfullcredit']['enquiryhistorytop'])

                    feature['rating'] = item['data']['consumerfullcredit']['creditaccountsummary'][
                        'rating']
                    feature['amount_arrear'] = item['data']['consumerfullcredit']['creditaccountsummary'][
                        'amountarrear']
                    feature['amount_arrear_extra'] = item['data']['consumerfullcredit']['creditaccountsummary'][
                        'amountarrear1']
                    feature['total_accounts'] = item['data']['consumerfullcredit']['creditaccountsummary'][
                        'totalaccounts']
                    feature['total_accounts_extra'] = item['data']['consumerfullcredit']['creditaccountsummary'][
                        'totalaccounts1']
                    feature['total_account_arrear'] = item['data']['consumerfullcredit']['creditaccountsummary'][
                        'totalaccountarrear']
                    feature['total_account_arrear_extra'] = item['data']['consumerfullcredit']['creditaccountsummary'][
                        'totalaccountarrear1']
                    feature['total_judgement_amount'] = item['data']['consumerfullcredit']['creditaccountsummary'][
                        'totaljudgementamount']
                    feature['total_judgement_amount_extra'] = \
                        item['data']['consumerfullcredit']['creditaccountsummary'][
                            'totaljudgementamount1']
                    feature['total_outstanding_debt'] = item['data']['consumerfullcredit']['creditaccountsummary'][
                        'totaloutstandingdebt']
                    feature['total_outstanding_debt_extra'] = \
                        item['data']['consumerfullcredit']['creditaccountsummary'][
                            'totaloutstandingdebt1']
                    feature['total_dishonoured_amount'] = item['data']['consumerfullcredit']['creditaccountsummary'][
                        'totaldishonouredamount']
                    feature['total_dishonoured_amount_extra'] = \
                        item['data']['consumerfullcredit']['creditaccountsummary'][
                            'totaldishonouredamount1']
                    feature['total_monthly_instalment'] = item['data']['consumerfullcredit']['creditaccountsummary'][
                        'totalmonthlyinstalment']
                    feature['total_monthly_instalment_extra'] = \
                        item['data']['consumerfullcredit']['creditaccountsummary'][
                            'totalmonthlyinstalment1']
                    feature['total_number_of_judgement'] = item['data']['consumerfullcredit']['creditaccountsummary'][
                        'totalnumberofjudgement']
                    feature['total_number_of_judgement_extra'] = \
                        item['data']['consumerfullcredit']['creditaccountsummary'][
                            'totalnumberofjudgement1']
                    feature['total_number_of_dishonoured'] = item['data']['consumerfullcredit']['creditaccountsummary'][
                        'totalnumberofdishonoured']
                    feature['total_number_of_dishonoured_extra'] = \
                        item['data']['consumerfullcredit']['creditaccountsummary'][
                            'totalnumberofdishonoured1']
                    feature['total_account_in_good_condition'] = \
                        item['data']['consumerfullcredit']['creditaccountsummary'][
                            'totalaccountingodcondition']
                    feature['total_account_in_good_condition_extra'] = \
                        item['data']['consumerfullcredit']['creditaccountsummary'][
                            'totalaccountingodcondition1']

                    feature['account_bank_name'] = item['data']['consumerfullcredit']['deliquencyinformation'][
                        'subscribername']
                    feature['account_age_date'] = item['data']['consumerfullcredit']['deliquencyinformation'][
                        'periodnum']

                    feature['identification_provision'] = 1 if 'identificationhistory' in item['data'][
                        'consumerfullcredit'] else 0

                    amount_overdue = 0
                    for credit_agreements in item['data']['consumerfullcredit']['creditagreementsummary']:
                        if 'amountoverdue' in credit_agreements:
                            amount_overdue += Decimal(sub(r'[^\d.]', '', credit_agreements['amountoverdue']))
                    feature['total_credit_amount_overdue'] = amount_overdue

                    feature['gender'] = item['data']['consumerfullcredit']['personaldetailssummary']['gender']
                    feature['birthdate'] = item['data']['consumerfullcredit']['personaldetailssummary'][
                        'birthdate']
                    feature['dependants'] = item['data']['consumerfullcredit']['personaldetailssummary'][
                        'dependants']
                    feature['nationality'] = item['data']['consumerfullcredit']['personaldetailssummary']['nationality']
                    feature['property_owned_type'] = item['data']['consumerfullcredit']['personaldetailssummary'][
                        'propertyownedtype']

                    # Add the transformed feature to the list
                    self.extracted_features.append(feature)

                self.save_to_csv()
                return self.extracted_features

        except BaseException as error:
            logging.error(error)

    def save_to_csv(self):
        """
            Class function to write extracted features to csv
            :return: str (Extracted features saved)
        """
        try:
            csv_columns = list(self.extracted_features[0].keys())
            with open(self.csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in self.extracted_features:
                    writer.writerow(data)
            print(f"Extracted features saved to {self.csv_file}")

        except IOError as error:
            logging.error(error)


path = 'credit_bureau_sample_data.json'
feature_extraction = FeatureExtraction(path)
features = feature_extraction.extract_features_from_json()
print(features)
