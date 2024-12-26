import datetime
import json

from pyb.toolbox import PropertiesManager
from pyb.tracer import trace, INFO
from pykafka.genericKafkaReport import GenericKafkaReport
from helpers.design.Singleton import Singleton


@Singleton
class GKRHelper(Singleton):

    def __init__(self):
        self.gkr = None
        self._default_req_body = ''

    @property
    def default_req_body(self):
        return self._default_req_body

    @default_req_body.setter
    def default_req_body(self, body):
        """
        :param body: can be str or dict
        :return:
        """

        def _datetime_converter(data):
            if isinstance(data, datetime.datetime):
                return str(data)

        if isinstance(body, dict):
            try:
                body = json.dumps(body, default=_datetime_converter)
            except Exception as e:
                trace(INFO, 'Error in parsing dict to json str::error::{}'.format(e))
        self._default_req_body = body

    def setup_gkr(self):
        trace_event = PropertiesManager.getProperty('TKT_KAFKA_TRACE_EVENT', 'N') == 'Y'
        if trace_event:
            try:
                if self.gkr is None:
                    self.gkr = GenericKafkaReport()
                # set cluster, topic and broker in GenericKafkaClient
                broker = PropertiesManager.getProperty('TKT_KAFKA_BROKER', None)
                topic = PropertiesManager.getProperty('TKT_KAFKA_TOPIC', None)
                cluster = PropertiesManager.getProperty('TKT_KAFKA_CLUSTER', None)
                self.gkr.setup(broker, topic, cluster)
            except Exception as e:
                trace(INFO, 'Error while setting up gkr::error:{}'.format(e))
        else:
            self.gkr = None
            trace(INFO, 'kafka event has been disabled::trace_kafka_event: {}'.format(trace_event))

    def trace_incoming_rq(self, request):
        """
        trace incoming request and send event to kafka for TicketingServer
        initialize resources (raw_message, otf_resources) for GenericKafkaClient
        set incoming request in gkr
        """
        trace(INFO, 'trace_incoming_rq::enter')
        wsgi_object = request.environ['WSGI_SERVICE_OBJECT']
        otf_resources = wsgi_object.getResources()
        trace(INFO, f"trace_incoming_rq wsgi_objects::  {wsgi_object}")
        trace(INFO, f"trace_incoming_rq otf resource::  {otf_resources}")
        raw_message = {}
        raw_message["message_name"] = wsgi_object._environ.get('REQUEST_METHOD', '') + ' ' + \
                                      wsgi_object._environ.get('PATH_INFO', '')
        raw_message["message_service_name"] = wsgi_object._environ.get('REQUEST_METHOD', '') + ' ' + \
                                              wsgi_object._environ.get('PATH_INFO', '')
        raw_message["message_version"] = -1
        raw_message["query_string"] = wsgi_object._environ.get('QUERY_STRING', '')
        raw_message["message_body"] = wsgi_object._environ['wsgi.input'].getvalue()
        trace(INFO, f"trace_incoming_rq raw_dict::  {raw_message}")

        self.setup_gkr()
        if self.gkr:
            try:
                wsgi_object = request.environ['WSGI_SERVICE_OBJECT']
                otf_resources = wsgi_object.getResources()
                trace(INFO, f"trace_incoming_rq wsgi_objects::  {wsgi_object}")
                trace(INFO, f"trace_incoming_rq otf resource::  {otf_resources}")
                self.gkr.init_resources(wsgi_object, otf_resources)
                self.gkr.set_incoming_rq(wsgi_object, otf_resources)
            except Exception as e:
                trace(INFO, 'Error in trace_incoming_rq, error:{}'.format(e))
        else:
            trace(INFO, 'kafka event has been disabled::trace_kafka_event: N')
        trace(INFO, 'trace_incoming_rq::exit')

    def trace_incoming_rs(self, response):
        """
        set incoming response in gkr
        set attache handler and send event
        """
        trace(INFO, 'trace_incoming_rs::enter')
        trace(INFO, f"trace_incoming_rs response :: {response}")
        raw_message = {}
        raw_message['status'] = str(response.status_code)
        raw_message['message_body'] = response.data.decode('utf-8')
        raw_message["message_name"] = ""
        raw_message["message_service_name"] = ""
        raw_message["query_string"] = ""
        raw_message["message_version"] = ""
        trace(INFO, f"trace_incoming_rs raw_dict :: {raw_message}")
        if self.gkr:
            attach_handler = PropertiesManager.getProperty('TKT_KAFKA_ATTACH_HANDLER', 'N') == 'Y'
            res_dict = dict()
            try:
                trace(INFO, f"trace_incoming_rs response :: {response}")
                res_dict['status'] = str(response.status_code)
                res_dict['content'] = response.data.decode('utf-8')
                self.gkr.set_incoming_rs(res_dict, content_type='application/json')
                self.gkr.send(attach_handler)
            except Exception as e:
                trace(INFO, 'Error in trace_incoming_rs(), error:{}'.format(e))
        else:
            trace(INFO, 'kafka event has been disabled, trace_kafka_event: N')
        trace(INFO, 'trace_incoming_rs::exit')
        return response

    def trace_outgoing_rq(self, otf_resources, req_body=None, msg_name=None, msg_service_name=None,
                          msg_version=None, content_type=None):
        trace(INFO, 'trace_outgoing_rq::enter')
        trace(INFO, f"trace_outgoing_rq otf_resource :: {otf_resources}")
        trace(INFO, f"trace_outgoing_rq req_body :: {req_body}")
        trace(INFO, f"trace_outgoing_rq msg_name:: {msg_name}")
        trace(INFO, f"trace_outgoing_rq msg_service_name :: {msg_service_name}")
        trace(INFO, f"trace_outgoing_rq msg_version :: {msg_version}")
        trace(INFO, f"trace_outgoing_rq content_type :: {content_type}")
        self.setup_gkr()
        req_dict = dict()
        if self.gkr:
            try:
                trace(INFO, f"trace_outgoing_rq otf_resource :: {otf_resources}")
                trace(INFO, f"trace_outgoing_rq req_body :: {req_body}")
                trace(INFO, f"trace_outgoing_rq msg_name:: {msg_name}")
                trace(INFO, f"trace_outgoing_rq msg_service_name :: {msg_service_name}")
                trace(INFO, f"trace_outgoing_rq msg_version :: {msg_version}")
                trace(INFO, f"trace_outgoing_rq content_type :: {content_type}")
                req_dict['message_body'] = req_body if req_body else self._default_req_body
                req_dict['message_name'] = msg_name
                req_dict['message_service_name'] = msg_service_name
                req_dict['message_version'] = msg_version
                req_dict['content_type'] = content_type
                self.gkr.init_resources(req_dict, otf_resources)
                self.gkr.set_outgoing_rq(req_dict)
            except Exception as e:
                trace(INFO, 'Error in _trace_outgoing_rq while setting set_outgoing_rq::error:{}'.format(e))
        trace(INFO, 'trace_outgoing_rq::exit')

    def trace_outgoing_rs(self, response=None, sender_type=None):
        """
        :param response:
        :param sender_type: sender type class name: supported values (EdifactSender, XmlSender)
        :return:
        """
        trace(INFO, 'trace_outgoing_rs::enter')
        trace(INFO, f"trace_outgoing_rs resonse :: {json.dumps(response)}")
        attach_handler = PropertiesManager.getProperty('TKT_KAFKA_ATTACH_HANDLER', 'N') == 'Y'
        if self.gkr:
            res_dict = {}
            try:
                if response:
                    trace(INFO, f"trace_outgoing_rs resonse :: {response}")
                    if sender_type is 'EdifactSender':
                        res_dict['content'] = json.dumps(response)
                        self.gkr.set_outgoing_rs(res_dict)
                    elif sender_type is 'XmlSender':
                        self.gkr.set_outgoing_rs(response.encode('utf-8'))
                    elif isinstance(response, dict):
                        res_dict['content'] = json.dumps(response, default=self._jsonify_datetime)
                        self.gkr.set_outgoing_rs(res_dict)
                else:
                    res_dict['content'] = 'None'
                    res_dict['status'] = '200'
                    self.gkr.set_outgoing_rs(res_dict)
                self.gkr.send(attach_handler)
            except Exception as e:
                trace(INFO, 'Error while sending kafka event::error:{}'.format(e))
        trace(INFO, 'trace_outgoing_rs::exit')

    def _jsonify_datetime(self, object):
        if isinstance(object, datetime.datetime):
            return object.__str__()
