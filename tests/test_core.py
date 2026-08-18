from main import local_command


def test_greeting():
    assert "HANS" in local_command("hello")


def test_help():
    assert "Commands" in local_command("help")


def test_status():
    assert "running" in local_command("status")
