var mongoose = require('mongoose'),  
    Schema   = mongoose.Schema;

var EstacionSchemaMad = new Schema({
    id: String,
	name: String,
	stations: [{
		name: String,
		latitude: Number,
		longitude: Number,
		id: String,
		empty_slots: Number,
		free_bikes: Number,
		timestamp: Date
	}]
});

module.exports = mongoose.model('EstacionMad', EstacionSchemaMad, 'estacionesMad');
