var apm = require('elastic-apm-node').start({
    serviceName: 'Elasticsearch Viewer',
    apiKey: 'TkE2VE01SUJRQTB4OU5xalVxR1E6c29xQ3o4d2FRM2kyRmcyWkFDdGJfQQ==',
    serverUrl: 'http://localhost:8200',
    environment: 'production'
})

var express = require('express');
var app = express();
app.get('/', function (req, res) {
    res.send('Hello World!');
});
app.listen(3000, function () {
    console.log('Example app listening on port 3000!');
});