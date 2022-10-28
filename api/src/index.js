const express = require ('express');
const mysql = require('mysql');

const app = express();

const connection = mysql.createConnection({
    host:'mysql-container',
    user: 'root',
    password: 'sadlpv',
    database: 'sadlpv'
});

connection.connect();

app.get('/veiculos', function(req,res) {
    connection.query('SELECT * FROM veiculos WHERE placa="PNM9200"', function(error, results){
        if(error) {
            throw error
        };

        res.send(results.map(item => ({proprietario: item.proprietario, placa: item.placa, chassi: item.chassi, situacao: item.situacao}
        
            )));
        
        var ocorrencia = results[0].situacao    

        console.log(ocorrencia)    
    });
}); 

console.log('olá mundo')





app.listen(9001, '0.0.0.0', function() {
    console.log('Listening on port 9001')
})