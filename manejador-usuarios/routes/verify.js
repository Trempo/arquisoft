const {getJwtid, hash_password, JWT_SECRET} = require('../model/models')

var express = require('express');
var router = express.Router();
var pgp = require('pg-promise')(/* options */)
var db = pgp('postgres://stigmergy:stigmergy@stigmergy2.cdtxxefugdnk.us-east-1.rds.amazonaws.com:5432/stigmergy')
const jwt = require('jsonwebtoken')
const {use} = require("express/lib/router");

/* Verify if a token is valid for a given user id. */
router.get('/token/:id', async function (req, res, next) {
    const requestedid = req.params.id
    if (req.headers.authorization.split(" ")[0] !== "Bearer") {
        res.status(412).send("Malformed bearer token")
    }
    let token = req.headers.authorization.split(" ")[1]
    try {
        let payload = jwt.verify(token, JWT_SECRET)
        if ((payload.user_id) === Number(requestedid)) {
            try {
                let user = await db.one(`SELECT *
                                         FROM auth_user
                                         WHERE id = $1`, [requestedid])
                if (user && user.id && user.id == requestedid){
                    res.status(200).send("The token is valid for the user with id " + requestedid)
                }else{
                    res.status(403).send("The requested user with id " + requestedid + " was not found.")
                }
            } catch (e) {
                res.status(403).send(`User of id ${requestedid} was not found: ` + e.toString())
            }
        } else {
            res.status(403).send("Token not valid for requested user.")
        }
    } catch (err) {
        res.status(403).send("Wrong or invalid token: " + err.toString())
    }
});

// Permite mandarle un objeto como {
//     "username":"testman",
//     "password": "testman"
// }
// y se retorna un JWT valido si las credenciales son correctas, o un 401 si no.
router.post('/login/', async function (req, res, next) {
    let username = req.body.username
    let password = req.body.password

    try{
        let foundUser = await db.one("SELECT * FROM auth_user WHERE username = $1", username);
        console.log(foundUser)
        if (foundUser && foundUser.username){
            let passwordHashReal = foundUser.password
            let passwordHashAttempt = hash_password(password, passwordHashReal)
            console.log(`${passwordHashAttempt} === \n${passwordHashReal}\n = ${passwordHashAttempt === passwordHashReal}`)
            if (passwordHashAttempt === passwordHashReal){
                const payload = {
                    "token_type": "access",
                    "user_id": foundUser.id
                }
                const signed_jwt = jwt.sign(payload, JWT_SECRET, {expiresIn: "2 days", jwtid: getJwtid()})
                res.status(200).send(signed_jwt)
            }else{
                res.status(401).send("Incorrect password!")
            }
        }else{
            res.status(401).send("No valid user was found with the username " + username);
        }
    }catch (e) {
        res.status(401).send("No valid user was found with the username " + username);
    }

});

module.exports = router;
