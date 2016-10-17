var mongoose = require('mongoose'),  
    Schema   = mongoose.Schema;

var TraficoSchemaMad = new Schema({    
	carga : Number,
    tipo_elem : String,
    ocupacion : Number,
    descripcion : String,
    intensidadSat : Number,
    accesoAsociado : Number,
    loaddata : String,
    intensidad : Number,
    codigo : Number,
    error : String,
    nivelServicio : String,
    subarea : Number,
	coordenadas: {
		lat: Number,
		lng: Number
		}
	});

module.exports = mongoose.model('Traf', TraficoSchemaMad, 'trafico');
