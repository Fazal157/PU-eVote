if __name__ == "__main__":
    import threading, webbrowser, time, socket

    def open_browser():
        while True:
            try:
                # Try to connect to server port
                with socket.create_connection(("127.0.0.1", 8000), timeout=2):
                    break
            except OSError:
                time.sleep(1)
        webbrowser.open("http://127.0.0.1:8000/")

    threading.Thread(target=open_browser).start()
    main()
