from flask import Flask, Response
import psutil
from prometheus_client import Gauge, generate_latest

app = Flask(__name__)

# Prometheus metrics
cpu_usage = Gauge('system_cpu_usage_percent', 'CPU usage in percent')
memory_usage = Gauge('system_memory_usage_percent', 'Memory usage in percent')
disk_usage = Gauge('system_disk_usage_percent', 'Disk usage in percent')

@app.route('/metrics')
def metrics():
    cpu_usage.set(psutil.cpu_percent(interval=1))
    memory_usage.set(psutil.virtual_memory().percent)
    disk_usage.set(psutil.disk_usage('/').percent)

    return Response(generate_latest(), mimetype='text/plain')

@app.route('/')
def home():
    return "Monitoring Exporter Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)