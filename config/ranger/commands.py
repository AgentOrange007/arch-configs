from typing import Tuple, Optional

from ranger.api.commands import Command
from ranger.ext.get_executables import get_executables


class wal(Command):
    """
    :wal [filename] [alpha [background]]

    Generate a Pywal color scheme for the selected or given image.
    """

    DEFAULT_ALPHA: int = 98
    DEFAULT_BACKGROUND: str = '#0a0a0a'

    def execute(self) -> None:
        """
        Run Pywal with a given image, alpha, and background color.

        :return: None
        """
        if 'wal' not in get_executables():
            self.fm.notify('Could not find pywal in PATH.', bad=True)
            return

        (image_filename, alpha, background) = self._get_arguments()

        self.fm.notify(f'Running pywal using {image_filename}.')
        self.fm.execute_command(f'wal -i "{image_filename}" '
                                f'-a {alpha} -b "{background}"')

    def tab(self, tabnum) -> Optional[str]:
        return self._tab_directory_content()

    def _get_arguments(self) -> Tuple[str, int, str]:
        """
        Parse any command arguments or use their respective default.

        :return: A tuple with image path, alpha, and background color
        """
        image_path: str = self.fm.thisfile.path
        alpha: int = self.DEFAULT_ALPHA
        background: str = self.DEFAULT_BACKGROUND

        if self.arg(1) and not self.arg(1).isdigit():
            image_path = self.arg(1)
            self.shift()

        if self.arg(1).isdigit():
            alpha = int(self.arg(1))

            if self.arg(2):
                background = self.arg(2)

        return image_path, alpha, background
