from selenium.webdriver.common.by import By


class DroppablePageLocators:
    FRAME_DROPPABLE = (
        By.XPATH,
        '//*[@id="example-1-tab-1"]/div/iframe'
    )
    ELMNT_TO_BE_DRAGGED = (
        By.ID,
        'draggable'
    )
    ELMNT_WHERE_TO_DRAG = (
        By.ID,
        'droppable'
    )
