var request = require('request'),
    mongoose = require('mongoose'),
    EstacionMad  = mongoose.model('EstacionMad');

exports.webScrapping = function(req, res) {

    request('https://api.citybik.es/v2/networks/bicimad', function (err, response, html) {
        if (err) {
            return res.status(404).send('Error en el WebScrapping Mad: ' + err);
        }

        var respuesta = JSON.parse(response.body);
        var arrayEstacionesMad = [];

        for (var dato in respuesta) {
            arrayEstacionesMad.push(respuesta[dato]);
        }

        EstacionMad.create(arrayEstacionesMad, function (err, data) {
            if (err) {
                return res.status(404).send('Error al guardar: ' + err);
            }
            return res.status(200).send(data);
        });
    })
};