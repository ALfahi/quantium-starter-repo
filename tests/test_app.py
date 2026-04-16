from app.app import app


def testHeaderPresent(dash_duo):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h2")
    assert header is not None
    assert "Soul Foods Analytics" in header.text


def testGraphPresent(dash_duo):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#lineChart")
    assert graph is not None


def testRadioButtonsPresent(dash_duo):
    dash_duo.start_server(app)

    radio = dash_duo.find_element("#regionFilter")
    assert radio is not None