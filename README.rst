GreenGlacier
=======================

A gevent-based concurrent uploader for glacier using Boto3

----

This package aims to provide a simple library interface for completing multipart
uploads to `AWS Glacier <https://aws.amazon.com/glacier/>`_. It uses `gevent
<http://www.gevent.org/>` provided greenlets for concurrency and connects using
a Boto3 Vault resource (or something which is acts like one) provided by the
consumer. This package does not depend directly on Boto3.

A reference implementation:

::

    import boto3
    import sys
    from greenglacier import GreenGlacierUploader

    glacier = boto3.resource('glacier')
    vault = glacier.Vault('-', 'vault name')
    uploader = GreenGlacierUploader(vault)
    try:
        uploader.upload(sys.argv[1])
    except GreenGlacierUploader.UploadFailedException as e:
        print("Failed to upload {}: {}".format(args.filename, e))
