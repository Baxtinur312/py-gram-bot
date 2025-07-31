import time
import threading
from .bot import Bot
from .dispatcher import Dispatcher
from .types import Update

class Updater:
    def __init__(self, token):
        self.bot = Bot(token)
        self.dispatcher = Dispatcher(self.bot)
        self.running = False
        self.last_update_id = 0
        self._thread = None
    
    def start_polling(self, timeout=10, clean=False):
        try:
            bot_info = self.bot.get_me()
            if bot_info.get('ok'):
                user = bot_info['result']
                print(f"Bot ulandi: {user['first_name']} (@{user.get('username', 'N/A')})")
            else:
                print("Bot tokenini tekshiring!")
                return
        except Exception as e:
            print(f"Bot ulanishida xatolik: {e}")
            return
        
        self.running = True
        
        if clean:
            self._clean_updates()
        
        self._thread = threading.Thread(target=self._polling_loop, args=(timeout,))
        self._thread.daemon = True
        self._thread.start()
        
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nBot to'xtatilmoqda...")
            self.stop()
    
    def stop(self):
        self.running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=5)
        print("Bot to'xtatildi")
    
    def _polling_loop(self, timeout):
        while self.running:
            try:
                response = self.bot.get_updates(
                    offset=self.last_update_id + 1,
                    timeout=timeout
                )
                
                if response.get('ok'):
                    updates = response.get('result', [])
                    
                    for update_data in updates:
                        update = Update(update_data)
                        self.last_update_id = update.update_id
                        
                        self.dispatcher.process_update(update)
                
                else:
                    print(f"Update olishda xatolik: {response}")
                
            except Exception as e:
                print(f"Polling xatosi: {e}")
                time.sleep(5)
    
    def _clean_updates(self):
        try:
            response = self.bot.get_updates(offset=-1)
            if response.get('ok') and response.get('result'):
                last_update = response['result'][-1]
                self.last_update_id = last_update['update_id']
        except Exception as e:
            print(f"Update lar tozalashda xatolik: {e}")