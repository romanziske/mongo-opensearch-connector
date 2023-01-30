
db = new Mongo().getDB("iqdm");

db.createCollection('collection', { capped: false });
db.createCollection('sigmf', { capped: false });

db.createView("collectionView", "collection", [ 
    {
        $lookup:
        {
            from: "sigmf",
            localField: "datasets",
            foreignField: "_id",
            as: "datasets"
        }
    }
])
