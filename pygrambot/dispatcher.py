class Dispatcher:
    def __init__(self, bot):
        self.bot = bot
        self.handlers = []
        self.error_handlers = []
    
    def add_handler(self, handler):
        self.handlers.append(handler)
    
    def add_error_handler(self, callback):
        self.error_handlers.append(callback)
    
    def process_update(self, update):
        try:
            for handler in self.handlers:
                if handler.handle_update(update):
                    break
                
        except Exception as e:
            for error_handler in self.error_handlers:
                try:
                    error_handler(update, e)
                except Exception as error_e:
                    print(f"Error handler xatosi: {error_e}")