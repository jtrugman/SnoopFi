exports.network_update = (req, res, next) => res.status(200).json(
    {
        response: req.body.test
    });