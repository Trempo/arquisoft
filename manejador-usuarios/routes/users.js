const {getJwtid, hash_password, JWT_SECRET} = require('../model/models')

var express = require('express');
var router = express.Router();
const db = require('../app').db
const jwt = require('jsonwebtoken')

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

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
  const date_joined = Date.now()
  const last_login = Date.now()

  try{
    let id = await db.one('INSERT INTO auth_user(username, password, first_name, last_name, email, is_staff, is_superuser, is_active, date_joined, last_login) ' +
        'VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10) RETURNING id', [
      username, password, first_name, last_name, email, is_staff, is_superuser, is_active, date_joined, last_login])
  const payload = {
    "token_type": "access",
    "user_id": id
  }
  const signed_jwt = jwt.sign(payload, JWT_SECRET, {expiresIn: "2 days", jwtid: getJwtid()})

  res.send(signed_jwt)
  }catch (e) {
    res.status(400).send({
      message: e
    })
  }

})

module.exports = router;
