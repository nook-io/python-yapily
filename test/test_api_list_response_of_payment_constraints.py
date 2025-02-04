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

from yapily.models.api_list_response_of_payment_constraints import (
    ApiListResponseOfPaymentConstraints,
)  # noqa: E501


class TestApiListResponseOfPaymentConstraints(unittest.TestCase):
    """ApiListResponseOfPaymentConstraints unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiListResponseOfPaymentConstraints:
        """Test ApiListResponseOfPaymentConstraints
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ApiListResponseOfPaymentConstraints`
        """
        model = ApiListResponseOfPaymentConstraints()  # noqa: E501
        if include_optional:
            return ApiListResponseOfPaymentConstraints(
                meta = yapily.models.response_list_meta.ResponseListMeta(
                    tracing_id = '', 
                    count = 56, 
                    pagination = yapily.models.pagination.Pagination(
                        total_count = 56, 
                        self = yapily.models.filter_and_sort.FilterAndSort(
                            from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            limit = 56, 
                            sort = 'date', 
                            offset = 56, 
                            cursor = '', ), 
                        next = yapily.models.next.Next(
                            from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            before = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            limit = 56, 
                            cursor = '', ), ), ),
                data = [
                    yapily.models.payment_constraints_response.PaymentConstraintsResponse(
                        institution_id = 'modelo-sandbox', 
                        institution_country_code = 'GB', 
                        endpoint_path = '', 
                        endpoint_method = '', 
                        payment_type = 'DOMESTIC_PAYMENT', 
                        request = yapily.models.request_constraints.RequestConstraints(
                            headers = yapily.models.schema.Schema(
                                title = '', 
                                maximum = 1.337, 
                                exclusive_maximum = 1.337, 
                                minimum = 1.337, 
                                exclusive_minimum = 1.337, 
                                pattern = '', 
                                max_items = 0, 
                                min_items = 0, 
                                unique_items = True, 
                                required = [
                                    ''
                                    ], 
                                enum = [
                                    null
                                    ], 
                                type = 'array', 
                                contains = yapily.models.schema.Schema(
                                    title = '', 
                                    maximum = 1.337, 
                                    exclusive_maximum = 1.337, 
                                    minimum = 1.337, 
                                    exclusive_minimum = 1.337, 
                                    pattern = '', 
                                    max_items = 0, 
                                    min_items = 0, 
                                    unique_items = True, 
                                    not = , 
                                    if = , 
                                    then = , 
                                    else = , 
                                    all_of = [
                                        
                                        ], 
                                    one_of = [
                                        
                                        ], 
                                    any_of = [
                                        
                                        ], 
                                    items = , 
                                    properties = {
                                        'key' : 
                                        }, 
                                    description = '', 
                                    format = '', 
                                    default = null, 
                                    example = null, 
                                    dependent_required = {
                                        'key' : [
                                            ''
                                            ]
                                        }, 
                                    __defs = {
                                        'key' : 
                                        }, 
                                    __ref = '', 
                                    x_yapily_annotations = yapily.models.schema_x_yapily_annotations.Schema_x_yapily_annotations(
                                        last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                    x_yapily_validations = yapily.models.schema_x_yapily_validations.Schema_x_yapily_validations(
                                        max_duration_from_now = '', ), ), 
                                not = , 
                                if = , 
                                then = , 
                                else = , 
                                all_of = [
                                    
                                    ], 
                                one_of = [
                                    
                                    ], 
                                any_of = [
                                    
                                    ], 
                                items = , 
                                properties = {
                                    'key' : 
                                    }, 
                                description = '', 
                                format = '', 
                                default = null, 
                                example = null, 
                                dependent_required = {
                                    'key' : [
                                        ''
                                        ]
                                    }, 
                                __defs = {
                                    'key' : 
                                    }, 
                                __ref = '', 
                                x_yapily_annotations = yapily.models.schema_x_yapily_annotations.Schema_x_yapily_annotations(
                                    last_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                                x_yapily_validations = yapily.models.schema_x_yapily_validations.Schema_x_yapily_validations(
                                    max_duration_from_now = '', ), ), 
                            body = , ), )
                    ]
            )
        else:
            return ApiListResponseOfPaymentConstraints(
        )
        """

    def testApiListResponseOfPaymentConstraints(self):
        """Test ApiListResponseOfPaymentConstraints"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
