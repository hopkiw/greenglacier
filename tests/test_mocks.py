from mock import mock_open, patch
from greenglacier import GreenGlacierUploader


class MockBotoGlacierVault(object):
    def __init__(self,  *args, **kwargs):
        pass

    def initiate_multipart_upload(self, *args, **kwargs):
        return MockBotoGlacierMultipartUpload()


class MockBotoGlacierMultipartUpload(object):
    def __init__(self,  *args, **kwargs):
        pass

    def upload_part(self, *args, **kwargs):
        return True

    def complete(self, *args, **kwargs):
        return True


def test_upload():
    mocked_open = mock_open()
    mocked_vault = MockBotoGlacierVault()
    with patch('__builtin__.open', mocked_open, create=True):
        g = GreenGlacierUploader(mocked_vault)
        g.upload('/dev/zero')
