from website import forwardmetrics
from waitress import serve


if __name__ == "__main__":
    serve(forwardmetrics(), host="0.0.0.0", port=5000)
    