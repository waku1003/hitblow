"""コマンドの入口。第3回で `hitblow` コマンドがここ（main）を呼ぶ。"""

from .game import play


def main():
    play()
# from .gui import main as gui_main

# def main():
#     gui_main()
