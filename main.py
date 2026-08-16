from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
import random
import os

class SmurfikApp(App):
    def build(self):
        # ფრაზების ჩატვირთვა
        self.phrases = self.load_phrases()
        
        # მთავარი განლაგება
        layout = BoxLayout(
            orientation='vertical',
            padding=30,
            spacing=20
        )
        
        # სურათი
        try:
            self.img = Image(
                source='smurfik.png',
                size_hint=(1, 0.45),
                keep_ratio=True
            )
            layout.add_widget(self.img)
        except:
            pass
        
        # საწყისი ტექსტი
        self.greeting_label = Label(
            text='დღე დაიწყო პოზიტივით! ✨',
            font_size='22sp',
            color=(0, 0.47, 1, 1),
            halign='center',
            valign='middle',
            size_hint=(1, 0.1)
        )
        self.greeting_label.bind(size=self.greeting_label.setter('text_size'))
        layout.add_widget(self.greeting_label)
        
        # ციტატის ველი
        self.quote_label = Label(
            text='',
            font_size='18sp',
            color=(0.13, 0.13, 0.13, 1),
            halign='center',
            valign='middle',
            size_hint=(1, 0.2),
            text_size=(None, None)
        )
        self.quote_label.bind(size=self.quote_label.setter('text_size'))
        layout.add_widget(self.quote_label)
        
        # ღილაკი "დააჭირე აქ"
        self.action_button = Button(
            text='დააჭირე აქ 👇',
            font_size='20sp',
            background_normal='',
            background_color=(0, 0.47, 1, 1),
            color=(1, 1, 1, 1),
            size_hint=(1, 0.12),
            opacity=0
        )
        self.action_button.bind(on_press=self.on_button_click)
        layout.add_widget(self.action_button)
        
        # დახურვის ღილაკი
        self.close_button = Button(
            text='წავედი, აბა ჰე! 👋',
            font_size='16sp',
            background_normal='',
            background_color=(0.88, 0.88, 0.88, 1),
            color=(0, 0, 0, 1),
            size_hint=(1, 0.1),
            opacity=0
        )
        self.close_button.bind(on_press=self.close_app)
        layout.add_widget(self.close_button)
        
        # 3 წამის შემდეგ ღილაკის ჩვენება
        Clock.schedule_once(self.show_button, 3)
        
        return layout
    
    def load_phrases(self):
        try:
            if os.path.exists('phrases.txt'):
                with open('phrases.txt', 'r', encoding='utf-8') as f:
                    phrases = [line.strip() for line in f if line.strip()]
                if phrases:
                    return phrases
        except:
            pass
        return ["მთავარია ავდგეთ, გაღვიძებას სამსახურშიც მოვასწრებთ 😎"]
    
    def show_button(self, dt):
        self.greeting_label.opacity = 0
        self.action_button.opacity = 1
    
    def on_button_click(self, instance):
        phrase = random.choice(self.phrases)
        self.quote_label.text = f'„{phrase}“'
        self.action_button.opacity = 0
        self.close_button.opacity = 1
    
    def close_app(self, instance):
        App.get_running_app().stop()

if __name__ == '__main__':
    SmurfikApp().run()