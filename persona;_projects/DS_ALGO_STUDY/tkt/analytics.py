from railpyanalytics.api import RailAnalytics
from pyb.tracer import trace, INFO
import json


class AnalyticsHelper:
    def __init__(self) -> None:
        self._analytics_lib_instance = None
        self._default_body = ''

    def setup_instance(self):
        try:
            self._analytics_lib_instance = RailAnalytics.get_instance("rdp", "ticketing", "TKT")

        except Exception as e:
            trace(INFO, "Issue in creating singleton instance of RailAnalytics::{}".format(e))

    def send_incoming_rq(self, request):
        """


        """
        self.setup_instance()
        raw_message = {}
        if self._analytics_lib_instance:
            try:
                wsgi_object = request.environ['WSGI_SERVICE_OBJECT']
                otf_resources = wsgi_object.getResources()
                raw_message["message_name"] = wsgi_object._environ.get('REQUEST_METHOD', '') + ' ' + \
                                              wsgi_object._environ.get('PATH_INFO', '')
                raw_message["message_service_name"] = wsgi_object._environ.get('REQUEST_METHOD', '') + ' ' + \
                                                      wsgi_object._environ.get('PATH_INFO', '')
                raw_message["message_version"] = -1
                raw_message["query_string"] = wsgi_object._environ.get('QUERY_STRING', '')
                decoded_message_body = wsgi_object._environ['wsgi.input'].getvalue()
                if isinstance(decoded_message_body, bytes):
                    byte_str = decoded_message_body
                    # Convert to a "unicode" object
                    decoded_message_body = byte_str.decode('UTF-8')
                if decoded_message_body:
                    raw_message["message_body"] = decoded_message_body
                else:
                    raw_message["message_body"] = ''
                self._analytics_lib_instance.send_request(raw_message, otf_resources)
            except Exception as e:
                trace(INFO, "Error in parsing and sending the incoming request :: {}".format(e))

    def send_incoming_rs(self, response, otf_resources):
        self.setup_instance()
        raw_message = {}
        if self._analytics_lib_instance:
            try:
                raw_message['status'] = str(response.status_code)
                raw_message['message_body'] = response.data.decode('utf-8')
                raw_message["message_name"] = ""
                raw_message["message_service_name"] = ""
                raw_message["query_string"] = ""
                raw_message["message_version"] = ""
                self._analytics_lib_instance.send_response(raw_message, otf_resources)
            except Exception as e:
                trace(INFO, "Error in parsing and sending the incoming request :: {}".format(e))

    def send_outgoing_rq(self, otf_resources, req_body=None, msg_name=None, msg_service_name=None,
                         msg_version=None):
        trace(INFO, 'send_outgoing_rq::enter')
        self.setup_gkr()
        raw_message = dict()
        if self.gkr:
            try:
                raw_message['message_body'] = req_body if req_body else self._default_req_body
                raw_message['message_name'] = msg_name
                raw_message['message_service_name'] = msg_service_name
                raw_message['message_version'] = msg_version
                self._analytics_lib_instance.send_request(raw_message, otf_resources)
            except Exception as e:
                trace(INFO, 'Error in send_outgoing_rq ::error:{}'.format(e))
        trace(INFO, 'send_outgoing_rq::exit')

    def send_outgoing_rs(self, response=None, msg_name=None, msg_service_name=None, msg_version=None, sender_type=None):
        """
        :param response:
        :param sender_type: sender type class name: supported values (EdifactSender, XmlSender)
        :return:
        """
        trace(INFO, 'send_outgoing_rs::enter')
        if self.gkr:
            raw_message = {}
            try:
                if response:
                    if sender_type is 'EdifactSender':
                        raw_message["message_body"] = json.dumps(response)

                    elif sender_type is 'XmlSender':
                        raw_message["message_body"] = response.encode('utf-8')
                    elif isinstance(response, dict):
                        raw_message["message_body"] = json.dumps(response)
                else:
                    raw_message["message_body"] = 'None'
                    raw_message['status'] = '200'
                raw_message['message_name'] = msg_name
                raw_message['message_service_name'] = msg_service_name
                raw_message['message_version'] = msg_version

            except Exception as e:
                trace(INFO, 'Error while sending outgoing request ::error:{}'.format(e))
        trace(INFO, 'send_outgoing_rs::exit')






