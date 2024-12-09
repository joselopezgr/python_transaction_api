from app import create_app, configure_logging

app = create_app()
configure_logging()

if __name__ == "__main__":
    app.run(debug=True)
