from website import forwardmetrics


if __name__ == "__main__":
    from waitress import serve
    serve(forwardmetrics(), host="0.0.0.0", port=5000)
    