module.exports = function (doc) {
    if (doc.datasets) {
        doc.datasets = doc.datasets.map(function (datasetID) {
            return findId(datasetID, {
                database: "iqdm",
                collection: "sigmf"
            });
        });
    }
    return doc;
}