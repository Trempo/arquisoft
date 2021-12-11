const {getJwtid, hash_password, JWT_SECRET} = require('../model/models')

var express = require('express');
var router = express.Router();
var pgp = require('pg-promise')(/* options */)
var db = pgp('postgres://stigmergy:stigmergy@stigmergy2.cdtxxefugdnk.us-east-1.rds.amazonaws.com:5432/stigmergy')
const jwt = require('jsonwebtoken')

/* GET users listing. */
router.get('/', function (req, res, next) {
    res.send('respond with a resource');
});

// Create user
router.post('/', async (req, res) => {
    const username = req.body.username
    let password = req.body.password
    password = hash_password(password)
    const first_name = req.body.first_name
    const last_name = req.body.last_name
    const email = req.body.last_name
    const is_staff = false
    const is_superuser = false
    const is_active = true
    const date_joined = new Date()
    const last_login = new Date()

    if (username.trim().length === 0 || password.trim().length === 0 || email.trim().length === 0) {
        res.status(400).send({
            message: "Faltaron valores"
        })
    }
    try {
        let id = await db.one('INSERT INTO auth_user(username, password, first_name, last_name, email, is_staff, is_superuser, is_active, date_joined, last_login) ' +
            'VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9::timestamptz, $10::timestamptz) RETURNING id', [
            username, password, first_name, last_name, email, is_staff, is_superuser, is_active, date_joined, last_login])
        const payload = {
            "token_type": "access",
            "user_id": id.id
        }
        const signed_jwt = jwt.sign(payload, JWT_SECRET, {expiresIn: "2 days", jwtid: getJwtid()})
        console.info(`token: ${signed_jwt}`)
        res.send(signed_jwt)
    } catch (e) {
        res.status(400).send({
            message: e.toString()
        })
    }
})

router.get('/:id', async (req, res) => {
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
                res.json(user)
            } catch (e) {
                res.status(403).send(`User of id ${requestedid} was not found: `+ e.toString())
            }
        }else{
            res.status(403).send("Token not valid for requested user.")
        }
    } catch (err) {
        res.status(403).send("Wrong or invalid token: "+ err.toString())
    }
})


router.delete('/:id', async (req, res) => {
    const requestedid = req.params.id
    if (req.headers.authorization.split(" ")[0] !== "Bearer") {
        res.status(412).send("Malformed bearer token")
    }
    let token = req.headers.authorization.split(" ")[1]
    try {
        let payload = jwt.verify(token, JWT_SECRET)
        if ((payload.user_id) === Number(requestedid)) {
            try {

                await db.none(`DELETE FROM auth_user
                                    WHERE id = $1`, [requestedid])
                res.status(200).send(`User with id ${requestedid} deleted successfully!`)
            } catch (e) {
                res.status(403).send(`User of id ${requestedid} was not found: `+ e.toString())
            }
        }else{
            res.status(403).send("Token not valid for requested user.")
        }
    } catch (err) {
        res.status(403).send("Wrong or invalid token: "+ err.toString())
    }
})

module.exports = router;
