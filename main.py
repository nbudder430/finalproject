from dndgui import *


def main() -> None:
    """
    Function that starts the GUI application
    :return: None
    """


    window = Tk()
    window.title('THE D&D BALANCE TESTER')
    window.geometry('600x700')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()

