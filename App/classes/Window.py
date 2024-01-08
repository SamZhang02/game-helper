from os import name
import pyautogui
from pywinauto.application import Application

class Window:

    def __init__(self, app_path:str) -> None:
        self.app = Application(backend="uia").start(app_path)

    def mouse_down(self) -> 'Window':
        pyautogui.mouseDown()
        return self

    def mouse_up(self) -> 'Window':
        pyautogui.mouseUp()
        return self

    def goto(self,x:int,y:int) -> 'Window':
        pyautogui.moveTo(x,y)
        return self

    def click(self) -> 'Window':
        pyautogui.click()
        return self

    def goto_and_click(self, x:int, y:int) -> 'Window':
        self.goto(x,y).click()
        return self

    def drag(self, x_from, y_from, x_to, y_to) -> 'Window':
        self.goto(x_from, y_from)\
            .mouse_down()\
            .goto(x_to, y_to)\
            .mouse_up()

        return self

    def find(self, image) -> tuple[int,int] | None: 
        """
        Returns the coordinates of the first instance of the image found in the window.
        """
        ...

        return (0,0)

    def find_all(self, image) -> list[tuple[int,int]]: 
        """
        Returns the coordinates of all instance of the image found in the window.
        """
        ...

        return [(0,0)]
    
    def has(self,image) -> bool:
        """
        Checks whether the window contains the image
        """

        return self.find(image) is not None


