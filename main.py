from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests
import urllib3

Builder.load_file('frontend.kv')

class FirstScreen(Screen):

    def get_image_link(self):
        #get user query from text input
        query = self.manager.current_screen.ids.user_query.text
        # get wikipedia page and first image urls
        page = wikipedia.page(query)
        image_link = page.images[0]
        return image_link

    def download_image(self):
        # download the image
        req = requests.get(self.get_image_link())
        image_path = 'files/image.jpeg'
        with open(image_path,'wb') as file:
            file.write(req.content)
        return image_path

    def set_image(self):
        # set the image in image widget
        self.manager.current_screen.ids.img.source = self.download_image()
class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()