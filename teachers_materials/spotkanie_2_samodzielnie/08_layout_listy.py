# wczytujemy niezbędne elementy
import PySimpleGUI as sg

# definiujemy wygląd aplikacji
app_layout = [
    [sg.Text("Sample text element")],
    [sg.Column([[sg.Text("Another text element"), sg.Text("AAA")]], justification="center")],
]
# uruchamiamy
window = sg.Window("Example layout", app_layout)
# poniższe wywołanie pozostaje na ekranie aż do zamknięcia okna [X]
window.read()


# definiujemy wygląd aplikacji
app_layout = [
    [sg.Text("Sample text element")],
    [sg.Text("Another text element")],
    [sg.OK(), sg.OK("Some text")],
]
# uruchamiamy
window = sg.Window("Example layout", app_layout)
# poniższe wywołanie otwiera okno
window.read()
# a poniższe zamyka
window.close()


# obieranie wartości tekstowych z instrukcją wunkową
text = sg.popup_get_text("Title", "Please input something")
if not text:
    text = "Nothing there!"

sg.popup("Results", "The value returned from PopupGetText", text)


# definiujemy wygląd aplikacji
app_layout = [
    [sg.Text("Sample text element")],
    [sg.Text("Enter value"), sg.Input("Default")],
    [sg.Text("Another text element")],
    [sg.Text("Enter another value"), sg.Input("Default")],
    [sg.OK(), sg.Button("Button text")],
]
# uruchamiamy
window = sg.Window("Example layout", app_layout)
# poniższe wywołanie otwiera okno i wczytuje dane
event, values = window.read()
# sprawdzamy wartości zwracane przez okno
sg.popup("Returned dict is:", values)
# a poniższe zamyka
window.close()
# dodajemy sprawdzenie wciśniętego przycisku
if event == "Button text":
    # i wyświetlamy okno na 4 sekundy
    sg.popup_auto_close(
        "So, you click on button...",
        title="Windows with some title",
        auto_close_duration=4,
    )

# wykorzystanie odliczania w pętli
value = 0
for i in range(10000):
    value += i + 2
    sg.one_line_progress_meter("My Meter", i, 10000, "Element", "Optional message")
print(f"Value at the end = {value}")
