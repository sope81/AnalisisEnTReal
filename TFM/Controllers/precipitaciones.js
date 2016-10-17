var mongoose = require('mongoose'),
    Precipitaciones  = mongoose.model('Preci');


exports.precipitacionesAll = function(req, res) {
    Precipitaciones.find({}, function(err, docs) {
        if(err) {
            return res.status(404).send('Error al recuperar los datos Precipitaciones: ' + err);
        }
        return res.status(200).send(docs);
    });
};

exports.precipitacionesAgg = function(req, res) {
    Precipitaciones.aggregate(
			[{$group : {_id:"Tot",
                                                Temp: {$avg: "$Temp_C"},
						VelViento: {$avg: "$VelViento_km_h"},
                                                Racha: {$avg:"$Racha_km_h"},
                                                Humedad:{$avg:"$Humedad_perc"},
												Precipitacion:{$avg:"$Precipitacion_mm"}
                                                }}]
	,
        function(err, result) {
        if(err) {
            return res.status(404).send('Error al recuperar las estadísticas Mad: ' + err);
        }
        return res.status(200).send(result);
    });
};


