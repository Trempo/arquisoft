const pbkdf = require('pbkdf2')
const crypto = require('crypto');
crypto.DEFAULT_ENCODING = 'base64'
//pbkdf2_sha256$150000$IifNCzK6LibP$WNxCYvHl5dER1k7IWKaQ2jpvaR9rReOFbXQKWqZIFps=
//jg2hrEpHodcKoB68bz1JUdNZytZly4isXr+qrA6PXbQ=
var derivedKey = pbkdf.pbkdf2Sync('testman', 'Osa3BBkRAuZf', 150000, 32, 'sha256')
console.log("Correct answer:  "+ "WNxCYvHl5dER1k7IWKaQ2jpvaR9rReOFbXQKWqZIFps")
console.log("Calculated answer " + derivedKey)