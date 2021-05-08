var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'ee629tm@gmail.com',
    pass: 'ee629test'
  }
});

exports.network_update = (req, res, next) => {
    var mailOptions = {
        from: 'ee629tm@gmail.com',
        to: req.body.to,
        subject: req.body.subject,
        text: req.body.net_data
      };
    transporter.sendMail(mailOptions, function(error, info){
        if (error) {
            console.log(error);
        } else {
            console.log('Email sent: ' + info.response);
        }
    })
    res.status(201).json(
        {
            response: "Update Sent"
        })
};