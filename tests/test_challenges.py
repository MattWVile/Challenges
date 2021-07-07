from programs.near import near

def test_near():
    assert near('dragon','dragoon') == False
    assert near('dragoon','dragon') == True
    assert near('dragoin','dragon') == True
    assert near('bigbrian','bigbrain') == False