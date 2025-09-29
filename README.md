# Auto-Automation — Bezpieczna wersja

## Opis

Edukacyjny skrypt demonstrujący automatyzację pulpitu w Pythonie przy użyciu `pyautogui`.
**Nie zmienia haseł ani nie wykonuje działań administracyjnych** — tylko bezpieczne operacje, np. otwarcie Notatnika i wpisanie tekstu.

---

## Ostrzeżenie

Nie używaj automatyzacji do działań, do których nie masz uprawnień. Testuj tylko na własnym komputerze lub w środowisku testowym.

---

## Wymagania

* Python 3.8+
* Biblioteki:

  * `pyautogui` (`pip install pyautogui`)
  * `time` (wbudowana)

---

## Przykład użycia

```python
import pyautogui, time

time.sleep(2)
pyautogui.hotkey('win', 'r')
time.sleep(0.5)
pyautogui.typewrite('notepad')
pyautogui.press('enter')
time.sleep(0.8)
pyautogui.typewrite('To jest bezpieczny test automatyzacji.\n')
```

---

## Najważniejsze funkcje

* `pyautogui.typewrite('tekst')` — wpisuje tekst
* `pyautogui.press('enter')` — naciska Enter
* `pyautogui.hotkey('win', 'r')` — skrót klawiszowy
* `time.sleep(sec)` — pauza między akcjami

---

## Dobre praktyki

* Testuj wyłącznie w środowisku kontrolowanym
* Dodaj opóźnienia (`time.sleep`) między akcjami
* Stwórz tryb „dry-run” do logowania akcji zamiast ich wykonywania

---

## Licencja

Używasz kod na własną odpowiedzialność.

#
