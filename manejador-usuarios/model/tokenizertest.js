const jwt = require('jsonwebtoken')
const SECRET = "django-insecure-w+vj23@hv1dprv*bo=iodi4^=e(kmvbgiv_$as$k$ydlo6723("
const payload = {
    "token_type": "access",
    "user_id": 40
}
const signed = jwt.sign(payload, SECRET)
console.log(signed)
console.log(jwt.verify(signed, SECRET))