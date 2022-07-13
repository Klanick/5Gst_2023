# coding: utf-8

"""
    Balancer API

    Speedtest load balancer  # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: support@5gst.ru
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def service_acquire_create(self, **kwargs):  # noqa: E501
        """service_acquire_create  # noqa: E501

        Acquires service for further iperf tests  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_acquire_create(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ServerAddressResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_acquire_create_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.service_acquire_create_with_http_info(**kwargs)  # noqa: E501
            return data

    def service_acquire_create_with_http_info(self, **kwargs):  # noqa: E501
        """service_acquire_create  # noqa: E501

        Acquires service for further iperf tests  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_acquire_create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ServerAddressResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_acquire_create" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/service/acquire/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServerAddressResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_create(self, data, **kwargs):  # noqa: E501
        """service_create  # noqa: E501

        Register caller as service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_create(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ServerAddressRequest data: (required)
        :return: ServerAddressRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_create_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.service_create_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def service_create_with_http_info(self, data, **kwargs):  # noqa: E501
        """service_create  # noqa: E501

        Register caller as service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_create_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ServerAddressRequest data: (required)
        :return: ServerAddressRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if self.api_client.client_side_validation and ('data' not in params or
                                                       params['data'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data` when calling `service_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/service/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServerAddressRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def service_delete(self, data, **kwargs):  # noqa: E501
        """service_delete  # noqa: E501

        Unregister caller as service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_delete(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ServerAddressRequest data: (required)
        :return: ServerAddressRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_delete_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.service_delete_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def service_delete_with_http_info(self, data, **kwargs):  # noqa: E501
        """service_delete  # noqa: E501

        Unregister caller as service  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_delete_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ServerAddressRequest data: (required)
        :return: ServerAddressRequest
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if self.api_client.client_side_validation and ('data' not in params or
                                                       params['data'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data` when calling `service_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/service/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServerAddressRequest',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)