import argparse
import OpenSSL
import ssl
from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument("-H", "--host", help="Host that used ssl protocol.")
parser.add_argument("-P", "--port", help="Port that used by host. i.e 443 (default port https)")
args = parser.parse_args()


def change_bytes_into_datetime(byte):
    format = '%Y-%m-%d'
    dateExpiry = byte.decode('utf-8')
    year = dateExpiry[:4]
    month = dateExpiry[4:6]
    day = dateExpiry[6:8]
    dateExpiryFormat = "{}-{}-{}".format(year, month, day)
    result = datetime.strptime(dateExpiryFormat, format)
    return result


def get_number_of_days(dateExpiry):
    dateNow = datetime.now()
    result = dateExpiry - dateNow
    result = str(result)
    return result


def ssl_expiry_result(host, port):
    try:
        cert = ssl.get_server_certificate((host, port))
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
        dateByte = x509.get_notAfter()
        dateExpiry =  change_bytes_into_datetime(dateByte)
        number_of_days = get_number_of_days(dateExpiry).split(',')
        result = number_of_days[0]
        return result
    except Exception as e:
        result = e, 'Please input your host and port correctly.'
        return result


def main(host, port):
    return ssl_expiry_result(host, port)


if __name__ == "__main__":
    print(main(args.host, args.port))
