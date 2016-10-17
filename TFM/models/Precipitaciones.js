var mongoose = require('mongoose'),  
    Schema   = mongoose.Schema;

var PrecipitacionesSchemaMad = new Schema(

{
    Estacion : String,
    Provincia : String,
    Temp_C : Number,
    VelViento_km_h : Number,
    DireccionViento : String,
    Racha_km_h : Number,
    DireccionRacha : String,
    Precipitacion_mm : Number,
    Presion_hPa : Number,
    Tendencia_hPa : Number,
    Humedad_perc : Number
}  
	);

module.exports = mongoose.model('Preci', PrecipitacionesSchemaMad, 'precipitaciones');
