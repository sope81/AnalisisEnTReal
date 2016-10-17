var mongoose = require('mongoose'),
    EstacionMad  = mongoose.model('EstacionMad');


exports.MadStationStats = function(req, res) {
    EstacionMad.aggregate([
			//{$project: {_id:0, stations:1 }}
			{$unwind :"$stations"} 
			,{$group : {_id:{
                            Estacion:"$stations.name" , Lat:"$stations.latitude" ,  Lng:"$stations.longitude"}
							, free_bikes: {$avg: "$stations.free_bikes"},
						empty_slots: {$avg: "$stations.empty_slots"}}}
					] 
	,
        function(err, result) {
        if(err) {
            return res.status(404).send('Error al recuperar las estadísticas Mad: ' + err);
        }
        return res.status(200).send(result);
    });
};
exports.TotBici = function(req, res) {
    EstacionMad.aggregate([
			//{$project: {_id:0, stations:1 }}
			{$unwind :"$stations"} 
			,{$group : {_id:"BiciMad", free_bikes: {$sum: "$stations.free_bikes"},
						empty_slots: {$sum: "$stations.empty_slots"}}}
					] 
	,
        function(err, result) {
        if(err) {
            return res.status(404).send('Error al recuperar las estadísticas Mad: ' + err);
        }
        return res.status(200).send(result);
    });
};


