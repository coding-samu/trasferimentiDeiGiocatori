from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from random import choice
import requests

class IndovinaGiocatore(App):
    def build(self):
        self.window = BoxLayout(orientation='vertical', padding=10, spacing=10)
        Window.clearcolor = '#19232d'

        self.scrollview = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.7))
        self.transfers_layout = GridLayout(cols=2, size_hint_y=None, spacing=10, padding=10)
        self.transfers_layout.bind(minimum_height=self.transfers_layout.setter('height'))
        self.scrollview.add_widget(self.transfers_layout)
        self.window.add_widget(self.scrollview)

        self.buttons_layout = BoxLayout(size_hint=(1, 0.1), orientation='horizontal', spacing=10)

        self.aggiorna = Button(text="Aggiorna", size_hint=(1, 1), bold=True, background_color='#455364')
        self.aggiorna.bind(on_press=self.aggiornaLista)
        self.buttons_layout.add_widget(self.aggiorna)

        self.prossimo = Button(text="Inizia", size_hint=(1, 1), bold=True, background_color='#455364')
        self.prossimo.bind(on_press=self.trovaTrasferimentiGiocatore)
        self.buttons_layout.add_widget(self.prossimo)

        self.soluzioneB = Button(text="Soluzione", size_hint=(1, 1), bold=True, background_color='#455364')
        self.soluzioneB.bind(on_press=self.mostraSoluzione)
        self.buttons_layout.add_widget(self.soluzioneB)

        self.window.add_widget(self.buttons_layout)

        self.url = "https://raw.githubusercontent.com/SamueleQuaresima/trasferimentiDeiGiocatori/main/players.json"
        self.diz = {}

        self.aggiornaLista(None)
        
        return self.window

    def aggiornaLista(self, instance):
        self.prossimo.text = "Inizia"
        self.transfers_layout.clear_widgets()
        try:
            self.r = requests.get(self.url)
            self.r.raise_for_status()
            self.diz = self.r.json()
            self.soluzione = "Devi prima iniziare"
        except requests.exceptions.RequestException as e:
            error_label = Label(
                text="Errore di connessione.",
                font_size='18sp',
                color='#ff0000',  # rosso per segnalare l'errore
                size_hint_y=None,
                height=30,
                halign='center',
                text_size=(Window.width * 0.8, None)
            )
            self.transfers_layout.add_widget(error_label)

    def trovaTrasferimentiGiocatore(self, instance):
        self.prossimo.text = "Prossimo"
        if len(self.diz) > 0:
            self.soluzione, trasferimenti = choice(list(self.diz.items()))
            self.mostraTrasferimenti(trasferimenti)
            self.diz.pop(self.soluzione)
        else:
            self.transfers_layout.clear_widgets()
            self.soluzione = Label(
                text="Hai completato la lista!\nPer continuare a giocare fai click su aggiorna",
                font_size='18sp',
                color='#ffffff',
                size_hint_y=None,
                height=30,
                halign='center',
                text_size=(Window.width * 0.8, None)
            )
            self.transfers_layout.add_widget(self.soluzione)

    def mostraTrasferimenti(self, trasferimenti):
        self.transfers_layout.clear_widgets()
        trasferimenti.reverse()
        for trasferimento in trasferimenti:
            stagione_label = Label(
                text=f"Stagione:",
                font_size='16sp',
                color='#ffffff',
                size_hint_y=None,
                height=30,
                halign='left',
                text_size=(Window.width * 0.4, None)
            )
            stagione_value = Label(
                text=f"{trasferimento['season']}",
                font_size='16sp',
                color='#ffffff',
                size_hint_y=None,
                height=30,
                halign='left',
                text_size=(Window.width * 0.4, None)
            )

            vecchio_club_label = Label(
                text=f"Vecchio Club:",
                font_size='16sp',
                color='#ffffff',
                size_hint_y=None,
                height=30,
                halign='left',
                text_size=(Window.width * 0.4, None)
            )
            vecchio_club_value = Label(
                text=f"{trasferimento['old_club']}",
                font_size='16sp',
                color='#ffffff',
                size_hint_y=None,
                height=30,
                halign='left',
                text_size=(Window.width * 0.4, None)
            )

            nuovo_club_label = Label(
                text=f"Nuovo Club:",
                font_size='16sp',
                color='#ffffff',
                size_hint_y=None,
                height=30,
                halign='left',
                text_size=(Window.width * 0.4, None)
            )
            nuovo_club_value = Label(
                text=f"{trasferimento['new_club']}",
                font_size='16sp',
                color='#ffffff',
                size_hint_y=None,
                height=30,
                halign='left',
                text_size=(Window.width * 0.4, None)
            )

            fee_label = Label(
                text=f"Tipo:",
                font_size='16sp',
                color='#ffffff',
                size_hint_y=None,
                height=30,
                halign='left',
                text_size=(Window.width * 0.4, None)
            )
            fee_value = Label(
                text=f"{trasferimento['fee']}",
                font_size='16sp',
                color='#ffffff',
                size_hint_y=None,
                height=30,
                halign='left',
                text_size=(Window.width * 0.4, None)
            )

            space_label = Label(
                text=f"---",
                font_size='16sp',
                color='#ffffff',
                size_hint_y=None,
                height=30,
                halign='left',
                text_size=(Window.width * 0.4, None)
            )
            space_value = Label(
                text=f"---",
                font_size='16sp',
                color='#ffffff',
                size_hint_y=None,
                height=30,
                halign='left',
                text_size=(Window.width * 0.4, None)
            )

            self.transfers_layout.add_widget(stagione_label)
            self.transfers_layout.add_widget(stagione_value)
            self.transfers_layout.add_widget(vecchio_club_label)
            self.transfers_layout.add_widget(vecchio_club_value)
            self.transfers_layout.add_widget(nuovo_club_label)
            self.transfers_layout.add_widget(nuovo_club_value)
            self.transfers_layout.add_widget(fee_label)
            self.transfers_layout.add_widget(fee_value)
            self.transfers_layout.add_widget(space_label)
            self.transfers_layout.add_widget(space_value)

    def mostraSoluzione(self, instance):
        self.transfers_layout.clear_widgets()
        if not self.diz:
            soluzione_label = Label(
                text="Errore: devi prima aggiornare.",
                font_size='18sp',
                color='#ff0000',  # rosso per segnalare l'errore
                size_hint_y=None,
                height=30,
                halign='center',
                text_size=(Window.width * 0.8, None)
            )
        else:
            soluzione_label = Label(
                text=self.soluzione,
                font_size='18sp',
                color='#ffffff',
                size_hint_y=None,
                height=30,
                halign='center',
                text_size=(Window.width * 0.8, None)
            )
        self.transfers_layout.add_widget(soluzione_label)

IndovinaGiocatore().run()
