from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def hover_rectangle(driver, element, steps=30, delay=0.02):
    """
    Move the mouse in a rectangular pattern along the border of `element`.
    """

    rect = element.rect
    w = rect['width']
    h = rect['height']

    # Start at top-left corner relative to the element center
    actions = ActionChains(driver)
    actions.move_to_element_with_offset(element, 1 - w/2, 1 - h/2).pause(0.1)

    # Top edge (left -> right)
    for _ in range(steps):
        actions.move_by_offset(w / steps, 0).pause(delay)

    # Right edge (top -> bottom)
    for _ in range(steps):
        actions.move_by_offset(0, h / steps).pause(delay)

    # Bottom edge (right -> left)
    for _ in range(steps):
        actions.move_by_offset(-w / steps, 0).pause(delay)

    # Left edge (bottom -> top)
    for _ in range(steps):
        actions.move_by_offset(0, -h / steps).pause(delay)

    actions.perform()


def find_and_hover_anchor_tags(driver, steps=30, delay=0.02):
    """
    Finds all anchor elements with href (excluding a specific domain)
    and performs a rectangular hover pattern on each.
    """

    elements = driver.find_elements(
        By.CSS_SELECTOR,
        "a[href]:not([href*='accountplusfinance.com'])"
    )

    elem_count = 0

    for el in elements:
        try:
            hover_rectangle(driver, el, steps=steps, delay=delay)
            elem_count += 1
        except Exception as e:
            print(f"Error moving over element: {e}")

    print(f"Number of elements hovered with rectangle: {elem_count}")

