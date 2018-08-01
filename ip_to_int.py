"""
Simple way to convert IP address to int and back.
When we make the switch to Python 3 this will not be necessary any more,
as Py3 has a library called ipaddress (IPv4/IPv6 manipulation library)"""


def ip2int(ip):
    """split ip address into 4 Octets and calculate the integer value."""
    o = map(int, ip.split('.'))
    res = (o[0] * pow(256, 3)) + (o[1] * pow(256, 2)) + (o[2] * 256) + o[3]
    return res


def int2ip(ipaddr):
    s1 = int(ipaddr / pow(256, 3)) % 256
    s2 = int(ipaddr / pow(256, 2)) % 256
    s3 = int(ipaddr / 256) % 256
    s4 = int(ipaddr) % 256
    return '%s.%s.%s.%s' % (s1, s2, s3, s4)
