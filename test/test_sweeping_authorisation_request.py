# coding: utf-8

"""
    Yapily API

    The Yapily API enables connections between your application and users' banks. For more information check out our [documentation](https://docs.yapily.com/).<br><br>In particular, make sure to view our [Getting Started](https://docs.yapily.com/pages/home/getting-started/) steps if this is your first time here.<br><br>While testing the API, our list of [sandbox credentials](https://docs.yapily.com/pages/key-concepts/sandbox-credentials/) maybe useful.

    The version of the OpenAPI document: 4.2.0
    Contact: support@yapily.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from yapily.models.sweeping_authorisation_request import SweepingAuthorisationRequest  # noqa: E501

class TestSweepingAuthorisationRequest(unittest.TestCase):
    """SweepingAuthorisationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SweepingAuthorisationRequest:
        """Test SweepingAuthorisationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SweepingAuthorisationRequest`
        """
        model = SweepingAuthorisationRequest()  # noqa: E501
        if include_optional:
            return SweepingAuthorisationRequest(
                user_id = '',
                application_user_id = '',
                forward_parameters = [
                    ''
                    ],
                context_type = 'OTHER',
                institution_id = 'yapily-mock',
                callback = 'https://display-parameters.com',
                redirect = yapily.models.redirect_request.RedirectRequest(
                    url = '', ),
                one_time_token = False,
                control_parameters = yapily.models.sweeping_control_parameters.SweepingControlParameters(
                    psu_authentication_methods = [
                        ''
                        ], 
                    periodic_limits = [
                        yapily.models.sweeping_periodic_limits.SweepingPeriodicLimits(
                            total_max_amount = null, 
                            frequency = '', 
                            alignment = '', )
                        ], 
                    max_amount_per_payment = null, 
                    valid_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    valid_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                initiation_details = yapily.models.initiation_details.InitiationDetails(
                    reference = 'Own Account Sweeping', 
                    payer = yapily.models.payer_details.Payer Details(
                        name = 'John Doe', 
                        account_identifications = [
                            yapily.models.account_identifications.Account Identifications(
                                type = 'SORT_CODE', 
                                identification = '401016', )
                            ], 
                        address = {"country":"GB"}, ), 
                    payee = yapily.models.payee_details.Payee Details(
                        name = 'Jane Doe', 
                        account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}], 
                        account_type = '', 
                        merchant_id = '24589303', 
                        merchant_category_code = '5551', ), ),
                compliance_data = yapily.models.compliance_data.ComplianceData(
                    payer = yapily.models.compliance_data_payer.ComplianceDataPayer(
                        type = 'INDIVIDUAL', 
                        individual = yapily.models.compliance_data_individual.ComplianceDataIndividual(
                            name = 'John Doe', 
                            birth_date = 'Sat Aug 12 01:00:00 BST 2000', ), 
                        business = yapily.models.compliance_data_business.ComplianceDataBusiness(
                            name = 'Company LTD', 
                            registration_number = 'COM123NO', 
                            registered_address = yapily.models.compliance_data_address.ComplianceDataAddress(
                                address_line1 = '123 Queens Street', 
                                address_line2 = 'Unit 13', 
                                town_name = 'York', 
                                post_code = '12345', 
                                country = 'GB', ), 
                            trading_address = yapily.models.compliance_data_address.ComplianceDataAddress(
                                address_line1 = '123 Queens Street', 
                                address_line2 = 'Unit 13', 
                                town_name = 'York', 
                                post_code = '12345', 
                                country = 'GB', ), ), ), )
            )
        else:
            return SweepingAuthorisationRequest(
                institution_id = 'yapily-mock',
                control_parameters = yapily.models.sweeping_control_parameters.SweepingControlParameters(
                    psu_authentication_methods = [
                        ''
                        ], 
                    periodic_limits = [
                        yapily.models.sweeping_periodic_limits.SweepingPeriodicLimits(
                            total_max_amount = null, 
                            frequency = '', 
                            alignment = '', )
                        ], 
                    max_amount_per_payment = null, 
                    valid_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    valid_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                initiation_details = yapily.models.initiation_details.InitiationDetails(
                    reference = 'Own Account Sweeping', 
                    payer = yapily.models.payer_details.Payer Details(
                        name = 'John Doe', 
                        account_identifications = [
                            yapily.models.account_identifications.Account Identifications(
                                type = 'SORT_CODE', 
                                identification = '401016', )
                            ], 
                        address = {"country":"GB"}, ), 
                    payee = yapily.models.payee_details.Payee Details(
                        name = 'Jane Doe', 
                        account_identifications = [{"identification":"401016","type":"SORT_CODE"},{"identification":"71518920","type":"ACCOUNT_NUMBER"}], 
                        account_type = '', 
                        merchant_id = '24589303', 
                        merchant_category_code = '5551', ), ),
        )
        """

    def testSweepingAuthorisationRequest(self):
        """Test SweepingAuthorisationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
