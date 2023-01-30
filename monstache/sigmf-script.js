module.exports = function (doc) {
    collectionDoc = findOne({ "datasets": doc._id }, {
        database: "iqdm",
        collection: "collection"
        });
    if (collectionDoc) {
        collectionDoc.datasets = collectionDoc.datasets.map(function (datasetID) {
            return findId(datasetID, {
                database: "iqdm",
                collection: "sigmf"
            });
        });
    }
    return doc;
}