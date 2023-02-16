class Name:
    def __init__(self, display):
        if display:
            self.display = display
            self.on_update("BME 680 Display")

    def on_update(self, text):
        self.display.text(text, 0)

