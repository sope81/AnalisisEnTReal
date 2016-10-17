var mongoose = require('mongoose'),  
    Schema   = mongoose.Schema;

var ContaminacionSchemaMad = new Schema({
    ESTACION: Number,
	MAGNITUD: Number,
	TECNICA: Number,
	HORARIO: Number,
	ANIO: Number,
	MES: Number,
	DIA: Number,
	HORA1: Number,
	HORA2: Number,
	HORA3: Number,
	HORA4: Number,
	HORA5: Number,
	HORA6: Number,
	HORA7: Number,
	HORA8: Number,
	HORA9: Number,
	HORA10: Number,
	HORA11: Number,
	HORA12: Number,
	HORA13: Number,
	HORA14: Number,
	HORA15: Number,
	HORA16: Number,
	HORA17: Number,
	HORA18: Number,
	HORA19: Number,
	HORA20: Number,
	HORA21: Number,
	HORA22: Number,
	HORA23: Number,
	HORA24: Number,
	EST_NAME: String,
	Alt: Number,
	coordenadas: {
		lat: Number,
		lng: Number
		}
	});

module.exports = mongoose.model('Cont', ContaminacionSchemaMad, 'contaminacion');
