class BaseHandler:
    def __init__(self, callback):
        self.callback = callback
    
    def check_update(self, update):
        raise NotImplementedError
    
    def handle_update(self, update):
        if self.check_update(update):
            return self.callback(update.message if update.message else update)
        return False

class MessageHandler(BaseHandler):
    def __init__(self, callback, content_types=None, func=None):
        super().__init__(callback)
        self.content_types = content_types or ['text']
        self.func = func
    
    def check_update(self, update):
        if not update.message:
            return False
            
        if update.message.content_type not in self.content_types:
            return False
            
        if self.func and not self.func(update.message):
            return False
            
        return True

class CommandHandler(BaseHandler):
    def __init__(self, command, callback):
        super().__init__(callback)
        self.command = command if isinstance(command, list) else [command]
    
    def check_update(self, update):
        if not update.message or not update.message.text:
            return False
            
        text = update.message.text
        if not text.startswith('/'):
            return False
            
        command = text.split()[0][1:]
        return command in self.command

class CallbackQueryHandler(BaseHandler):
    def __init__(self, callback, pattern=None):
        super().__init__(callback)
        self.pattern = pattern
    
    def check_update(self, update):
        if not update.callback_query:
            return False
            
        if self.pattern:
            return self.pattern in update.callback_query.data
            
        return True
    
    def handle_update(self, update):
        if self.check_update(update):
            return self.callback(update.callback_query)
        return False