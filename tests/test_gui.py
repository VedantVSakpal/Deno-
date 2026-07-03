import io
import unittest
from unittest.mock import patch

import gui


class GuiTests(unittest.TestCase):
    def test_main_falls_back_to_text_when_display_unavailable(self):
        with patch("gui.tk.Tk", side_effect=gui.tk.TclError("no display")), patch(
            "builtins.input", return_value="exit"
        ), patch("sys.stdout", new_callable=io.StringIO) as stdout:
            gui.main()

        output = stdout.getvalue()
        self.assertIn("Tkinter GUI is not available", output)
        self.assertIn("Deno Assistant is ready", output)


if __name__ == "__main__":
    unittest.main()
