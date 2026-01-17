from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import Interaction
import time

def find_and_hover_anchor_tags(driver, steps=30, delay=0.02):
    """
    Finds all elements with href and perform mouse movements
    """

    elements = driver.find_elements(By.CSS_SELECTOR, "a[href]:not([href*='accountplusfinance.com'])")

    for el in elements:
        try:
            # Get element location and size
            rect = el.rect
            x = rect['x']
            y = rect['y']
            w = rect['width']
            h = rect['height']

            # Define a pointer (mouse)
            mouse = PointerInput(PointerInput.MOUSE, "mouse")
            actions = ActionChains(driver)
            actions.w3c_actions = Interaction(driver)
            actions.w3c_actions.add_action(mouse)

            # Start at top-left corner
            actions.w3c_actions.pointer_action.move_to_location(x + 1, y + 1)
            actions.w3c_actions.pointer_action.pause(0.1)

            # Move across the top edge
            for i in range(steps):
                actions.w3c_actions.pointer_action.move_to_location(
                    x + int(w * (i / steps)),
                    y + 1
                )
                actions.w3c_actions.pointer_action.pause(delay)

            # Move down the right edge
            for i in range(steps):
                actions.w3c_actions.pointer_action.move_to_location(
                    x + w - 1,
                    y + int(h * (i / steps))
                )
                actions.w3c_actions.pointer_action.pause(delay)

            # Move across the bottom edge
            for i in range(steps):
                actions.w3c_actions.pointer_action.move_to_location(
                    x + int(w * (1 - i / steps)),
                    y + h - 1
                )
                actions.w3c_actions.pointer_action.pause(delay)

            # Move up the left edge
            for i in range(steps):
                actions.w3c_actions.pointer_action.move_to_location(
                    x + 1,
                    y + int(h * (1 - i / steps))
                )
                actions.w3c_actions.pointer_action.pause(delay)

            # Perform the full movement
            actions.perform()

        except Exception as e:
            print(f"Error moving over element: {e}")
