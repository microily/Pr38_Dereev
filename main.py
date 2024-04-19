import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
import random

kivy.require('2.0.0')

class OSQuizApp(App):
    def __init__(self):
        super(OSQuizApp, self).__init__()
        self.current_question = 0
        self.score = 0
        self.questions = [
            {"question": "Какая операционная система разработана компанией Microsoft?", "options": ["Windows", "Linux", "macOS", "Android"], "correct": "Windows", "image": "windows_logo.png"},
            {"question": "Кто является создателем операционной системы macOS?", "options": ["Apple", "Microsoft", "Google", "IBM"], "correct": "Apple", "image": "macos_logo.png"},
            {"question": "Какая операционная система является основой для Android?", "options": ["Linux", "Windows", "iOS", "macOS"], "correct": "Linux", "image": "android_logo.png"},
            {"question": "Какая операционная система использует ядро под названием 'Darwin'?", "options": ["macOS", "Windows", "Linux", "Android"], "correct": "macOS", "image": "macos_logo.png"},
            {"question": "Какая операционная система использует графический интерфейс под названием 'Unity'?", "options": ["Ubuntu", "macOS", "Windows", "Android"], "correct": "Ubuntu", "image": "ubuntu_logo.png"},
            {"question": "Какая операционная система является самой распространенной среди десктопных ПК?", "options": ["Windows", "Linux", "macOS", "Chrome OS"], "correct": "Windows", "image": "windows_logo.png"},
            {"question": "Какая операционная система предназначена для использования на устройствах компании Apple?", "options": ["macOS", "Windows", "Linux", "Android"], "correct": "macOS", "image": "macos_logo.png"},
            {"question": "Какая операционная система является открытым программным обеспечением?", "options": ["Windows", "macOS", "Linux", "iOS"], "correct": "Linux", "image": "linux_logo.png"},
            {"question": "Какая операционная система использует ядро под названием 'XNU'?", "options": ["macOS", "Windows", "Linux", "Android"], "correct": "macOS", "image": "macos_logo.png"},
            {"question": "Какая операционная система разработана компанией Canonical?", "options": ["macOS", "Windows", "Linux", "Android"], "correct": "Linux", "image": "linux_logo.png"}
        ]

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.question_image = AsyncImage(source=self.questions[self.current_question]["image"], size_hint=(1, 0.3))
        self.layout.add_widget(self.question_image)

        self.question_label = Label(text=self.questions[self.current_question]["question"], size_hint=(1, 0.2))
        self.layout.add_widget(self.question_label)

        for option in self.questions[self.current_question]["options"]:
            button = Button(text=option, size_hint=(1, 0.1))
            button.bind(on_press=self.check_answer)
            self.layout.add_widget(button)

        return self.layout

    def check_answer(self, instance):
        if instance.text == self.questions[self.current_question]["correct"]:
            self.score += 1
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.question_image.source = self.questions[self.current_question]["image"]
            self.question_label.text = self.questions[self.current_question]["question"]
            for child in self.layout.children:
                if isinstance(child, Button):
                    child.text = self.questions[self.current_question]["options"][self.layout.children.index(child)]
        else:
            self.show_result()

    def show_result(self):
        self.layout.clear_widgets()
        result_label = Label(text=f"Тест завершен! Ваш результат: {self.score} из {len(self.questions)}", size_hint=(1, 0.5))
        self.layout.add_widget(result_label)

if __name__ == '__main__':
    OSQuizApp().run()
