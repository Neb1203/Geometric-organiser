from pygame_menu.widgets.core.widget import Widget
from pygame_menu._types import EventVectorType

class MyWidget(Widget):

    def __init__(self, params):
        super(MyWidget, self).__init__(params)
        ...

    def _apply_font(self) -> None:
        """
        Function triggered after a font is applied to the widget
        by Menu._configure_widget() method.
        """
        ...

    def _draw(self, surface: 'pygame.Surface') -> None:
        """
        Draw the widget on a given surface.
        This method must be overridden by all classes.
        """
        # Draw the self._surface pygame object on the given surface
        surface.blit(self._surface, self._rect.topleft)

    def _render(self) -> Optional[bool]:
        """
        Render the Widget surface.

        This method shall update the attribute ``_surface`` with a :py:class:`pygame.Surface`
        object representing the outer borders of the widget.

        .. note::

            Before rendering, check out if the widget font/title/values are
            set. If not, it is probable that a zero-size surface is set.

        .. note::

            Render methods should call
            :py:meth:`pygame_menu.widgets.core.widget.Widget.force_menu_surface_update`
            to force Menu to update the drawing surface.

        :return: ``True`` if widget has rendered a new state, ``None`` if the widget has not changed, so render used a cache
        """
        ...

        # Generate widget surface
        self._surface = pygame.surface....

        # Update the width and height of the Widget
        self._rect.width, self._rect.height = self._surface.get_size() + SomeConstants

        # Force menu to update its surface on next Menu.render() call
        self.force_menu_surface_update()

    def update(self, events: EventVectorType) -> bool:
        """
        Update according to the given events list and fire the callbacks. This
        method must return ``True`` if it updated (the internal variables
        changed during user input).

        .. note::

            Update is not performed if the Widget is in ``readonly`` state or
            it's hidden. However, ``apply_update_callbacks`` method is called
            in most widgets, except :py:class:`pygame_menu.widgets.NoneWidget`.

        :param events: List/Tuple of pygame events
        :return: ``True`` if updated
        """
        ...
        return False