const express = require ('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false}));

const connection = mysql.createConnection({
    host:'mysql-container',
    user: 'root',
    password: 'sadlpv',
    database: 'sadlpv'
});

connection.connect();


app.get('/veiculos', function(req,res) {
    var placa = req.body.placa
    placa = '"'+placa+'"' 
    console.log(placa)
    connection.query('SELECT * FROM veiculos WHERE placa = ' + placa, function(error, results){
        if(error) {
            throw error
        };

        res.send(results.map(item => ({proprietario: item.proprietario, placa: item.placa, chassi: item.chassi, situacao: item.situacao, marca_modelo_cor: item.marca_modelo_cor}
        
            )));
        //var proprietario = results[0].proprietario
        //var chassi = results[0].chassi   
        //var situacao = results[0].situacao
         
        //CASO O METODO SEJA POST TEM QUE USAR RES.JSON, CASO SEJA GET NAO NECESSITA   
        //res.json({ proprietario: proprietario, chassi: chassi, situacao: situacao });

        //console.log(ocorrencia)    
    });
}); 

console.log('olá mundo')





app.listen(9001, '0.0.0.0', function() {
    console.log('Listening on port 9001')
})