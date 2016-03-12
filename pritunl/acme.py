from pritunl import settings
from pritunl import utils
from pritunl import app

import os

def get_acme_cert(account_key, csr):
    from pritunl import app
    from pritunl import acme_tiny

    temp_path = utils.get_temp_path()
    account_key_path = temp_path + '.key'
    csr_path = temp_path + '.csr'

    with open(account_key_path, 'w') as account_key_file:
        os.chmod(account_key_path, 0600)
        account_key_file.write(account_key)

    with open(csr_path, 'w') as csr_file:
        csr_file.write(csr)

    certificate = acme_tiny.get_crt(
        account_key_path,
        csr_path,
        app.set_acme,
    )

    cert_path = temp_path + '.crt'
    with open(cert_path, 'w') as cert_file:
        cert_file.write(certificate)

    try:
        os.remove(account_key_path)
    except:
        pass
    try:
        os.remove(csr_path)
    except:
        pass

    return certificate
