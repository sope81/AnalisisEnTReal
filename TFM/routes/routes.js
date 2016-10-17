var ctrlcontaminacion = require('../controllers/Contaminacion');
var ctrltrafico = require('../controllers/Trafico');
var ctrltrafico2 = require('../controllers/Trafico_v2');
var estacionesControllerMad = require('../controllers/estacionesMad');
var estacionesLoadBicis = require('../controllers/webscrappingMad');
var ctrlprecipitaciones = require('../controllers/precipitaciones');


module.exports = function(app) {
    app.get('/', function(req, res) {
        res.send('Proyecto TFM Ignacio Sopelana');
    });
    app.get('/contaminacion', ctrlcontaminacion.findAllContaminacion);
	app.get('/aggNOx', ctrlcontaminacion.aggNOx);
	app.get('/aggNO2', ctrlcontaminacion.aggNO2);
	app.get('/aggSO2', ctrlcontaminacion.aggSO2);
	app.get('/aggPM25', ctrlcontaminacion.aggPM25);
	app.get('/aggPM10', ctrlcontaminacion.aggPM10);
	app.get('/GeoAggNOx', ctrlcontaminacion.GeoAggNOx);
	app.get('/stationsMad/stats', estacionesControllerMad.MadStationStats);
	app.get('/Trafico', ctrltrafico.findAlltrafico);
	app.get('/Trafico2', ctrltrafico2.findAlltrafico);
	app.get('/bicis', estacionesControllerMad.MadStationStats);
	app.get('/totbicis', estacionesControllerMad.TotBici);
	app.get('/cargabicis', estacionesLoadBicis.webScrapping);
	app.get('/precipitacionesAll', ctrlprecipitaciones.precipitacionesAll);
	app.get('/precipitacionesAgg', ctrlprecipitaciones.precipitacionesAgg);
    
};
