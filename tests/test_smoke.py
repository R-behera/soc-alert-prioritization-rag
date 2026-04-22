from src.app.main import app


def test_title_present():
    assert app.title == 'SOC Alert Prioritization RAG'
