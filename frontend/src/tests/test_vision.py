from vision import detect_ball

def test_detect_ball():
    x, y = detect_ball()

    assert x >= 0
    assert y >= 0