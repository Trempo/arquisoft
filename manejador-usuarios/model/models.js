const pbkdf = require('pbkdf2')
const crypto = require('crypto');

// Genera un hash de contraseña igual que el de django
const hash_password = (password, pastPass = null) => {
    let final_output = "pbkdf2_sha256$150000$"
    let salt
    if (pastPass) {
        salt = getSaltFromPassHash(pastPass)
    }else{
        salt = crypto.randomBytes(9).toString('base64');
        salt = salt + salt
        salt = salt.substring(0, 12)
    }
    crypto.DEFAULT_ENCODING = 'base64'
    const derivedKey = pbkdf.pbkdf2Sync(password, salt, 150000, 32, 'sha256')

    final_output = final_output + `${salt}\$${derivedKey}`

    crypto.DEFAULT_ENCODING = 'buffer'
    console.log(`Hash password: ${password}, ${pastPass}. Final hash: ${final_output}`)
    return final_output
}

const getSaltFromPassHash = (password) => {
    return password.split("$")[2]
}

const getJwtid = () => {
    return "" + crypto.randomBytes(16).toString('hex');
}

const JWT_SECRET = 'django-insecure-w+vj23@hv1dprv*bo=iodi4^=e(kmvbgiv_$as$k$ydlo6723('


//pbkdf2_sha256$150000$IifNCzK6LibP$WNxCYvHl5dER1k7IWKaQ2jpvaR9rReOFbXQKWqZIFps=
//jg2hrEpHodcKoB68bz1JUdNZytZly4isXr+qrA6PXbQ=

module.exports = {getJwtid, hash_password, JWT_SECRET}