import pytest
from greenglacier import GreenGlacierUploader


def test_init_succeeds():
    g = GreenGlacierUploader(None)
    assert isinstance(g, GreenGlacierUploader)


def test_need_real_file():
    g = GreenGlacierUploader(None)
    with pytest.raises(OSError):
        g.upload('fake filename')


def test_need_real_vault():
    g = GreenGlacierUploader(None)
    with pytest.raises(AttributeError):
        g.upload('/dev/zero')
