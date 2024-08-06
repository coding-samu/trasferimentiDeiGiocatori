from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from random import choice
import requests

class IndovinaGiocatore(App):
    def build(self):
        self.window = GridLayout(cols=3, size_hint=(0.9, 0.9), pos_hint={"center_x": 0.5, "center_y": 0.5})
        Window.clearcolor = '#19232d'

        self.vuoto3 = Label(text="", font_size='1sp', color='#007dd1', width=1)
        self.window.add_widget(self.vuoto3)

        self.etichetta = Label(text="Fai click su prossimo per iniziare ...", font_size='18sp', color='#ffffff')
        self.window.add_widget(self.etichetta)

        self.vuoto4 = Label(text="", font_size='1sp', color='#007dd1', width=1)
        self.window.add_widget(self.vuoto4)

        self.aggiorna = Button(text="Aggiorna", size_hint=(1, 0.2), bold=True, background_color='#455364')
        self.window.add_widget(self.aggiorna)
        self.aggiorna.bind(on_press=self.aggiornaLista)

        self.prossimo = Button(text="Prossimo", size_hint=(1, 0.2), bold=True, background_color='#455364')
        self.window.add_widget(self.prossimo)
        self.prossimo.bind(on_press=self.trovaTrasferimentiGiocatore)

        self.soluzioneB = Button(text="Soluzione", size_hint=(1, 0.2), bold=True, background_color='#455364')
        self.window.add_widget(self.soluzioneB)
        self.soluzioneB.bind(on_press=self.mostraSoluzione)

        self.url = "https://raw.githubusercontent.com/SamueleQuaresima/trasferimentiDeiGiocatori/main/players.json"
        self.diz = {}
        self.soluzione = "Devi prima iniziare"
        
        # Prima volta, tenta di scaricare i dati
        self.aggiornaLista(None)
        
        return self.window

    def aggiornaLista(self, instance):
        try:
            self.r = requests.get(self.url)
            self.r.raise_for_status()  # Questo genera un'eccezione per codici di stato HTTP non 200
            self.diz = self.r.json()
            self.soluzione = "Devi prima iniziare"
            self.etichetta.text = "Fai click su prossimo per iniziare ..."
        except requests.exceptions.RequestException as e:
            self.etichetta.text = "Errore di connessione. Controlla la tua rete e riprova."
            self.mostraPopupErrore("Errore di connessione")

    def trovaTrasferimentiGiocatore(self, instance):
        if len(self.diz) > 0:
            self.soluzione, trasferimenti = choice(list(self.diz.items()))
            self.mostraPopupTrasferimenti(trasferimenti)
            self.diz.pop(self.soluzione)
        else:
            self.etichetta.text = "Hai completato la lista!\nSe vuoi continuare a giocare fai click su aggiorna"

    def mostraPopupTrasferimenti(self, trasferimenti):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        scrollview = ScrollView(size_hint=(1, None), size=(400, 400))
        label = Label(text=trasferimenti, font_size='18sp', color='#ffffff', size_hint_y=None)
        label.bind(texture_size=label.setter('size'))
        scrollview.add_widget(label)
        layout.add_widget(scrollview)

        popup = Popup(title='Trasferimenti Giocatore', content=layout, size_hint=(None, None), size=(500, 500))
        popup.open()

    def mostraSoluzione(self, instance):
        self.etichetta.text = self.soluzione

    def mostraPopupErrore(self, messaggio):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label = Label(text=messaggio, font_size='18sp', color='#ff0000')
        layout.add_widget(label)

        popup = Popup(title='Errore', content=layout, size_hint=(None, None), size=(400, 200))
        popup.open()

IndovinaGiocatore().run()
