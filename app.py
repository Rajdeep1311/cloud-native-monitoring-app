import psutil
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    message = None
    if cpu_percent >= 80 or mem_percent >= 80:
        message = "High CPU or Memory Utilization. Please reduce load or scale your resources"
    return render_template("index.html", cpu_metric=cpu_percent, mem_metric=mem_percent, message=message)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
