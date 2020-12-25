from app.flask_web import app
import os
import logging
from prometheus_flask_exporter import PrometheusMetrics

if __name__ == "__main__":
    debug_flag = False
    try:
        devserver = os.environ["devserver"]
        debug_flag = True
        logging.basicConfig(level=logging.DEBUG,
                            format='%(levelname)s:\t%(message)s')
    except KeyError:
        pass

    metrics = PrometheusMetrics(app)
    app.run(debug=debug_flag, host="0.0.0.0", port="8000")
