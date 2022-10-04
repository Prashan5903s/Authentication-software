import pyotp

ab = "6254E7647HL236QHO774766K633ZB237"
totp= pyotp.TOTP(ab)
ac = (totp.now())
print(ac)
ae=totp.verify(ac)
fg= bool(True)
if (ae==fg):
    print(4)
else:
    print(5)
