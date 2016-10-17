var mongoose = require('mongoose'),
    Contaminacion  = mongoose.model('Cont');
var d = new Date();
var hh = d.getHours();
exports.findAllContaminacion = function(req, res) {
    Contaminacion.find({"EST_NAME": { $exists: true}}, function(err, docs) {
        if(err) {
            return res.status(404).send('Error al recuperar los datos contaminación: ' + err);
        }
        return res.status(200).send(docs);
    });
};

exports.aggNOx = function(req, res) {
    Contaminacion.find({ EST_NAME: { $exists: true },MAG_ABV :'NOx' },{EST_NAME:1,  HORA: 1, }
					//	{$group : {_id:{EST_NAME:"$EST_NAME",TECNICA:"$TECNICA" },
                    //    HORA: {$sum: "$HORA"+hh},
					//	}}
					//] 
	,
        function(err, result) {
        if(err) {
            return res.status(404).send('Error al recuperar las estadísticas Mad: ' + err);
        }
        return res.status(200).send(result);
    });
};	

exports.aggNO2 = function(req, res) {
    Contaminacion.find({ EST_NAME: { $exists: true },MAG_ABV :'NO2' },{EST_NAME:1,  HORA: 1, }
					//	{$group : {_id:{EST_NAME:"$EST_NAME",TECNICA:"$TECNICA" },
                    //    HORA: {$sum: "$HORA"+hh},
					//	}}
					//] 
	,
        function(err, result) {
        if(err) {
            return res.status(404).send('Error al recuperar las estadísticas Mad: ' + err);
        }
        return res.status(200).send(result);
    });
};

exports.aggSO2 = function(req, res) {
    Contaminacion.find({ EST_NAME: { $exists: true },MAG_ABV :'SO2' },{EST_NAME:1,  HORA: 1, }
					//	{$group : {_id:{EST_NAME:"$EST_NAME",TECNICA:"$TECNICA" },
                    //    HORA: {$sum: "$HORA"+hh},
					//	}}
					//] 
	,
        function(err, result) {
        if(err) {
            return res.status(404).send('Error al recuperar las estadísticas Mad: ' + err);
        }
        return res.status(200).send(result);
    });
};

exports.aggPM25 = function(req, res) {
    Contaminacion.find({ EST_NAME: { $exists: true },MAG_ABV :'PM2.5' },{EST_NAME:1,  HORA: 1, }
					//	{$group : {_id:{EST_NAME:"$EST_NAME",TECNICA:"$TECNICA" },
                    //    HORA: {$sum: "$HORA"+hh},
					//	}}
					//] 
	,
        function(err, result) {
        if(err) {
            return res.status(404).send('Error al recuperar las estadísticas Mad: ' + err);
        }
        return res.status(200).send(result);
    });
};

exports.aggPM10 = function(req, res) {
    Contaminacion.find({ EST_NAME: { $exists: true },MAG_ABV :'PM10' },{EST_NAME:1,  HORA: 1, }
					//	{$group : {_id:{EST_NAME:"$EST_NAME",TECNICA:"$TECNICA" },
                    //    HORA: {$sum: "$HORA"+hh},
					//	}}
					//] 
	,
        function(err, result) {
        if(err) {
            return res.status(404).send('Error al recuperar las estadísticas Mad: ' + err);
        }
        return res.status(200).send(result);
    });
};
//Datos Geograficos
exports.GeoAggNOx = function(req, res) {
    Contaminacion.find({ EST_NAME: { $exists: true },MAG_ABV :'NOx' },{EST_NAME:1,  HORA: 1,coordenadas:1}
						,
        function(err, result) {
        if(err) {
            return res.status(404).send('Error al recuperar las estadísticas Mad: ' + err);
        }
        return res.status(200).send(result);
    });
};


