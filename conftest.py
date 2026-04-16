import sys
import os
import pytest

# fix imports since we need to force it to see the app and route folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# force selenium to we want expect chromedriver in PATH issues
@pytest.fixture(autouse=True)
def selenium_driver_path(monkeypatch):
    monkeypatch.setenv("SE_BROWSER", "chrome")# force dash to use chrome(fixes pytest errors)