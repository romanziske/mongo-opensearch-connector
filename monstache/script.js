module.exports = function (doc) {
    if (doc.datasets) {
        doc.datasets = doc.datasets.map(function (dataset) {
            return findId(dataset, {
                database: "iqdm",
                collection: "sigmf"
            });
        });
    }
    return doc;
}