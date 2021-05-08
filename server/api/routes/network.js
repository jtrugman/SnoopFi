const express = require('express');
const router = express.Router();

const networkController = require('../controllers/network');

router.post('/', networkController.network_update);

module.exports = router;