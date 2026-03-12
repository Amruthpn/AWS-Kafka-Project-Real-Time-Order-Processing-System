from flask import Flask, render_template_string
from kafka import KafkaConsumer
import json
import threading

app = Flask(__name__)

messages = []

def consume():
    consumer = KafkaConsumer(
        'solace-kafka',
        bootstrap_servers='54.201.215.233:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    for msg in consumer:
        messages.append(msg.value)
        if len(messages) > 20:
            messages.pop(0)

thread = threading.Thread(target=consume)
thread.daemon = True
thread.start()

HTML = """
<h2>Live Kafka Orders</h2>
<meta http-equiv="refresh" content="2">
<table border="1">
<tr><th>Order ID</th><th>Symbol</th><th>Price</th></tr>
{% for m in messages %}
<tr>
<td>{{m['order_id']}}</td>
<td>{{m['symbol']}}</td>
<td>{{m['price']}}</td>
</tr>
{% endfor %}
</table>
"""

@app.route("/")
def index():
    return render_template_string(HTML, messages=messages)

app.run(host="0.0.0.0", port=5000)
