from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import logging
import traceback
import datetime


class PromDb:
    logger = logging.getLogger('root')


    def get_registry(self):
        return CollectorRegistry()

    def push_2_gateway(self, registry):
        push_to_gateway('prometheus_server_hostname__or_ip:9091', job='Pushgateway', registry=registry, timeout=120)

    def push_data(self, registry, metrics):
        epoch_time = round(datetime.datetime.now().timestamp())
        if metrics is not None:
            
            for metric in metrics:
                metric_id = metric['id']
                try:
                    metric_gauge = Gauge(metric_id, "metrics", registry=registry)
                    metric_gauge.set(1)
                    metric['status'] = 'Completed'
                    metric['last_updated_date'] = epoch_time
                except:
                    self.logger.error("error occured for metric %s", metric_id)
                    traceback.print_exc()


