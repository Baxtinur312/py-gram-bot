class User:
    def __init__(self, data):
        self.id = data.get('id')
        self.is_bot = data.get('is_bot', False)
        self.first_name = data.get('first_name', '')
        self.last_name = data.get('last_name', '')
        self.username = data.get('username', '')
        self.language_code = data.get('language_code', '')
    
    def __str__(self):
        return f"User(id={self.id}, first_name='{self.first_name}')"

class Chat:
    def __init__(self, data):
        self.id = data.get('id')
        self.type = data.get('type', 'private')
        self.title = data.get('title', '')
        self.username = data.get('username', '')
        self.first_name = data.get('first_name', '')
        self.last_name = data.get('last_name', '')
    
    def __str__(self):
        return f"Chat(id={self.id}, type='{self.type}')"

class Message:
    def __init__(self, data):
        self.message_id = data.get('message_id')
        self.from_user = User(data.get('from', {})) if data.get('from') else None
        self.date = data.get('date')
        self.chat = Chat(data.get('chat', {}))
        self.text = data.get('text', '')
        self.caption = data.get('caption', '')
        
        self.photo = data.get('photo', [])
        self.video = data.get('video')
        self.audio = data.get('audio')
        self.document = data.get('document')
        self.voice = data.get('voice')
        
        self.new_chat_members = [User(u) for u in data.get('new_chat_members', [])]
        self.left_chat_member = User(data.get('left_chat_member', {})) if data.get('left_chat_member') else None
        
        self.reply_to_message = Message(data.get('reply_to_message')) if data.get('reply_to_message') else None
    
    @property
    def content_type(self):
        if self.text:
            return 'text'
        elif self.photo:
            return 'photo'
        elif self.video:
            return 'video'
        elif self.audio:
            return 'audio'
        elif self.document:
            return 'document'
        elif self.voice:
            return 'voice'
        elif self.new_chat_members:
            return 'new_chat_members'
        elif self.left_chat_member:
            return 'left_chat_member'
        else:
            return 'unknown'
    
    def __str__(self):
        return f"Message(id={self.message_id}, from={self.from_user}, text='{self.text[:50]}...')"

class CallbackQuery:
    def __init__(self, data):
        self.id = data.get('id')
        self.from_user = User(data.get('from', {}))
        self.message = Message(data.get('message', {})) if data.get('message') else None
        self.data = data.get('data', '')
    
    def __str__(self):
        return f"CallbackQuery(id={self.id}, data='{self.data}')"

class MyChatMember:
    def __init__(self, data):
        self.chat = Chat(data.get('chat', {}))
        self.from_user = User(data.get('from', {}))
        self.date = data.get('date')
        self.old_chat_member = data.get('old_chat_member', {})
        self.new_chat_member = data.get('new_chat_member', {})
    
    def __str__(self):
        return f"MyChatMember(chat={self.chat.id}, user={self.from_user.id})"

class Update:
    def __init__(self, data):
        self.update_id = data.get('update_id')
        self.message = Message(data.get('message')) if data.get('message') else None
        self.callback_query = CallbackQuery(data.get('callback_query')) if data.get('callback_query') else None
        self.my_chat_member = MyChatMember(data.get('my_chat_member')) if data.get('my_chat_member') else None
        
        self._raw_data = data
    
    def __str__(self):
        return f"Update(id={self.update_id})"