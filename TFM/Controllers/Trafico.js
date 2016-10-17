var mongoose = require('mongoose'),
    trafico  = mongoose.model('Traf');

exports.findAlltrafico = function(req, res) {
    trafico.find({}, function(err, docs) {
        if(err) {
            return res.status(404).send('Error al recuperar los datos trafico: ' + err);
        }
        return res.status(200).send(docs);
    });
};


