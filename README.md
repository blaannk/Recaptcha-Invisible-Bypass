# Bypass Invisible Recaptcha v2 / v3

Allows to bypass an invisible recaptcha just with **HTTP requests**, without **Selenium** or **OCR**.
## Important

1 - This bypass does not work on all invisible recaptchas, **you have to try it** to know if it works on your recaptcha;

2 - This bypass only works on **invisible recaptchas**.

3 - You must have **some knowledge** of HTTP requests to understand

## EXPLOIT

**TARGET** : https://bitly.com/a/sign_in
### STEP 1
Inspect network to find the **recaptcha anchor url**.

![](https://i.ibb.co/fFprvrH/anchor.png)

### STEP 2
Inspect network to find the **recaptcha reload url**.

![](https://i.ibb.co/1J3gxYY/reload.png)

### STEP 3
Let's now look at the **payload** of the reload request

1 - Find **CHR** [xx, xx, xx]

![](https://i.ibb.co/sjmFYCc/chr.png)

2 - Find **VH** (The **number sequence** after the character *)

![](https://i.ibb.co/HrchVCB/vh.png)

3 - Find **BG** (Not me :D, the other BG inside the payload **from the character** ! **to the character** *)

Starts here

![](https://i.ibb.co/nDTFfsY/bg1.png)

Ends here

![](https://i.ibb.co/BwMRhPt/bg2.png)

### STEP 4
Run **bypass.py** with python3 and fill inputs.

![](https://i.ibb.co/MB3nDMN/inputs.png)

Recaptcha is **vulnerable** :D we can generate the **recaptcha response** with HTTP requests !

![](https://i.ibb.co/3WCj0XC/bypass.png)

### STEP 5
Go in the **bypassed.txt** file, take the **variables** and you can now create your script to generate the **recaptcha response**.



## Generate Recaptcha Response

```python
import requests

def generateresponse(anchorurl, reloadurl, payload):
    s = requests.Session()
    r1 = s.get(anchorurl).text
    token1 = r1.split('recaptcha-token" value="')[1].split('">')[0]
    r2 = s.post(reloadurl, data=payload)
    try:
        token2 = str(r2.text.split('"rresp","')[1].split('"')[0])
        return token2
    except:
        return ""
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Credits
blank <3
