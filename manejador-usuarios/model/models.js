import {pbkdf2Sync} from 'pbkdf2'
import crypto from 'crypto';

export const hash_password = (password)=>{
    let final_output = "pbkdf2_sha256$150000$"
    let salt = crypto.randomBytes(9).toString('base64');
    salt = salt + salt
    salt = salt.substring(0, 12)

    const derivedKey = pbkdf2Sync(password, 'salt', 150000, 32, 'sha256')

    final_output = final_output + `${salt}\$${derivedKey}`

    return final_output
}

export const getJwtid = ()=>{
    return "" + crypto.randomBytes(16).toString('hex');
}

export const JWT_SECRET = 'django-insecure-w+vj23@hv1dprv*bo=iodi4^=e(kmvbgiv_$as$k$ydlo6723('


crypto.DEFAULT_ENCODING = 'base64'
//pbkdf2_sha256$150000$IifNCzK6LibP$WNxCYvHl5dER1k7IWKaQ2jpvaR9rReOFbXQKWqZIFps=
//jg2hrEpHodcKoB68bz1JUdNZytZly4isXr+qrA6PXbQ=
console.log("Correct answer:  "+ "WNxCYvHl5dER1k7IWKaQ2jpvaR9rReOFbXQKWqZIFps")
console.log("Calculated answer" + derivedKey)