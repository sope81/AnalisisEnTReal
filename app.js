var express = require('express'),
    app = express(),
    bodyParser  = require('body-parser'),
    methodOverride = require('method-override'),
    mongoose = require('mongoose');

//conexion a bbdd
console.log('[MONGODB] Conectando a bbdd...');
mongoose.connect('mongodb://localhost/TFM', function(err, res) {
    if(err) {
        return console.log('[KO]. ERROR: ' + err);
    }
    console.log('[OK]. Conectado a bbdd');

    app.use(methodOverride());
    app.use(bodyParser.urlencoded({ extended: false }));
    app.use(bodyParser.json());
    app.use(function(req, res, next) {
        res.header("Access-Control-Allow-Origin", "*");
        res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
        next();
    });

    // Registrar modelos
    require('./models/Contaminacion');
	require('./models/Trafico');
	require('./models/Trafico_v2');
	require('./models/estacionMad');
	require('./models/Precipitaciones');
    // Importar rutas
    require('./routes/routes')(app);

    // inicio servidor
    console.log('**************************************');
    console.log('Arrancando el servidor...');
    app.listen(3000, function() {
        console.log('[OK]. Servidor funcionando en http://localhost:3000');
    });
});



