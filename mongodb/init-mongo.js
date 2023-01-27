
db = new Mongo().getDB("iqdm");

db.createCollection('sigmf', { capped: false });